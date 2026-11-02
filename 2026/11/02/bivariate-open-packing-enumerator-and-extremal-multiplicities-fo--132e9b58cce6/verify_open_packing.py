#!/usr/bin/env python3
"""Standalone exact checks of open-packings in Cartesian clique--path graphs.

Run with Python 3.9+; standard library only. No external data are required.
"""
from collections import defaultdict
from math import comb


def add_scaled(dest, src, scalar=1, da=0, db=0):
    for (a, b), value in src.items():
        dest[(a + da, b + db)] += scalar * value


def transfer_poly(m, n):
    """Four memory states 00, 0a, a0, aa; count by vertices and induced edges."""
    states = [{(0, 0): 1}, {}, {}, {}]
    for _ in range(n):
        nxt = [defaultdict(int) for _ in range(4)]
        add_scaled(nxt[0], states[0])
        add_scaled(nxt[1], states[0], m, 1, 0)
        add_scaled(nxt[2], states[1])
        add_scaled(nxt[3], states[1], 1, 1, 1)
        add_scaled(nxt[0], states[2])
        add_scaled(nxt[1], states[2], m - 1, 1, 0)
        add_scaled(nxt[2], states[3])
        states = [{k: v for k, v in s.items() if v} for s in nxt]
    out = defaultdict(int)
    for s in states:
        add_scaled(out, s)
    return {k: v for k, v in out.items() if v}


def brute_graph_poly(m, n):
    """Independent graph-level exhaustive enumeration of all subsets."""
    N = m * n
    assert N <= 18
    adj = [0] * N
    for i in range(n):
        for a in range(m):
            v = i*m+a
            for b in range(m):
                if b != a:
                    adj[v] |= 1 << (i*m+b)
            for j in (i-1,i+1):
                if 0 <= j < n:
                    adj[v] |= 1 << (j*m+a)
    conflict = [0] * N
    for a in range(N):
        for b in range(a+1, N):
            if adj[a] & adj[b]:
                conflict[a] |= 1 << b
                conflict[b] |= 1 << a
    valid = bytearray(1<<N)
    valid[0]=1
    counts=defaultdict(int)
    counts[(0,0)]=1
    for mask in range(1, 1<<N):
        low = mask & -mask
        vertex = low.bit_length()-1
        rest = mask ^ low
        if valid[rest] and not (rest & conflict[vertex]):
            valid[mask] = 1
            size = mask.bit_count()
            twice_edges = sum((mask & adj[i]).bit_count() for i in range(N) if mask >> i & 1)
            assert twice_edges % 2 == 0
            counts[(size,twice_edges//2)] += 1
    return dict(counts)


def maximum_count(m,n):
    k=(2*n+2)//3
    q,r=divmod(n,3)
    if r==2:
        return k,m*(m-1)**q
    if r==1:
        return k,(q+1)*m*(m-1)**q
    if q==1:
        return k,m*(m+1)
    return k,(comb(q+1,2)*m*(m-1)**q+2*m*(m-1)**(q-1)
            +(q-1)*m*m*(m-1)**(q-2))


def polynomial_recurrence_check(m, n_max):
    p=[]
    for n in range(n_max+1):
        q=transfer_poly(m,n)
        p.append(q)
        lhs=defaultdict(int)
        add_scaled(lhs,p[n])
        if n>=1: add_scaled(lhs,p[n-1],-1)
        if n>=2: add_scaled(lhs,p[n-2],1-m,1,0)
        if n>=3:
            add_scaled(lhs,p[n-3],1-m,2,1)
            add_scaled(lhs,p[n-3],-1,1,0)
        if n>=4: add_scaled(lhs,p[n-4],-1,2,1)
        actual={k:v for k,v in lhs.items() if v}
        expected=[{(0,0):1},{(1,0):m},{(1,0):1,(2,1):m},{(2,1):1}][n] if n<=3 else {}
        assert actual==expected,(m,n,actual,expected)
        if n>=1:
            k,c=maximum_count(m,n)
            got=sum(value for (size,_), value in q.items() if size==k)
            assert got==c,(m,n,k,got,c)
            assert all(size<=k for size,_ in q)
    return n_max+1


def run():
    cases=[]
    for m in range(3,7):
        for n in range(1,7):
            if m*n<=18: cases.append((m,n))
    for m,n in cases:
        brute=brute_graph_poly(m,n)
        transfer=transfer_poly(m,n)
        assert brute==transfer,(m,n,brute,transfer)
    checks=sum(polynomial_recurrence_check(m,26) for m in range(3,9))
    print('VERIFY_OK: %d independent all-subset graph cases; %d exact recurrence/maximum cases' % (len(cases),checks))

if __name__=='__main__':
    run()
