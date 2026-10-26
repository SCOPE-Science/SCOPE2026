"""Reproduce finite exact checks for Ewens fixed-position/inversion covariance."""
from fractions import Fraction
from itertools import permutations
from math import factorial, isclose, sqrt


def cycle_count(p):
    seen = set()
    total = 0
    for a in range(len(p)):
        if a in seen:
            continue
        total += 1
        x = a
        while x not in seen:
            seen.add(x)
            x = p[x] - 1
    return total


def mean_inversions(n, theta):
    if n <= 1:
        return Fraction(0)
    t = theta
    return ((t - 1) * n * (n - 1) * (2*n - 1) / 6
            + Fraction(n*n*(n-1)*(n-1), 4)) / ((t+n-1)*(t+n-2))


def radius_squared(n, t):
    return ((1-t)*(n-1)*((n-3)*(2*n-1) + 3*(n-1)*t)
            / (12*(t+n-3)*(t+n-1)))


def exact_cov(n, i, t):
    d = Fraction(2*i-n-1, 2)
    return 2*t/((t+n-1)*(t+n-2))*(radius_squared(n, t)-d*d)


def regression_cov(n, i, t):
    p = t/(t+n-1)
    conditional = mean_inversions(n-1, t) + Fraction(2*(i-1)*(n-i), 1)/(t+n-2)
    return p*(conditional-mean_inversions(n, t))


thetas = [Fraction(1,3), Fraction(1,2), Fraction(1), Fraction(3,2), Fraction(3)]
for n in range(3, 9):
    cases = 0
    for t in thetas:
        weight = Fraction(0)
        inv_sum = Fraction(0)
        joint = [Fraction(0) for _ in range(n)]
        fixed = [Fraction(0) for _ in range(n)]
        for pi in permutations(range(1,n+1)):
            w = t ** cycle_count(pi)
            inv = sum(pi[a] > pi[b] for a in range(n) for b in range(a+1,n))
            weight += w
            inv_sum += w*inv
            for z in range(n):
                if pi[z] == z+1:
                    fixed[z] += w
                    joint[z] += w*inv
        mean = inv_sum/weight
        assert mean == mean_inversions(n, t)
        for i in range(1,n+1):
            empirical = joint[i-1]/weight - (fixed[i-1]/weight)*mean
            assert fixed[i-1]/weight == t/(t+n-1)
            assert empirical == regression_cov(n, i, t)
            assert empirical == exact_cov(n, i, t), (n, t, i, empirical, exact_cov(n,i,t))
            cases += 1
    print('EWENS_EXHAUSTIVE_PASS', n, factorial(n), 'permutations,', cases, 'position-parameter cases')

for n in range(3,151):
    for t in thetas:
        assert mean_inversions(n, t) == ((t+n-3)/(t+n-1)*mean_inversions(n-1,t) + Fraction((n-1)**2,1)/(t+n-1))
        for i in range(1,n+1):
            c = exact_cov(n,i,t)
            assert c == regression_cov(n,i,t)
            if t == 1:
                assert c == -Fraction((2*i-n-1)**2, 2*n*(n-1))
            elif t > 1:
                assert c < 0
            else:
                d = Fraction(2*i-n-1, 2)
                assert (c > 0) == (radius_squared(n,t)>d*d)
    if n in [3,50,150]:
        print('EXACT_FORMULA_AND_SIGN_PASS', n)

for t in [Fraction(1,3), Fraction(1,2), Fraction(4,5)]:
    for n in [1000,10000]:
        assert abs(float(radius_squared(n,t)/n - (1-t)/6)) < 0.004
print('ASYMPTOTIC_RADIUS_CHECK_PASS')
print('VERIFY_OK')
