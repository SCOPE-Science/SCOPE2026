#!/usr/bin/env python3
"""Numerical checks of the intrinsic Hessian at a regular inscribed simplex."""
import math
import numpy as np


def simplex(d):
    n = d + 1
    projector = np.eye(n) - np.ones((n, n)) / n
    eigvals, eigvecs = np.linalg.eigh(projector)
    u = eigvecs[:, 1:].T @ projector * math.sqrt(n / d)
    return u.T


def simplex_volume(u):
    n, d = u.shape
    return abs(np.linalg.det(np.column_stack([np.ones(n), u]))) / math.factorial(d)


def check(d):
    u = simplex(d)
    n = d + 1
    volume = simplex_volume(u)
    reference = n ** (n / 2) / (math.factorial(d) * d ** (d / 2))
    assert np.allclose(volume, reference, rtol=1e-10)
    assert np.allclose(u @ u.T, n / d * np.eye(n) - np.ones((n,n)) / d, atol=1e-10)
    basis = []
    for i in range(d-1):
        a = np.zeros((d, d))
        a[i,i] = 1
        a[d-1,d-1] = -1
        basis.append(a)
    for i in range(d):
        for j in range(i):
            a = np.zeros((d, d))
            a[i,j] = a[j,i] = 1
            basis.append(a)
    gram = np.zeros((len(basis),len(basis)))
    hessian = np.zeros_like(gram)
    velocity = []
    diag = []
    for s in basis:
        q = np.sum((u @ s) * u,axis=1)
        velocity.append(u @ s - u * q[:,None])
        diag.append(q)
    for i,s in enumerate(basis):
        for j,t in enumerate(basis):
            gram[i,j] = np.sum(velocity[i]*velocity[j])
            hessian[i,j] = 2*np.trace(s@t) - (2*d+1)/n * np.dot(diag[i],diag[j])
    eigenvalues = np.sort(np.linalg.eigvals(np.linalg.solve(gram,hessian)).real)
    prediction = sorted([1.0]*d+[2*d/n]*((d+1)*(d-2)//2))
    assert np.allclose(eigenvalues,prediction,rtol=1e-9,atol=1e-9), (eigenvalues,prediction)
    random = np.random.default_rng(d+19)
    largest_rel_error = 0.0
    for j in range(6):
        coefficients = random.normal(size=len(basis))
        w = sum(x*v for x,v in zip(coefficients,velocity))
        speeds = np.linalg.norm(w,axis=1)
        def geodesic(t):
            factor = np.where(speeds>0,np.sin(t*speeds)/np.maximum(speeds,1e-30),t)
            return u*np.cos(t*speeds)[:,None]+w*factor[:,None]
        t = 0.0002
        finite_difference = (2*math.log(volume)-math.log(simplex_volume(geodesic(t)))-math.log(simplex_volume(geodesic(-t))))/t**2
        calculated = coefficients @ hessian @ coefficients
        error = abs(finite_difference-calculated)/max(1,abs(calculated))
        largest_rel_error = max(largest_rel_error,error)
        assert error < 0.00005,(d,j,finite_difference,calculated,error)
    print(f'd={d} volume={volume:.12g} eigenvalues={np.array2string(eigenvalues,precision=8)} max_relative_fd_error={largest_rel_error:.4g}')


if __name__=='__main__':
    for dimension in range(2,7):
        check(dimension)
    print('All five dimensions and 30 geodesic checks passed.')
