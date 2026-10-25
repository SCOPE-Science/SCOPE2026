"""Standalone finite checks of four primitive intuitionistic modalities on chains.
Run with Python 3.10 or later: python checker.py
"""
from collections import defaultdict, Counter
from itertools import product
from math import prod


def endpoints(rows, n):
    return tuple(min(r) if r else n for r in rows), tuple(max(r) if r else -1 for r in rows)


def signature(rows, n):
    a, b = endpoints(rows, n)
    prefix_u, prefix_l, suffix_l, suffix_u = [], [], [None]*n, [None]*n
    mxu, mxl = -1, -1
    for i in range(n):
        mxu = max(mxu, b[i])
        mxl = max(mxl, a[i])
        prefix_u.append(mxu)
        prefix_l.append(mxl)
    mnl, mnu = n, n
    for i in range(n-1,-1,-1):
        mnl = min(mnl, a[i]); mnu = min(mnu, b[i])
        suffix_l[i] = mnl; suffix_u[i] = mnu
    return tuple(prefix_u), tuple(suffix_l), tuple(suffix_u), tuple(prefix_l)


def direct_ops(rows, n, k):
    U = set(range(k,n))
    ans=[]
    for i in range(n):
        below=range(i+1); above=range(i,n)
        ans.append((
            any(any(v in U for v in rows[t]) for t in below),
            all(all(v in U for v in rows[t]) for t in above),
            all(any(v in U for v in rows[t]) for t in above),
            any(all(v in U for v in rows[t]) for t in below),
        ))
    return tuple(ans)


def signature_ops(sig, n, k):
    pu,sl,su,pl=sig
    return tuple((pu[i]>=k,sl[i]>=k,su[i]>=k,pl[i]>=k) for i in range(n))


def valid_pair(a,b,n):
    return (a==n and b==-1) or (0 <= a <= b < n)


def row_count(a,b,n):
    if a==n and b==-1: return 1
    if a==b: return 1
    return 2**(b-a-1)


def local_choices(sig,n,i):
    pu,sl,su,pl=sig
    prev_u= -1 if i==0 else pu[i-1]
    prev_l= -1 if i==0 else pl[i-1]
    next_l= n if i==n-1 else sl[i+1]
    next_u= n if i==n-1 else su[i+1]
    return [(a,b) for a in range(n+1) for b in range(-1,n)
            if valid_pair(a,b,n)
            and max(prev_u,b)==pu[i]
            and max(prev_l,a)==pl[i]
            and min(a,next_l)==sl[i]
            and min(b,next_u)==su[i]]


def fiber_count(sig,n):
    return prod(sum(row_count(a,b,n) for a,b in local_choices(sig,n,i)) for i in range(n))


def check():
    checks=0
    census=[]
    for n in range(1,5):
        groups=defaultdict(lambda:[0,10**9,10**9])
        for cells in product([0,1], repeat=n*n):
            rows=tuple(tuple(j for j in range(n) if cells[i*n+j]) for i in range(n))
            sig=signature(rows,n)
            for k in range(n+1):
                assert direct_ops(rows,n,k)==signature_ops(sig,n,k), (n,rows,k)
                checks+=1
            count=sum(cells)
            g=groups[sig];g[0]+=1;g[1]=min(g[1],count);g[2]=min(g[2],sum(2 if len(r)>=2 else len(r) for r in rows))
        for sig,(actual,minedges,_) in groups.items():
            assert fiber_count(sig,n)==actual, (n,sig,actual,fiber_count(sig,n))
            checks+=1
        census.append((n,len(groups),max(v[0] for v in groups.values()),min(v[0] for v in groups.values()),max(v[1] for v in groups.values()), sum(v[0] for v in groups.values())))
        print('CENSUS n/classes/max_fiber/min_fiber/largest_min_edges/relations',*census[-1])
    assert census[0][1]==2
    for n in range(2,13):
        rows=tuple((i,i+1) for i in range(n-1)) + ((n-2,n-1),)
        sig=signature(rows,n)
        for i in range(n):
            choices=local_choices(sig,n,i)
            assert choices==[(rows[i][0],rows[i][1])], (n,i,choices)
            assert len(rows[i])==2
            checks+=1
        assert sum(len(r) for r in rows)==2*n
    # Each of the four one-step operations contributes distinct information
    # already on the two-world chain.
    n=2
    all_rows=[tuple(tuple(j for j in range(n) if bits[i*n+j]) for i in range(n))
              for bits in product([0,1], repeat=n*n)]
    for omitted in range(4):
        seen={}
        witness=None
        for rows in all_rows:
            s=signature(rows,n)
            projection=tuple(v for j,v in enumerate(s) if j!=omitted)
            if projection in seen and seen[projection][0]!=s:
                witness=(seen[projection][1], rows)
                break
            seen[projection]=(s,rows)
        assert witness is not None, omitted
        checks+=1
    print('ALL_CHECKS_OK',checks)

if __name__=='__main__':
    check()
