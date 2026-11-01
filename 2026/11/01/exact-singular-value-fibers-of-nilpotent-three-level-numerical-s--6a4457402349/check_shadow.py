"""Supplementary finite checks for nilpotent three-level shadow fibers.

The infinite-dimensional assertions are absent: this script tests only finite
matrix identities and constructive formulas. It is not a substitute for proof.
"""
import cmath
import math
import random

RNG = random.Random(20261026)


def determinant(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def adjoint(M):
    return [[M[j][i].conjugate() for j in range(3)] for i in range(3)]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def trace(A):
    return sum(A[i][i] for i in range(3))


def roots_interval(kappa, abs_tau):
    if not kappa > 0:
        raise ValueError("kappa must be positive")
    bound = (kappa / 3.0) ** 1.5
    if abs_tau > bound * (1 + 1e-12):
        raise ValueError("infeasible tau")
    abs_tau = min(abs_tau, bound)
    if abs_tau == 0.0:
        return (0.0, kappa / 2)
    if abs_tau == bound:
        return (kappa / 3, kappa / 3)

    def f(r):
        return 2*r*r*r - kappa*r*r + abs_tau*abs_tau

    def bisect(lo, hi):
        sign = f(lo)
        for _ in range(85):
            m = (lo + hi) / 2
            if f(m) * sign > 0:
                lo = m
            else:
                hi = m
        return (lo + hi) / 2

    return bisect(0, kappa/3), bisect(kappa/3, kappa/2)


def construct(kappa, tau, r):
    if r == 0:
        if abs(tau) != 0:
            raise ValueError("r=0 implies tau=0")
        x, y, z = math.sqrt(kappa), 0j, 0j
    else:
        S = kappa - abs(tau)**2 / r**2
        disc = max(0.0, S*S - 4*r*r)
        u = (S + math.sqrt(disc)) / 2
        w = r*r/u
        x, z, y = math.sqrt(u), math.sqrt(w), tau.conjugate()/r
    return [[0j, x, y], [0j, 0j, z], [0j, 0j, 0j]]


def within(actual, expected, atol=3e-9):
    assert abs(actual-expected) <= atol*max(1, abs(expected)), (actual, expected)


def run():
    checks = 0
    for j in range(400):
        kappa = 0.3 + RNG.random()*10
        fraction = 1e-5 + (1-2e-5)*RNG.random()
        tmag = (kappa / 3)**1.5 * fraction
        angle = RNG.random()*2*math.pi
        tau = tmag * cmath.exp(1j*angle)
        low, high = roots_interval(kappa, tmag)
        assert 0 < low < kappa/3 < high < kappa/2
        for r in [low, (low+high)/2, high]:
            A = construct(kappa, tau, r)
            AA = matmul(A, adjoint(A))
            A2 = matmul(A, A)
            A2Astar = matmul(A2, adjoint(A))
            within(trace(AA), kappa)
            within(trace(A2Astar), tau)
            within(abs(A2[0][2]), r)
            # Characteristic polynomial of AA* has roots 0 and two
            # nonzero squared singular values.
            eigen_high = (kappa+math.sqrt(kappa*kappa-4*r*r))/2
            eigen_low = (kappa-math.sqrt(kappa*kappa-4*r*r))/2
            within(eigen_high + eigen_low, kappa)
            within(eigen_high * eigen_low, r*r)
            within((math.sqrt(eigen_high)+math.sqrt(eigen_low))**2,
                   kappa+2*r)
            B = adjoint(A)
            for _ in range(2):
                s = (RNG.random()-.5) + 1j*(RNG.random()-.5)
                t = (RNG.random()-.5) + 1j*(RNG.random()-.5)
                M = [[(1 if a==b else 0)-s*A[a][b]-t*B[a][b]
                      for b in range(3)] for a in range(3)]
                target = 1-kappa*s*t-tau*s*s*t-tau.conjugate()*s*t*t
                within(determinant(M), target)
            checks += 8
    # Nonzero shadow with an exactly factorable endpoint cubic.
    kappa = 3.0
    tau = 1 / math.sqrt(2)
    lo, hi = .5, (1+math.sqrt(3))/2
    low, high = roots_interval(kappa, tau)
    within(low,lo)
    within(high,hi)
    within(math.sqrt(kappa+2*lo),2)
    within(math.sqrt(kappa+2*hi),math.sqrt(4+math.sqrt(3)))
    checks += 4
    # Critical square-root collapse of singular-spectrum ambiguity.
    for delta in [1e-4, 1e-5, 1e-6, 1e-7]:
        kappa=3.7
        tmag=(kappa/3)**1.5*math.sqrt(1-delta)
        low,high=roots_interval(kappa,tmag)
        rratio=(high-low)/(kappa*math.sqrt(delta))
        trratio=(math.sqrt(kappa+2*high)-math.sqrt(kappa+2*low))/(math.sqrt(kappa*delta))
        assert abs(rratio-2/(3*math.sqrt(3))) < 0.01
        assert abs(trratio-2/(3*math.sqrt(5))) < 0.01
        checks+=2
    print('PASS', checks, 'supplementary finite checks')

if __name__ == '__main__':
    run()
