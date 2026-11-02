"""Exact, standalone verification of a rank-resolved BST leaf/path covariance."""
from fractions import Fraction as Q
from itertools import permutations


def proposed(n, r):
    if not 1 <= r <= n or n < 2:
        raise ValueError((n, r))
    if r == 1 or r == n:
        return Q(-(n-2), 2*n)
    return (Q(-1,9)+Q(2,3*r*(r+1))+
            Q(2,3*(n-r+1)*(n-r+2)))


def binary_search_tree_statistics(order):
    n=len(order)
    children=[[None,None] for _ in range(n+1)]
    depth=[0]*(n+1)
    root=order[0]
    for key in order[1:]:
        here=root
        while True:
            side=int(key>here)
            nxt=children[here][side]
            if nxt is None:
                children[here][side]=key
                depth[key]=depth[here]+1
                break
            here=nxt
    path=sum(depth)
    leaf=tuple(int(children[r]==[None,None]) for r in range(1,n+1))
    return path,leaf


def exhaustive():
    checks=0
    for n in range(2,9):
        count=0
        p_sum=0
        leaf_sum=[0]*n
        pl_sum=[0]*n
        for order in permutations(range(1,n+1)):
            p, flags=binary_search_tree_statistics(order)
            count+=1
            p_sum+=p
            for j,flag in enumerate(flags):
                leaf_sum[j]+=flag
                pl_sum[j]+=p*flag
        covs=[Q(pl_sum[j],count)-Q(leaf_sum[j]*p_sum,count*count) for j in range(n)]
        for j,c in enumerate(covs,1):
            assert c==proposed(n,j),(n,j,c,proposed(n,j))
            checks+=1
        expected_total=Q(-(n-2)*(n+3),9*n)
        assert sum(covs)==expected_total,(n,sum(covs),expected_total)
        checks+=1
    return checks


def recurrence_check():
    bound=120
    mp=[Q(0)]*(bound+1)
    ml=[Q(0)]*(bound+1)
    mpl=[Q(0)]*(bound+1)
    ml[1]=Q(1)
    for n in range(2,bound+1):
        for j in range(n):
            k=n-1-j
            w=Q(1,n)
            mp[n]+=w*(mp[j]+mp[k]+n-1)
            ml[n]+=w*(ml[j]+ml[k])
            mpl[n]+=w*(mpl[j]+mpl[k]+mp[j]*ml[k]+mp[k]*ml[j]+(n-1)*(ml[j]+ml[k]))
        assert mpl[n]-mp[n]*ml[n]==sum(proposed(n,r) for r in range(1,n+1)),n
    return bound-1


def local_algebra_check():
    # These three probability-shift formulas are derived by beta integration.
    # Independently compare their telescoping finite sums with the proposed profile.
    def a(k): return Q((k-2)*(k+4),2*k*(k+1)*(k+2))
    def b(k): return Q(-(2*k+1),2*k*(k+1))
    checks=0
    for l in range(1,100):
        s=sum((a(k) for k in range(2,l+1)),Q(0))
        s+=sum((b(k) for k in range(3,l+2)),Q(0))
        s+=sum((Q(1,2*k) for k in range(4,l+3)),Q(0))
        assert s==Q(-1,3)+Q(2,(l+1)*(l+2)),(l,s)
        checks+=1
    for n in range(2,200):
        for r in range(1,n+1):
            c=proposed(n,r)
            if n>=6:
                if r==2 or r==n-1:
                    assert c>0
                else:
                    assert c<0
            checks+=1
    return checks


if __name__=='__main__':
    counts=(exhaustive(),recurrence_check(),local_algebra_check())
    print('PASS exact checks (exhaustive, independent recurrence, local telescoping and sign):',counts,'total',sum(counts))
