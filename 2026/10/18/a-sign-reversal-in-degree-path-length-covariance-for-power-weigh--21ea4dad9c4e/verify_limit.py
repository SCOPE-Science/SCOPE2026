"""Exact finite identities and a sample sign reversal.

Run with Python 3. The large-label and infinite-size limits require the proof.
"""
from fractions import Fraction as Q
from itertools import product


def profiles(alpha, n):
    w = [Q(0)] + [Q(k)**alpha for k in range(1, n+1)]
    W = [sum(w[:j+1]) for j in range(n+1)]
    p = [Q(0)] + [w[j]/W[j] for j in range(1, n+1)]
    return w, W, p


def outcomes(w, W, n, i):
    et = er = etr = Q(0)
    for parents in product(*(range(1, j) for j in range(2, n+1))):
        depths = [0, 0]
        mass = Q(1)
        for j, k in enumerate(parents, 2):
            depths.append(1 + depths[k])
            mass *= w[k]/W[j-1]
        t, r = sum(depths), parents.count(i)
        et += mass*t
        er += mass*r
        etr += mass*t*r
    return (etr-et*er)/n


def parts(w, W, p, n, i):
    B = {j: 1-sum(p[i:j]) for j in range(i+1, n+2)}
    a = {j: 1/W[j-1]-1/W[j] for j in range(i+1, n+1)}
    primary = sum(a[j]*B[j] for j in a)
    difference = sum(a[j]*(p[j]-p[i]) for j in a)
    correction = sum((1-j*p[j])*B[j]/W[j-1] for j in a)/n
    assert primary == difference+sum(p[i+1:n+1])/W[n]
    return w[i]*(primary+correction)


if __name__ == '__main__':
    cases = 0
    for alpha in (-3, -2, -1, 0, 1, 2):
        for n in range(2, 7):
            w, W, p = profiles(alpha, n)
            for i in range(1, n):
                assert parts(w, W, p, n, i) == outcomes(w, W, n, i)
                cases += 1

    # At alpha=-2, i=2, p_2=1/5, W_2=5/4, W_inf<=2 by the integral test.
    # The limiting bracket at i=2 is >= -p_2/W_2 + (1-p_2)/2 > 0.
    # At i=1, p_1=1 kills the boundary term and the series is strictly negative.
    w, W, p = profiles(-2, 3)
    assert -p[2]/W[2]+(1-p[2])/2 == Q(6, 25)
    assert p[3] < p[2]
    print(f'PASS: {cases} exact finite identities against enumeration; sign reversal at alpha=-2, i=1 vs i=2')
