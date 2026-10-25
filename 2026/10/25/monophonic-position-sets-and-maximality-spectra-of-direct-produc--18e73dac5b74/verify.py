"""Independent finite checks for induced-path position sets in direct products.

Run: python3 verify.py

The verifier implements the graph definition directly, lists induced paths
by DFS, tests all vertex subsets, and compares two enumerators to closed
expressions. This is a finite regression check, not a proof for all orders.
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def formula(p, q):
    m = min(p, q)
    counts = Counter({0: 1, 1: p*q, 2: comb(p*q, 2)})
    for k in range(3, m+1):
        counts[k] = comb(p, k) * comb(q, k) * factorial(k)
    return counts


def maximal_formula(p, q):
    m = min(p, q)
    counts = Counter({2: p*comb(q, 2)+q*comb(p, 2)})
    counts[m] += comb(p,m)*comb(q,m)*factorial(m)
    return counts


def enumerate_induced_triples(p, q):
    vertices = list(product(range(p),range(q)))
    size = len(vertices)
    adj = [[int(u[0] != v[0] and u[1] != v[1])
            for v in vertices] for u in vertices]
    bad = set()

    def walk(path, visited):
        if len(path) >= 3:
            for mid in path[1:-1]:
                bad.add((1 << path[0]) | (1 << mid) | (1 << path[-1]))
        for nxt in range(size):
            if nxt in visited or not adj[path[-1]][nxt]:
                continue
            if any(adj[nxt][i] for i in path[:-1]):
                continue   # chord
            walk(path+[nxt], visited | {nxt})

    for start in range(size):
        walk([start], {start})
    return vertices, bad, adj


def check_witness(path, selected, p, q):
    assert p >= 3 and q >= 3
    assert len(path) == len(set(path)), ('repeated vertex',path)
    assert set(selected).issubset(path)
    def adjacent(x, y):
        return x[0] != y[0] and x[1] != y[1]
    assert all(adjacent(path[i],path[i+1]) for i in range(len(path)-1))
    assert all(not adjacent(path[i],path[j])
               for i in range(len(path)) for j in range(i+2,len(path)))


def test():
    # Nonclique triple canonical cases: same row, a two-row corner,
    # a two-row induced P3; column analogues follow by transposition.
    checks = [
        ([(0,0),(1,1),(0,2),(1,0),(0,1)],
         [(0,0),(0,1),(0,2)]),
        ([(0,0),(2,1),(1,0),(0,1)],
         [(0,0),(0,1),(1,0)]),
        ([(0,0),(1,2),(0,1)],
         [(0,0),(0,1),(1,2)]),
    ]
    for path,selected in checks:
        check_witness(path, selected, 3, 3)
        check_witness([(y,x) for x,y in path], [(y,x) for x,y in selected], 3, 3)

    for p,q in [(3,3),(3,4),(3,5),(4,4)]:
        vertices,bad,adj=enumerate_induced_triples(p,q)
        n=len(vertices)
        valid = set()
        counts=Counter()
        for mask in range(1 << n):
            if not any((mask & triple)==triple for triple in bad):
                valid.add(mask)
                counts[mask.bit_count()]+=1
        maximal=Counter()
        for mask in valid:
            if all((mask | (1 << bit)) not in valid
                   for bit in range(n) if not (mask & (1 << bit))):
                maximal[mask.bit_count()]+=1
        assert counts==formula(p,q), (p,q,counts,formula(p,q))
        assert maximal==maximal_formula(p,q), (p,q,maximal,maximal_formula(p,q))
        print(f'PASS p={p},q={q}: all={dict(sorted(counts.items()))}; '
              f'maximal={dict(sorted(maximal.items()))}; '
              f'induced-path-forbidden-triples={len(bad)}')
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
