#!/usr/bin/env python3
"""Numerical checks of an exact-randomized-Ritz quadratic; Python standard library only."""
import cmath
import math
import random

R = random.Random(260401037)

def cg():
    return complex(R.gauss(0.0, 1.0 / math.sqrt(2.0)),
                   R.gauss(0.0, 1.0 / math.sqrt(2.0)))

def roots(a, b, d):
    # a*z*z-b*z+d=0. Avoid subtracting two nearly equal complex numbers.
    disc = cmath.sqrt(b*b - 4*a*d)
    if abs(b+disc) < abs(b-disc):
        disc = -disc
    small = 2*d/(b+disc)
    large = (b+disc)/(2*a)
    return small, large

def one(a, g1, g2, eps, detailed=False):
    c = math.sqrt(1-eps*eps)
    b = c*g1
    d = eps*c*g2 - eps*eps*a
    z1,z2 = roots(a,b,d)
    rr = min(abs(z1),abs(z2))
    sin2 = (eps*eps+rr*rr)/(1+rr*rr)
    if detailed:
        for z in z1,z2:
            residual = a*z*z-b*z+d
            assert abs(residual) < 1e-7*(1+abs(a*z*z)+abs(b*z)+abs(d))
            den = c*g1-a*z
            mu = eps*a/den
            # In orthonormal (e2,w2,w3) coordinates the residual is
            # (-mu*c,-eps-mu*z,-z-mu*eps), a scalar multiple of q.
            f0,f1,f2=-mu*c,-eps-mu*z,-z-mu*eps
            assert abs(f1*a-f0*g1)<1e-7*(1+abs(f0*g1)+abs(f1*a))
            assert abs(f2*a-f0*g2)<1e-7*(1+abs(f0*g2)+abs(f2*a))
            norm2 = 1+abs(z)**2
            projection_sin2 = 1-c*c/norm2
            formula_sin2 = (eps*eps+abs(z)**2)/norm2
            assert abs(projection_sin2-formula_sin2)<1e-12
    return sin2

count=0
for eps in (0.3,0.1,0.03,0.003):
    for _ in range(600):
        a,g1,g2=cg(),cg(),cg()
        one(a,g1,g2,eps,True)
        count+=1
print('Polynomial, generalized residual, and sine-angle checks:',count)

# First and second moments are computed from the same 110,000 independent
# triples at each epsilon. Asymptotic comparisons are intentionally loose
# because the p=2 observable has a long, truncated tail.
points=(0.03,0.006,0.001)
acc={v:[0.0,0.0] for v in points}
n=110000
for _ in range(n):
    a,g1,g2=cg(),cg(),cg()
    for eps in points:
        err=math.sqrt(one(a,g1,g2,eps))
        acc[eps][0]+=err/eps
        acc[eps][1]+=(err/eps)**2
for eps in points:
    m1,m2=(v/n for v in acc[eps])
    assert 1.55 < m1 < 2.45, (eps,m1)
    assert abs(m2-math.log(1/eps))<4.5, (eps,m2)
    print('epsilon',eps,'mean(E/epsilon)',round(m1,5),
          'mean((E/epsilon)^2)',round(m2,5),
          'log(1/epsilon)',round(math.log(1/eps),5))

n_tail=110000
for threshold in (1.25,1.5,2,3):
    observed=0
    for _ in range(n_tail):
        u=abs(cg())**2
        v=abs(cg())**2
        if math.sqrt(1+v/u)>threshold:
            observed+=1
    empirical=observed/n_tail
    theoretical=1/(threshold*threshold)
    assert abs(empirical-theoretical)<0.014,(threshold,empirical,theoretical)
    print('Pareto threshold',threshold,'empirical',round(empirical,5),
          'theoretical',round(theoretical,5))
print('PASS: deterministic identities and seeded stochastic diagnostics')
