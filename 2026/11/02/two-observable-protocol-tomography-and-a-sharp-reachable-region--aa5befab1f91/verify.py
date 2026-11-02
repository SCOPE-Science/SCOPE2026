#!/usr/bin/env python3
"""Exact-arithmetic and numerical diagnostics for a two-coordinate linear diffusion.

Only the Python standard library is required. The proof of the infinite family
of covariance identities and attainable regions is in RESULT.md; this program
checks representative exact instances and independent finite computations.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log, cosh, sinh, sqrt, atanh

count = 0

def check(condition, message='identity'):
    global count
    if not condition:
        raise AssertionError(message)
    count += 1

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]

def prop(p, q):
    # p=exp[-integral(k-u)], q=exp[-integral(k+u)].
    c, h = (p+q)/2, (p-q)/2
    return [[c, -h], [-h, c]]

def diags(c):
    D = c[0][0] - c[1][1]
    A = c[0][1] - c[1][0]
    return D, A

pqs = [F(1), F(1,2), F(2,3), F(3,4), F(1,3), F(3,7), F(5,6)]
sigmas = [
    [[F(7),F(2)],[F(2),F(4)]],
    [[F(1),F(0)],[F(0),F(3)]],
    [[F(9,4),F(-1,5)],[F(-1,5),F(1,2)]],
    [[F(5,2),F(4,3)],[F(4,3),F(3)]],
]
for p,q in product(pqs,pqs):
    G=prop(p,q)
    for sigma in sigmas:
        d=sigma[0][0]-sigma[1][1]
        C=mul(G,sigma)
        D,A=diags(C)
        check(D+A == d*p, 'plus contrast')
        check(D-A == d*q, 'minus contrast')
        check(D*D-A*A == d*d*p*q, 'hyperbolic invariant')
        check(abs(D)>abs(A), 'strict observable cone')
        check((D+A)/d == p and (D-A)/d == q, 'exact reconstruction')
        # Jacobian columns are (-D,-A) and (A,D).
        J=[[-D,A],[-A,D]]
        JTJ=[[sum(J[k][i]*J[k][j] for k in range(2))
              for j in range(2)] for i in range(2)]
        l1,l2=(abs(d)*p)**2,(abs(d)*q)**2
        check(JTJ[0][0]+JTJ[1][1] == l1+l2, 'sensitivity trace')
        check(JTJ[0][0]*JTJ[1][1]-JTJ[0][1]*JTJ[1][0] == l1*l2,
              'sensitivity determinant')
        check(D == d*(p+q)/2 and A == d*(p-q)/2, 'matrix contrast')

# Independent two-stage propagation, verified by ordinary matrix multiplication.
for p1,q1,p2,q2 in product(pqs[:5],pqs[:5],pqs[:4],pqs[:4]):
    G1,G2=prop(p1,q1),prop(p2,q2)
    G=mul(G2,G1)
    target=prop(p1*p2,q1*q2)
    for i in range(2):
        for j in range(2):
            check(G[i][j]==target[i][j], 'piecewise composition')
    sig=sigmas[0]
    d=sig[0][0]-sig[1][1]
    D,A=diags(mul(G,sig))
    check(D+A == d*p1*p2, 'multistage plus')
    check(D-A == d*q1*q2, 'multistage minus')

# Continuous-time reconstruction and exact reachable set: floating checks
# use independent log/exp evaluations, not the inverse contrast formulas.
for idx in range(1,400):
    lag=.15 + (idx%31)/17
    kmax=.3 + (idx%23)/6
    p=exp(-(idx%37)/37 * kmax*lag)
    q=exp(-(idx%29)/29 * kmax*lag)
    if p*q < exp(-2*kmax*lag):
        raise AssertionError('unexpected inadmissibility')
    k=-(log(p)+log(q))/(2*lag)
    u=(log(p)-log(q))/(2*lag)
    check(-1e-11 <= k <= kmax+1e-11 and abs(u) <= k+1e-11,
          'constant-control realization')
    K,U=k*lag,u*lag
    d=2.3
    D=d*exp(-K)*cosh(U)
    A=d*exp(-K)*sinh(U)
    check(abs(atanh(A/D)-U)<1e-11, 'integrated offdiagonal recovery')
    check(abs(-.5*log((D*D-A*A)/(d*d))-K)<1e-11,
          'integrated diagonal recovery')
    check(abs((D+A)/d-p)<1e-11 and abs((D-A)/d-q)<1e-11,
          'observable reachability')
    check(abs((max(abs(D+A),abs(D-A)) /
               min(abs(D+A),abs(D-A)))-exp(2*abs(U))) <1e-10,
          'Jacobian condition number')

# A zero initial variance contrast makes the two diagnostic channels identically
# zero even though the full two-time covariance is generally nonzero.
for p,q in product(pqs,pqs):
    sigma=[[F(2),F(1,3)],[F(1,3),F(2)]]
    D,A=diags(mul(prop(p,q),sigma))
    check(D==0 and A==0, 'sharp degeneracy')

print('PASS: {} deterministic assertions'.format(count))

# Independently integrate the covariance Lyapunov equation and the two-time
# cross-covariance ODE through driven stages with time-varying bath strengths.
# No propagator formula is used in this integration.
def rk4(y, t, h, rhs):
    a=rhs(t,y)
    b=rhs(t+h/2,[v+h*w/2 for v,w in zip(y,a)])
    c=rhs(t+h/2,[v+h*w/2 for v,w in zip(y,b)])
    d=rhs(t+h,[v+h*w for v,w in zip(y,c)])
    return [v+h*(aa+2*bb+2*cc+dd)/6 for v,aa,bb,cc,dd in zip(y,a,b,c,d)]

def var_rhs(k,u):
    def deriv(t,v):
        sx,c,sy=v
        tx=2.0+0.2*t
        ty=0.4+0.1*t
        return [-2*k*sx-2*u*c+2*tx,
                -2*k*c-u*(sx+sy),
                -2*k*sy-2*u*c+2*ty]
    return deriv

def cross_rhs(k,u):
    def deriv(t,v):
        c11,c12,c21,c22=v
        return [-k*c11-u*c21,-k*c12-u*c22,
                -u*c11-k*c21,-u*c12-k*c22]
    return deriv

v=[47/30,-4/15,17/30]
for t0,t1,k,u in [(0,0.7,1.1,.2),(.7,1.2,.6,-.6)]:
    n=round((t1-t0)/.001)
    for j in range(n):
        v=rk4(v,t0+j*(t1-t0)/n,(t1-t0)/n,var_rhs(k,u))
initial_delta=v[0]-v[2]
C=[v[0],v[1],v[1],v[2]]
for t0,t1,k,u in [(1.2,2.0,1.8,.9),(2.0,3.0,.8,-.4)]:
    n=round((t1-t0)/.001)
    for j in range(n):
        C=rk4(C,t0+j*(t1-t0)/n,(t1-t0)/n,cross_rhs(k,u))
D,A=C[0]-C[3],C[1]-C[2]
K=1.8*(2-1.2)+.8*(3-2)
U=.9*(2-1.2)-.4*(3-2)
check(abs(D-initial_delta*exp(-K)*cosh(U)) < 2e-11,
      'independent driven-ODE diagonal contrast')
check(abs(A-initial_delta*exp(-K)*sinh(U)) < 2e-11,
      'independent driven-ODE cross-lag contrast')
check(abs(atanh(A/D)-U)<2e-11 and
      abs(-log(sqrt(D*D-A*A)/abs(initial_delta))-K)<2e-11,
      'independent driven-ODE full reconstruction')
print('PASS: {} assertions including independently integrated driven covariance'.format(count))
