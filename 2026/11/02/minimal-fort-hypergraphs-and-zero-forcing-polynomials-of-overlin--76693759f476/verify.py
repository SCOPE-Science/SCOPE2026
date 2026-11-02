"""Independent finite checks of the path-complement fort and forcing classifications.
Python 3 standard library only. All tests use the graph definition directly.
"""
from itertools import combinations
from math import comb


def adjacency(n):
    return [set(j for j in range(n) if j != i and abs(i-j) != 1) for i in range(n)]


def is_fort(n, white, adj):
    w = set(white)
    return bool(w) and all(len(adj[v] & w) != 1 for v in range(n) if v not in w)


def can_force(n, whites, adj):
    remaining = set(whites)
    while remaining:
        chosen = None
        for v in range(n):
            if v not in remaining:
                neighbors = adj[v] & remaining
                if len(neighbors) == 1:
                    chosen = next(iter(neighbors))
                    break
        if chosen is None:
            return False
        remaining.remove(chosen)
    return True


def has_open_gap(triple):
    s = set(triple)
    return any(i + 2 in s and i + 1 not in s for i in s)


def predicted_min_forts(n):
    triples = {tuple(w) for w in combinations(range(n), 3) if not has_open_gap(w)}
    fours = {tuple((a,a+2,b,b+2)) for a in range(n) for b in range(a+3,n-2)}
    return triples | fours


def run():
    total_subsets = 0
    for n in range(4, 15):
        adj = adjacency(n)
        all_subsets = [tuple(i for i in range(n) if mask >> i & 1) for mask in range(1<<n)]
        forts = {s for s in all_subsets if is_fort(n,s,adj)}
        actual_min = {s for s in forts if not any(s[:j]+s[j+1:] in forts for j in range(len(s)))}
        predicted_min = predicted_min_forts(n)
        assert actual_min == predicted_min, (n, actual_min^predicted_min)
        assert len([s for s in actual_min if len(s)==3]) == comb(n,3)-(n*n-6*n+10)
        assert len([s for s in actual_min if len(s)==4]) == (comb(n-4,2) if n>=6 else 0)
        forcing_count = [0]*(n+1)
        for s in all_subsets:
            whites = set(range(n))-set(s)
            forcing = can_force(n, whites, adj)
            forcing_count[len(s)] += forcing
            assert forcing == (not any(set(f).issubset(whites) for f in actual_min))
        formula = [0]*(n+1)
        formula[n-3] = n*n-6*n+10
        formula[n-2] = comb(n,2)
        formula[n-1] = n
        formula[n] = 1
        assert forcing_count == formula, (n,forcing_count,formula)
        total_subsets += 1 << n
        print('n=',n,'small_forts=',len(actual_min),'minimum_force_sets=',formula[n-3])
    print('VERIFY_OK',total_subsets,'subsets')

if __name__ == '__main__':
    run()
