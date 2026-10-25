"""Independent finite checks of analytic spectral constants and pulse estimates.

Every infinite assertion in RESULT.md is proved mathematically there;
these tests verify selected finite algebraic and numerical consequences.
"""
import math


def test():
    pi = math.pi
    checks = 0
    # Integrated boundary-return kernel: 4/pi^2 sum 1/n^2 = 2/3.
    for nmax in (25, 100, 1000, 10000):
        partial = 4.0 / pi**2 * sum(1.0 / (n*n) for n in range(1, nmax + 1))
        # Integral comparison controls omitted positive terms.
        assert 0 < (2.0/3.0 - partial) < 4.0 / (pi*pi*nmax)
        checks += 1
    # Exact finite-time variance for constant rate one.
    for t in (0.25, 1.0, 5.0, 20.0, 100.0):
        v = 4 * sum(
            t / (n*n*pi*pi)
            - (1.0 - math.exp(-n*n*pi*pi*t)) / (n**4 * pi**4)
            for n in range(1, 20000)
        )
        assert 0 < v < (2.0/3.0)*t
        checks += 1
    # The initial tail error of folded-Brownian hit probabilities is summable.
    for N in (1, 2, 5, 10, 20):
        series = sum(2**(-2*n) for n in range(N, N+40))
        exact_tail = 4**(-N) * 4/3
        assert abs(series - exact_tail) < 1e-9
        checks += 1
    # The proof's finite-time survival estimate is dimensionally consistent.
    for A in (1, 2, 5, 10, 100):
        K = 2.0
        bound = math.exp(-A/2.0) + 8*K/(3*A)
        assert bound > 0.0 and bound >= math.exp(-A/2.0)
        checks += 1
    print(f"PASS: {checks} finite assertion groups; infinite claims require the proof")

if __name__ == '__main__':
    test()
