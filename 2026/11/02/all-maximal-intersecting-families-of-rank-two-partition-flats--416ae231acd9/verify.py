"""Independent finite checks for maximal pair-intersecting rank-two partitions.
Run with `python verify_partition.py`. No third-party dependencies.
"""
from itertools import combinations
from math import comb
from collections import Counter


def flats(n):
    items=[]
    for v in combinations(range(n),3):
        items.append(frozenset(combinations(v,2)))
    for v in combinations(range(n),4):
        a,b,c,d=v
        for x,y in [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]:
            items.append(frozenset((x,y)))
    return items


def maximal_cliques(flats):
    count=len(flats)
    adj=[]
    for i in range(count):
        adj.append(sum(1 << j for j in range(count) if i!=j and flats[i]&flats[j]))
    res=[]
    def bk(r,p,x):
        if not p and not x:
            res.append(r)
            return
        union=p|x
        if union:
            pivot=max((i for i in range(count) if union>>i&1),key=lambda i:(p&adj[i]).bit_count())
            cand=p&~adj[pivot]
        else:cand=p
        while cand:
            bit=cand&-cand
            v=bit.bit_length()-1
            bk(r|bit,p&adj[v],x&adj[v])
            p&=~bit;x|=bit;cand&=~bit
    bk(0,(1<<count)-1,0)
    return res


def run():
    for n in range(4,8):
        arr=flats(n)
        actual=Counter(mask.bit_count() for mask in maximal_cliques(arr))
        expected=Counter()
        expected[5]+=3*comb(n,4)
        if n>=5:
            expected[4]+=10*comb(n,5)
            expected[comb(n-1,2)]+=comb(n,2)
        if n>=6:
            expected[3]+=15*comb(n,6)
        if actual!=expected:
            raise AssertionError((n,actual,expected))
        print('DIRECT_MAXIMAL_CLIQUES_OK',n,len(arr),dict(sorted(actual.items())))
    # Independently check pair-of-atoms uniqueness, crucial for the proof.
    for n in range(4,8):
        arr=flats(n)
        occurrences={}
        for A in arr:
            for e,f in combinations(sorted(A),2):
                occurrences[(e,f)]=occurrences.get((e,f),0)+1
        assert all(v==1 for v in occurrences.values()),n
        print('PAIR_DETERMINES_FLAT_OK',n)
    print('VERIFY_OK')
if __name__=='__main__':run()
