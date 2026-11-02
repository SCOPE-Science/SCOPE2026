#!/usr/bin/env python3
"""Exact enumeration for adjacent-swap robustness in strict square marriage markets."""
from itertools import permutations, product
from collections import Counter
from fractions import Fraction


def study(n):
    orders=list(permutations(range(n)))
    allmatch=orders
    idx={p:k for k,p in enumerate(orders)}
    rank=[tuple(p.index(a) for a in range(n)) for p in orders]
    swaps=[[idx[p[:k]+(p[k+1],p[k])+p[k+2:]] for k in range(n-1)] for p in orders]
    tally=Counter()
    total=0
    for profile in product(range(len(orders)),repeat=2*n):
        pr=[rank[v] for v in profile]
        stable=[]
        for m in allmatch:
            reverse=[0]*n
            for a,b in enumerate(m):reverse[b]=a
            if all(not (pr[a][b]<pr[a][m[a]] and pr[n+b][a]<pr[n+b][reverse[b]])
                   for a in range(n) for b in range(n)):
                stable.append(m)
        assert stable
        for person in range(2*n):
            for pos in range(n-1):
                altered=profile[:person]+(swaps[profile[person]][pos],)+profile[person+1:]
                newrank=[rank[v] for v in altered]
                local=[]
                for m in stable:
                    if person<n:
                        a=person
                        x,y=orders[profile[person]][pos:pos+2]
                        survive=(m[a]!=x or newrank[n+y][a]>newrank[n+y][m.index(y)])
                    else:
                        b=person-n
                        x,y=orders[profile[person]][pos:pos+2]
                        survive=(m.index(b)!=x or newrank[y][b]>newrank[y][m[y]])
                    # The rank of the other side was not altered; strict > means no new block.
                    direct=True
                    reverse=[m.index(b) for b in range(n)]
                    for a in range(n):
                        for b in range(n):
                            if newrank[a][b]<newrank[a][m[a]] and newrank[n+b][a]<newrank[n+b][reverse[b]]:
                                direct=False
                    assert survive==direct, (n,profile,person,pos,m)
                    if direct:local.append(m)
                tally[(pos,len(stable),len(local))]+=1
                total+=1
    bybase=Counter()
    byrobust=Counter()
    bypos=Counter()
    for (pos,s,r),count in tally.items():
        bybase[(s,r)]+=count
        byrobust[r]+=count
        bypos[(pos,r)]+=count
    return dict(sorted(tally.items())),dict(sorted(bybase.items())),dict(sorted(byrobust.items())),dict(sorted(bypos.items())),total

if __name__=='__main__':
    for n in (2,3):
        allrows,bybase,byrobust,bypos,total=study(n)
        print('n=',n,'total=',total)
        print('bybase=',bybase)
        print('byrobust=',byrobust)
        print('bypos=',bypos)
        print('failure=',Fraction(byrobust.get(0,0),total))
        if n==2:
            assert total==64
            assert bybase=={(1,0):16,(1,1):40,(2,1):8}
        if n==3:
            assert total==559872
            assert bybase=={(1,0):64944,(1,1):344016,(2,0):5616,(2,1):49536,(2,2):82656,(3,1):1872,(3,2):7344,(3,3):3888}
            assert byrobust=={0:70560,1:395424,2:90000,3:3888}
            assert bypos[(0,0)]==49248 and bypos[(1,0)]==21312
    print('PASS: every altered matching independently checked against the local adjacent-swap criterion')
