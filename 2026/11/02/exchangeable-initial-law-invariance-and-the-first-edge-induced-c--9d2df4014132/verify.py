"""Exact finite-state verification for a four-vertex copying process.

Python 3.9+ standard library only. Run with: python3 verify.py
"""
from fractions import Fraction as Q
from itertools import combinations, permutations


def edges(n):
    return list(combinations(range(n), 2))


def adj(n, mask):
    a = [[False] * n for _ in range(n)]
    for z, (u, v) in enumerate(edges(n)):
        if mask & (1 << z):
            a[u][v] = a[v][u] = True
    return a


def connected(a):
    n = len(a)
    seen = {0}
    while True:
        nxt = seen | {j for i in seen for j in range(n) if a[i][j]}
        if nxt == seen:
            return len(nxt) == n
        seen = nxt


def permuted_mask(n, mask, perm):
    es = edges(n)
    eids = {e: k for k, e in enumerate(es)}
    result = 0
    for k, (i, j) in enumerate(es):
        if mask & (1 << k):
            result |= 1 << eids[tuple(sorted((perm[i], perm[j])))]
    return result


def canonical(n, mask):
    return min(permuted_mask(n, mask, p) for p in permutations(range(n)))


def linear_solve(A, b):
    n = len(b)
    a = [row[:] + [b[i]] for i, row in enumerate(A)]
    for j in range(n):
        piv = next(i for i in range(j, n) if a[i][j])
        a[j], a[piv] = a[piv], a[j]
        t = a[j][j]
        a[j] = [z/t for z in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                t = a[i][j]
                a[i] = [x-t*y for x, y in zip(a[i], a[j])]
    return [r[-1] for r in a]


def conditional_times(n, mask):
    a = adj(n, mask)
    assert connected(a)
    states = list(range(1, (1 << n)-1))
    pos = {s:i for i,s in enumerate(states)}
    A = [[Q(0) for _ in states] for __ in states]
    b = [Q(1) for _ in states]
    for i, state in enumerate(states):
        A[i][i] += n
        for u in range(n):
            neighbors = [v for v in range(n) if a[u][v]]
            d = len(neighbors)
            for v in neighbors:
                modified = (state & ~(1<<u)) | (((state>>v)&1)<<u)
                if modified in pos:
                    A[i][pos[modified]] -= Q(1,d)
    values = linear_solve(A,b)
    return {k:sum(values[pos[s]] for s in states if s.bit_count()==k)/Q(sum(1 for s in states if s.bit_count()==k)) for k in range(1,n)}


def graph_mask(n, pairs):
    es = edges(n)
    return sum(1 << es.index(tuple(sorted(e))) for e in pairs)


REPS = {
    'star':graph_mask(4, [(0,1),(0,2),(0,3)]),
    'P4':graph_mask(4, [(0,1),(0,3),(1,2)]),
    'paw':graph_mask(4, [(0,1),(0,2),(0,3),(1,2)]),
    'C4':graph_mask(4, [(0,2),(0,3),(1,2),(1,3)]),
    'diamond':graph_mask(4, [(0,1),(0,2),(0,3),(1,2),(1,3)]),
    'K4':graph_mask(4, edges(4)),
}
EXPECTED_SINGLE = {
    'star':Q(19,16),
    'paw':Q(1143,832),
    'K4':Q(11,8),
    'diamond':Q(397,288),
    'C4':Q(3,2),
    'P4':Q(23,14),
}
EXPECTED_PAIRS = {
    ('star','paw'):Q(155,832),
    ('P4','paw'):-Q(1567,5824),
    ('P4','C4'):-Q(1,7),
    ('paw','diamond'):Q(35,7488),
    ('C4','diamond'):-Q(35,288),
    ('diamond','K4'):-Q(1,288),
}

def main():
    all4 = [m for m in range(64) if connected(adj(4,m))]
    assert len(all4)==38
    orbit_types = {canonical(4,m) for m in all4}
    assert len(orbit_types)==6
    assert orbit_types=={canonical(4,m) for m in REPS.values()}
    values = {}
    for m in all4:
        t=conditional_times(4,m)
        assert t[3]==t[1]
        assert t[2]==Q(4,3)*t[1]-Q(1,12)
        values[m]=t[1]
    for label,m in REPS.items():
        assert values[m]==EXPECTED_SINGLE[label], (label, values[m], EXPECTED_SINGLE[label])
    map_names = {canonical(4,m):name for name,m in REPS.items()}
    jumps = {}
    for m in all4:
        for bit in range(6):
            if not(m>>bit & 1):
                enlarged=m|(1<<bit)
                k=(map_names[canonical(4,m)], map_names[canonical(4,enlarged)])
                delta=values[enlarged]-values[m]
                assert k not in jumps or jumps[k]==delta
                jumps[k]=delta
    assert jumps==EXPECTED_PAIRS, (jumps, EXPECTED_PAIRS)
    all3=[m for m in range(8) if connected(adj(3,m))]
    assert {canonical(3,m) for m in all3}=={canonical(3,graph_mask(3,[(0,1),(1,2)])),canonical(3,7)}
    for m in all3:
        t=conditional_times(3,m)
        assert t[1]==Q(1) and t[2]==Q(1)
    for n in (1,2):
        if n==1:continue
        assert sum(connected(adj(2,m)) for m in range(2)) == 1
    print('All 38 connected labelled four-vertex graphs; 6 isomorphism classes; exact rational equations: PASS')
    print('All four-vertex k=1,2,3 conditional-time identities: PASS')
    print('All three-vertex conditional mean times agree (one time unit): PASS')
    for name, t in sorted(EXPECTED_SINGLE.items(),key=lambda it:it[1]):
        print(name, 'single:',t,'balanced:',Q(4,3)*t-Q(1,12),'iid fair:',t-Q(1,32))
    for edge,delta in sorted(jumps.items()):
        print('single-edge',edge,'delta:',delta)
    print('All six isomorphism types of single-edge insertion and signs: PASS')

if __name__=='__main__':
    main()
