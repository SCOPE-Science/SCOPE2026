"""Exact-arithmetic checks for the inverse-leading/split-channel EKS theorem.
Run: python3 verify.py. No external dependencies.
"""
from fractions import Fraction as F
from random import Random

D = [F(-1), F(1), F(2)]

def dot(a,b): return sum((x*y for x,y in zip(a,b)), F(0))
def scale(c,a): return [c*x for x in a]
def sub(a,b): return [x-y for x,y in zip(a,b)]
def matvec(a): return [x*y for x,y in zip(D,a)]
def invvec(a): return [x/y for x,y in zip(a,D)]
def det3(u,v,w):
    return (u[0]*(v[1]*w[2]-v[2]*w[1]) -u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]))

def orth_squared(w,u,v):
    uu,uv,vv=dot(u,u),dot(u,v),dot(v,v)
    wu,wv=dot(w,u),dot(w,v)
    delta=uu*vv-uv*uv
    assert delta>0
    return dot(w,w) - (vv*wu*wu -2*uv*wu*wv + uu*wv*wv)/delta

def check(r):
    r=F(r)
    assert 0<r<=1
    b=[F(3),r,4*r]
    z=invvec(b); ab=matvec(b)
    assert det3(b,z,ab)==F(36)*r*r
    alpha=dot(b,z)/dot(b,b)
    assert alpha==9*(r*r-1)/(9+17*r*r)
    s=orth_squared(ab,b,z)
    assert s>0
    w=sub(b,scale(alpha,ab))
    m=orth_squared(w,b,z)
    assert m==alpha*alpha*s
    if r==1:
        assert alpha==0 and m==0 and w==b
    else:
        assert m>0
        gamma2=(m/dot(w,w))/(s/dot(ab,ab))
        formula=81*(r-1)**2*(r+1)**2*(65*r*r+9)/(4*r*r*(4*r*r+9)*(5*r*r+333))
        assert gamma2==formula,(r,gamma2,formula)
    return 1

runs=0
for den in range(2,40):
    for num in range(1,den+1):
        runs+=check(F(num,den))
for n in range(1,70):
    runs+=check(F(1,10**n))
    runs+=check(F(10**n-1,10**n))
rng=Random(340627)
for _ in range(1400):
    d=rng.randrange(2,100000)
    runs+=check(F(rng.randrange(1,d+1),d))
print('EXACT_VERIFY_PASS',runs)
