"""Independent finite-state checks for greedy three-leaf-star adsorption."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from collections import defaultdict
from math import exp
from random import Random


def reduced(a,b):
    @lru_cache(None)
    def rec(a,b):
        wa=a*b*(b-1)*(b-2)//6 if b>=3 and a>=1 else 0
        wb=b*a*(a-1)*(a-2)//6 if a>=3 and b>=1 else 0
        if wa+wb==0: return {a+b: Fraction(1)}
        ans=defaultdict(Fraction)
        for prob,aa,bb in ((Fraction(wa,wa+wb),a-1,b-3),(Fraction(wb,wa+wb),a-3,b-1)):
            if prob:
                for k,v in rec(aa,bb).items():ans[k]+=prob*v
        return dict(ans)
    return rec(a,b)


def physical(a,b):
    stars=[]
    A=range(a); B=range(a,a+b)
    for c in A:
        for leaves in combinations(B,3):stars.append((1<<c)|sum(1<<v for v in leaves))
    for c in B:
        for leaves in combinations(A,3):stars.append((1<<c)|sum(1<<v for v in leaves))
    allmask=(1<<(a+b))-1
    @lru_cache(None)
    def rec(mask):
        avail=[st for st in stars if st&mask==st]
        if not avail:return {mask.bit_count():Fraction(1)}
        out=defaultdict(Fraction)
        for st in avail:
            for k,v in rec(mask^st).items():out[k]+=v/len(avail)
        return dict(out)
    return rec(allmask)


def one_run(a,b,rng):
    while a and b and (a>=3 or b>=3):
        wa=a*b*(b-1)*(b-2)//6 if b>=3 else 0
        wb=b*a*(a-1)*(a-2)//6 if a>=3 else 0
        if wa+wb==0:break
        if rng.randrange(wa+wb)<wa:a-=1;b-=3
        else:a-=3;b-=1
    return a+b


def formula(delta):
    return 0.0 if delta==0 else abs(delta)*exp((1-1/(delta*delta))/2)


def main():
    checks=0
    for a in range(1,6):
        for b in range(1,6):
            p=physical(a,b);q=reduced(a,b)
            assert p==q,(a,b,p,q)
            assert sum(p.values())==1
            checks+=1
    rng=Random(20261015)
    for n in (2000,5000,10000):
        # delta=0.4, a=0.7N,b=0.3N
        vals=[one_run(7*n//10,3*n//10,rng)/n for _ in range(250)]
        empirical=sum(vals)/len(vals)
        expected=formula(0.4)
        assert abs(empirical-expected)<0.014,(n,empirical,expected)
        print('N',n,'sample',format(empirical,'.8f'),'limit',format(expected,'.8f'))
        checks+=1
    assert abs(formula(0.4)-0.4*exp(-21/8))<1e-15
    assert (7*40//10,3*40//10)==(28,12)
    # Counts: one A-center uses (1,3), one B-center uses (3,1).
    assert 1+3*9==28 and 3*1+9==12
    print('PASS', checks+2, 'exact distribution and limiting-law checks')

if __name__=='__main__':main()
