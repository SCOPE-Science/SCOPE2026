#!/usr/bin/env python3
"""Reproducibility checks for high-order Riemann--Liouville trace-norm asymptotics.

Run: python check.py
Requires Python 3, NumPy; numerical quadrature is corroborative only.
"""
from fractions import Fraction as F
from math import factorial
import numpy as np
from numpy.polynomial.legendre import leggauss

checks = 0

def check(condition, explanation):
    global checks
    assert condition, explanation
    checks += 1


def moment(k):
    # Integral from 0 to infinity of u^k exp(-2u) du.
    return F(factorial(k), 2 ** (k + 1))


def eval_poly(p):
    return sum((a * moment(k) for k, a in p.items()), F(0))


def mul(p, q):
    r = {}
    for i, a in p.items():
        for j, b in q.items():
            r[i+j] = r.get(i+j, F(0)) + a*b
    return {i:a for i,a in r.items() if a}


def add(p, q, c=F(1)):
    r = p.copy()
    for i, b in q.items():
        r[i] = r.get(i, F(0)) + c*b
    return {i:a for i,a in r.items() if a}

# Expansion exp((a-1)log(1-s/a)) = exp(-s)[1+f1(s)/a+f2(s)/a^2+...].
f1 = {1:F(1), 2:F(-1,2)}
log_second = {2:F(1,2), 3:F(-1,3)}
f2 = add(log_second, mul(f1, f1), F(1,2))
check(f2 == {2:F(1), 3:F(-5,6), 4:F(1,8)}, 'kernel expansion coefficient')

# Phi=sqrt(2)*exp(-u) is unit. K0=exp(-u-v), lambda0=1/2.
check(2*moment(0) == 1, 'phi normalization')
lam0 = F(1,2)
lam1 = 2*eval_poly({k+1:v for k,v in f1.items()})
lam2_direct = 2*eval_poly({k+1:v for k,v in f2.items()})
check(lam1 == F(1,8), 'first eigenvalue correction')
check(lam2_direct == F(-1,32), 'direct second eigenvalue correction')

# g(u) = 2 integral exp(-2v)*f1(u+v) dv, computed via moments.
from math import comb

def integrate_shifted(p):
    g = {}
    for k, a in p.items():
        for j in range(k+1):
            g[j] = g.get(j,F(0))+a*F(comb(k,j))*2*moment(k-j)
    return {k:v for k,v in g.items() if v}

g = integrate_shifted(f1)
check(g == {0:F(1,4), 1:F(1,2), 2:F(-1,2)}, 'K1 phi expression')
# K1 phi(u) = (1/sqrt(2))e^{-u}g(u).
k1phi_sq = F(1,2)*eval_poly(mul(g,g))
lam2 = lam2_direct + (k1phi_sq-lam1**2)/lam0
check(k1phi_sq == F(3,64), 'perturbation vector norm')
check(lam2 == F(1,32), 'second-order operator norm coefficient')

h={0:F(-1,2),1:F(1)}
h2=eval_poly(mul(h,h))
check(h2 == F(1,8), 'compressed first perturbation has one eigenvalue -1/8')
check(eval_poly(h) == 0, 'transverse eigenfunction orthogonal to phi')

# Exact Hilbert-Schmidt norm: alpha/(2(2alpha-1)); its square-root
# has coefficient 3/64 at alpha^-2, while top norm has 1/32.
check(F(3,64)-lam2 == F(1,64), 'singular-value square residual coefficient')
check(F(1,64) == h2*h2, 'second singular value explains all first residual mass')

# Numerical Nyström values for independently evaluating the exact positive Hankel
# kernel on [0,alpha]^2; truncation to [0,22]^2 costs exponentially little.
x,w=leggauss(160)
u=11*(x+1)
ww=11*w
s=u[:,None]+u[None,:]
sw=np.sqrt(ww[:,None]*ww[None,:])
for alpha in [12, 20, 32, 50, 80, 120]:
    k=np.maximum(1-s/alpha,0)**(alpha-1)
    eig=np.linalg.eigvalsh(sw*k)
    first=eig[-1]
    second=-eig[0]
    predicted=0.5+0.125/alpha+0.03125/(alpha**2)
    # Deliberately broad checks: discretization is not an asymptotic proof.
    check(abs(first-predicted) < 1/alpha**3, f'top singular at alpha={alpha}')
    check(abs(second-0.125/alpha)< 0.105/alpha**2, f'second singular at alpha={alpha}')
    check(eig[-2] < 0.15/alpha**2, f'third singular at alpha={alpha}')
    trace_norm = np.sum(np.abs(eig))
    check(abs((trace_norm-F(1,2))*alpha - F(1,4)) < 0.25/alpha,
          f'trace norm first-order at alpha={alpha}')
    residual = trace_norm-first
    check(abs(residual*alpha-F(1,8))<0.23/alpha,
          f'optimal rank-one nuclear error at alpha={alpha}')
    check(abs((trace_norm-first-second))*alpha**2 < 0.3,
          f'higher trace tail at alpha={alpha}')

# Exactly differentiated Taylor coefficient of kernel second derivative:
# k_alpha''(s) = ((alpha-1)(alpha-2)/alpha**2)*(1-s/alpha)**(alpha-3).
# Expansion about alpha^{-1}=0: exp(-s)[1+alpha^{-1}(-3+3s-s^2/2)+...].
check({0:F(-3),1:F(3),2:F(-1,2)} == add(add(f1,{0:F(-1)},F(1)),{0:F(-2),1:F(2)}), 'second derivative Taylor coefficient')
# Hankel trace lemma uses trace-class factorization J^2=J J and
# ||J||_{S2}^2=1/2 on (0,1); rescaling gives t^2/2 bound.
check(moment(0) == F(1,2), 'Volterra Hilbert-Schmidt normalization')
print(f'PASS {checks} exact identities and separate finite Nyström comparisons')
