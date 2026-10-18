"""Finite exact tests for rank and incidence formulas on odd prime-power Fourier matrices.
Runs with Python 3 standard library; all determinant tests use integer cyclotomic reductions.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction


def vp_diff(a, b, p, m):
    d=(a-b)%(p**m)
    assert d
    k=0
    while d%p==0:
        d//=p;k+=1
    return k


def typ(T, p, m):
    z=[vp_diff(a,b,p,m) for a,b in combinations(T,2)]
    return min(z),max(z)


def predicted(u,v,s,t,m):
    if u+s>=m: return 1
    return 2 if v+s>=m or u+t>=m else 3


def exact_cyclotomic_zero(pos,neg,p,m):
    N=p**m;step=N//p
    c=Counter([x%N for x in pos]);c.subtract([x%N for x in neg]);
    for residue in {x%step for x in c}:
        vals=[c.get(residue+k*step,0) for k in range(p)]
        if any(x!=vals[0] for x in vals[1:]):
            return False
    return True


def actual_rank_normalized(u,v,s,t,p,m):
    N=p**m
    # All 2-by-2 minors vanish iff every pair of row and column differences multiply to zero.
    rd=(u,v,v-u);cd=(s,t,t-s)
    if all((r*c)%N==0 for r in rd for c in cd): return 1
    pos=(u*s+v*t,u*t,v*s)
    neg=(u*t+v*s,u*s,v*t)
    if exact_cyclotomic_zero(pos,neg,p,m): return 2
    return 3


def count_type(p,m,u,v):
    if u==v: return (p-1)*(p-2)*p**(3*m-2*u-2)//6
    return (p-1)**2*p**(3*m-u-v-2)//2


def formula_counts(p,m):
    B=[(u,v,count_type(p,m,u,v)) for u in range(m) for v in range(u,m)]
    h=Counter()
    for u,v,a in B:
        for s,t,b in B:
            h[predicted(u,v,s,t,m)]+=a*b
    return h


def run():
    tally=0
    for p,m in [(5,2),(7,2)]:
        N=p**m
        obs=Counter(typ(T,p,m) for T in combinations(range(N),3))
        for u in range(m):
            for v in range(u,m):
                assert obs[u,v]==count_type(p,m,u,v)
                tally+=1
        C=formula_counts(p,m)
        assert sum(C.values())==(N*(N-1)*(N-2)//6)**2
        if p==5: assert C[1]+C[2]==102500
        print('type_count',p,m,'ranks',dict(C))
    for p,m in [(5,2),(7,2)]:
        N=p**m
        for u,v in combinations(range(1,N),2):
            ru,rv=typ((0,u,v),p,m)
            for s,t in combinations(range(1,N),2):
                cu,cv=typ((0,s,t),p,m)
                expect=predicted(ru,rv,cu,cv,m)
                got=actual_rank_normalized(u,v,s,t,p,m)
                assert expect==got, (p,m,u,v,s,t,expect,got)
                tally+=1
        print('determinants',p,m,'normalized exhaustive')
    # Entire group larger sample, deterministic offsets and step sizes.
    for p,m in [(5,3),(7,3)]:
        N=p**m
        vals=[1,2,3,p,p+1,p*p,N//p,N//p+1,N//p*2, N-1,N-2]
        pairs=[(a,b) for a,b in combinations(vals,2) if 0<a<b<N]
        for u,v in pairs:
            ru,rv=typ((0,u,v),p,m)
            for s,t in pairs:
                cu,cv=typ((0,s,t),p,m)
                expect=predicted(ru,rv,cu,cv,m)
                got=actual_rank_normalized(u,v,s,t,p,m)
                assert expect==got,(p,m,u,v,s,t,expect,got)
                tally+=1
        print('determinants',p,m,'selected exact cases',len(pairs)**2)
    for p in (5,7,11):
        last=0
        for m in range(1,9):
            N=p**m
            h=formula_counts(p,m)
            total=(N*(N-1)*(N-2)//6)**2
            assert sum(h.values())==total
            if m==1: assert h[1]+h[2]==0
            last=float(Fraction((h[1]+h[2])*N,total))
            tally+=3
        assert abs(last-6/p)<0.002,(p,last,6/p)
        print('asymptotic sample',p, last,'target',6/p)
    print('VERIFY_OK',tally,'exact comparisons and integer checks')

if __name__=='__main__':run()
