#!/usr/bin/env python3
"""Reproduce exact small cases and numerical checks of the basis-curvature laws."""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np


def quadratic_probe(H, x, Q, h):
    g = H @ x
    f = lambda y: 0.5 * float(y @ H @ y)
    return sum(((f(x + h * Q[:, j]) - f(x)) / h) * Q[:, j]
               for j in range(Q.shape[1])), g


def sq_bias(H, Q, h):
    return h*h/4 * sum(float(Q[:, j] @ H @ Q[:, j])**2
                        for j in range(Q.shape[1]))


def exact_cases():
    # Rational orthogonal rotations and finite-difference slopes.
    Q = [[F(3,5), -F(4,5)], [F(4,5), F(3,5)]]
    H = [F(1), F(-1)]
    x = [F(2), F(3)]
    h = F(2,7)
    def ff(y): return sum(H[i]*y[i]*y[i]/2 for i in range(2))
    qcols = [[Q[i][j] for i in range(2)] for j in range(2)]
    m = [F(0), F(0)]
    for v in qcols:
        s = (ff([x[i]+h*v[i] for i in range(2)]) - ff(x))/h
        for i in range(2): m[i] += s*v[i]
    grad = [H[i]*x[i] for i in range(2)]
    lhs = sum((m[i]-grad[i])**2 for i in range(2))
    rhs = h*h/4 * sum(sum(H[i]*v[i]*v[i] for i in range(2))**2 for v in qcols)
    assert lhs == rhs
    # Sign randomization cancels the quadratic truncation bias exactly.
    avg = [F(0), F(0)]
    for signs in product((-1,1), repeat=2):
        est = [F(0), F(0)]
        for j,sign in enumerate(signs):
            v = [sign * z for z in qcols[j]]
            s = (ff([x[i]+h*v[i] for i in range(2)])-ff(x))/h
            for i in range(2): est[i] += s*v[i]
        for i in range(2): avg[i] += est[i] / 4
    assert avg == grad
    # Traceless indefinite curvature is exactly removable by a rotation.
    from sympy import Matrix, sqrt, simplify
    H2=Matrix.diag(1,-1)
    T=Matrix([[1/sqrt(2),-1/sqrt(2)],[1/sqrt(2),1/sqrt(2)]])
    assert all(simplify((T.T*H2*T)[j,j])==0 for j in range(2))
    # Rank-one PSD curvature: a Walsh frame attains the universal minimum.
    T4=Matrix([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]) / 2
    R4=Matrix.diag(4,0,0,0)
    assert T4.T*T4 == Matrix.eye(4)
    assert all((T4.T*R4*T4)[j,j]==1 for j in range(4))
    assert sum((R4[j,j])**2 for j in range(4)) == 16
    return 4


def numeric_checks():
    rng=np.random.default_rng(20261023)
    count=0
    for k in (1,2,3,5,8):
        for _ in range(60):
            Y=rng.normal(size=(k,k))
            H=(Y+Y.T)/2
            Z=rng.normal(size=(k,k));Q,R=np.linalg.qr(Z)
            Q=Q @ np.diag(np.sign(np.diag(R)))
            x=rng.normal(size=k)
            h=0.013
            actual,target=quadratic_probe(H,x,Q,h)
            observed=float(np.dot(actual-target,actual-target))
            predicted=sq_bias(H,Q,h)
            assert abs(observed-predicted)<1e-8 * (1+predicted)
            low=h*h/4 * float(np.trace(H))**2/k
            high=h*h/4 * float(np.trace(H@H))
            assert low-1e-12 <= predicted <= high+1e-12
            count+=3
    haar_count=0
    for k in (2,3,6):
        X=rng.normal(size=(k,k));H=(X+X.T)/2
        target=(float(np.trace(H))**2+2*float(np.trace(H@H)))/(k+2)
        S=0.
        for _ in range(18000):
            Z=rng.normal(size=(k,k));Q,R=np.linalg.qr(Z)
            Q=Q @ np.diag(np.sign(np.diag(R)))
            d=np.diag(Q.T@H@Q)
            S+=float(d@d)
        sample=S/18000
        assert abs(sample-target) <= 0.055*max(target,0.01), (k,sample,target)
        haar_count+=18000
    return count,haar_count

if __name__ == '__main__':
    a=exact_cases()
    b,c=numeric_checks()
    print('PASS: 4 exact-rational/symbolic examples; '+str(b)+' deterministic numerical identities/inequalities; '+str(c)+' Haar frames for moment checks.')
    print('All infinite statements require the independent written argument in RESULT.md.')
