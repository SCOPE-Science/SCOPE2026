"""Standalone checks for the complete-bipartite length-two-path adsorption theorem.

Usage: python trimer_checks.py. Uses only the Python standard library.
The checks are finite and do not replace the asymptotic martingale proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from collections import defaultdict
from math import gamma, isclose
from random import Random
from statistics import mean

@lru_cache(None)
def reduced(x,y):
    s=x+y
    if not x or not y or s<3 or (x==1 and y==1):
        return {s:Fraction(1)}
    z=defaultdict(Fraction)
    for (a,b,w) in ((x-2,y-1,Fraction(x-1,s-2)),(x-1,y-2,Fraction(y-1,s-2))):
        if w:
            assert a>=0 and b>=0
            for k,p in reduced(a,b).items():
                z[k]+=w*p
    assert sum(z.values())==1
    return dict(z)

def physical(x,y):
    paths=[]
    A=range(x)
    B=range(x,x+y)
    for a in A:
        for b,c in combinations(B,2):
            paths.append((1<<a)|(1<<b)|(1<<c))
    for b in B:
        for a,c in combinations(A,2):
            paths.append((1<<a)|(1<<b)|(1<<c))
    @lru_cache(None)
    def run(used):
        possible=[p for p in paths if not(p & used)]
        if not possible: return {(x+y)-used.bit_count():Fraction(1)}
        z=defaultdict(Fraction)
        for p in possible:
            for k,v in run(used|p).items():
                z[k]+=v/Fraction(len(possible))
        return dict(z)
    return run(0)

def simulation(x,y,rng):
    while x>0 and y>0 and x+y>=3 and (x>1 or y>1):
        if rng.randrange(x+y-2)<x-1:
            x-=2;y-=1
        else:
            x-=1;y-=2
    return x+y

def main():
    cases=[(2,2),(2,3),(3,3),(4,2),(4,3),(4,4),(5,3),(5,4),(6,3)]
    for x,y in cases:
        a,b=reduced(x,y),physical(x,y)
        assert a==b,(x,y,a,b)
        print('EXACT',x,y,'distribution',','.join(f'{k}:{v}' for k,v in sorted(a.items())))
    assert reduced(4,2)=={0:Fraction(3,4),3:Fraction(1,4)}
    assert reduced(5,4)=={0:Fraction(25,28),3:Fraction(3,28)}
    for x in range(1,11):
        for y in range(1,11):
            s=x+y
            if s<3 or (x==1 and y==1):continue
            p=Fraction(x-1,s-2)
            q=Fraction(y-1,s-2)
            drift=q-p
            assert p+q==1
            assert drift==-Fraction(x-y,s-2)
            assert 1-drift*drift==1-Fraction((x-y)**2,(s-2)**2)
    print('DRIFT and conditional-variance 99 state cases OK')
    for s in range(5,130):
        ratio=(gamma((s-3)/3)/gamma((s-2)/3))/(gamma(s/3)/gamma((s+1)/3))
        assert isclose(ratio,(s-2)/(s-3),rel_tol=2e-12),s
    print('GAMMA recurrence 125 cases OK')
    rng=Random(20261015)
    for N,frac,rep in ((3000,.5,180),(12000,.5,180),(30000,.6,80),(30000,.75,80)):
        x=round(N*frac)
        samples=[simulation(x,N-x,rng) for _ in range(rep)]
        if frac!=.5: pred=N*abs(2*frac-1)**1.5
        else: pred=N**.25*(2**.75)*gamma(1.25)/(__import__('math').sqrt(__import__('math').pi))
        print('MONTE-CARLO',N,frac,'mean',round(mean(samples),4),'predicted',round(pred,4))
    print('CHECKS PASSED')

if __name__=='__main__':main()
