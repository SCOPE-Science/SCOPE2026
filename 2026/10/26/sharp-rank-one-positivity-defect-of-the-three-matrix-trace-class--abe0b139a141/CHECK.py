"""Reproducibility checks for a rank-one three-matrix mixing formula.

Requires Python 3, NumPy and SymPy. Finite tests supplement the proof in RESULT.md.
"""
import math
import random
import numpy as np
import sympy as sp


def matrix_abs(H):
    eig, vec = np.linalg.eigh(H)
    return (vec * abs(eig)) @ vec.conj().T


def mix(A, B, C):
    D = matrix_abs(A-B) + matrix_abs(B-C) + matrix_abs(C-A)
    inv = np.linalg.pinv(D, hermitian=True, rcond=1.e-11)
    X = (B-A) @ inv @ matrix_abs(C-A) + (C-A) @ inv @ matrix_abs(B-A)
    return A + (X + X.conj().T) / 2


def exact_symbolic_checks():
    z = sp.sqrt(2)
    P = sp.Matrix([[1,0],[0,0]])
    Q = sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2)],
                   [sp.Rational(1,2),sp.Rational(1,2)]])
    H = P-Q
    # The two eigenvalues of H have opposite signs and square to I/2.
    assert sp.simplify(H*H-sp.eye(2)/2) == sp.zeros(2)
    D = P+Q+sp.eye(2)/z
    Phi = sp.simplify(P*D.inv()*Q + Q*D.inv()*P)
    coefficient = sp.simplify((1-1/z)/2)
    assert sp.simplify(Phi - coefficient*sp.Matrix([[2,1],[1,0]])) == sp.zeros(2)
    eigminus = sp.simplify(coefficient*(1-z))
    assert sp.simplify(Phi.det() + coefficient**2) == 0
    assert float(eigminus) < 0
    assert float(eigminus + sp.Rational(1,32)) < 0
    t=sp.symbols('t', real=True)
    f=t*(1-t)**2/(2*(1+t*t))
    expected=(t-1)*(t**3+t**2+3*t-1)/(2*(1+t*t)**2)
    assert sp.simplify(sp.diff(f,t)-expected) == 0
    r=sp.symbols('r')
    resultant=sp.factor(sp.resultant(t**3+t*t+3*t-1, r*(1+t*t)-2*t, t))
    assert sp.simplify(resultant - 8*(r**3+r*r+r-1)) == 0
    return Phi,eigminus


def numerical_random_checks():
    rng=random.Random(17)
    count=0
    for j in range(900):
        a=10**rng.uniform(-2,2)
        b=10**rng.uniform(-2,2)
        r=rng.uniform(.02,.98)
        theta=rng.uniform(-math.pi,math.pi)
        u=np.array([1+0j,0+0j])
        v=np.exp(1j*theta)*np.array([r, math.sqrt(1-r*r)])
        B=a*np.outer(u,u.conj())
        C=b*np.outer(v,v.conj())
        got=mix(np.zeros((2,2),complex),B,C)
        overlap=np.vdot(u,v)
        q=math.sqrt((a-b)**2+4*a*b*(1-r*r))
        prediction=(a*b/(a+b+q))*(overlap*np.outer(u,v.conj()) +
                                           overlap.conjugate()*np.outer(v,u.conj()))
        assert np.allclose(got,prediction,rtol=2.e-8,atol=2.e-10), (a,b,r,got,prediction)
        eigen=np.linalg.eigvalsh(got)
        coefficient=a*b*r/(a+b+q)
        assert np.allclose(eigen,[coefficient*(r-1),coefficient*(r+1)],rtol=2.e-8,atol=2.e-10)
        count+=1
    return count

if __name__=='__main__':
    Phi, eigminus=exact_symbolic_checks()
    n=numerical_random_checks()
    root=float(sp.nroots(sp.Symbol('t')**3+sp.Symbol('t')**2+3*sp.Symbol('t')-1)[0])
    if root<=0:
        root=float([sp.re(z) for z in sp.nroots(sp.Symbol('t')**3+sp.Symbol('t')**2+3*sp.Symbol('t')-1) if abs(float(sp.im(z)))<1e-10 and 0<float(sp.re(z))<1][0])
    rstar=2*root/(1+root*root)
    kappa=root*(1-root)**2/(2*(1+root*root))
    print('exact witness matrix:',Phi)
    print('exact negative eigenvalue:',eigminus)
    print('rank-one random formula and spectra checks:',n)
    print('sharp threshold t, overlap, defect:',root,rstar,kappa)
