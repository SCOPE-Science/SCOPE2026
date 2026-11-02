"""Exact finite verification of the signed adjacent-order obstruction.
Pure standard-library Python 3.10+. No external records or dependencies.
"""
from itertools import product, permutations
from collections import Counter

SIGNS = tuple(product((-1, 1), repeat=3))
RANKS = tuple(permutations(range(3)))

def canonical(w):
    labels = {a:i for i,a in enumerate(dict.fromkeys(w))}
    return ''.join(str(labels[a]) for a in w)

def pass_by_ranks(w):
    n = len(w)
    for sign in SIGNS:
        for rank in RANKS:
            good = True
            for i in range(n-1):
                a, b = w[i], w[i+1]
                if a == b:
                    continue
                suffix_sign = 1
                for c in w[i+2:]:
                    suffix_sign *= sign[c]
                if (rank[b] - rank[a]) * suffix_sign <= 0:
                    good = False
                    break
            if good:
                return True
    return False

def pass_by_graph(w):
    for sign in SIGNS:
        adj = [set() for _ in range(3)]
        suffix_sign = 1
        for i in range(len(w)-2, -1, -1):
            a,b = w[i], w[i+1]
            if a != b:
                if suffix_sign > 0: adj[a].add(b)
                else: adj[b].add(a)
            suffix_sign *= sign[b]
        seen = [0]*3
        def visit(u):
            if seen[u] == 1: return False
            if seen[u] == 2: return True
            seen[u] = 1
            for v in adj[u]:
                if not visit(v): return False
            seen[u] = 2
            return True
        if all(visit(u) for u in range(3)):
            return True
    return False

expected_canonical = {
    '0100121', '0101102', '0102202', '0110102',
    '0120102', '0121021', '0121221', '0122121'
}
counts=[]
for n in range(3,8):
    allwords = [w for w in product(range(3),repeat=n) if len(set(w))==3]
    bad=[]
    for w in allwords:
        one=pass_by_ranks(w)
        two=pass_by_graph(w)
        assert one == two, (w, one, two)
        if not one:
            bad.append(w)
    classes={canonical(w) for w in bad}
    counts.append((n,len(allwords),len(bad),len(classes)))
assert counts == [(3,6,0,0),(4,36,0,0),(5,150,0,0),(6,540,0,0),(7,1806,48,8)],counts
assert {canonical(w) for w in product(range(3),repeat=7) if len(set(w))==3 and not pass_by_graph(w)} == expected_canonical
assert not pass_by_ranks(tuple(map(int,'0120102')))
print('n, surjective words, obstructions, inequivalent obstructions')
for row in counts: print(*row, sep=', ')
print('8 canonical obstructions:', ', '.join(sorted(expected_canonical)))
print('Rank-order and directed-cycle implementations agree on all 2538 surjective words.')
print('All assertions passed.')
