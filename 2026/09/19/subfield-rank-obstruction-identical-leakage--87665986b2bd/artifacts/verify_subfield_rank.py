"""Finite sanity checks for the single-output quotient-space criterion.

The script uses B = GF(2) and small binary extensions represented in polynomial
bases.  For each coefficient tuple mu it compares:
  (1) whether the classes mu_i + B are B-linearly dependent, and
  (2) the minimum B-rank of a nonzero word
      (x_1,...,x_K, sum mu_i x_i)
of the systematic single-output computation code.

The theorem predicts minimum rank 1 in the dependent case and 2 otherwise.
"""
from itertools import product

IRREDUCIBLE = {
    2: 0b111,    # x^2 + x + 1
    3: 0b1011,   # x^3 + x + 1
    4: 0b10011,  # x^4 + x + 1
}


def gf_mul(a, b, m):
    irr = IRREDUCIBLE[m]
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= irr
    return out & ((1 << m) - 1)


def rank_over_gf2(values, m):
    basis = [0] * m
    rank = 0
    for value in values:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if basis[pivot]:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                rank += 1
                break
    return rank


def quotient_rank(mu, m):
    # rank of {mu_i + GF(2)} in F/GF(2)
    return rank_over_gf2([1, *mu], m) - 1


def minimum_codeword_rank(mu, m):
    q = 1 << m
    best = m + 1
    for xs in product(range(q), repeat=len(mu)):
        if not any(xs):
            continue
        y = 0
        for coeff, x in zip(mu, xs):
            y ^= gf_mul(coeff, x, m)
        best = min(best, rank_over_gf2([*xs, y], m))
        if best == 1:
            return 1
    return best


def main():
    tests = [(2, 2), (3, 2), (3, 3), (4, 2)]
    rows = []
    for m, k in tests:
        q = 1 << m
        dependent = independent = 0
        for mu in product(range(q), repeat=k):
            dep = quotient_rank(mu, m) < k
            observed = minimum_codeword_rank(mu, m)
            expected = 1 if dep else 2
            assert observed == expected, (m, k, mu, observed, expected)
            dependent += int(dep)
            independent += int(not dep)
        rows.append((m, k, q**k, dependent, independent))

    print("criterion: PASS")
    for m, k, total, dep, indep in rows:
        print(
            f"m={m} K={k} tuples={total} "
            f"dependent={dep} independent={indep}"
        )
    assert rows[0][4] == 0
    print("quadratic-extension two-input obstruction: PASS")


if __name__ == "__main__":
    main()
