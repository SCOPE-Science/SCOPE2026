"""Reproducibility checks for a four-point affine Bargmann--Fock intensity design.

Requires numpy, scipy, mpmath and sympy. Numerical probes supplement the
analytic proof and do not certify global optimization by themselves.
"""
import math
import numpy as np
import mpmath as mp
import sympy as sp
from scipy.optimize import brentq


def operator(u):
    """Real lifting matrix in an orthonormal Frobenius basis of Herm(2)."""
    r=math.sqrt(u)
    t=math.exp(-u)
    M=np.zeros((4,4))
    M[0,0]=1.
    for j in range(3):
        theta=2*math.pi*j/3
        M[j+1,:]=t*np.array([1.,u,math.sqrt(2)*r*math.cos(theta),
                              -math.sqrt(2)*r*math.sin(theta)])
    return M


def spectrum(u):
    s=math.exp(-2*u)
    tr=1.+3*s*(1+u*u)
    gap=math.sqrt(tr*tr-12*s*u*u)
    return np.sort(np.array([(tr+gap)/2,(tr-gap)/2,3*u*s,3*u*s]))


def cond(u):
    ev=spectrum(u)
    return math.sqrt(ev[-1]/ev[0])


def eq(u):
    return (u-1)*math.exp(2*u)-3*(u*u-u+1)


u=brentq(eq,1,4/3,xtol=1e-14)
expected=math.exp(u)/math.sqrt(3)
assert 1 < u < 4/3
assert abs(cond(u)-expected)<2e-12
assert abs(spectrum(u)[0]-spectrum(u)[2])<2e-12
assert abs(spectrum(u)[3]-u)<2e-12
for x in np.r_[np.geomspace(.003,1.,30),np.linspace(1.,4.,81),np.geomspace(4.,12.,18)]:
    M=operator(x)
    ev=np.linalg.eigvalsh(M.T@M)
    assert np.allclose(ev,spectrum(x),rtol=2e-9,atol=1e-11),x
    if abs(x-u)>1e-6:
        assert cond(x)>expected-1e-10

# Independent direct Fourier inversion on random Hermitian inputs.
rng=np.random.default_rng(23921)
zeta=np.exp(2j*np.pi/3)
for t in range(150):
    x=float(rng.uniform(-2,2))
    y=float(rng.uniform(-2,2))
    c=complex(x,y)
    a=float(rng.normal());b=float(rng.normal())
    r=math.sqrt(u)
    zs=[r*zeta**j for j in range(3)]
    Y0=a
    Y=np.array([math.exp(-u)*(a+u*b+2*(c*z).real) for z in zs])
    b_rec=(math.exp(u)*np.sum(Y)/3-Y0)/u
    c_rec=math.exp(u)*sum(Y[j]*zeta**(-j) for j in range(3))/(3*r)
    assert abs(b_rec-b)<2e-12
    assert abs(c_rec-c)<2e-12

# Symbolic determinant and crossing-polynomial identities.
U,S=sp.symbols('u s',positive=True,real=True)
Gram=sp.Matrix([[1+3*S,3*S*U],[3*S*U,3*S*U**2]])
assert sp.simplify(Gram.det()-3*S*U**2)==0
L=3*U*S
p=sp.expand(L*L-sp.trace(Gram)*L+Gram.det())
assert sp.simplify(p-3*U*S*((U-1)-3*S*(U*U-U+1)))==0
# Rational Taylor certificates: 13 < exp(8/3) < 15.
x=sp.Rational(8,3)
lo=sum(x**j/sp.factorial(j) for j in range(6))
hi=sum(x**j/sp.factorial(j) for j in range(11))+sp.Rational(9,7)*x**11/sp.factorial(11)
assert lo>13 and hi<15
# Positive derivative of h: 1+3exp(-2u)(2(u-1)^2+1).
print('PASS: Gram eigenvalues, crossing, unique-root bracket certificates,')
print('      150 Fourier inversions, 129 independent singular-spectrum probes.')
print('u* = %.15f' % u)
print('r* = %.15f' % math.sqrt(u))
print('min condition number = %.15f' % expected)
print('optimal Gram spectrum =', spectrum(u))
