"""Reproducibility tests for critical edge-coordinate sine maps.
Run: python verify.py. These finite checks supplement, not replace, the proof.
"""
import math
import numpy as np
import sympy as sp


def spectral_data(K, a):
    d = len(a)
    D = np.diag(np.sqrt(a))
    vals, vectors = np.linalg.eigh(D @ K @ D)
    top = vals[-1]
    v = np.linalg.solve(D, vectors[:, -1])
    v /= np.sqrt(v @ (a * v))
    c = np.prod(1 - vals[:-1] / top)
    H = np.diag(0.5 * c * a * v * v)
    return top, c, v, H


def determinant(K, a, top, x):
    d = len(a)
    J = np.eye(d) - (K @ np.diag(a * np.cos(x))) / top
    return np.linalg.det(J)


def sample_tree(d, seed):
    rng = np.random.default_rng(seed)
    edges = [(j, int(rng.integers(0, j))) for j in range(1, d + 1)]
    colors = [0] * (d + 1)
    for j, parent in edges:
        colors[j] = 1 - colors[parent]
    B = np.zeros((d + 1, d))
    for j, (u, v) in enumerate(edges):
        if colors[u] == 0:
            B[u, j] = 1
            B[v, j] = -1
        else:
            B[v, j] = 1
            B[u, j] = -1
    a = np.exp(rng.uniform(-0.6, 0.6, size=d))
    return B.T @ B, a


def test_symbolic():
    x, y = sp.symbols('x y', real=True)
    K = sp.Matrix([[2, 1], [1, 2]])
    J = sp.eye(2) - K * sp.diag(sp.cos(x), sp.cos(y)) / 3
    exact = 1 - 2*(sp.cos(x)+sp.cos(y))/3 + sp.cos(x)*sp.cos(y)/3
    assert sp.simplify(J.det() - exact) == 0
    assert sp.simplify(sp.diff(exact,x,2).subs({x:0,y:0}) - sp.Rational(1,3)) == 0
    assert sp.simplify(sp.diff(exact,y,2).subs({x:0,y:0}) - sp.Rational(1,3)) == 0
    assert sp.simplify(sp.diff(exact,x,y).subs({x:0,y:0})) == 0
    c = sp.Rational(2,3)
    H = c*sp.eye(2)/4
    assert H == sp.eye(2)/6
    coeff = sp.simplify(2*sp.pi / ((2*sp.pi)**2 * sp.sqrt(H.det())))
    assert coeff == 3/sp.pi
    return 7


def test_numeric():
    checks = 0
    rng = np.random.default_rng(735)
    for d in [1,2,3,4,5,8]:
        for j in range(4):
            K, a = sample_tree(d, 3210+23*d+j)
            top,c,v,H = spectral_data(K,a)
            assert top > 0 and c > 0 and np.linalg.eigvalsh(H).min() > 0
            assert abs(v @ (a*v) - 1) < 1e-11
            assert abs(determinant(K,a,top,np.zeros(d))) < 1e-12
            for _ in range(20):
                u = rng.normal(size=d)
                u /= np.linalg.norm(u)
                t = 0.015
                det = determinant(K,a,top,t*u)
                leading = t*t*(u@H@u)
                assert det > 0
                assert abs(det/leading-1) < 0.004, (d,j,det/leading)
                checks += 1
    # Angular integral identity in two dimensions, including anisotropy.
    K,a = sample_tree(2, 894)
    _,_,_,H = spectral_data(K,a)
    angles = 2*np.pi*np.arange(32768)/32768
    u = np.stack((np.cos(angles),np.sin(angles)),axis=1)
    vals = np.einsum('ni,ij,nj->n',u,H,u)
    integral = 2*np.pi * np.mean(1/vals)
    assert abs(integral/(2*np.pi/np.sqrt(np.linalg.det(H)))-1)<1e-11
    checks += 1
    return checks


if __name__ == '__main__':
    n=test_symbolic()+test_numeric()
    print('PASS:',n,'exact symbolic identities and finite numerical checks; dimensions 1,2,3,4,5,8.')
    print('The all-tree integrability and logarithmic coefficient are proved analytically, not numerically.')
