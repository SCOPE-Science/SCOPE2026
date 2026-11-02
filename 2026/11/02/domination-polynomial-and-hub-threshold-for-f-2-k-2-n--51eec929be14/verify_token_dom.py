#!/usr/bin/env python3
"""Exact coefficient and independent adjacency checks for token domination.

Usage: python3 verify_token_dom.py
Requires only the Python standard library. Vertex labels are fixed, with the
first vertex representing the two vertices in the size-two bipartition class.
"""
from collections import defaultdict
from itertools import combinations
from math import comb, factorial


def add(dst, src, factor=1):
    for exponent, coefficient in src.items():
        dst[exponent] += factor * coefficient


def multiply(a, b):
    c = defaultdict(int)
    for i, ai in a.items():
        for j, bj in b.items():
            c[i+j] += ai*bj
    return c


def polynomial_power(a, k):
    result = {0: 1}
    for _ in range(k):
        result = multiply(result, a)
    return result


def binomial_poly(k):
    assert k >= 0
    return {j: comb(k,j) for j in range(k+1)}


def formula(n):
    assert n >= 2
    m = comb(n,2)
    hub = defaultdict(int)
    no_hub = defaultdict(int)
    # The distinguished pair is selected. The t zero-columns force K_t.
    for t in range(n+1):
        p = multiply(polynomial_power({1:2,2:1},n-t),
                     binomial_poly(m-comb(t,2)))
        add(hub,{j+1+comb(t,2):v*comb(n,t) for j,v in p.items()})
    # The distinguished pair is unselected. Nonselected cross pairs need
    # incident selected within-B pairs. Inclusion-exclusion enforces this.
    for t in range(n+1):
        for s in range(n-t+1):
            u = n-t-s
            if s+u==0:
                continue
            factor = factorial(n)//(factorial(t)*factorial(s)*factorial(u))*2**s
            p = defaultdict(int)
            if t >= 2:
                for j in range(s+1):
                    add(p, binomial_poly(comb(n-j,2)-comb(t,2)),
                        (-1)**j*comb(s,j))
                shift=comb(t,2)
            else:
                for j in range(s+t+1):
                    add(p, binomial_poly(comb(n-j,2)),
                        (-1)**j*comb(s+t,j))
                shift=0
            add(no_hub,{j+shift+s+2*u:v*factor for j,v in p.items()})
    total=defaultdict(int)
    add(total,hub)
    add(total,no_hub)
    return tuple({j:v for j,v in d.items() if v}
                 for d in (total,hub,no_hub))


def brute_force(n):
    # Build the token graph from the original K_{2,n} symmetric-difference
    # rule, independently of the state classification in formula().
    original = list(range(n+2))
    vertices = list(combinations(original,2))
    neighbors = [0]*len(vertices)
    for i,v in enumerate(vertices):
        mask=1<<i
        for j,w in enumerate(vertices):
            if i == j:
                continue
            sym = set(v).symmetric_difference(w)
            if len(sym)!=2:
                continue
            a,b=tuple(sym)
            if (a<2) != (b<2):
                mask |= 1<<j
        neighbors[i]=mask
    hub_index=vertices.index((0,1))
    full=defaultdict(int)
    hub=defaultdict(int)
    no_hub=defaultdict(int)
    for selected in range(1<<len(vertices)):
        if all(selected & neighborhood for neighborhood in neighbors):
            k=selected.bit_count()
            full[k]+=1
            if (selected>>hub_index)&1:
                hub[k]+=1
            else:
                no_hub[k]+=1
    return tuple(dict(x) for x in (full,hub,no_hub))


def expected_minimum(n):
    hub=n*(n+3)*2**(n-3) if n>=3 else 5
    nonhub={2:4,3:15,4:24}.get(n,0)
    return hub,nonhub


def main():
    examined=0
    for n in range(2,6):
        actual=brute_force(n)
        predicted=formula(n)
        examined+=2**comb(n+2,2)
        for name,a,b in zip(('all','hub','no_hub'),actual,predicted):
            assert a==b, ('polynomial mismatch',n,name,a,b)
        assert min(actual[0])==n
        hub,other=expected_minimum(n)
        assert actual[1].get(n,0)==hub, (n,actual[1].get(n,0),hub)
        assert actual[2].get(n,0)==other, (n,actual[2].get(n,0),other)
        assert sum(actual[0].values()) == sum(predicted[0].values())
    for n in range(6,12):
        whole, hub_part, other_part=formula(n)
        hub,nonhub=expected_minimum(n)
        assert min(whole)==n and whole[n]==hub+nonhub
        assert hub_part[n]==hub and other_part.get(n,0)==nonhub
    print('VERIFY_OK brute_parameters=2..5 examined_vertex_subsets=%d '
          'formula_parameters=2..11 min_hub_absent_after_4=True' % examined)

if __name__=='__main__':
    main()
