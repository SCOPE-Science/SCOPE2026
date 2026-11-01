"""Self-contained exact arithmetic checks for the diameter-two anticode enumerator.

Requires Python 3.10+; no external packages or input files.
"""
from itertools import product
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def coefficients(q, n):
    """Closed formula for number of diameter<=2 sets by cardinality."""
    r = q - 1
    highest = max(n * r + 1, q * q, 4)
    ans = [1]
    for k in range(1, highest + 1):
        j = k - 1
        anchored = (
            (1+n*r)*choose(n*r, j)
            + choose(n, 2)*choose(r*r + 2*r, j)
            - (choose(n, 2) + n*r*(n-1))*choose(2*r, j)
            + n*r*(n-2)*choose(r, j)
            + (choose(n, 3)*r**3 if j == 3 else 0)
        )
        numerator = q**n * anchored
        assert numerator >= 0 and numerator % k == 0, (q, n, k, numerator)
        ans.append(numerator // k)
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ans


def independent_clique_enumeration(q, n):
    """Count all vertex subsets, using only Hamming adjacency, not the theorem."""
    vertices = list(product(range(q), repeat=n))
    size = len(vertices)
    adj = [0] * size
    for i in range(size):
        for j in range(i + 1, size):
            if sum(a != b for a, b in zip(vertices[i], vertices[j])) <= 2:
                adj[i] |= 1 << j
    counts = [0] * (size + 1)
    counts[0] = 1

    def extend(candidates, depth):
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1
            counts[depth + 1] += 1
            extend(candidates & adj[v], depth + 1)

    extend((1 << size) - 1, 0)
    while len(counts) > 1 and counts[-1] == 0:
        counts.pop()
    return counts


def binary_known_total(n):
    # OEIS A295922, with its dimension parameter N = n+1.
    N = n + 1
    numerator = 24 * (2 + 4**N) + 2**N * N * ((N-9)*N-16)
    assert numerator % 48 == 0
    return numerator // 48


def main():
    cases = [(2,n) for n in range(1,9)] + [(3,n) for n in range(1,5)]
    cases += [(4,1),(4,2),(4,3),(5,1),(5,2)]
    for q,n in cases:
        a = coefficients(q,n)
        b = independent_clique_enumeration(q,n)
        assert a == b, (q,n,a,b)
        print(f"EXACT q={q} n={n}: {sum(a)} anticodes; {len(a)-1} maximum cardinality; PASS")
    for q in range(2,9):
        for n in range(1,21):
            c = coefficients(q,n)
            assert c[1] == q**n
            assert c[2] == q**n * (n*(q-1) + choose(n,2)*(q-1)**2) // 2
    print("COEFFICIENT arithmetic q=2..8, n=1..20: 140 cases; PASS")
    for n in range(1,21):
        assert sum(coefficients(2,n)) == binary_known_total(n)
    print("KNOWN BINARY TOTAL OEIS A295922, n=1..20: PASS")
    print("ALL TESTS PASSED")


if __name__ == '__main__':
    main()
