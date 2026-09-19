from fractions import Fraction
from math import prod
import random
import sympy as sp


def v2_int(n: int) -> int:
    if n == 0:
        raise ZeroDivisionError('v2(0) is infinite')
    n = abs(int(n))
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def v2_rat(q: Fraction) -> int:
    q = Fraction(q)
    if q == 0:
        raise ZeroDivisionError('v2(0) is infinite')
    return v2_int(q.numerator) - v2_int(q.denominator)


def H(a: int, primes) -> Fraction:
    primes = list(primes)
    out = Fraction(1, 1)
    for mask in range(1 << len(primes)):
        d = 1
        parity = 0
        for i, p in enumerate(primes):
            if (mask >> i) & 1:
                d *= p
                parity ^= 1
        factor = 2 ** (a * d) - 1
        if parity:
            out /= factor
        else:
            out *= factor
    return out


def signed_power(C: int, sign: int) -> Fraction:
    return Fraction(C, 1) if sign == 1 else Fraction(1, C)


def cyclotomic_value(n: int) -> int:
    out = Fraction(1, 1)
    for d in sp.divisors(n):
        mu = int(sp.mobius(n // d))
        factor = 2 ** d - 1
        if mu == 1:
            out *= factor
        elif mu == -1:
            out /= factor
    if out.denominator != 1:
        raise AssertionError('cyclotomic product is not integral')
    return out.numerator


def peel(n: int, C: int):
    a = v2_int(C - 1)
    if n % a:
        raise AssertionError('radical quotient does not divide n')
    r = n // a

    if a > 1:
        A = 2 ** a - 1
        cand = {
            s: v2_rat(signed_power(C, s) / A + 1)
            for s in (1, -1)
        }
        eps = max(cand, key=cand.get)
        if cand[eps] % a:
            raise AssertionError('initial scale is not divisible by a')
        found = [cand[eps] // a]
    else:
        p1 = v2_int(C + 1)
        found = [p1]
        if prod(found) == r:
            return found

        if p1 == 2 and r % 3 == 0:
            found.append(3)
            if prod(found) == r:
                return found

        h = H(1, found)
        cand = {
            s: v2_rat(signed_power(C, s) / h - 1)
            for s in (1, -1)
        }
        eps = max(cand, key=cand.get)
        found.append(cand[eps])

    while prod(found) < r:
        h = H(a, found)
        scale = v2_rat(signed_power(C, eps) / h - 1)
        if scale % a:
            raise AssertionError('peeling scale is not divisible by a')
        found.append(scale // a)

    if prod(found) != r:
        raise AssertionError('recovered support does not multiply to rad(n)')
    return found


def check_range(lo: int, hi: int):
    checked = 0
    for n in range(lo, hi + 1):
        C = cyclotomic_value(n)
        got = peel(n, C)
        want = sorted(sp.factorint(n))
        if got != want:
            raise AssertionError((n, got, want))
        checked += 1
    return checked


def check_random(seed: int, count: int, lo: int, hi: int):
    rng = random.Random(seed)
    values = rng.sample(range(lo, hi + 1), count)
    for n in values:
        C = cyclotomic_value(n)
        got = peel(n, C)
        want = sorted(sp.factorint(n))
        if got != want:
            raise AssertionError((n, got, want))
    return values


def diagnostics(n: int):
    C = cyclotomic_value(n)
    a = v2_int(C - 1)
    r = n // a
    return n, C, a, r, peel(n, C)


if __name__ == '__main__':
    total = check_range(2, 1199)
    random_values = check_random(260919, 100, 1200, 5000)
    print(f'SymPy {sp.__version__}')
    print(f'exhaustive n=2..1199: {total} passed')
    print('random n=1200..5000: 100 passed')
    print('random sample first five:', random_values[:5])
    for n in (45, 105, 210, 315):
        print('example', diagnostics(n))
