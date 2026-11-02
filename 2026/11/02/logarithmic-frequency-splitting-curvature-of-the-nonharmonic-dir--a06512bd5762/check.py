"""Deterministic numerical checks for the stated even-degree Dirichlet cusp.
Requires Python >=3.10, NumPy and SciPy; this code is illustrative rather than proof.
"""
import math
import numpy as np
from scipy.integrate import quad


def exact_C(n):
    assert n >= 2 and n % 2 == 0
    j = np.arange(1, n//2 + 1, dtype=float)
    x = np.pi*j/(n+1)
    return float(16*np.pi**2/(n+1)**3 * np.sum(j*j*np.sin(x)*np.cos(x)**2))


def centered_half_second(n, eps):
    zeros = [2*np.pi*j/(n+1) for j in range(-n//2, n//2+1) if j != 0]
    knots = [-np.pi] + zeros + [np.pi]
    def f(t):
        lower = sum(np.exp(1j*k*t) for k in range(n))
        pe = lower + np.exp(1j*(n+eps)*t)
        me = lower + np.exp(1j*(n-eps)*t)
        ze = lower + np.exp(1j*n*t)
        return abs(pe)+abs(me)-2*abs(ze)
    total = sum(quad(f, a, b, epsabs=3e-11, epsrel=2e-10, limit=200)[0]
                for a,b in zip(knots[:-1],knots[1:]))
    return total/(2*eps*eps)


def main():
    checks=0
    constant = 32*(3*math.pi-7)/(27*math.pi)
    assert 0.91476 < constant < 0.91477
    checks+=1
    for n in (2,4,6,8):
        c=exact_C(n)
        assert 0<c<1.3
        checks+=1
        v1=centered_half_second(n,0.01)
        v2=centered_half_second(n,0.002)
        slope=(v2-v1)/math.log(5)
        assert abs(slope-c) < 0.004, (n,c,slope)
        checks+=1
        print(f'N={n}, exact_C={c:.12f}, finite-epsilon slope={slope:.12f}')
    assert abs(exact_C(100)-constant)<2e-6
    checks+=1
    print(f'PASS {checks} checks; limiting coefficient {constant:.12f}')

if __name__=='__main__':
    main()
