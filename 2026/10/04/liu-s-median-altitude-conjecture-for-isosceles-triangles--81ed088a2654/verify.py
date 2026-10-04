#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb

# Exact arithmetic in Q(sqrt(3)); z=(a,b) represents a+b*sqrt(3).
def z(a=0,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(x,c): return (x[0]*F(c),x[1]*F(c))
def sq(x): return mul(x,x)
def eq(x,y): return x==y

def sgn(x):
    a,b=x
    if b==0: return (a>0)-(a<0)
    # Compare a with -b*sqrt(3), exactly by signs and squares.
    if a==0: return (b>0)-(b<0)
    if a>0 and b>0: return 1
    if a<0 and b<0: return -1
    lhs=a*a; rhs=3*b*b
    if a>0 and b<0:
        return 1 if lhs>rhs else (-1 if lhs<rhs else 0)
    if a<0 and b>0:
        return -1 if lhs>rhs else (1 if lhs<rhs else 0)
    raise AssertionError

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==z(): p.pop()
    return p

def padd(p,q):
    n=max(len(p),len(q)); r=[z() for _ in range(n)]
    for i in range(n):
        r[i]=add(p[i] if i<len(p) else z(), q[i] if i<len(q) else z())
    return trim(r)
def pneg(p): return [neg(c) for c in p]
def psub(p,q): return padd(p,pneg(q))
def pmul(p,q):
    r=[z() for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]=add(r[i+j],mul(a,b))
    return trim(r)
def pscale(p,c): return [scale(a,c) for a in p]
def ppow(p,n):
    r=[z(1)]
    for _ in range(n): r=pmul(r,p)
    return r
def peval(p,x):
    r=z()
    for c in reversed(p): r=add(mul(r,x),c)
    return r

def shift_poly(p,beta):
    # p(x), return p(beta+y), ascending coefficients in y.
    out=[z()]
    for i,c in enumerate(p):
        term=[z() for _ in range(i+1)]
        for j in range(i+1):
            term[j]=mul(c, scale(ppow([beta], i-j)[0], comb(i,j)))
        out=padd(out,term)
    return trim(out)

X=[z(),z(1)]
A=[z(-4),z(7)]
B=[z(4,-3),z(2)]
Xp2=[z(2),z(1)]
q2=[z(4),z(),z(-1)]
dpoly=[z(2),z(1),z(F(9,4))]
t2=[z(1),z(),z(2)]

U=psub(pmul(ppow(A,2),ppow(Xp2,2)), pscale(pmul(pmul(ppow(B,2),q2),dpoly),4))
V=pscale(pmul(pmul(ppow(B,2),q2),Xp2),4)
P=psub(ppow(U,2), pmul(ppow(V,2),t2))
Q=[z(-168,96), z(-496,288), z(-129,72), z(86,-48), z(52,-24), z(6,-6), z(1)]
fac=pscale(pmul(pmul(pmul(ppow([z(-1),z(1)],2), ppow([z(F(-4,7)),z(1)],2)), ppow(Xp2,2)), Q),784)
assert P==fac, "factor identity failed"

alpha=z(F(4,7))
beta=z(-2,F(3,2))
assert sgn(sub(beta,alpha))>0 and sgn(beta)>0 and sgn(sub(z(2),beta))>0

# Q is strictly increasing on [0,alpha]. Reconstruct Q', substitute x=alpha*t,
# and convert the resulting degree-five power polynomial to Bernstein form.
dQ=[scale(Q[i],i) for i in range(1,len(Q))]
power=[mul(c, ppow([alpha],i)[0]) for i,c in enumerate(dQ)]
n=len(power)-1
dbern=[]
for j in range(n+1):
    acc=z()
    for i in range(j+1):
        acc=add(acc, scale(power[i], F(comb(j,i),comb(n,i))))
    dbern.append(acc)
expected_dbern=[
 z(-496,288),
 z(F(-18392,35),F(10656,35)),
 z(F(-133904,245),F(77472,245)),
 z(F(-952344,1715),F(551328,1715)),
 z(F(-1313904,2401),F(3815328,12005)),
 z(F(-8686008,16807),F(725472,2401)),
]
assert dbern==expected_dbern and all(sgn(c)>0 for c in dbern)
Qalpha=peval(Q,alpha)
assert Qalpha==z(F(-55478520,117649),F(4574880,16807)) and sgn(Qalpha)<0

# For x=beta+y, Q has positive low coefficients, and its high block
# y^4*(y^2+c5*y+c4) is positive because its discriminant is -10.
Qb=shift_poly(Q,beta)
expected_Qb=[
 z(F(567,64),F(-81,16)), z(F(-27,8),F(99,16)),
 z(F(543,16),F(-21,2)), z(-7,F(27,2)),
 z(F(73,4),-9), z(-6,3), z(1)
]
assert Qb==expected_Qb
assert all(sgn(Qb[i])>0 for i in range(5)) and sgn(Qb[5])<0 and sgn(Qb[6])>0
disc=sub(sq(Qb[5]), scale(mul(Qb[6],Qb[4]),4))
assert disc==z(-10)

# U(beta+y) has every coefficient positive, hence U>0 for x>=beta.
Ub=shift_poly(U,beta)
expected_Ub=[
 z(F(70713,16),F(-5103,2)), z(-5103,F(5913,2)),
 z(F(33507,4),-4752), z(-6336,3720),
 z(2163,-1224), z(-272,216), z(36)
]
assert Ub==expected_Ub and all(sgn(c)>0 for c in Ub)

# Exact equality check at x=1: sqrt(4-x^2)=sqrt(3), sqrt(1+2x^2)=sqrt(3).
# G = sqrt(3)-sqrt(3)-3/2 + 3*sqrt(3)*(sqrt(3)/6) = 0.
G1=add(z(F(-3,2)), z(F(3,2)))
assert G1==z()
print("VERIFY_OK")
