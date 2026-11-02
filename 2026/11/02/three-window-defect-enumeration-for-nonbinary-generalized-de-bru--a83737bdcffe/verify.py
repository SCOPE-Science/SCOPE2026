#!/usr/bin/env python3
"""Exact integer checks for enumeration of 3-defect de Bruijn necklaces.

All operations use the Python standard library and integer arithmetic.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial


def det_bareiss(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            i = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if i is None:
                return 0
            a[k], a[i] = a[i], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def vertices_edges(q, n):
    vertices = list(product(range(q), repeat=n - 1))
    v_index = {v: i for i, v in enumerate(vertices)}
    edges = list(product(range(q), repeat=n))
    transitions = [(v_index[e[:-1]], v_index[e[1:]]) for e in edges]
    return vertices, edges, transitions


def cofactor(q, n, absent):
    verts, edges, transitions = vertices_edges(q, n)
    v = len(verts)
    absent = set(absent)
    M = [[0] * v for _ in range(v)]
    degrees = [0] * v
    for e, (i, j) in zip(edges, transitions):
        if e in absent:
            continue
        degrees[i] += 1
        M[i][i] += 1
        M[i][j] -= 1
    tree = det_bareiss([row[:-1] for row in M[:-1]])
    return tree, degrees


def typ(e, n):
    loops = sum(len(set(w)) == 1 for w in e)
    if loops == 3:
        return 'LLL'
    if loops == 1:
        return 'L2'
    assert loops == 0 and n >= 3
    base = e[0][:3]
    generated = {
        tuple(base[(phase + k) % 3] for k in range(n))
        for phase in range(3)
    }
    assert generated == set(e), ('non-periodic missing cycle', e)
    assert len(set(base)) in (2, 3)
    return 'AAB' if len(set(base)) == 2 else 'ABC'


def model(q, n, category):
    m = n - 1
    x = Fraction(1, q ** m)
    if category == 'LLL': return Fraction(1)
    if category == 'L2': return Fraction(q - 1 + 2 * (1 if m % 2 == 0 else -1) * x, q + 1)
    denom = q*q+q+1
    if category == 'ABC':
        return ( (q-1)**2 + {0:3*(q-1)*x+3*x*x, 1:3*x*x, 2:-3*(q-1)*x+3*x*x}[m%3] ) / denom
    if category == 'AAB':
        linear={0:-(q-1)*(q-2),1:q*(q-1),2:-2*(q-1)}[m%3]
        return ((q-1)**2+linear*x-q*(q+2)*x*x)/denom
    raise ValueError(category)


def expected(q,n):
    base = factorial(q)**(q**(n-1))//q**n
    if n==2:
        return base*Fraction(q*q-2*q+2,q*(q-1))
    weighted = (comb(q,3) +q*comb(q,2)*model(q,n,'L2') +q*(q-1)*model(q,n,'AAB') + 2*comb(q,3)*model(q,n,'ABC'))
    return base*weighted/(q-1)**3


def missing_sets(q,n):
    _, edges, transitions=vertices_edges(q,n)
    for combo in combinations(range(len(edges)),3):
        dif=Counter()
        for j in combo:
            u,v=transitions[j]
            dif[u]+=1; dif[v]-=1
        if all(t==0 for t in dif.values()):
            yield tuple(edges[j] for j in combo)


def brute(q,n):
    length=q**n-3
    if length>7: return None
    necklaces=set()
    for w in product(range(q),repeat=length):
        ww=w+w[:n-1]
        windows=[tuple(ww[j:j+n]) for j in range(length)]
        if len(set(windows)) != length: continue
        necklaces.add(min(w[j:]+w[:j] for j in range(length)))
    return len(necklaces)


def run():
    cases=0; examined=0; total_checks=0
    for q,n in [(3,2),(4,2),(5,2),(3,3),(4,3),(3,4)]:
        type_counts=Counter(); full_total=0
        base=factorial(q)**(q**(n-1))//q**n
        for E in missing_sets(q,n):
            examined+=1
            tree,degs=cofactor(q,n,E)
            ratio=Fraction(tree,q**(q**(n-1)-n))
            if n>=3:
                category=typ(E,n)
                assert ratio==model(q,n,category),(q,n,E,ratio,category)
            else:
                loops=[w for w in E if w[0]==w[1]]
                if len(loops)==3: category='LLL'
                elif len(loops)==1: category='L2_shared' if loops[0][0] in {x for e in E for x in e if len(set(e))>1} else 'L2_disjoint'
                else: category='ABC'
            type_counts[category]+=1
            circuit=tree
            for d in degs:
                assert d>0,(q,n,E)
                circuit*=factorial(d-1)
            full_total+=circuit
        if n>=3:
            assert type_counts==Counter({'LLL':comb(q,3),'L2':q*comb(q,2),'AAB':q*(q-1),'ABC':2*comb(q,3)}),(q,n,type_counts)
        else:
            assert type_counts==Counter({'LLL':comb(q,3),'L2_disjoint':(q-2)*comb(q,2), 'L2_shared':2*comb(q,2),'ABC':2*comb(q,3)}),(q,n,type_counts)
        assert full_total==expected(q,n),(q,n,full_total,expected(q,n))
        b=brute(q,n)
        if b is not None:
            assert b==full_total,(q,n,b,full_total)
        print('OK',q,n,'types',dict(type_counts),'necklaces',full_total,'direct_brute',b)
        cases+=1
    print(f'VERIFY_OK parameter_cases={cases} balanced_missing_sets={examined} exact_cofactors={examined} independent_direct_necklaces_q3n2=True')

if __name__=='__main__':run()
