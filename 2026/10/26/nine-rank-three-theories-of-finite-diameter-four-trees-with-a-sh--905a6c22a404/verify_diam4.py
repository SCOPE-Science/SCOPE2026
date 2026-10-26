"""Exact rank-three type census for finite trees of diameter four.
Only standard-library Python required. No external data or computational resource.
"""
from itertools import product
from collections import defaultdict,Counter


def construct(m):
    """One center and m[t] branches whose centers have t pendent leaves."""
    n=1+sum(m[t]*(t+1) for t in range(4))
    a=[0]*n; j=1
    for t in range(4):
        for _ in range(m[t]):
            b=j; j+=1
            a[0] |= 1<<b; a[b]|=1
            for _ in range(t):
                z=j; j+=1
                a[b] |=1<<z; a[z]|=1<<b
    assert j==n
    return tuple(a)


def compact_type(a):
    n=len(a); allbits=(1<<n)-1; s=set()
    for x in range(n):
        sig=set(); mask=a[x]
        sig.add((2,(1 if mask else 0)|(2 if (allbits &~(1<<x)&~mask) else 0)))
        for y in range(n):
            if y==x:continue
            yy=a[y]; remaining=allbits ^ (1<<x) ^ (1<<y)
            flags=0
            for bit,pattern in enumerate((mask&yy,mask&~yy,~mask&yy,~mask&~yy)):
                if pattern&remaining:flags |=1<<bit
            sig.add((1 if (mask>>y)&1 else 0,flags))
        s.add(tuple(sorted(sig)))
    return frozenset(s)


def generic_type(a):
    """Independent recursion on literal equality/adjacency atomic diagrams."""
    n=len(a)
    def atomic(t):
        return tuple((int(t[i]==t[j]),int((a[t[i]]>>t[j])&1))
                     for i in range(len(t)) for j in range(i+1,len(t)))
    return frozenset(
        frozenset(
            frozenset(atomic((x,y,z)) for z in range(n))
            for y in range(n))
        for x in range(n))


def classify():
    types=defaultdict(list)
    generic_by_compact={}
    cases=0
    for m in product(range(4),repeat=4):
        if sum(m[1:])<2: continue
        g=construct(m)
        c=compact_type(g)
        p=generic_type(g)
        if c in generic_by_compact:
            assert generic_by_compact[c]==p
        else:
            assert p not in generic_by_compact.values()
            generic_by_compact[c]=p
        types[c].append((len(g),m))
        cases+=1
    best=sorted(min(q) for q in types.values())
    print('canonical_trees:',cases)
    print('distinct_rank3_types:',len(types))
    print('minimal_representatives:',best)
    print('minimal_size_histogram:',sorted(Counter(x for x,m in best).items()))
    assert cases==240 and len(types)==9
    assert [x for x,m in best]==[5,6,6,7,7,7,8,9,10]
    return types,best


def ef3(a,b):
    """Literal three-round EF recursion, neither of the signature functions."""
    from functools import lru_cache
    n,m=len(a),len(b)
    @lru_cache(None)
    def play(X,Y,k):
        for i in range(len(X)):
            for j in range(i):
                if (X[i]==X[j]) != (Y[i]==Y[j]):return False
                if bool(a[X[i]]&(1<<X[j])) !=bool(b[Y[i]]&(1<<Y[j])):return False
        if k==0: return True
        for x in range(n):
            if not any(play(X+(x,),Y+(y,),k-1) for y in range(m)):
                return False
        for y in range(m):
            if not any(play(X+(x,),Y+(y,),k-1) for x in range(n)):
                return False
        return True
    return play((),(),3)

if __name__=='__main__':
    types,best=classify()
    reps=[construct(m) for n,m in best]
    for i,a in enumerate(reps):
        for j,b in enumerate(reps):
            assert ef3(a,b)==(i==j),(i,j)
    print('EF pairwise cross-check:',len(reps)**2,'games')
    print('VERIFY_OK')
