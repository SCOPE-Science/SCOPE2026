"""Finite, reproducible checks for the strong-selection replicator horseshoe theorem.

These computations are diagnostics. The uniform-in-measure theorem follows from
analytic interval bounds and symbolic entropy inequalities, not from sampling.
Requires Python 3 and scipy (for bracketed scalar roots).
"""
import math
from itertools import product
from scipy.optimize import brentq


def make_system(a, b):
    assert a > 4 and 0 < b < 0.5
    c = math.acosh(a / 2 - 1)

    def x(y):
        return 1 / (1 + math.exp(y)) if y < 600 else math.exp(-y)

    def g(y):
        return y + a * (x(y) - b)

    def gp(y):
        z = x(y)
        return 1 - a * z * (1-z)

    y_max, y_min = -c, c
    hi = a * b + 10 * math.log(a) + 20
    y2minus = brentq(lambda y: g(y) - y_max, y_min, hi, xtol=1e-12)
    y2plus = brentq(lambda y: g(y) - y_min, y_min, hi, xtol=1e-12)
    y1minus = brentq(lambda y: g(y) - y2plus, y_max, y_min, xtol=1e-12)
    y1plus = brentq(lambda y: g(y) - y_max, y_max, y_min, xtol=1e-12)
    intervals = ((y1minus, y1plus), (y2minus, y2plus))
    assert y_max < y1minus < y1plus < y_min < y2minus < y2plus
    assert g(y1minus) > y2minus and abs(g(y1minus) - y2plus) < 1e-8
    assert abs(g(y2minus) - y_max) < 1e-8
    assert abs(g(y2plus) - y_min) < 1e-8
    return g, gp, x, intervals


def periodic_orbit(a, b, word):
    g, gp, x, intervals = make_system(a, b)
    assert any(t == 0 for t in word)
    assert all(not (word[i] == word[(i+1) % len(word)] == 1)
               for i in range(len(word)))
    def inverse(letter, y):
        lo, hi = intervals[letter]
        return brentq(lambda z: g(z) - y, lo, hi, xtol=5e-12)
    y = sum(intervals[word[0]]) / 2
    for k in range(100):
        yy = y
        for j in range(len(word)-1, -1, -1):
            yy = inverse(word[j], yy)
        if abs(yy-y) < 5e-12:
            y = yy
            break
        y = yy
    orbit = [None]*len(word)
    ynext = y
    for j in range(len(word)-1, -1, -1):
        orbit[j] = inverse(word[j], ynext)
        ynext = orbit[j]
    assert abs(ynext-y) < 1e-7
    for j, yy in enumerate(orbit):
        lo, hi = intervals[word[j]]
        assert lo - 1e-7 <= yy <= hi + 1e-7
        assert abs(g(yy)-orbit[(j+1)%len(word)]) < 1e-7
    return orbit, gp, x


def test():
    tested = 0
    for n in range(1, 13):
        for word in product((0,1), repeat=n):
            if any(word[j] == word[(j+1)%n] == 1 for j in range(n)):
                continue
            q = sum(word)/n
            # The stationary pair frequencies of a cyclic word are exact.
            n00 = sum(word[j]==0 and word[(j+1)%n]==0 for j in range(n))
            n01 = sum(word[j]==0 and word[(j+1)%n]==1 for j in range(n))
            n10 = sum(word[j]==1 and word[(j+1)%n]==0 for j in range(n))
            assert abs(n00/n-(1-2*q)) < 1e-12 and abs(n01/n-q) < 1e-12 and abs(n10/n-q) < 1e-12
            assert abs(((1-2*q)*0 + q*1 + q*(-1))) < 1e-12
            tested += 1
    max_errs = [0,0,0]
    for b, avals in [(.20, (80,180,500)), (.30, (80,180,500)),
                      (.45, (300,500,800))]:
        for a in avals:
            for word in [(0,), (0,1), (0,0,1), (0,0,0,1),
                         (0,0,1,0,1), (0,0,0,1,0,1)]:
                yy, gp, x = periodic_orbit(a,b,word)
                xx = [x(t) for t in yy]
                q = sum(word)/len(word)
                mean = sum(xx)/len(xx)
                var = sum((z-b)**2 for z in xx)/len(xx)
                exponent = sum(math.log(abs(gp(t))) for t in yy)/len(yy)
                leading = ((1-q)*math.log(a)
                           +(1-2*q)*math.log(b*(1-b))
                           +q*math.log(2*b*(1-2*b)))
                max_errs[0] = max(max_errs[0],abs(mean-b))
                max_errs[1] = max(max_errs[1],abs(var-2*b*b*q))
                max_errs[2] = max(max_errs[2],abs(exponent-leading))
                assert abs(mean-b) < 2e-6
                assert abs(var-2*b*b*q) < 0.04
                assert abs(exponent-leading) < 0.5
                tested += 1
    for q in [0, 0.1, 0.27639320225002, 0.4, 0.5]:
        if q in (0, .5):
            H = 0.0
        else:
            H = ((1-q)*math.log(1-q)-q*math.log(q)
                 -(1-2*q)*math.log(1-2*q))
        assert -1e-12 <= H <= math.log((1+5**0.5)/2)+1e-10
        tested += 1
    print('PASS: %d finite symbolic/numerical diagnostics' % tested)
    print('max mean, variance, exponent approximation errors:', *max_errs)
    print('All symbolic word tests are finite; no infinite theorem is inferred.')

if __name__ == '__main__':
    test()
