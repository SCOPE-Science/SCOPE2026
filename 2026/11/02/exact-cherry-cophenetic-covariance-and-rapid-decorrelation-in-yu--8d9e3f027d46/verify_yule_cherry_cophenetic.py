"""Exact verification of cherry--cophenetic covariance in Yule random trees.

The enumerator performs uniform leaf splitting and aggregates unordered tree
shapes at each size, with exact rational probabilities. A separately written
root-split moment recurrence checks the claimed closed form at larger sizes.
Python 3 standard library only.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb


def normalize(t):
    if t is None:
        return None
    a,b=normalize(t[0]),normalize(t[1])
    return (a,b) if repr(a)<=repr(b) else (b,a)


def leaves(t,path=()):
    if t is None:
        yield path
        return
    yield from leaves(t[0],path+(0,))
    yield from leaves(t[1],path+(1,))


def grow_at(t,path):
    if not path:
        assert t is None
        return (None,None)
    if path[0]==0:
        return normalize((grow_at(t[0],path[1:]),t[1]))
    return normalize((t[0],grow_at(t[1],path[1:])))


def grow(dist,n):
    out=defaultdict(F)
    for t,p in dist.items():
        positions=list(leaves(t))
        assert len(positions)==n
        for path in positions:
            out[grow_at(t,path)]+=p/n
    assert sum(out.values())==1
    return dict(out)


def tree_stats(t):
    """Return number of leaves, cherry count, cophenetic sum."""
    if t is None:
        return 1,0,0
    na,ca,pa=tree_stats(t[0])
    nb,cb,pb=tree_stats(t[1])
    cherry=int(na==1 and nb==1)
    return na+nb,ca+cb+cherry,pa+pb+comb(na,2)+comb(nb,2)


def independent_phi(t):
    """Directly sum common-prefix lengths over all pairs of leaf paths."""
    paths=list(leaves(t))
    total=0
    for a in range(len(paths)):
        for b in range(a+1,len(paths)):
            total+=next((i for i,(x,y) in enumerate(zip(paths[a],paths[b])) if x!=y),
                        min(len(paths[a]),len(paths[b])))
    return total


def closed(n):
    return F(0) if n<=3 else -F((n-3)*(5*n-8),9*(n-1))


def verify():
    checks=0
    dist={(None,None):F(1)}
    for n in range(2,15):
        ec=ep=ecp=F(0)
        for t,p in dist.items():
            nt,c,phi=tree_stats(t)
            assert nt==n; checks+=1
            if n<=11:
                assert phi==independent_phi(t); checks+=1
            ec+=p*c;ep+=p*phi;ecp+=p*c*phi
        h=sum((F(1,k) for k in range(1,n+1)),F(0))
        assert ep==n*(n-1)-2*n*(h-1); checks+=1
        assert ec==(F(1) if n==2 else F(n,3));checks+=1
        assert ecp-ec*ep==closed(n);checks+=1
        if n<14:
            dist=grow(dist,n)
    # Independent first/mixed moment recursion from the uniform root split.
    c={1:F(0),2:F(1)}
    phi={1:F(0),2:F(0)}
    cp={1:F(0),2:F(0)}
    for n in range(3,301):
        c[n]=sum((c[k]+c[n-k] for k in range(1,n)),F(0))/(n-1)
        phi[n]=sum((phi[k]+phi[n-k]+comb(k,2)+comb(n-k,2) for k in range(1,n)),F(0))/(n-1)
        cp[n]=sum((cp[k]+cp[n-k]+c[k]*phi[n-k]+c[n-k]*phi[k]
                   +(c[k]+c[n-k])*(comb(k,2)+comb(n-k,2))
                   for k in range(1,n)),F(0))/(n-1)
        assert cp[n]-c[n]*phi[n]==closed(n);checks+=1
    print('PASS:',checks,'exact integer/rational assertions')
    print('PASS: full Yule shape distribution through n=14 and independent pairwise-LCA computation through n=11')
    print('PASS: separate recursive moments through n=300')
    print('Sample values: n=4: -4/9; n=5: -17/18; n=10: -98/27')


if __name__=='__main__':
    verify()
