#!/usr/bin/env python3
"""Direct exhaustive checks for odd-induced colorings of clique coronas.
Only the standard finite graph definitions and Python stdlib are used.
"""
from itertools import product, combinations
from math import factorial
from collections import defaultdict


def base_adj(n, mask):
    adj = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(combinations(range(n), 2)):
        if (mask >> bit) & 1:
            adj[u].add(v)
            adj[v].add(u)
    return adj


def clique_corona(adj, r):
    n = len(adj)
    out = [set(a) for a in adj] + [set() for _ in range(n*r)]
    for v in range(n):
        leaves = [n+v*r+j for j in range(r)]
        for u in leaves:
            out[v].add(u)
            out[u].add(v)
            for w in leaves:
                if w != u:
                    out[u].add(w)
    return out


def valid_odd(adj, c):
    return all((sum(c[u] == c[v] for u in adj[v]) & 1) for v in range(len(adj)))


def valid_even(adj, c):
    return all(not (sum(c[u] == c[v] for u in adj[v]) & 1) for v in range(len(adj)))


def enumerate_colors(adj, q, parity):
    pred = valid_odd if parity == 'odd' else valid_even
    return sum(pred(adj, c) for c in product(range(q), repeat=len(adj)))


def local_count(r, q, odd_r):
    # Independently inspect every leaf assignment, with root fixed to color zero.
    res = 0
    for leaves in product(range(q), repeat=r):
        counts = [leaves.count(k) for k in range(q)]
        target_root_parity = int(odd_r)
        if counts[0] % 2 != target_root_parity:
            continue
        if all((counts[k] + (k == 0)) % 2 == 0 for k in range(q) if counts[k]):
            res += 1
    return res


def local_count_coeff(r, q, odd_r):
    # EGF coefficients via integer multinomials, rather than leaf enumeration.
    def rec(k, remain, den, root_parity):
        if k == q:
            return factorial(r) // den if remain == 0 else 0
        acc = 0
        for number in ([0] if k == 0 and not root_parity else range(root_parity if k == 0 else 0, remain + 1, 2)):
            acc += rec(k+1, remain-number, den*factorial(number), root_parity)
        return acc
    return rec(0, r, 1, int(odd_r))


def binary_nullity(adj):
    n = len(adj)
    rows=[]
    for v in range(n):
        bits = (len(adj[v]) % 2) << v
        for u in adj[v]:
            bits ^= (1 << u)
        rows.append(bits)
    rank=0
    for col in range(n):
        pivot=next((j for j in range(rank,n) if (rows[j]>>col)&1),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for j in range(n):
            if j != rank and ((rows[j]>>col)&1):rows[j]^=rows[rank]
        rank+=1
    return n-rank


def run():
    cases=0
    directly_tested=0
    for r in range(1, 6):
        for q in range(1, 5):
            x=local_count(r,q,r%2==1)
            y=local_count_coeff(r,q,r%2==1)
            assert x==y,(r,q,x,y)
            assert (x == 2**(r-1)) if (q == 2 and r % 2) else True
            assert (x == 1) if (q == 2 and not r % 2) else True
    print('local EGF coefficients: verified by direct leaf assignments for r=1..5, q=1..4')
    for n in range(1, 4):
        for mask in range(1 << (n*(n-1)//2)):
            g=base_adj(n,mask)
            for r in range(1, 4):
                h=clique_corona(g,r)
                for q in range(1,4):
                    core_count=enumerate_colors(g,q,'even' if r%2 else 'odd')
                    local=local_count_coeff(r,q,bool(r%2))
                    predicted=core_count*(local**n)
                    direct=enumerate_colors(h,q,'odd')
                    assert direct == predicted,(n,mask,r,q,direct,predicted)
                    cases+=1
                    directly_tested += q**len(h)
            # Exhaustive binary even-partition count, independently using rank.
            assert enumerate_colors(g,2,'even') == 2**binary_nullity(g)
    print('direct brute-force corona parity comparisons:',cases)
    print('complete color assignments checked:',directly_tested)
    print('binary even-coloring/nullity checks: 11 labeled bases of orders 1..3')
    # Boundary: r even all q=1 impossible; odd r q=1 iff G degrees even.
    for n in range(1,6):
        for mask in range(1 << (n*(n-1)//2)):
            g=base_adj(n,mask)
            g_even=all(len(a)%2 == 0 for a in g)
            assert (enumerate_colors(g,1,'even')>0)==g_even
            assert enumerate_colors(g,2,'even')==2**binary_nullity(g)
            # Odd two-colourings solve Lx=d+1; it need not be soluble even
            # when components have even order (e.g. the six-cycle).
            for parity in ('even','odd'):
                assert enumerate_colors(g,2,parity) == linear_parity_count(g,parity)
    print('1-color boundary and 2-color binary counts: all 1,099 labeled base graphs orders 1..5')
    c6 = [set(((i-1)%6,(i+1)%6)) for i in range(6)]
    assert enumerate_colors(c6,2,'odd') == 0
    assert enumerate_colors(c6,3,'odd') > 0
    print('six-cycle odd-coloring boundary: q=2 impossible, q=3 possible')
    print('VERIFY_OK')

def linear_parity_count(g, parity):
    n = len(g)
    desired = int(parity == 'odd')
    count = 0
    for bits in product((0,1),repeat=n):
        if all(((len(g[v])%2) ^ (sum((bits[u]^bits[v]) for u in g[v])%2)) == desired for v in range(n)):
            count += 1
    return count

def component_sizes(g):
    seen=set(); sizes=[]
    for v in range(len(g)):
        if v in seen:continue
        todo=[v];seen.add(v);size=0
        while todo:
            u=todo.pop();size+=1
            for w in g[u]:
                if w not in seen:
                    seen.add(w);todo.append(w)
        sizes.append(size)
    return sizes

if __name__=='__main__':run()
