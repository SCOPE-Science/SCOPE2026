"""Reproducibility checks for the half-line boundary-sink absorption optimum.

Run with: python verification.py
Dependencies: numpy>=1.23, scipy>=1.9. All checks are finite sanity tests;
the analytic theorem and large-distance statements use the written proof.
"""
from math import pi, sin, isfinite
import numpy as np
from scipy.integrate import quad, trapezoid
from scipy.optimize import brentq
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply


def f(eta):
    return (2 / pi) * quad(lambda k: eta * sin(k) / (1 + eta ** 2 + 2 * eta * sin(k)), 0, pi, epsabs=5e-13)[0]


def g(s, eta):
    return (2 / pi) * quad(lambda q: eta * q ** (2 * s - 2) * (1 - q*q) / (1 + eta*eta*q*q), 0, 1, epsabs=5e-13)[0]


def p(s, eta):
    return f(eta) + g(s, eta)


def df(eta):
    return (2 / pi) * (1 - eta*eta) * quad(lambda k: sin(k) / (1 + eta*eta + 2*eta*sin(k))**2, 0, pi, epsabs=5e-13)[0]


def dg(s, eta):
    return (2 / pi) * quad(lambda q: q ** (2*s-2) * (1-q*q) * (1-eta*eta*q*q) / (1+eta*eta*q*q)**2, 0, 1, epsabs=5e-13)[0]


def dp(s, eta):
    return df(eta)+dg(s, eta)


def reciprocal_defect(s, eta):
    return (2 * eta * (eta*eta - 1) / pi) * quad(lambda q: q**(2*s-2)*(1-q*q)**2/((1+eta*eta*q*q)*(eta*eta+q*q)),0,1,epsabs=5e-13)[0]


def check(lhs, rhs, tol, label):
    assert isfinite(float(lhs)) and abs(lhs - rhs) <= tol, (label, lhs, rhs)


count=0
# The source integral and reciprocal difference are checked for many finite distances and rates.
for s in [1,2,3,4,5,7,10,20,40]:
    for eta in [0.15,0.3,0.7,1,1.125,1.8,2.8,4.5]:
        check(p(s,eta)-p(s,1/eta),reciprocal_defect(s,eta),4e-12,('reciprocity',s,eta))
        count+=1
        h=1e-5
        check((p(s,eta+h)-p(s,eta-h))/(2*h),dp(s,eta),6e-9,('derivative',s,eta))
        count+=1
        if s>=2:
            assert g(s,eta)<=1/(2*pi*s*(s-1))+1e-12
            count+=1

# All global maximizers lie on the strong-loss side; large-s coefficient tends to 3/4.
for s in [2,3,4,5,6,8,10,15,20,30,50,80,100]:
    eta=brentq(lambda z:dp(s,z),1+1e-11,20,xtol=1e-14)
    assert 1<eta<2 and dp(s,eta-0.001)>0 and dp(s,eta+0.001)<0
    assert p(s,eta)>p(s,1)
    count+=2
    if s>=40:
        assert abs(s**3*(eta-1)-0.75)<0.05
        count+=1

# Verify boundary curvature and derivative coefficient from independent integrations.
check(f(1), 1-2/pi, 1e-12, 'boundary probability')
count+=1
h=5e-4
check((f(1+h)-2*f(1)+f(1-h))/h**2,-2/(3*pi),1e-7,'curvature')
count+=1
for s in [25,50,100,200]:
    assert 0.5/pi <= s**3*dg(s,1) <= 0.6/pi
    count+=1

# Independently reconstruct the non-Hermitian time-domain walk (no source integral used).
N=380
eta=1.128036558506169
s=2
A=diags([-.5j*np.ones(N-1), -eta/2*np.eye(N)[0], -.5j*np.ones(N-1)],[-1,0,1],shape=(N,N),format='csc')
x0=np.zeros(N,dtype=complex)
x0[s-1]=1
traj=expm_multiply(A,x0,start=0,stop=135,num=1351,endpoint=True)
physical=trapezoid(eta*np.abs(traj[:,0])**2,dx=0.1)
assert physical<=p(s,eta) and 0<p(s,eta)-physical<0.0001,(physical,p(s,eta))
count+=1
print('VERIFY_OK',count,'direct integral, derivative, asymptotic and time-domain comparisons')
