"""Finite diagnostics for a variance-drift law for periodic weighted shifts.

This script performs finite checks only. Infinite orbital and spectral statements
must be justified by the mathematical proof accompanying this script.
"""
import math
from fractions import Fraction


def log_product(alpha, periodic, start, length):
    p = len(periodic)
    return sum(math.log1p(float(alpha)/j+float(periodic[(j-1)%p])/math.sqrt(j))
               for j in range(start, start+length))


def check():
    cases = [
        (Fraction(1, 10), (Fraction(-2,5), Fraction(2,5))),
        (Fraction(1, 20), (Fraction(-2,5), Fraction(2,5))),
        (Fraction(2, 25), (Fraction(-2,5), Fraction(2,5))),
        (Fraction(1, 12), (Fraction(1,2), Fraction(0), Fraction(-1,2))),
        (Fraction(1, 8), (Fraction(1,2), Fraction(-1,2), Fraction(-1,2), Fraction(1,2))),
        (Fraction(0), (Fraction(0),)),
        (Fraction(1), (Fraction(0),)),
    ]
    results = []
    for alpha, c in cases:
        assert sum(c) == 0
        assert max(map(abs,c))<=Fraction(1,2)
        variance = sum(x*x for x in c)/len(c)
        delta = alpha-variance/2
        for start in (1, 2, 7, 36):
            residuals = [log_product(alpha, c, start, n)-float(delta)*math.log((start+n)/start)
                         for n in (100, 1000, 5000)]
            # Finite diagnostics for bounded and converging log corrections.
            assert max(residuals)-min(residuals)<.30, (alpha,c,start,residuals)
            assert max(abs(x) for x in residuals)<3.0,(alpha,c,start,residuals)
            results.append((str(alpha), tuple(str(x) for x in c), str(delta), start,
                            tuple(round(x,8) for x in residuals)))
    for row in results:
        print(*row)
    print('28 finite parameter/start-index diagnostics passed')


if __name__ == '__main__':
    check()
