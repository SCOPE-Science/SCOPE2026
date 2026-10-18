"""Exact finite checks for local sums of two cubes over powers of three.

Uses integer arithmetic only; no numerical Fourier transforms or external packages.
The symbolic infinite proof is supplied in RESULT.md.
"""
from collections import Counter
from fractions import Fraction


def normalized_fibres(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1, 1]
    q = 3 ** n
    h = (2, 2, 1, 0, 0, 0, 0, 1, 2)
    earlier = normalized_fibres(n - 3) if n >= 3 else None
    result = []
    for a in range(q):
        d = h[a % 9]
        if n == 2 and a == 0:
            d += 1
        if n >= 3 and a % 27 == 0:
            d += 3 * earlier[a // 27]
        result.append(d)
    assert sum(result) == q
    return result


def brute_representation_counts(n):
    q = 3 ** n
    powers = Counter(pow(x, 3, q) for x in range(q))
    results = [0] * q
    for a, ac in powers.items():
        for b, bc in powers.items():
            results[(a + b) % q] += ac * bc
    assert sum(results) == q * q
    return results


def normalized_collision(n):
    q = 3 ** n
    density = normalized_fibres(n)
    return Fraction(sum(d * d for d in density), q)


def main():
    direct_checks = 0
    for n in range(9):
        q = 3 ** n
        observed = brute_representation_counts(n)
        expected = normalized_fibres(n)
        for a in range(q):
            assert observed[a] == q * expected[a], (n, a)
            direct_checks += 1
        m = Fraction(sum(v * v for v in observed), q ** 3)
        assert m == normalized_collision(n), n
        print(f"direct mod 3^{n}: {q} target residues, collision={m}")
    bases = (Fraction(1), Fraction(1), Fraction(19, 9))
    for n in range(12):
        k, r = divmod(n, 3)
        expected = Fraction(3) + Fraction(1, 3 ** k) * (bases[r] - 3)
        assert normalized_collision(n) == expected, n
    assert normalized_collision(0) == 1
    assert normalized_collision(1) == 1
    assert normalized_collision(2) == Fraction(19, 9)
    print(f"PASS: {direct_checks} direct target comparisons; 12 exact rational moment identities")


if __name__ == '__main__':
    main()
