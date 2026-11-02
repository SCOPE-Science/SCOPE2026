#!/usr/bin/env python3
"""Reproduce exact three-person diversity-popularity classification.

No third-party dependencies.  The Hungarian assignment computes the most favorable
label matching for a challenger in every possible room-composition profile.
"""
from itertools import combinations_with_replacement
from math import factorial

def compositions(m,s,r):
    return [tuple(c.count(j) for j in range(s+1))
            for c in combinations_with_replacement(range(s+1),m)
            if sum(c)==r]

def canonical(m,r,s=3):
    q,h=divmod(r,m)
    return tuple((m-h if j==q else 0)+(h if j==q+1 else 0) for j in range(s+1))

def hungarian_min(a):
    n=len(a)
    if not n:return 0
    u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
    for i in range(1,n+1):
        p[0]=i;j0=0;minv=[10**12]*(n+1);used=[False]*(n+1)
        while True:
            used[j0]=True;i0=p[j0];delta=10**12;j1=0
            for j in range(1,n+1):
                if not used[j]:
                    cur=a[i0-1][j-1]-u[i0]-v[j]
                    if cur<minv[j]:minv[j]=cur;way[j]=j0
                    if minv[j]<delta:delta=minv[j];j1=j
            for j in range(n+1):
                if used[j]:u[p[j]]+=delta;v[j]-=delta
                else:minv[j]-=delta
            j0=j1
            if p[j0]==0:break
        while True:
            j1=way[j0];p[j0]=p[j1];j0=j1
            if j0==0:break
    return -v[0]

def max_vote_margin(src,dst,s,red):
    before=[j for j,n in enumerate(src) for _ in range(n*(j if red else s-j))]
    after=[j for j,n in enumerate(dst) for _ in range(n*(j if red else s-j))]
    if not before:return 0
    # Negative margin is the assignment cost to minimize.
    def vote(j,k):
        diff=(j-k) if red else (k-j)
        return 1 if diff>0 else (-1 if diff<0 else 0)
    cost=[[-vote(j,k) for k in after] for j in before]
    return -hungarian_min(cost)

def full_margin(src,dst,s):
    return sum(max_vote_margin(src,dst,s,red) for red in (True,False))

def count_parts(x,s):
    r=sum(j*x[j] for j in range(s+1))
    b=sum((s-j)*x[j] for j in range(s+1))
    d=1
    for j,q in enumerate(x):d*=factorial(j)**q * factorial(s-j)**q *factorial(q)
    assert (factorial(r)*factorial(b))%d==0
    return factorial(r)*factorial(b)//d

def labeled_partitions(items):
    if not items:
        yield ()
        return
    from itertools import combinations
    first=items[0]
    for pair in combinations(items[1:],2):
        remaining=tuple(j for j in items[1:] if j not in pair)
        for rest in labeled_partitions(remaining):
            yield ((first,)+pair,)+rest

def direct_labeled_test():
    checked=0
    for m in range(1,4):
        partitions=list(labeled_partitions(tuple(range(3*m))))
        for redcount in range(3*m+1):
            def utilities(partition):
                utility=[0]*(3*m)
                for room in partition:
                    reds=sum(j<redcount for j in room)
                    for agent in room:
                        utility[agent]=3-reds if agent<redcount else reds
                return utility
            outcomes=[utilities(p) for p in partitions]
            hmax=min(m,redcount,3*m-redcount)
            for index,part in enumerate(partitions):
                a=outcomes[index]
                expected=sum(0<sum(j<redcount for j in room)<3 for room in part)==hmax
                observed=True
                for b in outcomes:
                    if sum(y>x for x,y in zip(a,b))>sum(y<x for x,y in zip(a,b)):
                        observed=False
                        break
                assert observed==expected,(m,redcount,part)
            checked+=1
    print('DIRECT_LABELED_ENUMERATION_OK',checked,'profiles; room counts 1..3')

def run():
    profiles=0;pairs=0;one_side_strict=0
    for m in range(1,8):
        for r in range(3*m+1):
            xstar=canonical(m,r)
            cfgs=compositions(m,3,r)
            assert xstar in cfgs
            for src in cfgs:
                actual=all(full_margin(src,dst,3)<=0 for dst in cfgs)
                desired=(src==xstar)
                assert actual==desired, (m,r,src,actual)
                pairs+=len(cfgs)
                if src != xstar:
                    assert full_margin(xstar,src,3)<0, (m,r,src)
                    one_side_strict+=1
            profiles+=len(cfgs)
            total=factorial(3*m)//(factorial(3)**m*factorial(m))
            assert sum(count_parts(z,3) for z in cfgs)==total
    sparse_profiles=0
    for s in range(2,8):
        for m in range(1,7):
            for r in range(m+1):
                star=canonical(m,r,s)
                choices=compositions(m,s,r)
                assert star in choices
                for src in choices:
                    is_popular=all(full_margin(src,dst,s)<=0 for dst in choices)
                    assert is_popular==(src==star),(s,m,r,src)
                    if src!=star:assert full_margin(star,src,s)<0
                    sparse_profiles+=1
    print('SPARSE_GENERAL_CHECK_OK',sparse_profiles,'composition profiles with room size 2..7 and rooms 1..6')
    print('TRIPLES_COMPOSITION_CHECK_OK',profiles,'profiles;',pairs,'comparisons;',one_side_strict,'noncanonical profiles')
    print('Exact popular counts:',[(m,r,count_parts(canonical(m,r),3)) for m,r in [(2,3),(3,3),(3,4),(4,6)]])
    direct_labeled_test()

if __name__=='__main__':
    run()
