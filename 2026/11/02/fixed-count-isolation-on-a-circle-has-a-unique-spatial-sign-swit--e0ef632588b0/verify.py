#!/usr/bin/env python3
"""Reproducible finite checks for spatial isolation covariance formulas.

No simulation or finite calculation is used as a proof of the continuum theorem.
"""
from fractions import Fraction as F
from math import sqrt, exp
from itertools import product

checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def overlap_of_arcs(r, d):
    # Equal circular arcs of radius r at circular distance d.
    return max(F(0), 2*r-d) + max(F(0), 2*r-(1-d))

def overlap_by_interval_clipping(r, d):
    # Independent geometry: union of lifted interval intersections.
    out = F(0)
    for shift in (-2, -1, 0, 1, 2):
        lo = max(-r, d+shift-r)
        hi = min(r, d+shift+r)
        out += max(F(0), hi-lo)
    return out

radii = [F(i, 40) for i in range(1,20)]
separations = [F(j,80) for j in range(41)]
for r in radii:
    threshold = 2*r-4*r*r
    for d in separations:
        C = overlap_of_arcs(r,d)
        check(C == overlap_by_interval_clipping(r,d), 'independent arc geometry')
        check((C-(2*r)**2 > 0) == (d < threshold), 'positive sign threshold')
        check((C-(2*r)**2 < 0) == (d > threshold), 'negative sign threshold')
        # Fixed-count covariance, conditioned on the absence of a direct link.
        a = 1-2*r
        b = 1-4*r+C
        for n in (3,4,5,9):
            cov = b**(n-2)-a**(2*(n-2))
            check((cov > 0) == (d < threshold), 'sample-size invariant sign')
            check((cov < 0) == (d > threshold), 'sample-size invariant negative sign')

# Exact finite-grid enumeration checks, independent of continuum arc identities.
# Uniform grid points are sampled WITH replacement and all tagged edges are absent.
q = 11
for r in (F(1, 7), F(2, 7), F(3, 7)):
    A = {z for z in range(q) if min(z, q-z)*F(1,q) <= r}
    count_available = q-len(A)
    for j in range(1,(q//2)+1):
        d = F(j,q)
        if d <= r:  # tagged pair would have a deterministic direct edge
            continue
        B = {z for z in range(q) if min((z-j)%q,(j-z)%q)*F(1,q) <= r}
        neither = q-len(A|B)
        for n in (3,4,5):
            outcomes=product(range(q),repeat=n-2)
            isolated_a=isolated_b=both=0
            total=q**(n-2)
            for draws in outcomes:
                ia=all(z not in A for z in draws)
                ib=all(z not in B for z in draws)
                isolated_a+=ia
                isolated_b+=ib
                both+=ia and ib
            check(F(isolated_a,total) == F(count_available,q)**(n-2), 'grid marginal A')
            check(F(isolated_b,total) == F(count_available,q)**(n-2), 'grid marginal B')
            check(F(both,total) == F(neither,q)**(n-2), 'grid joint')

# Independent exact discretization of a SOFT strictly decreasing profile:
# h(x) = 1 - 2 circular_distance(x, 0); convolution is evaluated by sums.
for q in (19, 31, 47):
    H = [F(1)-2*F(min(i,q-i),q) for i in range(q)]
    m = sum(H,F(0))/q
    C = [sum((H[k]*H[(k-j)%q] for k in range(q)),F(0))/q for j in range(q//2+1)]
    check(all(C[j]>C[j+1] for j in range(len(C)-1)), 'strict soft convolution monotonicity')
    check(C[0]>m*m>C[-1], 'soft sign crossing')
    for n in (3,5,11):
        cov = [(1-2*m+c)**(n-2)-(1-m)**(2*(n-2)) for c in C]
        check(all((v>0)==(c>m*m) for v,c in zip(cov,C)), 'soft finite-count sign')
        check(all((v<0)==(c<m*m) for v,c in zip(cov,C)), 'soft negative sign')
        # Poisson counterpart: p_both = exp(-lambda*(2m-C)), p_one=exp(-lambda*m).
        lam=n-2
        check(all(exp(-lam*(2*float(m)-float(c)))-exp(-2*lam*float(m)) >= -1e-14 for c in C), 'soft Poisson nonnegative')

# A second independent exact integration of the triangular soft kernel.
# Product of two affine pieces is quadratic; Simpson is exact on each interval.
def H_continuous(x):
    x=x % 1
    return 1-2*min(x,1-x)

def simpson_integral(d):
    grid=sorted(set([F(0), d, F(1,2), F(1,2)+d, F(1)]))
    total=F(0)
    for a,b in zip(grid[:-1],grid[1:]):
        mid=(a+b)/2
        f=lambda x:H_continuous(x)*H_continuous(x-d)
        total+=(b-a)*(f(a)+4*f(mid)+f(b))/6
    return total
for j in range(21):
    d=F(j,40)
    c=(1-6*d*d+8*d*d*d)/3
    check(simpson_integral(d)==c,'triangular kernel independent exact integral')
    check((c>F(1,4))==(d<F(1,4)), 'triangular positive quarter-point threshold')
    check((c<F(1,4))==(d>F(1,4)), 'triangular negative quarter-point threshold')
check((1-2*F(1,2)+F(1,6))-F(1,4)==-F(1,12), 'triangular antipodal exact negative covariance')
check(exp(-5/6)-exp(-1)>0, 'Poissonized antipodal positive covariance')

r_star = (2-sqrt(2))/4
fraction=lambda r:2*r*(1-4*r)/(1-2*r) if 0<r<0.25 else 0
check(abs(fraction(r_star)-(3-2*sqrt(2)))<1e-13,'sharp maximum exact algebra')
check(all(fraction(k/10000)<=fraction(r_star)+1e-12 for k in range(1,5000)), 'sharp optimizer grid corroboration')
print(f'PASS: {checks} exact/numerical assertions')
