"""Reproducible finite checks for widths of fixed-sum cube sections.
Exact cut comparisons; randomized directional cross-checks. Not an all-dimensional proof.
"""
from fractions import Fraction
from itertools import permutations
from math import sqrt
from random import Random

def vertices(n,t):
    k=t.numerator//t.denominator
    r=t-Fraction(k)
    base=[Fraction(1)]*k+([r] if r else [])+[Fraction(0)]*(n-k-int(r>0))
    return tuple(sorted(set(permutations(base))))

def width_normal(V,z):
    values=[sum(float(x)*u for x,u in zip(v,z)) for v in V]
    return max(values)-min(values)

def exact_cut(n,t,j):
    return min(Fraction(j),t)-max(Fraction(0),t-Fraction(n-j))

def predicted(n,t):
    q=(n//2)*(n-n//2)
    return sqrt(n)*min(1/sqrt(n-1),float(min(t,n-t))/sqrt(q))

def check():
    rng=Random(201014)
    cuts=0; randoms=0; min_gap=float('inf')
    for n in range(4,9):
        values={Fraction(1,7),Fraction(1,2),Fraction(1),Fraction(n,2),Fraction(n-1),Fraction(n)-Fraction(1,7)}
        values.update(Fraction(j,7) for j in range(1,7*n) if 0<j<7*n)
        for t in sorted(values):
            if not 0<t<n:continue
            V=vertices(n,t)
            for j in range(1,n):
                obs=max(sum(v[:j]) for v in V)-min(sum(v[:j]) for v in V)
                assert obs==exact_cut(n,t,j),(n,t,j,obs,exact_cut(n,t,j))
                assert sqrt(n/(j*(n-j)))*float(obs)>=predicted(n,t)-1e-10
                cuts+=1
            best=1 if 1/sqrt(n-1)<float(min(t,n-t))/sqrt((n//2)*(n-n//2)) else n//2
            norm=sqrt(n/(best*(n-best)))
            z=[-norm*(n-best)/n]*best+[norm*best/n]*(n-best)
            assert abs(width_normal(V,z)-predicted(n,t))<1e-9
            for _ in range(14):
                z=[rng.gauss(0,1) for _ in range(n)];avg=sum(z)/n
                z=[a-avg for a in z];norm=sqrt(sum(a*a for a in z));z=[a/norm for a in z]
                gap=width_normal(V,z)-predicted(n,t)
                assert gap>=-1e-9,(n,t,gap)
                min_gap=min(min_gap,gap); randoms+=1
    checked_threshold=0
    for n in range(4,90):
        q=(n//2)*(n-n//2)
        tau=sqrt(q/(n-1))
        assert 1<tau<n/2
        for t,branch in [(tau*.9,0),((tau+n/2)/2,1),(n/2,1),(n-(tau+n/2)/2,1),(n-.9*tau,0)]:
            A=1/sqrt(n-1); B=min(t,n-t)/sqrt(q)
            assert (A>B)==(branch==0)
        checked_threshold+=1
    print(f'PASS cuts={cuts} random_directions={randoms} threshold_dimensions={checked_threshold} min_random_gap={min_gap:.9f}')
if __name__=='__main__':check()
