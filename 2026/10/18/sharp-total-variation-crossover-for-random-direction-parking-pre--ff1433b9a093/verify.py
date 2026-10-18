"""Reproducible exact finite checks and asymptotic numerical probes for the parking-preference theorem.
No external data or third-party manuscripts are needed; Python 3 standard library only.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, factorial, gamma, lgamma, log, pi, sqrt


def coefficient(n, j):
    """The finite Abel-Cayley weight; integer powers at endpoints are exactly 1."""
    assert n >= 2 and 1 <= j <= n
    numerator = comb(n - 1, j - 1) * (1 if j == 1 else j ** (j - 2)) * (1 if j == n else (n + 1 - j) ** (n - j - 1))
    # Negative exponents occur only with base 1, hence numerator is integral.
    assert isinstance(numerator, int)
    return Fraction(numerator, (n + 1) ** (n - 1))


def parking_distribution(n, p):
    b = [coefficient(n, j) for j in range(1, n + 1)]
    assert sum(b) == Fraction(2, n + 1)
    q = []
    for j in range(n):
        f = sum(b[:j]) - sum(b[j + 1 :])
        q.append(Fraction(1, n + 1) + b[j] / 2 - (p - Fraction(1, 2)) * f)
    return q


def process_distribution(n, p):
    """Independently enumerate all preference lists and all conditional coin outcomes."""
    q = [Fraction(0) for _ in range(n)]
    success = Fraction(0)
    for preference in product(range(n), repeat=n):
        states = {0: Fraction(1)}
        for a in preference:
            nextstates = {}
            for occupied, mass in states.items():
                if not ((occupied >> a) & 1):
                    entries = [(a, Fraction(1))]
                else:
                    right = next((b for b in range(a + 1, n) if not ((occupied >> b) & 1)), None)
                    left = next((b for b in range(a - 1, -1, -1) if not ((occupied >> b) & 1)), None)
                    entries = []
                    if right is not None: entries.append((right, p))
                    if left is not None: entries.append((left, 1 - p))
                for where, wt in entries:
                    state = occupied | (1 << where)
                    nextstates[state] = nextstates.get(state, Fraction(0)) + mass * wt
            states = nextstates
        mass = sum(states.values())
        success += mass
        q[preference[-1]] += mass
    assert success == Fraction((n + 1) ** (n - 1), 1)
    return [x / success for x in q]


def tv_float(n, p):
    """Log-gamma evaluation avoids astronomical powers for large n."""
    b = []
    for j in range(1, n + 1):
        k = n + 1 - j
        z = (lgamma(n) - lgamma(j) - lgamma(k)
             + (j - 2) * log(j) + (k - 2) * log(k)
             - (n - 1) * log(n + 1))
        b.append(exp(z))
    total = sum(b)
    f = []
    pref = 0.0
    for v in b:
        f.append(2 * pref + v - total)
        pref += v
    return sum(abs(-1 / (n * (n + 1)) + v / 2 - (p - 0.5) * w)
               for v, w in zip(b, f)) / 2


def main():
    count = 0
    for n in range(2, 25):
        for j in range(1, n + 1):
            assert coefficient(n, j) == coefficient(n, n + 1 - j)
            count += 1
        for p in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1)):
            q = parking_distribution(n, p)
            assert sum(q) == 1 and all(v >= 0 for v in q)
            assert q == list(reversed(parking_distribution(n, 1-p)))
            count += 3
    for n in (2, 3, 4):
        for p in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1)):
            assert parking_distribution(n, p) == process_distribution(n, p)
            count += n
    assert Fraction(0) < sum(parking_distribution(10, Fraction(1, 2))) == 1
    # These are convergence diagnostics, not substitutes for the analytic limit proof.
    checks = []
    for n in (200, 1000, 5000, 20000):
        data = []
        for t in (0, Fraction(1, 2), 1, 2):
            v = n * tv_float(n, 0.5 + float(t) / sqrt(n))
            target = (1 + sqrt(1 + 32 * float(t) ** 2 / pi)) / 2
            data.append((float(t), v, target))
        fixed = sqrt(n) * tv_float(n, 1)
        checks.append((n, data, fixed))
    for (na, da, fa), (nb, db, fb) in zip(checks, checks[1:]):
        for (ta, va, la), (tb, vb, lb) in zip(da, db):
            assert ta == tb and abs(vb - lb) < abs(va - la)
            count += 1
        assert abs(fb - sqrt(2 / pi)) < abs(fa - sqrt(2 / pi))
        count += 1
    print('PASS:', count, 'finite identities, independent process comparisons and monotone numerical asymptotic probes')
    for n, triples, fixed in checks:
        print('n', n, 'nTV(t=0,0.5,1,2)', [round(x[1], 6) for x in triples],
              'sqrt(n)TV(p=1)', round(fixed, 6))


if __name__ == '__main__':
    main()
