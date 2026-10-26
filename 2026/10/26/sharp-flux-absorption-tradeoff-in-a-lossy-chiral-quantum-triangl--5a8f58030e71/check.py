"""Reproduce the exact chiral-triangle absorption-time identity and examples.

Requirements: Python 3, sympy, numpy, scipy. No external files or network calls.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov
from scipy.optimize import minimize_scalar


def symbolic_check():
    gamma, s, c = sp.symbols('gamma s c', real=True, nonzero=True)
    I = sp.I
    H = sp.Matrix([[0, 1, c-I*s], [1, 0, 1], [c+I*s, 1, 0]])
    A = -I*H-sp.diag(gamma, 0, 0)
    Q = sp.Matrix([
        [sp.Rational(3, 2)/gamma, -c/(2*s)+I/2, 1/(2*s)],
        [-c/(2*s)-I/2, sp.Rational(3, 2)/gamma+gamma/(2*s*s)+1/(2*s), -gamma*c/(2*s*s)],
        [1/(2*s), -gamma*c/(2*s*s), sp.Rational(3, 2)/gamma+gamma/(2*s*s)-1/(2*s)]
    ])
    assert sp.simplify(Q-Q.conjugate().T) == sp.zeros(3)
    R = A.conjugate().T*Q+Q*A+sp.eye(3)
    relation = c*c+s*s-1
    for i in range(3):
        for j in range(3):
            numerator = sp.together(R[i, j]).as_numer_denom()[0]
            rem = sp.rem(sp.Poly(sp.expand(sp.simplify(numerator)),c), sp.Poly(relation,c))
            assert sp.simplify(rem.as_expr()) == 0, (i, j, numerator)
    assert sp.simplify(Q[1,1]-(sp.Rational(3,2)/gamma+gamma/(2*s*s)+1/(2*s))) == 0
    return 11  # Hermiticity, nine residual entries, and diagonal identity


def exact(g,phi):
    s=math.sin(phi)
    return 3/(2*g)+g/(2*s*s)+1/(2*s)


def model(g,phi):
    H=np.array([[0,1,np.exp(-1j*phi)], [1,0,1], [np.exp(1j*phi),1,0]],dtype=complex)
    A=-1j*H-np.diag([g,0.,0.])
    Q=solve_continuous_lyapunov(A.conj().T,-np.eye(3))
    assert np.allclose(Q,Q.conj().T,rtol=1e-10,atol=1e-10)
    assert np.allclose(A.conj().T@Q+Q@A,-np.eye(3),rtol=5e-10,atol=5e-10)
    return float(Q[1,1].real)


def numerical_checks():
    checks=0
    for g in [0.04, 0.1, 0.25, 0.5, 0.8, 1., math.sqrt(3), 3.0, 9.0]:
        for phi in [-2.8,-2.1,-1.6,-0.9,-0.25,0.3,1.,2.,2.8]:
            assert abs(exact(g,phi)-model(g,phi))<5e-8*max(1,exact(g,phi))
            checks+=1
        target=-min(2*g,1.)
        best=3/(2*g)+g/(2*target*target)+1/(2*target)
        if g<=.5:
            assert abs(best-11/(8*g))<1e-10
        else:
            assert abs(best-(3/(2*g)+g/2-.5))<1e-10
        opt=minimize_scalar(lambda phi: exact(g,phi),bounds=(-math.pi+1e-5,-1e-5),method='bounded',options={'xatol':1e-12})
        assert abs(opt.fun-best)<1e-7*max(1,best), (g,opt.fun,best)
        checks+=1
    bestg=math.sqrt(3)
    best=math.sqrt(3)-.5
    assert abs(exact(bestg,-math.pi/2)-best)<1e-12
    checks+=1
    for g in [0.08,0.2,0.5,0.75,1.,bestg,4.,10.]:
        for phi in [-2.8,-1.5,-.2,.25,1.,2.2]:
            assert exact(g,phi)>=best-1e-11
            checks+=1
    return checks


if __name__=='__main__':
    a=symbolic_check()
    b=numerical_checks()
    print(f'PASS: {a} symbolic matrix/identity checks; {b} independent numerical/optimization checks')
