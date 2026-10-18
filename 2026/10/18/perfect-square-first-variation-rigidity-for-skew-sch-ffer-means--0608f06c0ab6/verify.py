"""Reproducible algebraic and finite-sample checks for the real L4 skew variation.
Finite tests supplement rather than replace the dimension-free analytic proof.
Requires only the Python standard library.
"""
import math
import random

sqrt2 = math.sqrt(2)
sqrt3 = math.sqrt(3)
# The identity is an exact polynomial expansion after integration and normalizations.
# Check the integrand expansion on rational test values independently.
for p in range(-5, 6):
    for q in range(-5, 6):
        x = p / 3
        y = q / 3
        lhs = (x*y+(x*x-y*y)/sqrt2)**2
        rhs = x*x*y*y+(x**4-2*x*x*y*y+y**4)/2+sqrt2*x*y*(x*x-y*y)
        assert abs(lhs-rhs) < 1e-12

r_plus = (sqrt3-1)/sqrt2
r_minus = -(sqrt3+1)/sqrt2
for r in [r_plus, r_minus]:
    assert abs(r*r+sqrt2*r-1) < 1e-13

a = ((2+sqrt3)/4)**0.25
b = ((2-sqrt3)/4)**0.25
assert abs(a**4+b**4-1) < 1e-14
assert abs(a*a-b*b-sqrt2*a*b) < 1e-14
u = [a, b]
v = [-b, a]

def l4(v):
    return sum(abs(z)**4 for z in v)**0.25

def Q2(u,v):
    return sum((x*y+(x*x-y*y)/sqrt2)**2 for x,y in zip(u,v))

def F(t,tau,u,v):
    c=l4([x+tau*y for x,y in zip(u,v)])
    d=l4([tau*x-y for x,y in zip(u,v)])
    return ((c**t+d**t)/2)**(1/t)

assert abs(l4(u)-1) < 1e-14 and abs(l4(v)-1) < 1e-14
assert Q2(u,v) < 1e-26
rng = random.Random(1729)
for dim in [2,5,23]:
    for _ in range(300):
        uu=[rng.gauss(0,1) for j in range(dim)]
        vv=[rng.gauss(0,1) for j in range(dim)]
        cu=l4(uu); cv=l4(vv)
        uu=[z/cu for z in uu]; vv=[z/cv for z in vv]
        J=sum(x*y*(x*x-y*y) for x,y in zip(uu,vv))
        assert abs(Q2(uu,vv)-(1+sqrt2*J)) < 5e-12
        assert J>=-1/sqrt2-1e-12
        for t in [1,2,3.5]:
            tau=1e-4
            approximation=1-tau/(2*sqrt2)+tau*Q2(uu,vv)/(2*sqrt2)
            assert abs(F(t,tau,uu,vv)-approximation) < 1e-6
for t in [1,2,3.5]:
    tau=1e-5
    observed=(F(t,tau,u,v)-1)/tau
    assert abs(observed+1/(2*sqrt2)) < 3e-5
print('VERIFY_OK: polynomial expansion, two-band algebra, finite stress, endpoint slopes')
