#!/usr/bin/env python3
"""Reproducible exact finite-size and asymptotic checks for a nonlinear hypergraph voter model."""
from fractions import Fraction
from math import comb, gamma, log, exp, lgamma, pi, sqrt, log1p


def transition_probabilities(N, d, k):
    """Direct hypergeometric enumeration, independent of the closed ratio."""
    denom = N * comb(N - 1, d) * d * d
    up = 0
    down = 0
    for j in range(d + 1):
        if j <= k and d - j <= N - 1 - k:
            up += (N - k) * comb(k, j) * comb(N - 1 - k, d - j) * j*j
        if j <= N - k and d - j <= k - 1:
            down += k * comb(N - k, j) * comb(k - 1, d - j) * j*j
    return Fraction(up, denom), Fraction(down, denom)


def exact_finite(N, d):
    c = Fraction(N - 1 - d, d - 1)
    ws = [Fraction(1)]
    for i in range(1, N):
        ws.append(ws[-1] * (N + c - i) / (c + i))
    denominator = sum(ws)
    ps = [Fraction(0)]
    running = Fraction(0)
    for k in range(1, N):
        running += ws[k - 1]
        ps.append(running / denominator)
    ps.append(Fraction(1))
    for k in range(1, N):
        up, down = transition_probabilities(N, d, k)
        assert up > 0 and down > 0
        assert down / up == (N + c - k)/(c + k)
        assert up * (ps[k+1] - ps[k]) == down * (ps[k] - ps[k-1])
        assert ps[k] + ps[N-k] == 1
    for j in range(N):
        assert ws[j] == ws[N-1-j]
    return ps


def asymptotic_constants(d):
    a = 1/(d-1)
    b = 1+2*a
    I = (1+a)*log(1+a)+a*log(a) -(1+2*a)*log(a+0.5)
    C = ((1+a)**(b+0.5) * a**(b-0.5)) / (sqrt(pi)*(a+0.5)**(2*b+0.5))
    gaussian = (d-1)/(2*(d+1))
    assert I > gaussian
    return I,C,gaussian


def logsumexp(numbers):
    m = max(numbers)
    return m + log(sum(exp(t-m) for t in numbers))


def log_exact_p(N, d, k):
    c = (N-1-d)/(d-1)
    lnw = [lgamma(N+c) + lgamma(c+1) - lgamma(N+c-j) - lgamma(c+j+1) for j in range(N)]
    return logsumexp(lnw[:k]) - logsumexp(lnw)


def main():
    finite_checks = 0
    for N in range(3, 13):
        previous_p1 = Fraction(1, N)
        for d in range(2, N):
            p = exact_finite(N, d)
            assert p[1] < previous_p1, (N,d, p[1], previous_p1)
            previous_p1 = p[1]
            if d == N-1:
                assert p[1] == Fraction(1, 2**(N-1))
            finite_checks += (N-1)
    asymptotic_checks = 0
    for d in (2,3,5,11):
        I,C,J = asymptotic_constants(d)
        for N in (300,1000):
            log_exact = log_exact_p(N, d, 1)
            log_approx = log(C)-0.5*log(N)-N*I
            assert abs(log_exact-log_approx) < 0.02, (N,d,log_exact,log_approx)
            asymptotic_checks += 1
        print(f'd={d} I={I:.12f}, Gaussian J={J:.12f}, C={C:.12f}')
    assert abs(asymptotic_constants(2)[0]-log(32/27)) < 1e-12
    print(f'PASS: {finite_checks} exact finite-state harmonic/reversibility checks; {asymptotic_checks} fixed-degree Laplace approximations')


if __name__ == '__main__':
    main()
