"""Supplementary finite checks for odd-dimensional hyperbolic-harmonic concentration.
Run: python CHECK.py   (requires Python 3, NumPy and SciPy).
No finite check is substituted for the asymptotic analytical argument.
"""
from math import factorial, comb
from scipy.integrate import quad
from scipy.special import hyp2f1, roots_genlaguerre, gamma
import numpy as np

checks = 0

def verify(condition, label):
    global checks
    assert condition, label
    checks += 1

def dim_h(m, n):
    return (2*m+n-2)*factorial(m+n-3)//(factorial(m)*factorial(n-2))

def I_constant(n, alpha, grid=100):
    d = n/2
    x, wx = roots_genlaguerre(grid, alpha)
    y, wy = roots_genlaguerre(grid, d-1)
    q = (x[:,None]+y[None,:])**(d-1) @ wy / gamma(d)
    return float(np.dot(wx, q*q))

def exact_eigenvalue(n, alpha, T, m):
    d = n/2
    def f(t):
        F = hyp2f1(m, 1-d, m+d, t)
        return t**(m+d-1)*(1-t)**alpha*F*F
    a = quad(f, 0, T, epsabs=1e-14, epsrel=1e-12)[0]
    b = quad(f, 0, 1, epsabs=1e-14, epsrel=1e-12)[0]
    return a/b

# Internal identity checks of harmonic dimensions and integer-d normalization.
for n in (3,5,7):
    for m in range(1,26):
        verify(dim_h(m,n) == comb(m+n-1,n-1) - (comb(m+n-3,n-1) if m>=2 else 0), f'dimension n={n},m={m}')
verify(abs(I_constant(4,0)-10)<1e-10, 'integer-shape normalization I(4,0)=10')
# Odd-dimensional finite checks are consistent with asymptotic direction, not proofs of limits.
for n in (3,5):
    a,T=0.0,0.45
    I=I_constant(n,a)
    verify(I>0 and np.isfinite(I), f'positive constant n={n}')
    C=T**(n/2)*(1-T)**(a+n-2)/I
    vals=[]
    for m in (15,30,60,120):
        lam=exact_eigenvalue(n,a,T,m)
        pred=C*m**(a+n-2)*T**m
        verify(0<lam<1, f'eigenvalue range n={n},m={m}')
        verify(pred>0, f'predicted range n={n},m={m}')
        vals.append(lam/pred)
    verify(all(vals[j+1]<vals[j] for j in range(3)), f'trending asymptotic n={n}')
    verify(abs(vals[-1]-1)<(0.05 if n==3 else 0.20), f'largest-degree agreement n={n}')
print(f'PASS: {checks} finite assertions; numerical checks do not establish infinite-dimensional statements')
