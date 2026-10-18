"""Self-contained arithmetic and simulation checks for the circle graph covariance law."""
from fractions import Fraction
from math import comb, sqrt
from random import Random


def theory(n, r):
    assert n >= 2 and 0 < r < Fraction(1, 2)
    a = 1 - 2*r
    p = 1 - ((a-r)/a)**2 if r <= Fraction(1, 3) else Fraction(1)
    return Fraction(n * comb(n-1, 2)) * a**(n-1) * p - Fraction(n*comb(n, 2))*a**(n-1)*2*r


def polynomial_form(n, r):
    assert r <= Fraction(1, 3)
    return Fraction(n*(n-1), 2)*r*(1-2*r)**(n-3)*(-4+(3*n+10)*r-8*n*r*r)


def simulate(n, r, trials, seed):
    rng = Random(seed)
    si = se = sie = 0
    rr = float(r)
    for _ in range(trials):
        pos = sorted(rng.random() for _ in range(n))
        degrees = [0]*n
        edges = 0
        for i in range(n):
            for j in range(i+1, n):
                d = pos[j]-pos[i]
                if min(d, 1-d) <= rr:
                    edges += 1
                    degrees[i] += 1
                    degrees[j] += 1
        isol = degrees.count(0)
        si += isol
        se += edges
        sie += edges*isol
    return sie/trials-(si/trials)*(se/trials)


if __name__ == '__main__':
    for n in range(2, 41):
        for k in range(1, 100):
            r = Fraction(k, 200)
            if r <= Fraction(1, 3):
                assert theory(n, r) == polynomial_form(n, r), (n, r)
            if n <= 5:
                assert theory(n, r) < 0
            elif n >= 6:
                # This test uses the independently derived threshold signs.
                lo = ((3*n+10)-sqrt((3*n+10)**2-128*n))/(16*n)
                hi = (n-2)/(2*n)
                wanted = 1 if lo < float(r) < hi else -1
                actual = (theory(n, r)>0)-(theory(n, r)<0)
                if abs(float(r)-lo)>1e-12 and abs(float(r)-hi)>1e-12:
                    assert actual == wanted, (n, r, actual, wanted)
    print('Exact rational identities and signs: n=2..40, r=k/200, k=1..99: PASS')
    tests = [(5, Fraction(3,10)), (6, Fraction(7,25)),
             (6, Fraction(7,20)), (7, Fraction(11,50)),
             (7, Fraction(19,50)), (10, Fraction(1,10))]
    for idx, (n,r) in enumerate(tests):
        predicted = float(theory(n, r))
        observed = simulate(n, r, 180000, 105 + idx)
        print('n=%d r=%s predicted=% .7f MonteCarlo=% .7f' % (n,str(r),predicted,observed))
        assert abs(predicted-observed) < (0.025 if n<10 else 0.045)
    print('Independent Monte Carlo checks: PASS (not a proof)')
