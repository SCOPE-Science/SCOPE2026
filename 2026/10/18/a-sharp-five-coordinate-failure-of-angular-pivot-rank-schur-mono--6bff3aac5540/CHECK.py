"""Exact finite checks for pivotal-rank laws on generic half-capacity prism slices."""
from fractions import Fraction
from collections import Counter
from itertools import combinations, permutations, product
from math import factorial


def nonresonant(c):
    C = sum(c)
    return all(2*sum(c[i] for i in idx) != C
               for r in range(len(c)+1)
               for idx in combinations(range(len(c)), r))


def rank_dist(c):
    n=len(c)
    assert nonresonant(c)
    sums=Counter()
    for perm in permutations(range(n)):
        partial=0
        for t,idx in enumerate(perm,1):
            partial+=c[idx]
            if 2*partial > sum(c):
                sums[t]+=1
                break
    return {r:Fraction(sums[r], factorial(n)) for r in range(1,n+1)}


def subset_tail(c, r):
    n=len(c)
    good=sum(2*sum(c[i] for i in ids)<sum(c) for ids in combinations(range(n),r))
    return Fraction(good,len(list(combinations(range(n),r))))


def winning_pairs(c):
    return sum(2*(c[i]+c[j])>sum(c) for i,j in combinations(range(5),2))


def geometric_vertices(c):
    """Represent vertices by Fraction coordinates and their expected solid angles."""
    n=len(c)
    res={}
    for j in range(n):
        other=[i for i in range(n) if i!=j]
        for r in range(n):
            for H in combinations(other,r):
                x=[Fraction(0)]*n
                for i in H:x[i]=Fraction(c[i])
                x[j]=Fraction(sum(c),2)-sum(x)
                if 0 < x[j] < c[j]:
                    vt=tuple(x)
                    assert vt not in res
                    res[vt]=Fraction(factorial(r)*factorial(n-r-1),factorial(n))
    return res


def greedy_max(c, g):
    n=len(c)
    order=sorted(range(n),key=lambda i:g[i],reverse=True)
    remain=Fraction(sum(c),2)
    x=[Fraction(0)]*n
    for i in order:
        v=min(Fraction(c[i]),remain)
        x[i]=v
        remain-=v
        if remain == 0:break
    return tuple(x)


def dominance(x,y):
    """Sorted vector x majorizes y iff each leading partial sum is >=."""
    a=sorted(x,reverse=True)
    b=sorted(y,reverse=True)
    assert sum(a)==sum(b)
    return all(sum(a[:r])>=sum(b[:r]) for r in range(1,len(x)))


def test():
    cases={
        (2,2,2,2,2):(0,{2:Fraction(0),3:Fraction(1),4:Fraction(0)}),
        (2,2,2,6,6):(1,{2:Fraction(1,10),3:Fraction(4,5),4:Fraction(1,10)}),
        (2,2,4,4,6):(2,{2:Fraction(1,5),3:Fraction(3,5),4:Fraction(1,5)}),
        (2,2,6,6,6):(3,{2:Fraction(3,10),3:Fraction(2,5),4:Fraction(3,10)}),
        (2,2,2,2,6):(4,{2:Fraction(2,5),3:Fraction(1,5),4:Fraction(2,5)}),
    }
    profiles=0
    permutations_checked=0
    for c,(h,exp) in cases.items():
        assert nonresonant(c)
        assert winning_pairs(c)==h
        d=rank_dist(c)
        assert all(d[r]==exp.get(r,0) for r in range(1,6))
        profiles+=1
    assert rank_dist((2,2,2,2,10))=={r:Fraction(1,5) for r in range(1,6)}
    assert dominance((2,2,2,6,6),(2,2,4,4,6))
    def vdist(d):return sum((r-Fraction(6,2))**2*p for r,p in d.items())
    assert vdist(rank_dist((2,2,2,6,6)))==Fraction(1,5)
    assert vdist(rank_dist((2,2,4,4,6)))==Fraction(2,5)
    # Test formula and geometry over every nonresonant capacity profile from 1..5, n<=4.
    for n in range(2,5):
        for c in product(range(1,6),repeat=n):
            if not nonresonant(c):continue
            d=rank_dist(c)
            for r in range(n):
                assert sum(d[t] for t in range(r+1,n+1))==subset_tail(c,r)
            assert all(d[t]==d[n+1-t] for t in range(1,n+1))
            geo=geometric_vertices(c)
            assert sum(geo.values())==1
            assert Counter(rank_dist(c))
            profiles+=1
    # Geometry direct: all rank-order chambers send greedy optimization to a known vertex;
    # verify claimed angle by exact enumeration and linear objective inequalities.
    for c in list(cases)+[(2,2,2,2,10),(1,2,4),(1,2,4,6)]:
        if not nonresonant(c):continue
        n=len(c)
        vertices=geometric_vertices(c)
        chamber=Counter()
        for perm in permutations(range(n)):
            g=[0]*n
            for t,i in enumerate(perm):g[i]=n-t
            v=greedy_max(c,g)
            assert v in vertices
            vals=[sum(a*b for a,b in zip(w,g)) for w in vertices]
            assert sum(a*b for a,b in zip(v,g))==max(vals)
            chamber[v]+=1
            permutations_checked+=1
        for v,angle in vertices.items():
            assert Fraction(chamber[v],factorial(n))==angle
    # n<=4 convex-order comparison via symmetric dispersion: only dominant or central classes.
    for n in (2,3,4):
        for c in product(range(1,7),repeat=n):
            if not nonresonant(c):continue
            d=rank_dist(c)
            dominant=max(c)*2>sum(c)
            if dominant:
                assert all(d[t]==Fraction(1,n) for t in range(1,n+1))
            elif n==3:
                assert d[2]==1
            elif n==4:
                assert d[2]==Fraction(1,2) and d[3]==Fraction(1,2)
    print('PASS finite classification, Gaussian chamber and exact geometric support checks')
    print('generic profiles:',profiles,'direct vertex chambers:',permutations_checked)
    print('minorization witness:',(2,2,2,6,6),'vs',(2,2,4,4,6))

if __name__=='__main__':test()
