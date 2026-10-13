"""Independent algebraic and numerical checks of the stated scalar SOFIM identities.

The accompanying proof, rather than finite numerical experiments, establishes
universal statements and the source-initialization error bound.
"""
from fractions import Fraction as Q
from math import sqrt
from random import Random


def psi(v):
    return v / (1 + v * v)


def period_amplitude_squared(beta, c):
    q = (1 - beta) / (1 + beta)
    return (c * q / 2 - 1) / (q * q)


def jury_values(beta, c):
    q = (1 - beta) / (1 + beta)
    u = c * q
    assert u > 2
    a2 = period_amplitude_squared(beta, c)
    m2 = q * q * a2
    k = c * (1 - m2) / ((1 + m2) ** 2)
    tr = 1 + beta - k * (1 - beta)
    det = beta
    return 1 - tr + det, 1 + tr + det, 1 - det


# General two-cycle equality: all exact rational identities avoid floats.
for beta in (Q(0), Q(1,100), Q(1,10), Q(1,4), Q(1,2)):
    q = (1 - beta) / (1 + beta)
    for u in (Q(21,10), Q(3), Q(39,10), Q(4), Q(5)):
        c = u / q
        a2 = period_amplitude_squared(beta, c)
        assert a2 > 0
        assert c*q == 2*(1+q*q*a2)
        j1,j2,j3 = jury_values(beta,c)
        assert j1 == 2*(1+beta)*(4-u)/u
        assert j2 == 4*(1+beta)*(u-2)/u
        assert j3 == 1-beta
        assert (j1 > 0 and j2 > 0 and j3 > 0) == (u < 4)
        assert (j1 == 0) == (u == 4)


# Exact differentiation bounds used in the weighted-contraction proof.
def dpsi(v):
    return (1-v*v) / (1+v*v)**2
assert Q(13,100) < dpsi(Q(4,5))
assert dpsi(Q(3,5)) < Q(35,100)
assert Q(614,1000)+Q(42,1000) < Q(2,3)
assert Q(1,4)+Q(1,100) < Q(2,3)
assert Q(15,1000)+3*Q(1,100)**2/(Q(2,3)-Q(1,100)) < Q(16,1000)
assert Q(1,6) < dpsi(Q(18,25))
assert dpsi(Q(69,100)) < Q(1,2)


# Exact source initialization identity and numerical geometric bound.
# Dimensionless variables: y = h*x/sqrt(rho), u = m/sqrt(rho), c = eta*h/rho.
for beta in (0, 1e-6, 0.0001, 0.001, 0.003, 0.005, 0.009, 0.01):
    c = 3.0
    q = (1-beta)/(1+beta)
    a = sqrt(period_amplitude_squared(beta,c))
    y = sqrt(0.5)
    m = 0.0
    for t in range(1,161):
        m = beta*m+(1-beta)*y
        v = m/(1-beta**t)
        # Sherman-Morrison agrees with direct scalar Fisher inversion.
        direct = psi(v)
        sm = v-v**3/(1+v*v)
        assert abs(direct-sm) < 2e-15
        y = y-c*direct
        yt = (-1)**t*a
        mt = (-1)**(t-1)*q*a
        err = max(abs(y-yt),0.25*abs(m-mt))
        assert err < 0.016*(2.0/3)**(t-1)+2e-14, (beta,t,err)
        if t == 1:
            assert abs(y+sqrt(0.5)) < 3e-15
    assert abs(y-a) < 1e-12


# Independent direct SOFIM update, using randomly selected h, rho,
# parameters satisfying c=3 and source initialization.
rng=Random(350083)
for k in range(100):
    h = 10.0**rng.uniform(-2,2)
    rho = 10.0**rng.uniform(-4,2)
    eta = 3*rho/h
    beta = rng.random()/100.0
    y0=sqrt(0.5)+rng.uniform(-0.01,0.01)
    x=sqrt(rho)*y0/h
    moment=0.0
    q=(1-beta)/(1+beta)
    a=sqrt(period_amplitude_squared(beta,3))
    for t in range(1,35):
        gradient=h*x
        moment=beta*moment+(1-beta)*gradient
        corrected=moment/(1-beta**t)
        fisher=rho+corrected**2
        x=x-eta*corrected/fisher
        signed=(-1)**t*a
        normalized=h*x/sqrt(rho)
        assert abs(normalized-signed) < 0.016*(2.0/3)**(t-1)+1e-12
print('verification passed')
