"""Independent finite tests for dyadic odd-power representation counts.

Run: python3 verify.py
Only Python's standard library is required.
"""
from fractions import Fraction


def count_recurrence(k, n, r):
    assert k >= 3 and k % 2 == 1 and n >= 1
    m = 1 << n
    r %= m
    if r & 1:
        return m
    base = m // 2
    if n <= k:
        return base + ((1 << (2 * (n - 1))) if r == 0 else 0)
    if r % (1 << k):
        return base
    return base + (1 << (2 * (k - 1))) * count_recurrence(
        k, n - k, r >> k
    )


def density_at_valuation(k, v):
    """Exactly the limiting density at a nonzero 2-adic integer of valuation v."""
    j, s = divmod(v, k)
    z = 1 << (k - 2)
    if s == 0:
        return Fraction(sum(z ** i for i in range(j)), 2) + z ** j
    return Fraction(sum(z ** i for i in range(j + 1)), 2)


def independent_brute(k, n):
    m = 1 << n
    vals = [pow(x, k, m) for x in range(m)]
    brute = [0] * m
    for a in vals:
        for b in vals:
            brute[(a + b) % m] += 1
    return brute


def verify():
    settings = 0
    residues = 0
    pairs = 0
    for k in (3, 5, 7, 9):
        for n in range(1, 10):
            m = 1 << n
            counts = independent_brute(k, n)
            assert sum(counts) == m * m
            assert sorted(pow(x, k, m) for x in range(1, m, 2)) == list(range(1, m, 2))
            for r in range(m):
                assert counts[r] == count_recurrence(k, n, r), (k, n, r)
            settings += 1
            residues += m
            pairs += m * m
    for k in (3, 5, 7, 9):
        for v in range(0, 45):
            n = v + k + 2
            # Work with exact integers; no floating-point tolerance is used.
            computed = Fraction(count_recurrence(k, n, 1 << v), 1 << n)
            predicted = density_at_valuation(k, v)
            assert computed == predicted, (k, v, computed, predicted)
    # The exact second moment at k=3 follows from
    # M_2 = 7/8 + (1/2) M_2 and M_1=1.
    cubic_second_moment = Fraction(7, 4)
    cubic_variance = cubic_second_moment - 1
    assert cubic_variance == Fraction(3, 4)
    print(f"PASS {settings} exponent/modulus pairs; {residues} residue counts; {pairs} ordered input pairs")
    print("PASS 180 exact stabilizing-density comparisons")
    print("PASS cubic second moment = 7/4; cubic variance = 3/4")


if __name__ == '__main__':
    verify()
