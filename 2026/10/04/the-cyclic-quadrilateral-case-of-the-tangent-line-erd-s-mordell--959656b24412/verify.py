from fractions import Fraction
import math

# Coefficients are a+b*s with s^2=2; monomials are exponent triples (x,y,z).
def addc(p,q): return (p[0]+q[0], p[1]+q[1])
def mulc(p,q): return (p[0]*q[0]+2*p[1]*q[1], p[0]*q[1]+p[1]*q[0])
def add(P,Q):
    R=dict(P)
    for m,c in Q.items():
        R[m]=addc(R.get(m,(Fraction(0),Fraction(0))),c)
        if R[m]==(0,0): del R[m]
    return R
def scale(P,c): return {m:mulc(v,c) for m,v in P.items()}
def mul(P,Q):
    R={}
    for a,ca in P.items():
        for b,cb in Q.items():
            m=tuple(a[i]+b[i] for i in range(3))
            R[m]=addc(R.get(m,(Fraction(0),Fraction(0))),mulc(ca,cb))
    return {m:c for m,c in R.items() if c!=(0,0)}
X={(1,0,0):(Fraction(1),Fraction(0))}
Y={(0,1,0):(Fraction(1),Fraction(0))}
Z={(0,0,1):(Fraction(1),Fraction(0))}
s=(Fraction(0),Fraction(1)); one=(Fraction(1),Fraction(0)); two=(Fraction(2),Fraction(0))
E=add(add(mul(X,X),mul(Y,Y)),mul(Z,Z))
E=add(E,scale(add(mul(Y,X),mul(Y,Z)),(Fraction(0),Fraction(-1))))
left=scale(E,two)
XmZ=add(X,scale(Z,(Fraction(-1),Fraction(0))))
XpZmsY=add(add(X,Z),scale(Y,(Fraction(0),Fraction(-1))))
right=add(mul(XmZ,XmZ),mul(XpZmsY,XpZmsY))
assert left==right

# Direct coordinate smoke tests for the affine theorem.
def dist_line(p,a,b):
    return abs((b[0]-a[0])*(a[1]-p[1])-(a[0]-p[0])*(b[1]-a[1]))/math.hypot(b[0]-a[0],b[1]-a[1])
def run(gaps,weights):
    t=[0.0]
    for g in gaps[:-1]: t.append(t[-1]+g)
    A=[(math.cos(q),math.sin(q)) for q in t]
    P=(sum(weights[i]*A[i][0] for i in range(4)),sum(weights[i]*A[i][1] for i in range(4)))
    D=sum(1-(P[0]*a[0]+P[1]*a[1]) for a in A)
    d=sum(dist_line(P,A[i],A[(i+1)%4]) for i in range(4))
    return D-math.sqrt(2)*d
cases=[
 ([0.4,1.2,2.0,2*math.pi-3.6],[.1,.2,.3,.4]),
 ([1.0,1.5,0.8,2*math.pi-3.3],[.25,.25,.25,.25]),
 ([math.pi/2]*4,[.13,.27,.31,.29]),
]
vals=[run(*c) for c in cases]
assert vals[0] > -1e-12 and vals[1] > -1e-12 and abs(vals[2]) < 1e-12
print('VERIFY_OK', vals)
