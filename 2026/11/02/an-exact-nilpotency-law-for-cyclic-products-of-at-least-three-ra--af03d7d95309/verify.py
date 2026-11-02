"""Exhaustive small finite-field checks for cyclic matrix-product nilpotency.

Run with python3 verify.py. All enumerations in this file use prime fields.
They verify finite instances only; the general theorem has a separate proof.
"""
from itertools import product
from collections import Counter
from fractions import Fraction


def all_matrices(rows, cols, q):
    return list(product(range(q), repeat=rows * cols))


def mul(a, b, nrows, middle, ncols, q):
    return tuple(sum(a[i * middle + k] * b[k * ncols + j]
                     for k in range(middle)) % q
                 for i in range(nrows) for j in range(ncols))


def nilpotent(a, n, q):
    power = a
    for _ in range(n):
        if all(x == 0 for x in power):
            return True
        power = mul(power, a, n, n, n, q)
    return False


def count_cycles(dims, q):
    # dims=(n0,...,n_{t-1}) and A_i maps V_{i-1} to V_i,
    # with V_t=V0. Product A_t ... A_1 acts on V0.
    sizes = tuple(dims) + (dims[0],)
    maps = [all_matrices(sizes[i + 1], sizes[i], q)
            for i in range(len(dims))]
    success = 0
    total = 0
    for mats in product(*maps):
        composed = mats[0]
        for i in range(1, len(mats)):
            composed = mul(mats[i], composed, sizes[i + 1], sizes[i], sizes[0], q)
        success += nilpotent(composed, sizes[0], q)
        total += 1
    prediction = 1 - __import__('functools').reduce(
        lambda a, dim: a * (1 - Fraction(1, q ** dim)), dims, Fraction(1))
    assert Fraction(success, total) == prediction, (dims, q, success, total, prediction)
    print(f"cycle_dims={dims} q={q} nilpotent={success}/{total} probability={prediction}")


def rank(a, rows, cols, q):
    a = [list(a[i * cols:(i + 1) * cols]) for i in range(rows)]
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if a[i][c] % q), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        inv = pow(a[r][c], -1, q)
        a[r] = [(v * inv) % q for v in a[r]]
        for i in range(rows):
            if i != r:
                coef = a[i][c]
                a[i] = [(v - coef * w) % q for v, w in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


def conditional_check(n0, n1, q):
    for a in all_matrices(n1, n0, q):
        r = rank(a, n1, n0, q)
        possible_b = all_matrices(n0, n1, q)
        k = sum(nilpotent(mul(b, a, n0, n1, n0, q), n0, q)
                for b in possible_b)
        assert Fraction(k, len(possible_b)) == Fraction(1, q ** r), (a, r, k)
    print(f"conditional_rank_lemma_dims={(n0,n1)} q={q} verified")


if __name__ == '__main__':
    for dims, q in [((1,), 2), ((2,), 2), ((2, 2), 2),
                    ((2, 2, 2), 2), ((2, 2), 3),
                    ((1, 2), 2), ((2, 1), 2),
                    ((1, 2, 3), 2), ((3, 2, 1), 2),
                    ((1, 1, 1, 1), 3)]:
        count_cycles(dims, q)
    conditional_check(2, 2, 2)
    conditional_check(2, 2, 3)
    conditional_check(2, 1, 3)
    print('VERIFY_OK')
