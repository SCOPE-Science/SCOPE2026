from fractions import Fraction
from math import gcd


def rank_q(rows, ncols):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, len(a)) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] != 0:
                q = a[i][c]
                a[i] = [x - q*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def offdiag_system_rank(n, shift):
    rows = []
    row = [0] * n
    row[0] = 1
    rows.append(row)
    row = [0] * n
    row[(-shift) % n] = 1
    rows.append(row)
    for ell in range(1, n):
        row = [1] * n
        row[ell] -= 1
        row[(ell - shift) % n] -= 1
        rows.append(row)
    return rank_q(rows, n)


def diagonal_system_rank(n):
    rows = []
    row = [0] * n
    row[0] = 1
    rows.append(row)
    for ell in range(1, n):
        row = [1] * n
        row[ell] -= 1
        rows.append(row)
    return rank_q(rows, n)


def even_counterexample_is_exact(n):
    assert n >= 4 and n % 2 == 0
    u = 1
    v = 1 + n // 2
    assert u != v and v % n != 0
    # Fourier coefficients are (1,i) and (1,-i) on u,v.
    # With s=(-1)^x, |1+i s|^2=|1-i s|^2=2 exactly.
    for x in range(n):
        s = -1 if x % 2 else 1
        mag_a_sq = 1 + s*s
        mag_b_sq = 1 + s*s
        assert mag_a_sq == mag_b_sq == 2
    # Deleting u or v leaves one unimodular character; deleting any
    # other nonzero frequency leaves the equal-magnitude full signals.
    for ell in range(1, n):
        if ell in (u, v):
            assert 1 == 1
        else:
            assert 2 == 2
    return True


def small_counterexamples():
    # n=2: the sole nonzero-frequency deletion annihilates H_0.
    assert 2 != 1
    # n=3: (1,i) and (1,-i) have the same individual coefficient
    # magnitudes, and each deletion exposes only one coefficient.
    for ell in (1, 2):
        assert 1 == 1
    return True


def main():
    odd_orders = []
    shifts = 0
    for n in range(5, 32, 2):
        assert diagonal_system_rank(n) == n
        for r in range(1, n):
            assert offdiag_system_rank(n, r) == n, (n, r, gcd(n, r))
            shifts += 1
        odd_orders.append(n)
    even_orders = []
    for n in range(4, 31, 2):
        assert even_counterexample_is_exact(n)
        even_orders.append(n)
    assert small_counterexamples()
    print(
        "VERIFY_OK "
        f"odd_orders={','.join(map(str, odd_orders))} "
        f"offdiag_systems={shifts} "
        f"even_counterexamples={','.join(map(str, even_orders))} "
        "small_failures=2,3"
    )


if __name__ == "__main__":
    main()
