#!/usr/bin/env python3
"""Reproduce the exact sample and directly check steered coherence.

Only Python's standard library is required. Finite checks supplement the
analytic projection-and-quadratic proof in RESULT.md.
"""
from fractions import Fraction
from math import sqrt

I = ((1 + 0j, 0j), (0j, 1 + 0j))
X = ((0j, 1 + 0j), (1 + 0j, 0j))
Y = ((0j, -1j), (1j, 0j))
Z = ((1 + 0j, 0j), (0j, -1 + 0j))
SIGMA = (X, Y, Z)


def dagger(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a)))
                 for i in range(len(a[0])))


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def tensor(a, b):
    return tuple(tuple(a[i // len(b)][j // len(b[0])] *
                       b[i % len(b)][j % len(b[0])]
                       for j in range(len(a[0]) * len(b[0])))
                 for i in range(len(a) * len(b)))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def density(beta, kappa, tau):
    ops = (tensor(I, I), tensor(I, X), tensor(X, X),
           tensor(Y, Y), tensor(Z, Z))
    coefficients = (1, beta, tau, kappa, kappa)
    return tuple(tuple(sum(c * op[i][j]
                           for c, op in zip(coefficients, ops)) / 4
                       for j in range(4)) for i in range(4))


def after_damping(rho, gamma):
    q = 1 - gamma
    k0 = ((1 + 0j, 0j), (0j, sqrt(q) + 0j))
    k1 = ((0j, sqrt(gamma) + 0j), (0j, 0j))
    terms = []
    for kraus in (k0, k1):
        a = tensor(I, kraus)
        terms.append(mm(mm(a, rho), dagger(a)))
    return tuple(tuple(sum(x[i][j] for x in terms)
                       for j in range(4)) for i in range(4))


def reduced_b(rho):
    return tuple(tuple(rho[i][j] + rho[i + 2][j + 2]
                       for j in range(2)) for i in range(2))


def bloch(rho_b):
    return tuple(trace(mm(rho_b, s)).real for s in SIGMA)


def conditional_b(rho, m):
    e = tuple(tuple((I[i][j] + sum(m[k] * SIGMA[k][i][j]
                                    for k in range(3))) / 2
                    for j in range(2)) for i in range(2))
    out = tuple(tuple(sum(e[j][i] * rho[2 * i + u][2 * j + v]
                              for i in range(2) for j in range(2))
                      for v in range(2)) for u in range(2))
    p = trace(out).real
    assert p > 0
    return tuple(tuple(out[i][j] / p for j in range(2)) for i in range(2))


def l1_in_b_basis(rho, m):
    b = bloch(reduced_b(rho))
    bn = sqrt(sum(x*x for x in b))
    assert bn > 0
    n = tuple(x / bn for x in b)
    r = bloch(conditional_b(rho, m))
    return sqrt(max(0., sum(x*x for x in r) -
                         sum(x*y for x, y in zip(r, n))**2))


def exact_squared(beta, kappa, tau, gamma):
    q = 1 - gamma
    a = q * kappa**2
    b = ((q * gamma**2 * tau**2 + q**3 * beta**2 * kappa**2)
         / (gamma**2 + q * beta**2))
    return a, b


def signed_poly(beta, kappa, tau, gamma):
    return (-(tau*tau + beta*beta*kappa*kappa)*gamma*gamma
            + (tau*tau - kappa*kappa + 3*beta*beta*kappa*kappa)*gamma
            - 2*beta*beta*kappa*kappa)


def run():
    b, k, t, g = (Fraction(1, 4), Fraction(1, 8),
                  Fraction(1, 2), Fraction(1, 2))
    assert b*b + 4*k*k == Fraction(1, 8)
    assert exact_squared(b, k, t, g)[1] == Fraction(257, 2304)
    assert exact_squared(b, k, t, Fraction(0))[1] == k*k
    assert signed_poly(b, k, t, g) > 0
    assert signed_poly(b, k, t, Fraction(0)) < 0
    assert signed_poly(b, k, t, Fraction(1)) == -k*k
    delta = ((t*t-k*k*(1+b*b))**2 - 8*b*b*k**4)
    assert delta == Fraction(56993, 1024**2)
    assert t*t > k*k*(1+b*b+2*sqrt(2)*float(b))
    samples = ((.25, .125, .5), (.1, .12, .45), (.33, .08, .34),
               (.22, .23, .33))
    cases = 0
    for beta, kappa, tau in samples:
        assert 1-tau >= sqrt(beta**2+4*kappa**2)
        for gamma in (0., .025, .1, .3, .5, .7, .95, 1.):
            a, c = exact_squared(beta, kappa, tau, gamma)
            q = 1-gamma
            denom = sqrt((gamma*tau)**2+(q*beta*kappa)**2)
            m_xz = (gamma*tau/denom, 0., -q*beta*kappa/denom)
            rho = after_damping(density(beta, kappa, tau), gamma)
            cy = l1_in_b_basis(rho, (0., 1., 0.))
            cxz = l1_in_b_basis(rho, m_xz)
            assert abs(cy**2-a) < 5e-12, (beta,kappa,tau,gamma,cy**2,a)
            assert abs(cxz**2-c) < 5e-12, (beta,kappa,tau,gamma,cxz**2,c)
            assert abs(max(cy,cxz)-sqrt(max(a,c))) < 5e-12
            cases += 1
    print('VERIFY_OK exact_fraction_witness=passed direct_kraus_steering_cases=' +
          str(cases) + ' boundary=passed')


if __name__ == '__main__':
    run()
