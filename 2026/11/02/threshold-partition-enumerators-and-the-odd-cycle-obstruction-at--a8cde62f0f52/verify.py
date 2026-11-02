#!/usr/bin/env python3
"""Exact, standard-library checks for threshold partitions of degree-two graphs."""
from itertools import combinations, combinations_with_replacement, product


def component_edges(kind, n, offset=0):
    es = {(offset+i, offset+i+1) for i in range(n-1)}
    if kind == 'C':
        assert n >= 3
        es.add((offset, offset+n-1))
    return {tuple(sorted(e)) for e in es}


def factor(kind, n):
    if kind == 'P':
        if n == 1:
            return (2, 0, 0, 0)
        if n == 2:
            return (2, 1, 1, 0)
        return (2, 2*n-3, 2*n-3, 2*(n-3)**2)
    assert kind == 'C' and n >= 3
    if n == 3:
        return (0, 4, 4, 0)
    return (2 if n % 2 == 0 else 0, n, n, n*(n-3))


def poly_product(factors):
    # coefficients indexed as 00, x, y, xy
    a = [1, 0, 0, 0]
    for b in factors:
        a = [a[0]*b[0], a[0]*b[1]+a[1]*b[0],
             a[0]*b[2]+a[2]*b[0],
             a[0]*b[3]+a[1]*b[2]+a[2]*b[1]+a[3]*b[0]]
    return a


def forbidden_foursets(N, E):
    """Original forbidden induced P4,C4,2K2, by independent adjacency test."""
    out = []
    for ss in combinations(range(N), 4):
        EE = [e for e in E if e[0] in ss and e[1] in ss]
        degrees = [sum(v in e for e in EE) for v in ss]
        if len(EE) == 2 and sorted(degrees) == [1, 1, 1, 1]:
            out.append(ss)
        elif len(EE) == 3 and sorted(degrees) == [1, 1, 2, 2]:
            out.append(ss)
        elif len(EE) == 4 and degrees == [2, 2, 2, 2]:
            out.append(ss)
    return out


def direct_count(parts):
    N = sum(n for _, n in parts)
    E = set()
    offset = 0
    for kind, n in parts:
        E |= component_edges(kind, n, offset)
        offset += n
    bad = forbidden_foursets(N, E)
    count = 0
    for bits in product((0, 1), repeat=N):
        if all(not (bits[v[0]] == bits[v[1]] == bits[v[2]] == bits[v[3]]) for v in bad):
            count += 1
    return count


def run():
    tests = 0
    for n in range(1, 15):
        q = [('P', n)]
        predicted = sum(poly_product([factor('P', n)]))
        actual = direct_count(q)
        assert actual == predicted, (q, actual, predicted)
        tests += 1
    for n in range(3, 15):
        q = [('C', n)]
        predicted = sum(poly_product([factor('C', n)]))
        actual = direct_count(q)
        assert actual == predicted, (q, actual, predicted)
        tests += 1
    print('DIRECT_FORBIDDEN_SUBGRAPH_SINGLE_COMPONENT_OK', tests)
    tested = 0
    catalog = [('P',i) for i in range(1,8)]+[('C',i) for i in range(3,8)]
    for k in (2,3):
        for indices in combinations_with_replacement(range(len(catalog)), k):
            parts = [catalog[i] for i in indices]
            if sum(n for _,n in parts)>10:
                continue
            predicted = sum(poly_product([factor(*p) for p in parts]))
            actual = direct_count(parts)
            assert predicted == actual, (parts,actual,predicted)
            tested += 1
    print('DIRECT_FORBIDDEN_SUBGRAPH_DISCONNECTED_OK',tested)
    for n in range(3,1001):
        if n >= 3:
            pn = factor('P',n)
            assert sum(pn)==2*n*n-8*n+14
            cn = factor('C',n)
            target = (8 if n==3 else n*(n-1)+(2 if n%2==0 else 0))
            assert sum(cn)==target
    print('FORMULAE_ALL_LENGTHS_3_TO_1000_OK')
    for a in range(0,5):
        for b in range(0,5):
            if a+b==0: continue
            parts = [('C',3)]*a+[('C',5)]*b
            val = sum(poly_product([factor(*p) for p in parts]))
            assert (val>0) == (a+b<=2)
    print('ODD_CYCLE_OBSTRUCTION_AND_ATTAINMENT_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
