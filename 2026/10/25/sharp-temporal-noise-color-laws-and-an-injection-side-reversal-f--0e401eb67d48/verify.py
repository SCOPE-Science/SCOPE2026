"""Exact-rational checks for stationary noise coloring in midpoint schemes.

Run with Python 3 standard library: python verify.py
Analytical proofs of the universal statements are in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt

count = 0

def verify(condition, message):
    global count
    count += 1
    if not condition:
        raise AssertionError(message)

def stationary(mu, rho, q):
    return q * (1 + mu * rho) / ((1 - mu * mu) * (1 - mu * rho))

def recurrence_solution(mu, rho, q):
    # Cross moment C=E[X_n eta_n] and the stationary variance.
    cross = rho * q / (1 - mu * rho)
    return (q + 2 * mu * cross) / (1 - mu * mu)

def risk(u, v, q1, q2, rho):
    return stationary(u, rho, q1) + stationary(-v, rho, q2)

def derivative(mu, rho, q):
    return 2 * q * mu / ((1 - mu * mu) * (1 - mu * rho)**2)

def curvature(mu, rho, q):
    return 4 * q * mu * mu / ((1 - mu * mu) * (1 - mu * rho)**3)

mus = [F(-3,4),F(-2,3),F(-1,2),F(-1,5),F(0),F(1,5),F(1,3),F(2,3),F(3,4)]
rhos = [F(-4,5),F(-3,4),F(-1,2),F(-1,5),F(0),F(1,5),F(1,2),F(3,4),F(4,5)]
qs = [F(1,17),F(1,2),F(1),F(7,3)]
for mu in mus:
    for rho in rhos:
        for q in qs:
            verify(stationary(mu,rho,q) == recurrence_solution(mu,rho,q), 'stationary recurrence')
            if mu != 0:
                verify(curvature(mu,rho,q)>0, 'strict convexity')
            else:
                verify(derivative(mu,rho,q)==0, 'zero mode')

# Exact polynomial numerators, without numerical differentiation.
for rho in rhos:
    den = 20*(rho-3)**2*(2*rho+3)**2
    verify(derivative(F(1,3),rho,F(1)) + derivative(F(-2,3),rho,F(1)) ==
           27*(4*rho*rho +156*rho-99)/den, 'post-step derivative')
    verify(derivative(F(1,3),rho,F(4,9)) + derivative(F(-2,3),rho,F(1,36)) ==
           3*(19*rho*rho+66*rho+36)/(5*(rho-3)**2*(2*rho+3)**2), 'residual-injected derivative')

# Exact risk values at nondegenerate test steps and independent sampling.
u,v=F(1,3),F(2,3)
verify(risk(u,v,F(1),F(1),F(0))==F(117,40),'isotropic-state independent risk')
verify(risk(u,v,F(4,9),F(1,36),F(0))==F(11,20),'isotropic-residual independent risk')
verify(risk(u,v,F(1),F(1),F(1,2))==F(99,40),'positive color state')
verify(risk(u,v,F(4,9),F(1,36),F(-1,2))<F(11,20),'negative color residual')

# The two roots lie strictly on opposite sides and their risks decrease.
rho_state = -F(39,2) + 9*sqrt(5)
rho_rhs = -F(33,19) + F(9,19)*sqrt(5)
verify(F(0)<rho_state<1,'state optimizer interval')
verify(-1<rho_rhs<0,'residual optimizer interval')
verify(abs(float(risk(u,v,F(1),F(1),rho_state))-(6*sqrt(5)/5-9/40))<1e-12,'state risk closed form')
verify(abs(float(risk(u,v,F(4,9),F(1,36),rho_rhs))-(3/20+2*sqrt(5)/15))<1e-12,'residual risk closed form')

# Finite-lag covariance summation independently approaches the stationary formula.
for mu in [F(1,3),F(-2,3)]:
    for rho in [F(-1,2),F(1,2)]:
        for q in [F(1),F(4,9)]:
            s=F(0)
            N=75
            for i in range(N):
                for j in range(N):
                    s += q*mu**(i+j)*rho**abs(i-j)
            verify(abs(float(s-stationary(mu,rho,q)))<1e-15,'truncated stationary filter')

# Strict convexity gives the global minimum; check exact rational grid order.
for k in range(-99,100):
    rr=F(k,100)
    verify(float(risk(u,v,F(1),F(1),rr)) >= 6*sqrt(5)/5-9/40-1e-12,'state global minimum')
    verify(float(risk(u,v,F(4,9),F(1,36),rr)) >= 3/20+2*sqrt(5)/15-1e-12,'rhs global minimum')

print('PASS',count,'checks')
