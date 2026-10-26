"""Reproduce the two-year lake-loading reversal calculations (Python standard library)."""
from decimal import Decimal, getcontext
from fractions import Fraction
import math
import random


def transition(p, loss, recycle, half, loading):
    return ((1 - loss) * p + recycle * p * p / (half * half + p * p)
            + loading)


def order_difference(p, loss, recycle, half, low, high):
    high_low = transition(transition(p, loss, recycle, half, high),
                          loss, recycle, half, low)
    low_high = transition(transition(p, loss, recycle, half, low),
                          loss, recycle, half, high)
    return high_low - low_high


def formula_difference(p, loss, recycle, half, low, high):
    first = transition(p, loss, recycle, half, 0)
    t, d = first + low, high - low
    gain = half * half * (2 * t + d) / (
        (half * half + t * t) * (half * half + (t + d) ** 2))
    return d * (recycle * gain - loss)


def bisect(fun, lower, upper):
    f0 = fun(lower)
    f1 = fun(upper)
    assert f0 * f1 < 0
    for _ in range(260):
        mid = (lower + upper) / 2
        fm = fun(mid)
        if fm == 0:
            return mid
        if f0 * fm > 0:
            lower, f0 = mid, fm
        else:
            upper, f1 = mid, fm
    return (lower + upper) / 2


def exact_example():
    b, r, m = Fraction(12, 25), Fraction(1), Fraction(1)
    low, high = Fraction(0), Fraction(3, 10)
    def slope(p):
        return 1 - b + 2 * r * m * m * p / (m * m + p * p) ** 2
    for p in (Fraction(0), Fraction(3, 4), Fraction(4, 3)):
        assert transition(p, b, r, m, Fraction(0)) == p
    assert slope(Fraction(0)) == Fraction(13, 25)
    assert slope(Fraction(3, 4)) == Fraction(709, 625)
    assert slope(Fraction(4, 3)) == Fraction(541, 625)
    for x, expected in ((Fraction(0), -1), (Fraction(1, 2), 1),
                        (Fraction(1), -1)):
        value = order_difference(x, b, r, m, low, high)
        assert value * expected > 0
        assert value == formula_difference(x, b, r, m, low, high)
    d = high - low
    k = lambda t: (2 * t + d) / ((1 + t * t) * (1 + (t + d) ** 2))
    assert k(Fraction(0)) < b / r < k(Fraction(1, 2))
    getcontext().prec = 85
    bd, dd = Decimal(12) / Decimal(25), Decimal(3) / Decimal(10)
    def kd(t):
        return (2*t+dd)/((1+t*t)*(1+(t+dd)**2))
    def gd(x):
        return (1-bd)*x + x*x/(1+x*x)
    t1 = bisect(lambda t: kd(t)-bd, Decimal(0), Decimal('0.5'))
    t2 = bisect(lambda t: kd(t)-bd, Decimal('0.5'), Decimal(2))
    x1 = bisect(lambda x: gd(x)-t1, Decimal(0), Decimal('0.5'))
    x2 = bisect(lambda x: gd(x)-t2, Decimal('0.5'), Decimal(2))
    assert abs(x1-Decimal('0.2005578231464619247581292044')) < Decimal('1e-25')
    assert abs(x2-Decimal('0.8769914992399731600155127343')) < Decimal('1e-25')
    print('initial_stock_crossover_1 =', x1)
    print('initial_stock_crossover_2 =', x2)
    print('state_crossover_1 =', t1)
    print('state_crossover_2 =', t2)


def random_checks():
    rng = random.Random(20261022)
    for _ in range(3000):
        loss = rng.uniform(.03, .97)
        recycle = 10 ** rng.uniform(-1.2, .5)
        half = 10 ** rng.uniform(-.5, .5)
        low = rng.uniform(0, 1)
        high = low + rng.uniform(.02, 1.5)
        p = rng.uniform(0, 5)
        a = order_difference(p, loss, recycle, half, low, high)
        b = formula_difference(p, loss, recycle, half, low, high)
        assert math.isclose(a, b, abs_tol=5e-13*(1+abs(a)), rel_tol=3e-12)
    print('3000 direct-vs-identity floating-point comparisons passed')


if __name__ == '__main__':
    exact_example()
    random_checks()
