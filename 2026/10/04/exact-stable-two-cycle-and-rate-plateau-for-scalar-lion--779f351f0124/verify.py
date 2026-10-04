from fractions import Fraction
import random

def sgn(x): return 0 if x == 0 else (1 if x > 0 else -1)
def step(x,m,a,eta,wd,b1,b2):
    u=b1*m+(1-b1)*a*x
    return (1-eta*wd)*x-eta*sgn(u), b2*m+(1-b2)*a*x, u

# Exact rational instance
a=Fraction(3,2); eta=Fraction(1,5); wd=Fraction(2,1); b1=Fraction(4,5); b2=Fraction(9,10)
q=eta*wd; D=1+b2-2*b1; c=eta/(2-q); M=(1-b2)*a*c/(1+b2)
x1,m1,u1=step(c,-M,a,eta,wd,b1,b2); x2,m2,u2=step(-c,M,a,eta,wd,b1,b2)
assert x1==-c and m1==M and u1>0 and x2==c and m2==-M and u2<0

for _ in range(200):
    b2=random.uniform(0,0.999)
    b1=random.uniform(0,max(1e-8,(1+b2)/2-1e-6))
    q=random.uniform(1e-4,1.999); eta=random.uniform(1e-3,.5); wd=q/eta; a=random.uniform(.1,5)
    D=1+b2-2*b1; c=eta/(2-q); M=(1-b2)*a*c/(1+b2)
    x1,m1,u1=step(c,-M,a,eta,wd,b1,b2); x2,m2,u2=step(-c,M,a,eta,wd,b1,b2)
    assert abs(x1+c)<1e-10 and abs(m1-M)<1e-10 and u1>0
    assert abs(x2-c)<1e-10 and abs(m2+M)<1e-10 and u2<0
    assert max(abs(1-q),b2)<1

for b2 in (0,.2,.5,.9,.99):
    lo,hi=1-b2,1+b2
    for q in (lo,(lo+hi)/2,hi):
        assert abs(max(abs(1-q),b2)-b2)<1e-12

for q in (.2,.8,1,1.2,1.8):
    eta=.1; wd=q/eta; c=eta/(2-q)
    assert (c<=1/wd+1e-12)==(q<=1)

print("verification passed")
