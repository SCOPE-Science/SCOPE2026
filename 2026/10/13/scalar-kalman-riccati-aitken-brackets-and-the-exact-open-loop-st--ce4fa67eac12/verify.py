import sympy as sp
from fractions import Fraction as F

p,m,rho,t = sp.symbols("p m rho t")
phi = lambda s: (p-m*s)/(1-s)
x0,x1,x2 = phi(t),phi(rho*t),phi(rho**2*t)
ait = sp.factor(x0-(x1-x0)**2/(x2-2*x1+x0))
assert sp.simplify(ait-phi(rho**2*t**2)) == 0
assert sp.simplify((ait-p)/(ait-m)-rho**2*t**2) == 0

def ric(P,a,q,r=F(1),h=F(1)):
    return q+a*a*r*P/(h*h*P+r)

def aitken(x0,x1,x2):
    d=x2-2*x1+x0
    assert d != 0
    return x0-(x1-x0)**2/d

# Stable exact witness.
a=q=r=h=F(1)
P0=F(0)
P1=ric(P0,a,q,r,h)
P2=ric(P1,a,q,r,h)
P3=ric(P2,a,q,r,h)
assert (P0,P1,P2,P3)==(F(0),F(1),F(3,2),F(8,5))
assert aitken(P0,P1,P2)==F(2)
assert aitken(P1,P2,P3)==F(13,8)

# Unstable exact witness.
a=F(2); q=r=h=F(1)
P0=F(0); P1=ric(P0,a,q,r,h); P2=ric(P1,a,q,r,h)
assert (P0,P1,P2)==(F(0),F(1),F(3))
assert aitken(P0,P1,P2)==F(-1)

# Parametric first-Aitken formula for h=r=1.
aa,qq=sp.symbols("aa qq", positive=True)
P1s=qq
P2s=qq+aa**2*qq/(qq+1)
A0=sp.factor(-(P1s**2)/(P2s-2*P1s))
assert sp.simplify(A0 + qq*(qq+1)/(aa**2-1-qq)) == 0

print("VERIFY_OK")
