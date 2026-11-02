"""Independent finite checks for binary diameter-two anticodes."""
from collections import Counter
from itertools import combinations
from math import comb


def maximal_cliques(n):
    q = 1 << n
    adj = [0] * q
    for u in range(q):
        for v in range(q):
            if u != v and (u ^ v).bit_count() <= 2:
                adj[u] |= 1 << v
    found = []
    def iterate(bits):
        while bits:
            t = bits & -bits
            yield t.bit_length() - 1
            bits -= t
    def bk(R, P, X):
        if not (P | X):
            found.append(frozenset(iterate(R)))
            return
        U = P | X
        pivot = max(iterate(U), key=lambda u: (P & adj[u]).bit_count())
        for v in list(iterate(P & ~adj[pivot])):
            bv = 1 << v
            bk(R | bv, P & adj[v], X & adj[v])
            P &= ~bv
            X |= bv
    bk(0, (1 << q) - 1, 0)
    assert len(found) == len(set(found))
    return set(found)


def types(n):
    q = 1 << n
    B = {frozenset([x] + [x ^ (1 << i) for i in range(n)]) for x in range(q)}
    F = {frozenset(x ^ mask for mask in [0, 1 << i, 1 << j, (1 << i) | (1 << j)])
         for i, j in combinations(range(n), 2)
         for x in range(q) if not ((x >> i) & 1) and not ((x >> j) & 1)}
    P = {frozenset([x, x ^ ((1 << i) | (1 << j)),
                    x ^ ((1 << i) | (1 << k)), x ^ ((1 << j) | (1 << k))])
         for i, j, k in combinations(range(n), 3) for x in range(q)}
    assert len(B) == q
    assert len(F) == (q // 4) * comb(n, 2)
    assert len(P) == (q // 4) * comb(n, 3)
    assert not (B & F or B & P or F & P)
    return B, F, P


def coeffs(n):
    q = 1 << n
    c = [0] * (n+2)
    c[0] = 1
    c[1] = q
    c[2] = (q // 2) * (n + comb(n, 2))
    c[3] = q * (comb(n, 2) + comb(n, 3))
    for j in range(4, n+2):
        c[j] = q * comb(n+1,j)
    c[4] += (q // 4) * (comb(n, 2) + comb(n, 3))
    return c


def independently_count(n):
    N = 1 << n
    out = Counter()
    for mask in range(1 << N):
        bits = [i for i in range(N) if mask & (1 << i)]
        if all((a ^ b).bit_count() <= 2 for a, b in combinations(bits, 2)):
            out[len(bits)] += 1
    return out


def main():
    total_facets = 0
    checked_subsets = 0
    for n in range(3, 8):
        B, F, P = types(n)
        independent_facets = maximal_cliques(n)
        assert independent_facets == B | F | P, n
        total_facets += len(independent_facets)
        for j in range(4, n+2):
            s = set()
            for f in independent_facets:
                if len(f) < j:
                    continue
                for subset in combinations(sorted(f), j):
                    # Every large anticode has one unique facet.
                    assert subset not in s, (n, j, subset)
                    s.add(subset)
            assert len(s) == coeffs(n)[j]
        if n <= 4:
            count = independently_count(n)
            checked_subsets += 1 << (1 << n)
            assert [count[j] for j in range(n+2)] == coeffs(n), (n, count, coeffs(n))
        print(f'n={n} fac={len(independent_facets)} sizes={dict(Counter(map(len,independent_facets)))} coefficients={coeffs(n)}')
    print(f'VERIFY_OK dimensions=3..7 maximal_facets={total_facets} exhaustively_examined_subsets={checked_subsets}')


if __name__ == '__main__':
    main()
