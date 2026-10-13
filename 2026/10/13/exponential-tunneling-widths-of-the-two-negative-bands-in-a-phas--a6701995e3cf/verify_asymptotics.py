#!/usr/bin/env python3
import math


def fpoly(k, mu):
    return k**4 + 1.0 - 6.0*k*k + 4.0*k*(k*k-1.0)/math.tan(2.0*mu)


def normalized(k, q, mu, ell):
    s = math.sin(2.0*mu)
    cot = math.cos(2.0*mu)/s
    y = math.exp(-k*ell)
    F = k**4 + 1.0 - 6.0*k*k + 4.0*k*(k*k-1.0)*cot
    B = k**4 + 1.0 - 6.0*k*k - 4.0*k*(k*k-1.0)*cot
    return (F + 4.0*q*k*(1.0+k*k)/s*(y-y**3)
            - 2.0*(1.0+k*k)**2*y*y + B*y**4)


def secant(fun, x0, x1):
    f0, f1 = fun(x0), fun(x1)
    for _ in range(80):
        den = f1-f0
        if abs(den) < 1e-30:
            break
        x2 = x1 - f1*(x1-x0)/den
        if abs(x2-x1) < 2e-14:
            return x2
        x0, x1, f0, f1 = x1, x2, f1, fun(x2)
    return x1


def edge_root(r, sign, q, mu, ell):
    shift = sign*r*q*math.exp(-r*ell)
    return secant(lambda x: normalized(x,q,mu,ell),
                  r+0.5*shift, r+1.5*shift + 1e-10)


def width_ratio(r, sign, mu, ell):
    a = edge_root(r,sign,-2.0,mu,ell)
    b = edge_root(r,sign, 2.0,mu,ell)
    measured = abs(a*a-b*b)
    predicted = 8.0*r*r*math.exp(-r*ell)
    return measured/predicted

mu = 0.7
t = math.tan(mu/2.0)
u = math.tan(mu/2.0 + math.pi/4.0)
assert abs(fpoly(t,mu)) < 1e-12
assert abs(fpoly(u,mu)) < 1e-10
r12 = width_ratio(t,+1.0,mu,12.0)
r16 = width_ratio(t,+1.0,mu,16.0)
ru8 = width_ratio(u,-1.0,mu,8.0)
assert abs(r16-1.0) < abs(r12-1.0)
assert abs(r16-1.0) < 0.01
assert abs(ru8-1.0) < 1e-5
print('VERIFY_OK', 't_ratio_12=%.9f'%r12, 't_ratio_16=%.9f'%r16, 'u_ratio_8=%.9f'%ru8)
