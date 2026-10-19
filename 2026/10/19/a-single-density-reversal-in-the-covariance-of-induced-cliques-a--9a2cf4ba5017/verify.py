"""Exact checks of a clique/one-edge-defect covariance identity (Python standard library)."""
from fractions import Fraction
from itertools import combinations
from math import comb


def covariance_formula(n, r, p):
    a = comb(r, 2)
    out = Fraction(0)
    for s in range(2, r + 1):
        b = comb(s, 2)
        A = comb(r, s) * comb(n-r, r-s) if 0 <= r-s <= n-r else 0
        out += A * (1-p) * p ** (2*a-b-1) * ((a-b)-a*p**b)
    return comb(n, r)*out


def covariance_enumerated(n, r, p):
    edges = list(combinations(range(n), 2))
    pos = {edge:i for i,edge in enumerate(edges)}
    windows = [tuple(pos[e] for e in combinations(vs,2)) for vs in combinations(range(n),r)]
    ex=ey=exy=Fraction(0)
    for mask in range(1 << len(edges)):
        w = p**mask.bit_count()*(1-p)**(len(edges)-mask.bit_count())
        if not w: continue
        x=y=0
        for window in windows:
            k=sum((mask >> i)&1 for i in window)
            y += k == len(window)
            x += k == len(window)-1
        ex+=w*x;ey+=w*y;exy+=w*x*y
    return exy-ex*ey


def normalized_polynomial(n,r,p):
    a=comb(r,2)
    return sum(comb(r,s)*comb(n-r,r-s)*((a-comb(s,2))*p**(a-comb(s,2))-a*p**a)
               for s in range(2,r+1) if 0<=r-s<=n-r)


def root_bisection(n,r,iterations=70):
    lo,hi=0.,1.
    for _ in range(iterations):
        mid=(lo+hi)/2
        if normalized_polynomial(n,r,mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

checks=0
for n,r in [(4,3),(5,3),(6,3),(5,4),(6,4)]:
    for p in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
        assert covariance_enumerated(n,r,p)==covariance_formula(n,r,p), (n,r,p)
        checks+=1
for r in range(3,11):
    a=comb(r,2)
    for n in range(r+1,r+31):
        p0=Fraction(a-1,a)
        assert normalized_polynomial(n,r,p0)<0
        assert normalized_polynomial(n,r,Fraction(1,10000))>0
        for j in range(1,50):
            p=Fraction(j,50)
            assert covariance_formula(n,r,p)*normalized_polynomial(n,r,p)>=0
            checks+=1
        root=root_bisection(n,r)
        assert 0<root<float(p0)
        assert abs(normalized_polynomial(n,r,root))<1e-5*comb(n,r)**2
        checks+=1
    n=r+1
    predicted=(2/(r+1))**(1/comb(r-1,2))
    assert abs(root_bisection(n,r)-predicted)<1e-12
    checks+=1
for r in range(3,11):
    a=comb(r,2)
    c=(r-2)**2*(3*a-1)/(3*a*(a-1)**2)
    for n in [100*r,200*r,400*r]:
        p=root_bisection(n,r)
        assert abs(n*((a-1)/a-p)-c)<0.025
        checks+=1
print('PASS:',checks,'exact/enumeration/bisection/asymptotic checks')
