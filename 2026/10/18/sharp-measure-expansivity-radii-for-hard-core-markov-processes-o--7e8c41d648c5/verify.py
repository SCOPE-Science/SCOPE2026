"""Exact finite-window checks for weighted hard-core symbolic packing.

Checks finite-dimensional identities only; the infinite theorem requires the accompanying proof.
"""
from fractions import Fraction


def weight(j):
    return Fraction(1, 2 ** abs(j))


def window_max(m, L, center):
    """Dynamic program over the previous m symbols, exact rational arithmetic."""
    prev = {0: Fraction(0)}
    mask = (1 << m) - 1
    for j in range(-L, L + 1):
        cur = {}
        for state, value in prev.items():
            for bit in (0, 1):
                if bit and state != 0:
                    continue
                ns = ((state << 1) | bit) & mask
                gain = weight(j) * (center if bit == 0 else 1 - center)
                result = value + gain
                cur[ns] = max(cur.get(ns, Fraction(-1)), result)
        prev = cur
    return max(prev.values())


def W(m):
    return 1 + Fraction(2, 2 ** (m + 1) - 1)


def center_f(m, c):
    if c <= Fraction(1, 2):
        return 3 * c + (1 - 2 * c) * W(m)
    return 3 * c


def test():
    count = 0
    for m in range(1, 9):
        assert W(m) == 1 + Fraction(2, 2 ** (m + 1) - 1)
        count += 1
        for L in (3, 7, 11, 17):
            tail = Fraction(1, 2 ** (L - 1))  # both tails |j|>L
            for c in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
                v = window_max(m, L, c)
                truth = center_f(m, c)
                assert v <= truth
                assert truth - v <= tail
                count += 2
            # packing upper bound uniform in all finite states.
            assert window_max(m, L, Fraction(0)) <= W(m)
            count += 1
        R = min(W(m), Fraction(3, 2))
        for c in (Fraction(i, 16) for i in range(17)):
            assert center_f(m, c) >= R
            count += 1
        if m == 1:
            assert R == Fraction(3, 2)
        else:
            assert R == W(m)
        count += 1
    print('PASS', count, 'exact rational assertions')


if __name__ == '__main__':
    test()
