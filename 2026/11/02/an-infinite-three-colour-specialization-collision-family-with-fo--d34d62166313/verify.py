#!/usr/bin/env python3
"""Exact checks for an infinite family of caterpillar specialization collisions.
Requires Python 3 and SymPy; independent tree-DP and short brute-force controls.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
import sympy as sp

q, z = sp.symbols('q z')


def pr(count):
    return sp.Poly(sum(q**i for i in range(count)), q)


def leaf_polynomials(m):
    return [sp.Poly(sum(q**i for i in range(m) if i != c), q) for c in range(m)]


def coefficient_certificate():
    """Compute [q^8] of the parameter generating function, exact rational functions."""
    P = leaf_polynomials(4)
    total = sp.Integer(0)
    pair_results = {}
    for i, j in combinations(range(4), 2):
        pair_sum = sp.Integer(0)
        for h in range(4):
            if h in (i, j):
                continue
            num = sp.Poly(sp.expand(q**(i+j+h)*P[i].as_expr()*P[j].as_expr()
                         *(P[j].as_expr()-P[i].as_expr())
                         *(q**j*P[j].as_expr()**2 - q**i*P[i].as_expr()**2)), q)
            denpoly = P[i]*P[j]*P[h]
            den = [denpoly.nth(k) for k in range(9)]
            coeff = [sp.Integer(0)]*9
            c0 = 1/(1-z*den[0])
            coeff[0] = c0
            for k in range(1, 9):
                coeff[k] = c0*z*sum(den[e]*coeff[k-e] for e in range(1, k+1))
            pair_sum += z*sum(num.nth(k)*coeff[8-k] for k in range(9))
        pair_results[(i,j)] = sp.cancel(pair_sum)
        total += pair_results[(i,j)]
    total = sp.cancel(total)
    desired = -14*z-4*z*z-2*z**3/(1-z)
    assert sp.cancel(total-desired) == 0, (total, desired)
    return pair_results


def graph_from_parts(parts):
    counts = [x - 1 for x in parts]
    assert len(counts) == 4 and counts[0]>=1 and counts[3]>=1 and min(counts)>=0
    n=4+sum(counts)
    adj=[[] for _ in range(n)]
    def edge(a,b):
        adj[a].append(b); adj[b].append(a)
    for i in range(3):edge(i,i+1)
    k=4
    for i,ct in enumerate(counts):
        for _ in range(ct):edge(i,k); k+=1
    assert k==n
    return adj


def dp_invariant(parts,m):
    """Exact graph-based proper-coloring DP, NOT using spine transfer formula."""
    adj=graph_from_parts(parts)
    @lru_cache(None)
    def rooted(u,p,c):
        d={(c,1<<c):1}
        for v in adj[u]:
            if v==p:continue
            nxt=defaultdict(int)
            child=[]
            for cv in range(m):
                if cv!=c:
                    child.extend(rooted(v,u,cv).items())
            for (a,mask),count in d.items():
                for (b,ms2),ct2 in child:
                    nxt[(a+b,mask|ms2)]+=count*ct2
            d=nxt
        return dict(d)
    out=defaultdict(int)
    for c in range(m):
        for (power,mask),count in rooted(0,-1,c).items():
            out[(power,mask.bit_count())]+=count
    return dict(out)


def direct_enumeration(parts,m):
    adj=graph_from_parts(parts)
    n=len(adj)
    edges=[(i,j) for i in range(n) for j in adj[i] if i<j]
    out=defaultdict(int)
    for cols in product(range(m),repeat=n):
        if all(cols[u]!=cols[v] for u,v in edges):
            out[(sum(cols),len(set(cols)))]+=1
    return dict(out)


def run():
    pairs=coefficient_certificate()
    print('COEFFICIENT_CERTIFICATE_OK pairs='+str(len(pairs)))
    for r in range(1,7):
        lhs=(3,r+1,r,r+2)
        rhs=(3,r+2,r,r+1)
        v3a=dp_invariant(lhs,3);v3b=dp_invariant(rhs,3)
        assert v3a==v3b,(r, 'ps3 conflict')
        v4a=dp_invariant(lhs,4);v4b=dp_invariant(rhs,4)
        diff8=sum(c for (weight,used),c in v4a.items() if weight==8)-sum(c for (weight,used),c in v4b.items() if weight==8)
        assert diff8==(-14 if r==1 else -4 if r==2 else -2),(r,diff8)
        assert v4a != v4b
        print(f'R={r} vertices={3*r+6} PS3_EQUAL=YES PS4_Q8_DIFFERENCE={diff8}')
    for r,m in [(1,3),(1,4),(2,3)]:
        for parts in [(3,r+1,r,r+2),(3,r+2,r,r+1)]:
            assert dp_invariant(parts,m)==direct_enumeration(parts,m),(r,m,parts)
    print('INDEPENDENT_FULL_COLORING_CHECK_OK r=1 m=3,4 and r=2 m=3')
    print('VERIFY_OK: infinite ps3 identity; ps4 q8 separation; exact independent small-graph checks')

if __name__ == '__main__':run()
