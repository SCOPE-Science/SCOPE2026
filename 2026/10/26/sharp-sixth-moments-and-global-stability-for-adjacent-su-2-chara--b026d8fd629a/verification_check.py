"""Reproduce the mixed sixth moments and sharp scalar extremizers for SU(2) character pairs.

Requires Python 3 and NumPy. Run: python verification_check.py
"""
import math
from collections import defaultdict
import numpy as np


def tensor_multiply(decomp, highest_weight):
    out = defaultdict(int)
    for weight, multiplicity in decomp.items():
        for component in range(abs(weight-highest_weight), weight+highest_weight+1, 2):
            out[component] += multiplicity
    return out


def trivial_multiplicity(n, a, b):
    decomp = {0: 1}
    for highest_weight in [n]*a + [n+1]*b:
        decomp = tensor_multiply(decomp, highest_weight)
    return decomp.get(0, 0)


def mixed_moments(n):
    return ((n+1)*(n*n+2*n+2)/2,
            (n+1)**2*(n+2)/2,
            (n+1)*(n+2)**2/2,
            (n+2)*(n*n+4*n+5)/2)


def polynomial(n, x):
    A, B, C, D = mixed_moments(n)
    return A*x**3 + 15*B*x*x*(1-x) + 15*C*x*(1-x)**2 + D*(1-x)**3


def optimizer(n):
    A, B, C, D = mixed_moments(n)
    c3 = A-15*B+15*C-D
    c2 = 15*B-30*C+3*D
    c1 = 15*C-3*D
    r = np.roots([3*c3,2*c2,c1])
    candidates=[float(z.real) for z in r if abs(z.imag)<1e-8 and 0<float(z.real)<1]
    assert len(candidates)==1, (n,r)
    return candidates[0]


def character(n, theta):
    # Stable Chebyshev recursion, including the endpoints by continuity.
    c = 2*np.cos(theta)
    if n==0: return np.ones_like(theta)
    prev = np.ones_like(theta)
    cur = c
    for _ in range(1,n):
        prev, cur = cur, c*cur-prev
    return cur


def direct_sixth(n, a, b):
    N=6*(n+2)+20
    j=np.arange(1,N+1)
    theta=np.pi*j/(N+1)
    vals=a*character(n,theta)+b*character(n+1,theta)
    return (2/(N+1))*np.sum(np.sin(theta)**2*np.abs(vals)**6)


def closed_sixth(n,a,b):
    S=abs(a)**2+abs(b)**2
    if S==0: return 0.0
    x=abs(a)**2/S
    A,B,C,D=mixed_moments(n)
    cosphi=(a*np.conjugate(b)).real/(abs(a)*abs(b)) if a and b else 1.0
    return S**3*(A*x**3+(3+12*cosphi**2)*(B*x*x*(1-x)+C*x*(1-x)**2)+D*(1-x)**3)


def check():
    for n in range(0,31):
        A,B,C,D=mixed_moments(n)
        assert all(abs(trivial_multiplicity(n,*v)-target)<1e-12 for v,target in [((6,0),A),((4,2),B),((2,4),C),((0,6),D)])
        x=optimizer(n)
        assert 0<x<.5
        assert polynomial(n,x)>max(polynomial(n,0),polynomial(n,1))
        assert abs(3*(A-15*B+15*C-D)*x*x + 2*(15*B-30*C+3*D)*x + 15*C-3*D)<1e-7
        for phase in [0, .31, 1.19, math.pi/2]:
            a=math.sqrt(x)*np.exp(0.4j)
            b=math.sqrt(1-x)*np.exp(1j*(phase+0.4))
            direct=direct_sixth(n,a,b)
            expected=closed_sixth(n,a,b)
            assert abs(direct-expected)<2e-8*(1+abs(expected)),(n,phase,direct,expected)
            c3=A-15*B+15*C-D
            c2=15*B-30*C+3*D
            q= -c2-c3*(x+2*x)
            deficit=polynomial(n,x)-expected
            rhs=12*x*(1-x)*(B*x+C*(1-x))*math.sin(phase)**2
            assert abs(deficit-rhs)<2e-7*(1+abs(deficit)),(n,deficit,rhs)
        for y in np.linspace(0,1,51):
            c3=A-15*B+15*C-D
            c2=15*B-30*C+3*D
            q=-c2-c3*(y+2*x)
            assert q>=-1e-9
            assert abs(polynomial(n,x)-polynomial(n,y)-(y-x)**2*q)<2e-7*(1+abs(polynomial(n,x)))
    print('PASS: 31 index values; 124 independent quadrature tests; 1581 deficit checks; all four exact mixed-moment formulas.')

if __name__=='__main__': check()
