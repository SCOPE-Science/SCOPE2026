"""Independent numerical and exact-arithmetic checks for affine projector endpoint norms on ball-box products.

Run with: python3 verification.py
Requires Python 3 with scipy and sympy.
"""
from fractions import Fraction
from math import comb, factorial
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
import sympy as sp


def marginal_density(d, z):
    if abs(z) >= 1:
        return 0.0
    return float(gamma(d / 2 + 1) / (math.sqrt(math.pi) * gamma((d + 1) / 2))) * (1-z*z)**((d-1)/2)


def truncated_formula(d, k):
    coefficient = 12 / math.factorial(k+1) * ((d+2)/6)**(k+1)
    def H(q):
        if q <= -1: return 0.0
        return quad(lambda z: (q-z)**(k+1) * marginal_density(d,z), -1, min(q,1), epsabs=3e-12,epsrel=3e-12)[0]
    return 1 + coefficient*sum((-1)**j*comb(k,j)*H((3*k-1-6*j)/(d+2)) for j in range(k+1))


def direct_formula(d, k):
    # Independent method: integrate |1+(d+2)z+3 sum(U)| over the
    # Irwin-Hall density, without using positive-part antiderivatives.
    if k == 0:
        return quad(lambda z: abs(1+(d+2)*z)*marginal_density(d,z),-1,1,epsabs=1e-11)[0]
    def irwin_density(x):
        if x <= 0 or x >= k: return 0
        return sum((-1)**j*comb(k,j)*(x-j)**(k-1) for j in range(int(x)+1))/factorial(k-1)
    def inner(z):
        root=(3*k-1-(d+2)*z)/6
        knots=sorted(set([0.0,float(k)]+[float(j) for j in range(1,k)]+([root] if 0<root<k else [])))
        return sum(quad(lambda s: abs(1+(d+2)*z+6*s-3*k)*irwin_density(s),lo,hi,epsabs=3e-11)[0]
                   for lo,hi in zip(knots,knots[1:]))
    splits=[-1.0,1.0]
    splits += [z for j in range(k+1) if -1 < (3*k-1-6*j)/(d+2) < 1 for z in [(3*k-1-6*j)/(d+2)]]
    splits=sorted(set(splits))
    return sum(quad(lambda z: inner(z)*marginal_density(d,z),lo,hi,epsabs=2e-8,epsrel=2e-8)[0]
               for lo,hi in zip(splits,splits[1:]))


def exact_odd_formula(d,k):
    assert d%2==1
    z=sp.symbols('z')
    b=(d-1)//2
    normalization=sp.Rational(sp.gamma(sp.Rational(d,2)+1)/
                              (sp.sqrt(sp.pi)*sp.gamma(sp.Rational(d+1,2))))
    density=normalization*(1-z*z)**b
    coefficient=sp.Rational(12,factorial(k+1))*sp.Rational(d+2,6)**(k+1)
    terms=0
    for j in range(k+1):
        v=sp.Rational(3*k-1-6*j,d+2)
        if v <= -1: continue
        end=min(v,sp.Integer(1))
        poly=sp.Poly((v-z)**(k+1)*density,z)
        integral=sum(c*(end**(p[0]+1)-(-1)**(p[0]+1))/sp.Integer(p[0]+1)
                     for p,c in poly.terms())
        terms+=(-1)**j*comb(k,j)*integral
    return sp.cancel(1+coefficient*terms)


def main():
    tested=0
    for d in range(1,7):
        for k in range(0,4):
            a,b=truncated_formula(d,k),direct_formula(d,k)
            assert abs(a-b)<2e-8, (d,k,a,b)
            tested+=1
    rationals=0
    for d in (1,3,5,7):
        for k in range(0,6):
            exact=exact_odd_formula(d,k)
            assert exact.is_Rational,(d,k,exact)
            assert abs(float(exact)-truncated_formula(d,k))<2e-8
            rationals+=1
    d,k=2,1
    benchmark=sp.Rational(17,9)+sp.Rational(3,4)*sp.sqrt(3)/sp.pi
    assert abs(truncated_formula(d,k)-float(benchmark))<2e-9
    assert exact_odd_formula(1,2)==sp.Rational(415,162)
    # Row monotonicity is checked directly by independent Gaussian quadrature
    # at a discrete test grid, not used as a proof of strictness.
    quad_nodes,quad_weights=np.polynomial.legendre.leggauss(80)
    tests=0
    for d,k in ((1,1),(2,1),(3,2),(5,3)):
        z=quad_nodes
        wz=quad_weights*np.array([marginal_density(d,float(x)) for x in z]); wz/=sum(wz)
        for r in (0.6,0.95):
            # conditioning cube coordinates at their extremal amplitudes
            # numerical monotonicity for a representative direction
            if k==1:
                p0=sum(wz[i]*sum(quad_weights[j]*abs(1+(d+2)*r*z[i]+3*quad_nodes[j])/2 for j in range(80)) for i in range(80))
                p1=sum(wz[i]*sum(quad_weights[j]*abs(1+(d+2)*z[i]+3*quad_nodes[j])/2 for j in range(80)) for i in range(80))
                assert p1>p0
                tests+=1
    print(f'PASS: {tested} independent nested-quadrature comparisons; {rationals} exact rational odd-ball comparisons; exact disk-cylinder constant; {tests} monotonicity sanity checks.')

if __name__=='__main__':
    main()
