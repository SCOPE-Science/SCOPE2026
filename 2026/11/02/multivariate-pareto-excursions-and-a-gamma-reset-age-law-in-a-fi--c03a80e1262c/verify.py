"""Numerical diagnostics for fixed-population threshold-reset Brownian rare excursions.

Requires Python 3.10+, scipy >= 1.10. No finite quadrature is used as a
substitute for the asymptotic proof.
"""
from math import erf, exp, gamma, pi, sqrt
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

D = L = 1.0
nodes, weights = leggauss(20)
nodes = (nodes + 1) / 2
weights = weights / 2


def mean_cycle(N):
    """Integral of erf(L/sqrt(4Dt))**N, with u=L/sqrt(4Dt)."""
    def integrand(u):
        if u == 0:
            return (2 / sqrt(pi)) ** N * (L * L / (2 * D)) if N == 3 else 0.0
        return L * L / (2 * D) * erf(u) ** N / u ** 3
    return quad(integrand, 0, float("inf"), epsabs=2e-12, epsrel=2e-12,
                limit=300)[0]


def scaled_joint(N, R, levels, age_power=0):
    """R**(N-2) times joint left tail and an optional power of U_R.

    Dimensionless integration u=R/sqrt(4Dt) avoids subtractive
    cancellation in near-identical Gaussian distribution functions.
    """
    k = len(levels)
    def integrand(u):
        if u == 0: return 0.0
        # R*survival, not survival, to keep scales O(1) at large R.
        survival_scaled = R * erf(L*u/R)
        v = survival_scaled ** (N-k)
        for a in levels:
            # R * half integral of erfc difference = 2 L u/sqrt(pi)
            # times the Gaussian's average across the short interval.
            delta = 2 * L * u / R
            avg = sum(w * exp(-(a*u + delta*n)**2)
                      for n, w in zip(nodes, weights))
            v *= 2 * L * u / sqrt(pi) * avg
        return v * u ** (2 * age_power - 3) / (2 * D * mean_cycle_cached[N])
    return quad(integrand, 0, 30, epsabs=1e-13, epsrel=2e-11,
                limit=400)[0]


def exact_coefficient(N, levels):
    B = sum(a*a for a in levels)
    return (2**(N-2) * gamma(N/2 - 1) * L**N /
            (pi**(N/2) * D * mean_cycle_cached[N]) * B**(1-N/2))


def close(a, b, tol, label):
    global checks
    checks += 1
    assert abs(a-b) <= tol*max(abs(b), 1e-14), (label, a, b)


if __name__ == '__main__':
    checks = 0
    mean_cycle_cached = {N: mean_cycle(N) for N in range(3, 9)}
    for N in range(3, 9):
        z = mean_cycle_cached[N]
        assert z > 0
        # An independent quadrature in time via t=y/(1-y).
        def g(y):
            if y == 1: return 0
            if y == 0: return 1
            t = y/(1-y)
            return erf(L/sqrt(4*D*t))**N/(1-y)**2
        z_direct = quad(g, 0, 1, epsabs=3e-10,
                        epsrel=3e-10, limit=600)[0]
        close(z, z_direct, 2e-8, ('mean-cycle',N))
        for levels in ([1.0], [1.0, 1.0], [1.0, 1.75]):
            c = exact_coefficient(N, levels)
            prev = None
            for R in (40., 160., 640.):
                y = scaled_joint(N, R, levels)
                assert 0 < y < c
                if prev is not None: assert y > prev
                prev = y
            close(prev, c, 0.07, ('tail-limit',N,levels))
            # At fixed N and R, exchangeability under threshold permutation.
            if len(levels) == 2:
                close(scaled_joint(N, 80., levels),
                      scaled_joint(N, 80., levels[::-1]),
                      1e-11, ('exchange',N,levels))
        # An age, U_R=R**2/(4DA), conditioned on X_1<-R.
        R=640.
        p0=scaled_joint(N,R,[1])
        alpha=N/2-1
        for p in (1,2):
            actual = scaled_joint(N,R,[1],age_power=p)/p0
            expected = gamma(alpha+p)/gamma(alpha)
            close(actual, expected, 0.065, ('age-gamma',N,p))
        # The limiting k-fold conditional-tail ratio is k**(1-N/2).
        for k in (2,3):
            ratio=scaled_joint(N,640.,[1]*k)/p0
            expected=k**(1-N/2)
            close(ratio,expected,.007,('tail-dependence',N,k))
    print(f'PASS {checks} numerical diagnostics; all N=3..8 and multi-label limits checked')
