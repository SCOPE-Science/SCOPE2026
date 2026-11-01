"""Deterministic numerical checks for the weighted-skew Hilbert-space phase law.

These finite tests are illustrations, not proofs of all quantified cases.
Requires only the Python standard library.
"""
import math
import random


def value(alpha, p):
    delta = abs(2.0 * alpha - 1.0)
    if p == 1:
        return 1.0
    if p < 2:
        q = p / (p - 1.0)
        return (1.0 + delta**q)**(1.0 / q)
    return 2.0**(1.0 - 1.0 / p) * math.sqrt(alpha**2 + (1.0 - alpha)**2)


def tested(alpha, p, r, s, c):
    norm = r + s if p == 1 else max(r, s) if math.isinf(p) else (r**p + s**p)**(1.0/p)
    r, s = r / norm, s / norm
    a = math.sqrt(max(0.0, r*r + s*s + 2*r*s*c))
    b = math.sqrt(max(0.0, r*r + s*s - 2*r*s*c))
    return alpha*a + (1.0-alpha)*b


def witness(alpha, p):
    d = abs(2.0*alpha - 1.0)
    sign = 1.0 if alpha >= .5 else -1.0
    if p == 1:
        return (1.0, 0.0, 0.0)
    if p < 2:
        t = d**(1.0/(p-1.0))
        return (1.0, t, sign)
    return (1.0, 1.0, (2.0*alpha-1.0)/(alpha**2+(1.0-alpha)**2))


def entropy(q):
    return -(q*math.log(q) if q > 0 else 0.0) - ((1-q)*math.log(1-q) if q < 1 else 0.0)


def main():
    rng = random.Random(26800933)
    count = 0
    alphas = [0.001, 0.08, 0.2, 0.41, 0.5, 0.59, 0.8, 0.92, 0.999]
    ps = [1.0, 1.01, 1.15, 1.5, 1.8, 1.99, 2.0, 2.01, 2.5, 3.0, 10.0, 100.0, float('inf')]
    for a in alphas:
        for p in ps:
            bound = value(a, p)
            rr, ss, cc = witness(a, p)
            assert abs(tested(a, p, rr, ss, cc) - bound) < 2e-11, (a, p, bound)
            count += 1
            for j in range(160):
                r = 10.0 ** rng.uniform(-3.0, 3.0)
                s = 10.0 ** rng.uniform(-3.0, 3.0)
                c = rng.uniform(-1.0, 1.0)
                assert tested(a, p, r, s, c) <= bound + 3e-11, (a, p, r, s, c)
                count += 1
    for a in [0.1, 0.4, 0.5, 0.8, 0.95]:
        delta = abs(2*a - 1)
        qq = delta*delta/(1.0+delta*delta)
        expected = entropy(qq)/4.0
        for h in [0.005, 0.002, 0.001]:
            left = (math.log(value(a, 2.0)) - math.log(value(a, 2.0-h)))/h
            assert abs(left - expected) < 0.012
            count += 1
        right = math.log(2)/4
        for h in [0.005,0.002,0.001]:
            found = (math.log(value(a, 2+h)) - math.log(value(a, 2)))/h
            assert abs(found - right) < 0.012
            count += 1
    print(f'PASS: {count} deterministic checks; numerical experiments do not certify infinite statements.')

if __name__ == '__main__':
    main()
