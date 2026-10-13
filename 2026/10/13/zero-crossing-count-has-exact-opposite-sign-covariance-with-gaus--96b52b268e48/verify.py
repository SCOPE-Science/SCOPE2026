#!/usr/bin/env python3
import math


def simpson(f, a, b, n=200000):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a) + f(b)
    for k in range(1,n):
        s += (4 if k%2 else 2)*f(a+k*h)
    return s*h/3


def phi(x):
    return math.exp(-x*x/2)/math.sqrt(2*math.pi)


def Phi(x):
    return 0.5*(1+math.erf(x/math.sqrt(2)))


def local_integral(rho):
    a = rho/math.sqrt(1-rho*rho)
    # By symmetry, E[X^2 1{XY<0}] = 2 int_0^inf x^2 phi(x) Phi(-a x) dx.
    f = lambda x: 2*x*x*phi(x)*Phi(-a*x)
    return simpson(f,0.0,10.0,120000)


def local_formula(rho):
    p = math.acos(rho)/math.pi
    return p-rho*math.sqrt(1-rho*rho)/math.pi


def covariance_closed(n,rho,sigma2=1.0):
    b = sum(1-rho**(2*r) for r in range(1,n))
    return -2*sigma2*rho*b/(math.pi*math.sqrt(1-rho*rho))


def covariance_edge_sum(n,rho,sigma2=1.0):
    c0 = -sigma2*rho*math.sqrt(1-rho*rho)/math.pi
    total = 0.0
    for i in range(1,n):
        left = sum(rho**(2*d) for d in range(i))
        right = sum(rho**(2*d) for d in range(n-i))
        total += c0*(left+right)
    return total

local_checks=0
for rho in (-0.9,-0.7,-0.3,0.0,0.25,0.6,0.9):
    got=local_integral(rho)
    want=local_formula(rho)
    assert abs(got-want) < 2e-10, (rho,got,want)
    local_checks += 1

formula_checks=0
sign_checks=0
for n in range(2,81):
    for rho in (-0.95,-0.8,-0.5,-0.2,0.2,0.5,0.8,0.95):
        a=covariance_closed(n,rho,1.7)
        b=covariance_edge_sum(n,rho,1.7)
        assert abs(a-b) < 2e-11*max(1.0,abs(a),abs(b)), (n,rho,a,b)
        formula_checks += 1
        assert a*rho < 0
        sign_checks += 1

# The independent case is exactly zero.
for n in range(2,101):
    assert covariance_closed(n,0.0,2.3) == 0.0
    sign_checks += 1

print('VERIFY_OK')
print('local_integral_checks=', local_checks)
print('closed_vs_edge_sum_checks=', formula_checks)
print('sign_and_independence_checks=', sign_checks)
