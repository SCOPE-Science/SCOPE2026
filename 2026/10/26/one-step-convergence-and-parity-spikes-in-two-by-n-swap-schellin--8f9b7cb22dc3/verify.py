"""Exhaustive finite checks for the open-neighborhood bipartite swap theorem.

Run with Python 3. No external packages are needed.
"""
from fractions import Fraction
from math import comb


def utility_distance2(bits, i, n):
    # Twice the distance to an equal-color neighborhood, using integer ratio.
    # Return (abs(2 * same - degree), degree): smaller ratio is preferred.
    other = range(2, n + 2) if i < 2 else range(2)
    degree = n if i < 2 else 2
    same = sum(bits[j] == bits[i] for j in other)
    return abs(2 * same - degree), degree


def improves(bits, changed, old_vertex, new_vertex, n):
    old_num, old_den = utility_distance2(bits, old_vertex, n)
    new_num, new_den = utility_distance2(changed, new_vertex, n)
    return new_num * old_den < old_num * new_den


def profitable_swaps(bits, n):
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            if bits[i] == bits[j]:
                continue
            new = list(bits)
            new[i], new[j] = new[j], new[i]
            if improves(bits, new, i, j, n) and improves(bits, new, j, i, n):
                yield i, j, new


def predicted_stability(a, b, n):
    if a == 1:
        return True
    if a == 0:
        return b <= 1 or (n % 2 == 0 and b == n // 2)
    return b >= n - 1 or (n % 2 == 0 and b == n // 2)


def predicted_coefficients(n):
    coeff = [0] * (n + 3)
    for b in range(n + 1):
        for a in range(3):
            if predicted_stability(a, b, n):
                coeff[a + b] += comb(2, a) * comb(n, b)
    return coeff


def closed_formula_coefficients(n):
    coeff = [0] * (n + 3)
    for b in range(n + 1):
        coeff[b + 1] += 2 * comb(n, b)
    coeff[0] += 1
    coeff[1] += n
    coeff[n + 1] += n
    coeff[n + 2] += 1
    if n >= 4 and n % 2 == 0:
        coeff[n // 2] += comb(n, n // 2)
        coeff[n // 2 + 2] += comb(n, n // 2)
    return coeff


def check(n):
    census = [0] * (n + 3)
    total = 0
    for mask in range(1 << (n + 2)):
        bits = [(mask >> i) & 1 for i in range(n + 2)]
        a = bits[0] + bits[1]
        b = sum(bits[2:])
        swaps = list(profitable_swaps(bits, n))
        stable = not swaps
        assert stable == predicted_stability(a, b, n), (n, bits, stable)
        if stable:
            census[a + b] += 1
        else:
            assert a != 1
            for _, _, changed in swaps:
                assert changed[0] + changed[1] == 1
                assert not list(profitable_swaps(changed, n))
        total += 1
    assert census == predicted_coefficients(n)
    assert census == closed_formula_coefficients(n)
    assert total == 2 ** (n + 2)
    return (n, total, sum(census), census)


if __name__ == '__main__':
    for n in range(2, 11):
        print(*check(n)[:3])
    for k in range(2, 50):
        n = 2*k
        eq = closed_formula_coefficients(n)
        critical = Fraction(eq[k], comb(n+2,k))
        balanced = Fraction(eq[k+1], comb(n+2,k+1))
        assert critical == Fraction((k+2)*(3*k+1), 2*(k+1)*(2*k+1))
        assert balanced == Fraction(k+1, 2*k+1)
        assert critical > balanced
    print('VERIFICATION_OK')
