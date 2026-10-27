"""Exhaustive finite check of super domination in two cliques joined by a partial matching.
No external packages required. Run: python verify_superdom.py
"""
from collections import Counter
from math import comb


def adjacencies(n, t):
    N = [0] * (2*n)
    for v in range(2*n):
        for w in range(2*n):
            if v == w: continue
            same_side = (v < n) == (w < n)
            matched = (v % n == w % n) and v % n < t
            if same_side or matched:
                N[v] |= 1 << w
    return N


def definition(n, t, excluded, adj):
    allmask = (1 << (2*n)) - 1
    chosen = allmask ^ excluded
    # Every excluded vertex has a selected witness adjacent to exactly that excluded vertex.
    for u in range(2*n):
        if excluded >> u & 1:
            if not any((chosen >> v & 1) and (adj[v] & excluded) == (1 << u)
                       for v in range(2*n)):
                return False
    return True


def theorem(n, t, excluded):
    a = excluded & ((1 << n) - 1)
    b = excluded >> n
    if a and b:
        return a.bit_count() == b.bit_count() == 1
    if a:
        return a.bit_count() == 1 or a >> t == 0
    if b:
        return b.bit_count() == 1 or b >> t == 0
    return True


def expected_coeffs(n, t):
    out = Counter()
    # No omissions.
    out[2*n] += 1
    # Omissions of one matched-side subset, both sides.
    for k in range(1, t+1):
        out[2*n-k] += 2*comb(t,k)
    # One unmatched omission in either side.
    out[2*n-1] += 2*(n-t)
    # One omission from each side.
    out[2*n-2] += n*n
    return +out


def expected_minimal(n,t):
    out = Counter({2*n-2:n*n})
    if t >= 2:
        out[2*n-t] += 2
    return +out


def main():
    total = 0
    for n in range(3,8):
        for t in range(n+1):
            adj = adjacencies(n,t)
            goods = set()
            coeffs = Counter()
            for x in range(1 << (2*n)):
                got = definition(n,t,x,adj)
                want = theorem(n,t,x)
                if got != want:
                    raise AssertionError(f"classification mismatch n={n} t={t} omissions={x:b} got={got} want={want}")
                if got:
                    goods.add(x)
                    coeffs[2*n-x.bit_count()] += 1
            if +coeffs != expected_coeffs(n,t):
                raise AssertionError(f"count mismatch n={n} t={t}: {coeffs} != {expected_coeffs(n,t)}")
            maximal_omissions = Counter()
            for x in goods:
                if not any((x|1<<v) in goods for v in range(2*n) if not (x>>v&1)):
                    maximal_omissions[2*n-x.bit_count()] += 1
            if +maximal_omissions != expected_minimal(n,t):
                raise AssertionError(f"minimal mismatch n={n} t={t}: {maximal_omissions} != {expected_minimal(n,t)}")
            total += 1 << (2*n)
            print(f'PASS n={n} t={t} subsets={1<<(2*n)} superdom={len(goods)} minimal={sum(maximal_omissions.values())}')
    print(f'PASS total {total} subsets, {sum(n+1 for n in range(3,8))} parameter pairs.')

if __name__ == '__main__': main()
