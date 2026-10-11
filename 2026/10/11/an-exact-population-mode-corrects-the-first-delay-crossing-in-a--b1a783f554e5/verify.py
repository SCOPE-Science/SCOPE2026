from fractions import Fraction as F
from itertools import permutations
import cmath, math

# Exact equilibrium for the printed system (5.1).
S=F(1407,4561); P1=F(544506,305587); P2=F(105271160,2139109); T=F(18603955,2139109)

def infection(s,p1,p2):
    return F(2,25)*s*(p1+F(5,4)*p2)/(1+s)
I=infection(S,P1,P2)
res=[
    F(6,5)-F(1,50)*S-I,
    I-F(9,20)*P1-F(11,50)*P1,
    F(9,20)*P1+F(7,10)*T-F(7,50)*P2,
    F(1,5)*P1+F(3,25)*P2-F(18,25)*T,
]
assert res==[0,0,0,0]
assert S+P1+P2+T==60

# Polynomial in lambda and z=exp(-lambda*tau), represented by (lambda_power,z_power)->Fraction.
def C(x): return {(0,0):F(x)}
def L(): return {(1,0):F(1)}
def Z(c=1): return {(0,1):F(c)}
def add(a,b):
    r=dict(a)
    for k,v in b.items(): r[k]=r.get(k,F(0))+v
    return {k:v for k,v in r.items() if v}
def neg(a): return {k:-v for k,v in a.items()}
def mul(a,b):
    r={}
    for (i,j),x in a.items():
        for (k,l),y in b.items(): r[(i+k,j+l)]=r.get((i+k,j+l),F(0))+x*y
    return {k:v for k,v in r.items() if v}
def scale(a,c): return {k:v*F(c) for k,v in a.items() if v*F(c)}
def parity(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

def determinant(M):
    out={}
    for p in permutations(range(4)):
        term=C(parity(p))
        for i,j in enumerate(p): term=mul(term,M[i][j])
        out=add(out,term)
    return out

A0=[
[F(-416714303,139949600),F(-1407,74600),F(-1407,59680),F(0)],
[F(413915311,139949600),F(-3001,14920),F(1407,59680),F(0)],
[F(0),F(0),F(-7,50),F(7,10)],
[F(0),F(1,5),F(3,25),F(-18,25)],
]
A1=[[F(0) for _ in range(4)] for _ in range(4)]
A1[1][1]=F(-9,20); A1[2][1]=F(9,20)
M=[]
for i in range(4):
    row=[]
    for j in range(4):
        x=C(-A0[i][j])
        if i==j: x=add(x,L())
        if A1[i][j]: x=add(x,Z(-A1[i][j]))
        row.append(x)
    M.append(row)
det=determinant(M)

A3=349874000000; A2=1406053367500; A1c=1163274624350; A0c=191256352392
B2=157443300000; B1=597344121000; B0=391122490185
P={(3,0):F(A3),(2,0):F(A2),(1,0):F(A1c),(0,0):F(A0c)}
Qz={(2,1):F(B2),(1,1):F(B1),(0,1):F(B0)}
target=scale(mul(add(C(1),scale(L(),50)),add(P,Qz)),F(1,17493700000000))
assert det==target

# Exact modulus polynomial |P(iw)|^2-|Q(iw)|^2 in u=w^2.
# coefficients low to high
poly=[F(A0c*A0c-B0*B0),
      F(-2*A0c*A2 + A1c*A1c + 2*B0*B2 - B1*B1),
      F(A2*A2 - 2*A1c*A3 - B2*B2),
      F(A3*A3)]
expected=[F(-116397809998222537212561),F(581713807208182432802500),F(1138198587703536256250000),F(122411815876000000000000)]
assert poly==expected

def evalF(u): return sum(poly[i]*u**i for i in range(4))
lo=F(1533334188148464,10**16); hi=F(1533334188148465,10**16)
assert evalF(lo)<0<evalF(hi)
# derivative is positive for u>0 because all derivative coefficients are positive.
assert all(c>0 for c in poly[1:])

# Zero-delay cubic Hurwitz test.
a3=F(A3); a2=F(A2+B2); a1=F(A1c+B1); a0=F(A0c+B0)
assert min(a3,a2,a1,a0)>0
rh=a2*a1-a3*a0
assert rh==2548962325924970823125000 and rh>0

# Numerical replay at the unique root.
def ff(u): return float(poly[0])+float(poly[1])*u+float(poly[2])*u*u+float(poly[3])*u*u*u
left=float(lo); right=float(hi)
for _ in range(100):
    mid=(left+right)/2
    if ff(mid)>0: right=mid
    else: left=mid
u=(left+right)/2
w=math.sqrt(u)
def Pc(l): return A3*l**3+A2*l**2+A1c*l+A0c
def Qc(l): return B2*l**2+B1*l+B0
ratio=-Pc(1j*w)/Qc(1j*w)
assert abs(abs(ratio)-1)<1e-10
arg=cmath.phase(ratio)
tau=(-arg if arg<0 else 2*math.pi-arg)/w
assert abs(w-0.39157811329905353)<5e-14
assert abs(tau-5.31769616572693)<5e-13
l=1j*w; z=cmath.exp(-l*tau)
scale0=max(abs(Pc(l)),abs(Qc(l)),1.0)
assert abs(Pc(l)+Qc(l)*z)/scale0<1e-10
Pp=lambda l: 3*A3*l*l+2*A2*l+A1c
Qp=lambda l: 2*B2*l+B1
dl=l*Qc(l)*z/(Pp(l)+(Qp(l)-tau*Qc(l))*z)
assert abs(dl.real-0.016975869135618388)<5e-13 and dl.real>0
print('VERIFY_OK')
