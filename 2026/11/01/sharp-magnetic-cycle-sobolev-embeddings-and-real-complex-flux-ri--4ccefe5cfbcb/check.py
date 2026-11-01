"""Supplementary exact and floating-point checks for the twisted-cycle Sobolev law.

Finite checks verify identities in sampled dimensions, not the theorem for all n
and boundary phases. The analytical proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, pi, sin, sqrt
import numpy as np


def matmul(a, b):
    return [[sum(a[i][t]*b[t][j] for t in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mat(n, c):
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(n-1):
        a[j][j] += 1; a[j+1][j+1] += 1
        a[j][j+1] -= 1; a[j+1][j] -= 1
    a[0][0] += 1; a[-1][-1] += 1
    a[0][-1] -= c; a[-1][0] -= c
    return a


def gram_formula(n, c):
    g = [[F(n-2*abs(i-j),4) for j in range(n)] for i in range(n)]
    u = F(1+c, 4*(1-c))
    v = F(1+c, n+1+(n-1)*c)
    w = [F(n-1-2*i,2) for i in range(n)]
    return [[g[i][j]+u-v*w[i]*w[j] for j in range(n)] for i in range(n)]


def exact_runs():
    count = 0
    cs = [-1, F(-3,4), F(-1,2), F(0), F(1,3), F(3,4), F(9,10)]
    for n in range(2,10):
        for c in cs:
            a = mat(n,c); g = gram_formula(n,c)
            ag = matmul(a,g)
            assert all(ag[i][j] == int(i == j)
                       for i in range(n) for j in range(n))
            count += n*n
            optimum = F(n*(n-1)*(n-2),12)+F(n*n,2*(1-c))
            vmax = None; maxima = []
            for sig in product((-1,1),repeat=n):
                val = sum(sig[i]*g[i][j]*sig[j]
                          for i in range(n) for j in range(n))
                if vmax is None or val > vmax:
                    vmax = val; maxima = [sig]
                elif val == vmax:
                    maxima.append(sig)
                count += 1
            assert vmax == optimum
            if c != -1:
                assert set(maxima) == {(-1,)*n,(1,)*n}
            else:
                assert len(maxima) == 2*n
                assert all(sum(sig[j]!=sig[j+1] for j in range(n-1))<=1
                           for sig in maxima)
            count += 4
            z = [F(j*(n+1-j),2)+n*c/F(2*(1-c))
                 for j in range(1,n+1)]
            assert all(z[j] == sum(g[j]) for j in range(n))
            assert all(x>0 for x in z)
            count += n+1
    return count


def numerical_runs():
    count = 0
    rng = np.random.default_rng(20261028)
    for n in range(2,27):
        for theta in [0.02,0.2,0.7,pi/2,2.2,pi-0.01,pi]:
            c=cos(theta)
            a=np.asarray(mat(n,c),dtype=float)
            rhs=n*(n-1)*(n-2)/12+n*n/(2*(1-c))
            zr=np.linalg.solve(a,np.ones(n))
            assert np.all(zr>0)
            assert abs(zr.sum()/rhs-1)<5e-7
            count += 2
            # A complex eigenvector saturates both the spectral gap and Cauchy.
            z=np.exp(-1j*np.arange(n)*theta/n)
            en=sum(abs(z[j+1]-z[j])**2 for j in range(n-1))
            en+=abs(z[0]-np.exp(1j*theta)*z[-1])**2
            cc2=n/(4*sin(theta/(2*n))**2)
            assert abs(n*n/en/cc2-1)<2e-10
            count += 1
            # Random vectors cannot violate either sharp bound.
            for _ in range(10):
                x=rng.standard_normal(n)
                en=sum((x[j+1]-x[j])**2 for j in range(n-1))
                en+=abs(x[0]-np.exp(1j*theta)*x[-1])**2
                assert sum(abs(x))**2 <= rhs*en*(1+3e-9)
                y=rng.standard_normal(n)+1j*rng.standard_normal(n)
                eny=sum(abs(y[j+1]-y[j])**2 for j in range(n-1))
                eny+=abs(y[0]-np.exp(1j*theta)*y[-1])**2
                assert sum(abs(y))**2 <= cc2*eny*(1+3e-9)
                count+=2
    return count


def main():
    a=exact_runs(); b=numerical_runs()
    print(f"PASS: {a} exact rational and {b} numerical finite assertions; {a+b} total.")

if __name__ == '__main__': main()
