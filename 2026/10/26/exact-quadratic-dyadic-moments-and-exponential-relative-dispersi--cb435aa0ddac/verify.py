#!/usr/bin/env python3
"""Exact checks for a dyadic quadratic-moment identity of a 2-regular sequence."""
from functools import lru_cache

@lru_cache(maxsize=None)
def sequence(k):
    if k == 1:
        return 0
    if k in (2, 3):
        return 1
    a, b = divmod(k, 4)
    if b == 0:
        return 2*sequence(2*a)-sequence(a)
    if b == 1:
        return 2*sequence(2*a)+sequence(2*a+1)
    if b == 2:
        return 2*sequence(2*a+1)+sequence(2*a)
    return 2*sequence(2*a+1)-sequence(a)

def children(d,e,m):
    assert d*e == m*m+1 and d > 0 and e > 0 and m >= 0
    w = d+e+2*m
    return (d,w,m+d),(w,e,m+e)

def matrix(v):
    a,b,p,t = v
    return (3*a+8*b+12*p+4*t,
            2*a+5*b+6*p+2*t,
            a+2*b+2*p,2*t)

def test(max_depth=12):
    nodes=[(1,1,0)]
    v=(2,0,0,1)
    ps=[]
    for n in range(max_depth+1):
        sums=(sum(d*d+e*e for d,e,m in nodes),
              sum(m*(d+e) for d,e,m in nodes),
              sum(m*m for d,e,m in nodes), len(nodes))
        assert v==sums,(n,'matrix / tree mismatch',v,sums)
        direct=[sequence(k) for k in range(1<<n,1<<(n+1))]
        assert direct == [m for _,_,m in nodes],(n,'sequence/tree mismatch')
        p=sum(x*x for x in direct)
        assert p==v[2]
        ps.append(p)
        if n>=4:
            assert p==12*ps[n-1]-11*ps[n-2]-20*ps[n-3]+4*ps[n-4]
        v=matrix(v)
        nodes=[child for node in nodes for child in children(*node)]
    assert ps[:9]==[0,2,26,294,3202,34678,375138,4057334,43880738]
    print('VERIFY_OK depths=%d exact_tree_nodes=%d moment_recurrences=%d base_terms=PASS' % (max_depth,(1<<(max_depth+1))-1,max_depth-3))

if __name__=='__main__':
    test()
