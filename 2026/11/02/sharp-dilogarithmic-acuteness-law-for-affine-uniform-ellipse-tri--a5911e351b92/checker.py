"""Deterministic numerical cross-checks for the angular-ellipse acute-triangle law.
Run with Python 3.11+; standard library only.
Numerical checks complement, but do not replace, the analytic proof.
"""
import math
import random

PI=math.pi

def dilog(z):
    if not 0 <= z <= 1:
        raise ValueError('dilog series domain')
    if z == 1: return PI*PI/6
    if z > .5:
        return PI*PI/6 - math.log(z)*math.log1p(-z)-dilog(1-z)
    s=0.0
    for k in range(1,20000):
        add=z**k/(k*k)
        s+=add
        if abs(add)<1e-18:
            break
    return s

def theoretical(r):
    t=(r*r-1)/(r*r+1)
    return .25-3*dilog(t*t)/(2*PI*PI)

def simpson_avg_arcsin2(t,n=8192):
    def f(i):
        v=math.asin(t*math.cos(2*PI*i/n))
        return v*v
    s=f(0)+f(n)
    for i in range(1,n):s+=(4 if i%2 else 2)*f(i)
    return s/(3*n)

for r in (1,1.01,1.25,2,5,20):
    t=(r*r-1)/(r*r+1)
    avg=simpson_avg_arcsin2(t)
    val=dilog(t*t)/2
    assert abs(avg-val)<1e-10, (r,avg,val)
    from_quadrature=.25-3*avg/(PI*PI)
    assert abs(from_quadrature-theoretical(r))<1e-10
print('INDEPENDENT_ARCSINE_QUADRATURE_AND_DILOGARITHM_IDENTITY_PASSED 6')

# Independent random triples, tested directly by Euclidean dot products.
rng=random.Random(921042)
N=85000
angles=[tuple(2*PI*rng.random() for j in range(3)) for i in range(N)]
for r in (1,1.25,2,5,20):
    yes=0
    for angles3 in angles:
        p=[(r*math.cos(q),math.sin(q)) for q in angles3]
        ux=p[1][0]-p[0][0]; uy=p[1][1]-p[0][1]
        vx=p[2][0]-p[0][0]; vy=p[2][1]-p[0][1]
        wx=p[2][0]-p[1][0]; wy=p[2][1]-p[1][1]
        if ux*vx+uy*vy>0 and -ux*wx-uy*wy>0 and vx*wx+vy*wy>0:
            yes+=1
    empirical=yes/N; expected=theoretical(r)
    sig=math.sqrt(expected*(1-expected)/N)
    assert abs(empirical-expected)<6*sig+0.001, (r,empirical,expected,sig)
    print('DIRECT_THREE_ANGLE_ELLIPSE_MONTE_CARLO_PASSED',r,round(empirical,6),round(expected,6))

# Exact endpoint laws and numerical diagnostics of asymptotic rates.
assert abs(theoretical(1)-.25)<1e-14
assert all(theoretical(b)<theoretical(a) for a,b in [(1,1.05),(1.05,1.2),(1.2,2),(2,5),(5,20)])
for ratio in (1e3,1e4):
    exact=theoretical(ratio)
    # Direct Li2 subtraction near 1 loses little precision at these ratios.
    lead=12*math.log(ratio)/(PI*PI*ratio*ratio)
    assert abs(exact/lead-1)<.15, (ratio,exact,lead)
print('ENDPOINT_RIGIDITY_MONOTONICITY_AND_SLENDER_ASYMPTOTIC_DIAGNOSTICS_PASSED')
print('ALL_CHECKS_PASSED')
