"""Exact-rational diagnostic for sharp Lipschitz variance on spoke-weighted wheels.

Run with standard Python 3: python verify_weighted_wheel_spread.py
Finite tests supplement, and do not replace, the all-parameter mathematical proof.
"""
from fractions import Fraction as Q
from itertools import product


def expected(n, t):
    N = n + 1
    if 2*t <= 1:
        return n*t*t/Q(N) - (n % 2)*t*t/Q(N*N)
    a = 1-t
    return ((n-2)*t*t + 2*a*a)/Q(N) - (n % 2)*(3*t-2)**2/Q(N*N)


def variance(y):
    n = len(y)
    N = n + 1
    return sum(x*x for x in y)/N - sum(y)**2/Q(N*N)


def feasible(y, t):
    return all(-t <= x <= t and abs(x-y[(i+1) % len(y)]) <= 1
               for i,x in enumerate(y))


def classify(n, t, y):
    if t <= Q(1, 2):
        assert all(abs(x) == t for x in y)
        assert abs(sum(y)) == (n % 2)*t
        return
    a = 1-t
    assert sum(abs(x) == a for x in y) == 2
    assert t in y and -t in y
    assert all(x in (-t, -a, a, t) for x in y)
    assert all(not (abs(y[i]) == t and abs(y[(i+1) % n]) == t
                    and y[i] != y[(i+1) % n]) for i in range(n))
    if n % 2 == 0:
        assert y.count(t) == y.count(-t) == (n-2)//2
        assert sum(y) == 0
    else:
        assert abs(y.count(t)-y.count(-t)) == 1
        assert abs(sum(y)) == abs(3*t-2)


def exhaustive():
    cases, feasible_count, winners = 0, 0, 0
    t_values = [Q(1,3), Q(1,2), Q(11,20), Q(3,5), Q(2,3),
                Q(3,4), Q(4,5), Q(9,10), Q(1)]
    for n in range(4, 9):
        for t in t_values:
            a = 1-t
            levels = sorted({-t, t} if t <= Q(1,2) else {-t, -a, a, t})
            target = expected(n, t)
            best = Q(-1)
            attained = 0
            for y in product(levels, repeat=n):
                if not feasible(y, t):
                    continue
                feasible_count += 1
                v = variance(y)
                if v > best:
                    best, attained = v, 1
                elif v == best:
                    attained += 1
                if v == target:
                    classify(n, t, y)
                    winners += 1
            assert best == target, (n,t,best,target)
            assert attained > 0
            cases += 1
    print('EXACT_FOUR_LEVEL_EXTREME_CONFIGURATIONS_OK', cases, feasible_count, winners)


def algebra():
    trials = 0
    for n in range(4, 31):
        N = n+1
        for t in (Q(5001,10000), Q(11,20), Q(3,5), Q(2,3),
                  Q(3,4), Q(4,5), Q(9,10), Q(99,100), Q(1)):
            a = 1-t
            d = 2*t-1
            best = expected(n,t)
            p = (n+1)//2
            q = n-p
            one = (p*q+p*t*t+q*a*a)/Q(N*N)
            assert one < best, (n,t,one,best)
            # Test a cap that ignores all rim-order constraints; it is an
            # independent upper envelope for additional transition sites.
            if n%2 == 0:
                for r in range(3,n-1):
                    assert (n*t*t-r*d)/N < best
            else:
                for r in range(3,n-1):
                    best_residual = (3*t-2)**2
                    signed_sums=[]
                    for npos in range(n-r+1):
                        for apos in range(r+1):
                            S = (2*npos-(n-r))*t +(2*apos-r)*a
                            signed_sums.append(S*S)
                    assert N*(r-2)*d+min(signed_sums) > best_residual,(n,t,r)
            trials += 1
    print('EXACT_ONE_SIGN_AND_EXTRA_INTERFACE_DOMINANCE_OK', trials)


def transitions():
    for n in range(4,101):
        N=n+1
        # One-sided derivatives at the sharp hub/rim geodesic threshold.
        left = Q(n,N) -Q(n%2,N*N)
        right = Q(n-4,N)+Q(3*(n%2),N*N)
        assert left-right == (Q(4,N) if n%2==0 else Q(4*n,N*N))
        assert left>right
        assert expected(n,Q(1,2)) == n*Q(1,4)/N-(n%2)*Q(1,4)/(N*N)
        assert expected(n,Q(1)) == Q(n-2,N) -(n%2)*Q(1,N*N)
    print('EXACT_PARITY_AND_SHARP_CORNER_JUMPS_OK', 97)


if __name__=='__main__':
    exhaustive()
    algebra()
    transitions()
    print('ALL_WEIGHTED_WHEEL_SPREAD_CHECKS_OK')
