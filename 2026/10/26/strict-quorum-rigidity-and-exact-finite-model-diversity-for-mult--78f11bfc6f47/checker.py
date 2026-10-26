"""Independent finite checks of strict-quorum successor-path classification.
Run with Python 3.9+; no third-party libraries required.
"""
from itertools import permutations, product
from collections import Counter
from math import factorial, comb


def successor_mask(perm, n):
    out = 0
    for a, b in zip(perm, perm[1:]):
        out |= 1 << (a*n+b)
    return out


def coefficient(n, r, cap, distinct=None):
    """r![z^r](sum_{j=0}^cap z^j/j!)^n,
    optionally exactly 'distinct' positive occupancies, via integer DP.
    """
    dp = {(0, 0): 1}  # ways to map labelled tuple positions into first cells
    for _ in range(n):
        nxt = {}
        for (used, active), ways in dp.items():
            for j in range(min(cap, r-used)+1):
                key = (used+j, active+(j > 0))
                nxt[key] = nxt.get(key, 0) + ways*comb(r-used, j)
        dp = nxt
    return sum(ways for (used, active), ways in dp.items()
               if used == r and (distinct is None or active == distinct))


def expected(n, r, q):
    c = r-q
    return factorial(n)+factorial(n-1)*coefficient(n, r, c)


def brute(n, r, q):
    paths = list(permutations(range(n)))
    masks = [successor_mask(p, n) for p in paths]
    counts = Counter()
    for choices in product(range(len(paths)), repeat=r):
        union = 0
        for x in choices:
            union |= masks[x]
        satisfied = 0
        for edge in range(n*n):
            bit = 1 << edge
            if union & bit:
                if sum(bool(masks[x]&bit) for x in choices) >= q:
                    satisfied |= bit
                else:
                    break
        else:
            if union == satisfied:
                counts[len(set(choices))] += 1
    return counts


def test():
    cases = [(2, 3, 2),(3,3,2),(4,3,2),(5,3,2),
             (3,4,3),(4,4,3),(3,5,3),(4,3,3)]
    for n,r,q in cases:
        observed = brute(n,r,q)
        anticipated = {1:factorial(n)}
        for s in range(2,min(n,r)+1):
            val = factorial(n-1)*coefficient(n,r,r-q,s)
            if val:anticipated[s]=val
        assert dict(observed)==anticipated,(n,r,q,observed,anticipated)
        assert sum(observed.values())==expected(n,r,q)
        if q>r//2:
            assert 2 not in observed
        print(f'OK n={n} r={r} q={q}: total {sum(observed.values())}; diversity {dict(observed)}')
    # Exact boundary counterexample for all r >= 2*q is constructive:
    for r in range(2,9):
        q=r//2
        a,b=(0,1,2),(1,0,2)
        words=[a]*(r-q)+[b]*q
        mask=[successor_mask(w,3) for w in words]
        edges={i for v in mask for i in range(9) if v>>i&1}
        assert all(sum(bool(v>>i&1) for v in mask)>=q for i in edges)
        assert len(edges)>3
    print('ALL_CHECKS_OK')

if __name__=='__main__':
    test()
