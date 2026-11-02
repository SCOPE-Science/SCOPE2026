"""Exact finite checks for motif-count/isolated-count covariance laws.
Only Python standard library is required.
"""
from itertools import combinations, permutations
from fractions import Fraction
from math import comb, factorial, log


def falling(a, b):
    out = 1
    for j in range(b):
        out *= a-j
    return out


def masks_for_h(n, v, h_edges):
    eidx = {pair:i for i,pair in enumerate(combinations(range(n),2))}
    masks = set()
    for pts in permutations(range(n), v):
        m = 0
        for x,y in h_edges:
            m |= 1 << eidx[tuple(sorted((pts[x],pts[y])))]
        masks.add(m)
    return sorted(masks)


def predictions(n, m, v, ee, copies):
    N = comb(n, 2)
    P = comb(n-1,2)
    pi = Fraction(comb(P,m),comb(N,m)) if m <= P else Fraction(0)
    mi = n*pi
    mx = Fraction(copies*falling(m,ee),falling(N,ee)) if m >= ee else Fraction(0)
    if mi*mx == 0:
        cov = Fraction(0)
    else:
        ratio=Fraction(n-v,n) * Fraction(falling(N,ee),falling(P,ee))
        cov=mi*mx*(ratio-1)
    return mi,mx,cov


def check():
    patterns={
        'edge':(2,[(0,1)]),
        'P3':(3,[(0,1),(1,2)]),
        'K3':(3,[(0,1),(0,2),(1,2)]),
        'P4':(4,[(0,1),(1,2),(2,3)]),
        'star4':(4,[(0,1),(0,2),(0,3)]),
        'K4':(4,list(combinations(range(4),2))),
    }
    checks=0
    graphs=0
    for n in (4,5,6):
        N=comb(n,2)
        deg_masks=[sum(1<<i for i,pair in enumerate(combinations(range(n),2)) if u in pair) for u in range(n)]
        subset_masks={name: masks_for_h(n,v,edges) for name,(v,edges) in patterns.items() if v<n}
        agg={m:{name:[0,0,0] for name in subset_masks} for m in range(N+1)}
        size={m:0 for m in range(N+1)}
        for g in range(1<<N):
            m=g.bit_count()
            I=sum(1 for d in deg_masks if g&d==0)
            size[m]+=1
            graphs+=1
            for name,ms in subset_masks.items():
                X=sum(1 for h in ms if (g&h)==h)
                a=agg[m][name]
                a[0]+=I;a[1]+=X;a[2]+=I*X
        for m in range(N+1):
            assert size[m]==comb(N,m)
            checks+=1
            for name,(sumI,sumX,sumIX) in agg[m].items():
                v,edges=patterns[name]
                ei,ex,co=predictions(n,m,v,len(edges),len(subset_masks[name]))
                den=size[m]
                assert Fraction(sumI,den)==ei,(n,m,name,'I')
                assert Fraction(sumX,den)==ex,(n,m,name,'X')
                assert Fraction(sumIX,den)-Fraction(sumI*sumX,den**2)==co,(n,m,name,'cov')
                checks+=3
    # Exact tree universal sign check plus unimodality: ratio at v=2 is unity,
    # grows up to midpoint and decreases thereafter.
    for n in range(4,101):
        N=comb(n,2);P=comb(n-1,2)
        ratios=[]
        for v in range(2,n):
            ratio=Fraction(n-v,n)*Fraction(falling(N,v-1),falling(P,v-1))
            ratios.append(ratio)
            checks+=1
        assert ratios[0]==1
        for v in range(2,n-1):
            delta = Fraction(n-2,2)*(n+1-2*v)
            direction=1 if delta>0 else -1 if delta<0 else 0
            actual=1 if ratios[v-1]>ratios[v-2] else -1 if ratios[v-1]<ratios[v-2] else 0
            assert direction==actual, (n,v)
            checks+=1
    # Root of 2a+log(1-a)=0 and asymptotic sign.
    lo,hi=0.7,0.9
    for _ in range(100):
        mid=(lo+hi)/2
        if 2*mid+log(1-mid)>0:lo=mid
        else:hi=mid
    alpha=(lo+hi)/2
    assert abs(alpha-0.79681213002002)<1e-12
    checks+=1
    print('VERIFY_OK', 'graphs',graphs,'assertions',checks,'alpha',format(alpha,'.14f'))


if __name__=='__main__':
    check()
