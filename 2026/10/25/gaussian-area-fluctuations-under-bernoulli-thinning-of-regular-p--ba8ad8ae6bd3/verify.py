"""Independent numerical checks for Bernoulli-thinned cyclic polygons.

Uses only Python's standard library. These are finite checks, not a proof.
"""
from itertools import combinations
import math
import random


def poly_area(n, retained):
    if len(retained) < 3:
        return 0.0
    t = 2 * math.pi / n
    pts = [(math.cos(t * j), math.sin(t * j)) for j in retained]
    return 0.5 * abs(sum(x * pts[(i + 1) % len(pts)][1] - y * pts[(i + 1) % len(pts)][0]
                         for i, (x, y) in enumerate(pts)))


def mean_formula(n, p):
    q = 1-p
    t = 2 * math.pi / n
    return n * p*p * math.sin(t) * (-math.expm1(n * math.log(q))) / (2*(p*p + 2*q*(1-math.cos(t))))


def deficit_gap(n, retained):
    t = 2 * math.pi/n
    full = n * math.sin(t)/2
    if not retained:
        return full
    ext = retained + [retained[0]+n]
    return sum((k * math.sin(t) - math.sin(k*t))/2
               for k in (ext[i+1]-ext[i] for i in range(len(retained))))


def var_coef(p):
    q=1-p
    return 16 * math.pi**6 * q*(1+q)*(1+5*q+q*q)/p**5


def mean_coef(p):
    return 4*math.pi**3*(1-p)/p**2


for n in range(3,13):
    A0=n*math.sin(2*math.pi/n)/2
    per_p={p:0.0 for p in (0.25,0.5,0.75)}
    for mask in range(1<<n):
        chosen=[j for j in range(n) if mask & (1<<j)]
        area=poly_area(n,chosen)
        assert abs(A0-area-deficit_gap(n,chosen)) < 4e-13
        for p in per_p:
            q=1-p
            per_p[p]+=p**len(chosen)*q**(n-len(chosen))*area
    for p, observed in per_p.items():
        assert abs(observed-mean_formula(n,p)) < 3e-12, (n,p,observed,mean_formula(n,p))
print('EXHAUSTIVE_POLYGON_AREA_AND_CYCLIC_GAP_CHECKS_OK n=3..12 p=1/4,1/2,3/4')

for p in (0.25,0.5,0.75):
    q=1-p
    for n in (100,300,1000,3000):
        full = n*math.sin(2*math.pi/n)/2
        deficit=full-mean_formula(n,p)
        leading=mean_coef(p)/n**2 - 4*math.pi**5*q*(1+q)**2/(p**4*n**4)
        assert abs(deficit-leading) < 3.0e-3*mean_coef(p)/n**2, (p,n,deficit,leading)
print('EXACT_MEAN_TWO_TERM_ASYMPTOTIC_CHECK_OK')

rng=random.Random(7182016)
for p in (0.35,0.5,0.75):
    n=700
    trials=4500
    theta=2*math.pi/n
    full=n*math.sin(theta)/2
    d=[]
    for z in range(trials):
        selected=[j for j in range(n) if rng.random()<p]
        if len(selected)<3:
            area=0.0
        else:
            cyc=selected+[selected[0]+n]
            area=0.5*sum(math.sin((cyc[k+1]-cyc[k])*theta)
                         for k in range(len(selected)))
        d.append(full-area)
    em=sum(d)/trials
    ev=sum((v-em)**2 for v in d)/trials
    predicted_var=var_coef(p)/n**5
    assert abs(em - (full-mean_formula(n,p))) < 0.07*math.sqrt(predicted_var)
    assert 0.80 < ev/predicted_var < 1.20, (p, ev/predicted_var)
    print('MONTE_CARLO_ASYMPTOTIC_VARIANCE_OK',p,round(ev/predicted_var,5))
print('ALL_BERNOULLI_CYCLIC_AREA_CHECKS_OK')
