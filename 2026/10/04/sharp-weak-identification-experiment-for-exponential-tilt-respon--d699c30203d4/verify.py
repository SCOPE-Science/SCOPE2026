#!/usr/bin/env python3
import math

N = 20000
P = (math.log1p(math.e) - math.log1p(math.exp(-5.0))) / 6.0

def logistic(x):
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)

def simpson(f):
    h = 2.0 / N
    s = f(-1.0) + f(1.0)
    for i in range(1, N):
        x = -1.0 + i*h
        s += (4.0 if i % 2 else 2.0) * f(x)
    return 0.5 * (h/3.0) * s

def mean_pi(d, eta):
    return simpson(lambda v: logistic(d + 3.0*eta*v))

def d_eta(eta):
    lo, hi = -20.0, 20.0
    for _ in range(100):
        mid = 0.5*(lo+hi)
        if mean_pi(mid, eta) < P:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo+hi)

def q(b):
    return P*math.exp(b) / ((1.0-P)*math.exp(-b) + P*math.exp(b))

def density_parts(b, eta):
    d = d_eta(eta)
    qb = q(b)
    def s(v):
        return (logistic(d + 3.0*eta*v)-P)/(P*(1.0-P))
    def r(v):
        return 1.0 + (qb-P)*s(v)
    return qb, s, r

def kl(b0, b1, eta):
    _, _, r0 = density_parts(b0, eta)
    _, _, r1 = density_parts(b1, eta)
    return simpson(lambda v: r0(v)*math.log(r0(v)/r1(v)))

def fisher(b, eta):
    qb, s, r = density_parts(b, eta)
    qp = 2.0*qb*(1.0-qb)
    return simpson(lambda v: (qp*s(v)/r(v))**2*r(v))

def mean_v(b, eta):
    _, _, r = density_parts(b, eta)
    return simpson(lambda v: v*r(v))

b0, b1 = 0.2, 1.2
Delta = q(b0)-q(b1)
kl_target = 1.5*Delta*Delta
f_target = 12.0*q(b1)**2*(1.0-q(b1))**2
m_target = q(b1)-P
eta = 0.0125
k = kl(b0,b1,eta)/(eta*eta)
f = fisher(b1,eta)/(eta*eta)
m = mean_v(b1,eta)/eta
assert abs(k-kl_target) < 1.0e-3, (k,kl_target)
assert abs(f-f_target) < 1.0e-3, (f,f_target)
assert abs(m-m_target) < 1.0e-3, (m,m_target)
print('p=', format(P,'.16g'))
print('scaled_KL=', format(k,'.16g'), 'target=', format(kl_target,'.16g'))
print('scaled_Fisher=', format(f,'.16g'), 'target=', format(f_target,'.16g'))
print('scaled_mean=', format(m,'.16g'), 'target=', format(m_target,'.16g'))
print('VERIFY_OK')
