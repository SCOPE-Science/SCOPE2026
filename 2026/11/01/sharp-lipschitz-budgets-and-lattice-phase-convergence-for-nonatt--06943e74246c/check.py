"""Finite arithmetic checks for the accumulating-atom projection theorem.

Python 3 standard library only.  The analytic proof, not these tests, covers
infinitely many atoms and every parameter in the stated domain.
"""
from decimal import Decimal, getcontext

getcontext().prec = 90
D = Decimal
TRUNC = 340


def weights(q):
    u = 1 - q
    for _ in range(TRUNC):
        yield u
        u *= q


def first_moment(q, beta):
    return sum((w / (D(m) ** beta)
                for m, w in enumerate(weights(q), 1)), D(0))


def phi(q, beta, L, t):
    return sum((w * min(t, L / (2 * D(m) ** beta))
                for m, w in enumerate(weights(q), 1)), D(0))


def eta(q, beta, s):
    N = int(s)
    r = s - N
    # Explicit geometric tail; first term has m=N+1.
    return (1-q) * q**N * sum(
        (q**(j-1) * (1 - (s / D(N+j))**beta)
         for j in range(1, 220)), D(0))


def root(q, beta, L):
    lo, hi = D(1), L / 2
    for _ in range(360):
        mid = (lo + hi) / 2
        if phi(q, beta, L, mid) >= 1:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


checks = 0
for q, beta in [(D('0.5'), 1), (D('0.3'), 2)]:
    B = first_moment(q, beta)
    Lc = 2 / B
    assert D(0) < B < 1
    checks += 1
    # At the feasibility threshold the affine witness is exact to precision.
    assert abs(phi(q, beta, Lc, Lc/2) - 1) < D('1e-70')
    checks += 1
    assert phi(q, beta, Lc*D('0.99'), Lc*10) < 1
    checks += 1
    for scale in [D('1.02'), D('1.2'), D(2), D(3), D(10)]:
        L = Lc*scale
        t = root(q, beta, L)
        assert 1 < t <= L/2
        checks += 1
        assert abs(phi(q, beta, L, t) - 1) < D('1e-65')
        checks += 1
        # The ramp is h(x)=min(t,-t+L*x).  Its atomic integral
        # agrees with the independent bounded-amplitude expression.
        direct = sum((w * (min(t, -t+L/D(m)**beta)+t)/2
                      for m, w in enumerate(weights(q), 1)), D(0))
        assert abs(direct - phi(q, beta, L, t)) < D('1e-65')
        checks += 1
    for N in [6, 12, 24, 48]:
        for rs in ['0', '0.5']:
            r = D(rs)
            s = D(N) + r
            L = 2*s**beta
            t = root(q, beta, L)
            # Both sides remain well resolved at 90 digits.
            scaled = s*q**(-s)*(t-1)
            target = D(beta)*q**(-r)*(1/(1-q)-r)
            assert abs(scaled-target) < D(10)/D(N)
            checks += 1
            e = eta(q, beta, s)
            assert abs((t-1)/e - 1) < D(8)/D(N)
            checks += 1

# The original dyadic case has an independent finite logarithm formula.
# Compare with the convergent geometric tail, avoiding cancellation.
q = D('0.5')
for Lint in range(1, 35):
    L = D(Lint)/3
    t = max(D('0.5'), L/2)
    K = int(L/(2*t))
    partial = sum((D(1)/(D(2)**m*D(m))
                   for m in range(1, K+1)), D(0))
    # B is the infinite sum of 2^-m/m; it converges to log 2.
    B = first_moment(q, 1)
    rhs = t*(1-q**K) + L/2*(B-partial)
    assert abs(rhs-phi(q, 1, L, t)) < D('1e-68')
    checks += 1

print('PASSED', checks, 'finite arithmetic checks')
