"""Supplementary numerical and exact-arithmetic tests of the sparse Rhaly/Meixner reduction.
Run: python CHECK.py (requires numpy and scipy; see requirements.txt).
Finite matrix tests are diagnostics; analytic completeness is established in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial, sqrt
import numpy as np
from scipy.linalg import eigh_tridiagonal

def meixner(n, m, b):
    # M_n(m;2,1/b) = sum (-n)_j(-m)_j/(2)_j j! (1-b)^j.
    ans = F(0)
    for j in range(min(n,m)+1):
        z = F(factorial(n),factorial(n-j))*F(factorial(m),factorial(m-j))
        z *= F((1-b)**j, factorial(j+1)*factorial(j))
        ans += z
    return ans

def exact_tests():
    total = 0
    for b in (2,3,5,7):
        c = F(1,b)
        for n in range(0,9):
            for m in range(0,16):
                curr = meixner(n,m,b)
                nxt = meixner(n+1,m,b)
                prev = meixner(n-1,m,b) if n else F(0)
                rhs = (-c*(n+2)*nxt + (n+(n+2)*c)*curr - n*prev)/(1-c)
                assert F(m)*curr == rhs, (b,n,m)
                total+=1
        for k in range(1,9):
            for l in range(1,k+1):
                block = (b-1)*b**(l-1)
                observed = F(block,k*b**k)
                expected = F(b-1,b)* F(1,k)*F(1,b)**(k-l)
                assert observed == expected, (b,k,l)
                total+=1
    return total

def spectral_diagnostics():
    for b in (2,3,5):
        c = 1.0 / b
        N=1600
        k = np.arange(1,N+1,dtype=float)
        diag = (1+c)/(1-c)*k
        off = -sqrt(c)/(1-c)*np.sqrt(k[:-1]*(k[1:]))
        ev = eigh_tridiagonal(diag,off,select='i',select_range=(0,7),eigvals_only=True)
        residual = max(abs(float(v)-j) for j,v in enumerate(ev,1))
        assert residual < 2e-5, (b,residual,ev)
        print('base',b,'first inverse-square singular eigenvalues',ev,'maximum deviation',residual)

if __name__ == '__main__':
    print('exact recurrence/block tests:',exact_tests())
    spectral_diagnostics()
    print('All diagnostic checks passed. Infinite-dimensional completeness is analytic.')
