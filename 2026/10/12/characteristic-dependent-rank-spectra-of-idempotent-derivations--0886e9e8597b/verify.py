"""Finite-prime-field checks for idempotent derivations of triangular matrix algebras.

Run with: python3 verify.py
The symbolic proof covers all fields; these finite checks are supplementary.
"""
from itertools import product
from math import comb


def expected(n, p):
    ranks = {0: 1}
    for k in range(1, n):
        exponent = k * (n - k)
        multiplicity = comb(n-1, k) if p == 2 else 1
        ranks[exponent] = ranks.get(exponent, 0) + multiplicity * p**exponent
    return ranks


def direct_count(n, p):
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    dim = len(pairs)
    idx = {a: i for i, a in enumerate(pairs)}
    answers = {}
    # The first diagonal entry is normalized to zero; inner derivations
    # have a unique representative modulo scalar matrices.
    for coefficients in product(range(p), repeat=dim-1):
        h = dict(zip(pairs, (0,) + coefficients))
        # Compute D(E_ab) = HE_ab - E_ab H by matrix-unit multiplication.
        D = [[0] * dim for _ in range(dim)]
        for col, (a, b) in enumerate(pairs):
            for i in range(a + 1):
                D[idx[i,b]][col] = (D[idx[i,b]][col] + h[i,a]) % p
            for j in range(b, n):
                D[idx[a,j]][col] = (D[idx[a,j]][col] - h[b,j]) % p
        # Exact matrix multiplication tests D^2 = D.
        if any(sum(D[row][j] * D[j][col] for j in range(dim)) % p
               != D[row][col] for row in range(dim) for col in range(dim)):
            continue
        # Gaussian elimination computes actual rank, not trace modulo p.
        rows = [r[:] for r in D]
        rank = 0
        for col in range(dim):
            pivot = next((t for t in range(rank, dim) if rows[t][col]), None)
            if pivot is None:
                continue
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            inv = pow(rows[rank][col], -1, p)
            rows[rank] = [(a * inv) % p for a in rows[rank]]
            for row in range(rank + 1, dim):
                f = rows[row][col]
                if f:
                    rows[row] = [(a - f*b) % p for a, b in zip(rows[row], rows[rank])]
            rank += 1
        answers[rank] = answers.get(rank, 0) + 1
    return answers


def main():
    cases = [(2,2), (2,3), (2,5), (3,2), (3,3), (3,5), (4,2), (4,3), (5,2)]
    for n, p in cases:
        observed = direct_count(n, p)
        predicted = expected(n, p)
        assert observed == predicted, (n, p, observed, predicted)
        print(f"n={n}, p={p}: ranks={sorted(observed.items())}, verified")
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
