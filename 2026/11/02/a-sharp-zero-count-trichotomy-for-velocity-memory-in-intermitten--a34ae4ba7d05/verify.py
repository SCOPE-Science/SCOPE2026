"""Reproduce exact velocity-correlation and sign-transition identities.

Run with: python verify.py
Requires numpy and scipy; comparisons are supplementary to the written proof.
"""
import math
import numpy as np
from scipy.linalg import expm


def reduced_matrix(alpha, beta, dr, dt, cosine):
    return np.array([[-alpha - dr, alpha],
                     [beta * cosine, -beta - dt]], dtype=float)


def normalized_correlation(t, alpha, beta, dr, dt, cosine):
    a, b = alpha + dr, beta + dt
    s = a + b
    delta = (a - b) ** 2 + 4 * alpha * beta * cosine
    if delta > 1e-13:
        root = math.sqrt(delta)
        return math.exp(-s * t / 2) * (math.cosh(root * t / 2)
            + (b - a) * math.sinh(root * t / 2) / root)
    if delta < -1e-13:
        root = math.sqrt(-delta)
        return math.exp(-s * t / 2) * (math.cos(root * t / 2)
            + (b - a) * math.sin(root * t / 2) / root)
    return math.exp(-s * t / 2) * (1 + (b - a) * t / 2)


def root_count_category(alpha, beta, dr, dt, cosine):
    a, b = alpha + dr, beta + dt
    delta = (a - b) ** 2 + 4 * alpha * beta * cosine
    if cosine >= 0 or (a < b and delta >= 0):
        return 'zero'
    if delta < 0:
        return 'infinite'
    if cosine < 0 and a > b and delta >= 0:
        return 'one'
    raise AssertionError((alpha, beta, dr, dt, cosine))


def first_zero(alpha, beta, dr, dt, cosine):
    a, b = alpha + dr, beta + dt
    delta = (a - b) ** 2 + 4 * alpha * beta * cosine
    kind = root_count_category(alpha, beta, dr, dt, cosine)
    if kind == 'zero':
        return None
    if kind == 'one':
        if abs(delta) < 1e-13:
            return 2 / (a - b)
        return 2 * math.atanh(math.sqrt(delta) / (a - b)) / math.sqrt(delta)
    root = math.sqrt(-delta)
    return 2 * (math.pi / 2 + math.atan((b - a) / root)) / root


checks = 0
for alpha in (0.3, 0.8, 1.0, 2.0, 5.0):
    for beta in (0.5, 1.0, 2.0, 3.0):
        for dr, dt in ((0., 0.), (0.2, 0.7), (1.0, 0.1)):
            for cosine in (-1., -0.5, -0.1, 0., 0.3, 1.):
                M = reduced_matrix(alpha, beta, dr, dt, cosine)
                for t in (0., 0.05, 0.3, 0.9, 1.8):
                    expected = float(expm(t * M)[0, 0])
                    got = normalized_correlation(t, alpha, beta, dr, dt, cosine)
                    assert np.isclose(expected, got, rtol=4e-11, atol=2e-13), (alpha,beta,dr,dt,cosine,t,got,expected)
                    checks += 1
                cat = root_count_category(alpha, beta, dr, dt, cosine)
                first = first_zero(alpha, beta, dr, dt, cosine)
                if cat != 'zero':
                    assert first > 0 and abs(float(expm(first*M)[0,0])) < 5e-11
                    assert float(expm(first * 0.5 * M)[0,0]) > 0
                    assert float(expm(first * 1.1 * M)[0,0]) < 0
                    checks += 3
                    if cat == 'infinite':
                        w = math.sqrt(-((alpha+dr-beta-dt)**2+4*alpha*beta*cosine))
                        second = first + 2*math.pi/w
                        assert abs(float(expm(second*M)[0,0])) < 1e-10
                        checks += 1

# Test the two repeated-eigenvalue boundaries analytically.
lo, hi = 3-2*math.sqrt(2), 3+2*math.sqrt(2)
for h, expect in ((lo, 'zero'), (hi, 'one')):
    a, b, c = h, 1., -1.
    t = 0.4
    value = math.exp(-(a+b)*t/2)*(1+(b-a)*t/2)
    assert abs(float(expm(t*reduced_matrix(a,b,0,0,c))[0,0])-value) < 5e-14
    assert (a<b) if expect == 'zero' else (a>b)
    checks+=2

# Independent initial derivative and signed-integral check: 
# Laplace transform at zero equals b/(ab-alpha*beta*cosine).
for alpha,beta,dr,dt,c in ((2,3,.1,.3,-.5),(.7,1.,0,0,-1),(3,1,0,0,-1),(1,4,.3,.6,.8)):
    a,b=alpha+dr,beta+dt
    det=a*b-alpha*beta*c
    assert det>0
    M=reduced_matrix(alpha,beta,dr,dt,c)
    assert np.isclose(float((-np.linalg.inv(M))[0,0]),b/det,rtol=5e-14)
    assert np.isclose(float(M[0,0]),-a)
    checks+=2

print('PASS', checks, 'independent matrix-exponential and analytical boundary checks')

# Four-state process, formed independently from physical jump transitions.
# State order: R+, R-, T+, T-. Orientation transition is ± with
# conditional probability (1+cosine)/2 (the symmetric ±pi kernel).
for alpha in (.12, .5, 1., 2., 7.):
    for beta in (.4, 1.3, 3.):
        for cosine in (-1., -.5, 0., .5, 1.):
            Q = np.zeros((4, 4))
            for run_index in (0, 1):
                Q[run_index, run_index+2] += alpha
                Q[run_index, run_index] -= alpha
            for tumble_index in (2, 3):
                for run_index in (0, 1):
                    prob = (1+cosine)/2 if run_index==tumble_index-2 else (1-cosine)/2
                    Q[tumble_index, run_index] += beta*prob
                Q[tumble_index, tumble_index] -= beta
            assert np.allclose(np.sum(Q,axis=1),0)
            prob = np.array([beta,beta,alpha,alpha])/(2*(alpha+beta))
            assert np.allclose(prob@Q,np.zeros(4))
            v = np.array([1.,-1.,0.,0.])
            for lag in (.07,.3,.7,1.2,2.5):
                direct = np.dot(prob*v, expm(lag*Q)@v)
                analytic = beta/(alpha+beta)*normalized_correlation(lag,alpha,beta,0,0,cosine)
                assert np.isclose(direct,analytic,rtol=5e-11,atol=3e-14)
                checks += 1
print('PASS', checks, 'including 4-state physical jump-process comparisons')
