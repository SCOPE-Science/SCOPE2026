"""Exact integer checks for the even two-prime arithmetic-derivative/totient theorem.

Dependency: sympy. Checks are finite experiments, not the unrestricted proof.
"""
from fractions import Fraction
from sympy import factorint, primerange


def arithmetic_derivative(n):
    if n == 1:
        return 0
    factors = factorint(n)
    return sum(exponent * (n // prime) for prime, exponent in factors.items())


def admissible(p):
    assert p > 2 and len(factorint(p)) == 1
    u = p - 1
    while u % 2 == 0:
        u //= 2
    return len(factorint(u)) <= 2


def classified(a, p, b):
    if not admissible(p):
        return False
    if p == 3:
        return (a, b) in {(6, 1), (4, 4), (2, 7)}
    if p == 5:
        return (a, b) in {(4, 1), (2, 6)}
    if p == 61:
        return (a, b) == (2, 1)
    return (p - 1) % 2 == 0 and len(factorint((p - 1) // 2)) == 1 and \
        all(e == 1 for e in factorint((p - 1) // 2).values()) and \
        (p - 1) // 2 > 2 and ((a, b) == (4, 1) or (a, b) == (2, p + 1))


def equation(a, p, b):
    n = (2 ** a) * (p ** b)
    phi_n = (2 ** (a - 1)) * (p ** (b - 1)) * (p - 1)
    return arithmetic_derivative(phi_n) == n


def exact_criterion(a, p, b):
    f = factorint(p - 1)
    t = f.pop(2)
    u = (p - 1) // 2 ** t
    if t not in (1, 2) or any(e != 1 for e in f.values()) or (b - 1) % p:
        return False
    k = (b - 1) // p
    s = sum((Fraction(1, q) for q in f), Fraction(0))
    h = (s - Fraction(1, u)) if t == 1 else (2 * s - Fraction(1, u))
    if h.denominator != 1:
        return False
    return a == (4 if t == 1 else 3) - (2 * k) - (2 * h.numerator if t == 1 else h.numerator)


def main():
    total = 0
    observed = []
    for p in primerange(3, 501):
        for a in range(1, 11):
            for b in range(1, 18):
                answer = equation(a, p, b)
                criterion = exact_criterion(a, p, b)
                assert answer == criterion, (a, p, b, answer, criterion)
                if admissible(p):
                    assert answer == classified(a, p, b), (a, p, b, answer)
                if answer:
                    observed.append((a, p, b))
                total += 1
    long_exp = 0
    for p in primerange(3, 201):
        if not admissible(p):
            continue
        for a in range(1, 9):
            for b in (1, p + 1, 2 * p + 1):
                assert equation(a, p, b) == classified(a, p, b), (a, p, b)
                long_exp += 1
    assert (2, 61, 1) in observed
    assert (2, 7, 8) in observed
    print(f"EXACT_CHECK_OK short_triples={total} extended_exponents={long_exp} "
          f"short_hits={len(observed)} exceptional=(2,61,1)")


if __name__ == '__main__':
    main()
