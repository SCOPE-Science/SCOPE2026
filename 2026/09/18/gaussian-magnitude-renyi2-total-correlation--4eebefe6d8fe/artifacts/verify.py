#!/usr/bin/env python3
import itertools
import math
import numpy as np

def renyi2_gaussian_magnitudes(R):
    """Exact D2 between |N(0,R)| and the product of its half-normal marginals."""
    R = np.asarray(R, dtype=float)
    n = R.shape[0]
    Ri = np.linalg.inv(R)
    lam_max = np.linalg.eigvalsh(R).max()
    if lam_max >= 2.0:
        return math.inf
    total = 0.0
    for signs in itertools.product((-1.0, 1.0), repeat=n):
        D = np.diag(signs)
        B = Ri + D @ Ri @ D - np.eye(n)
        sign, logdet = np.linalg.slogdet(B)
        assert sign > 0
        total += math.exp(-0.5 * logdet)
    exp_d2 = total / ((2.0 ** n) * np.linalg.det(R))
    return math.log(exp_d2)

def bivariate_check():
    for rho in (0.1, 0.5, 0.8, 0.95):
        R = np.array([[1.0, rho], [rho, 1.0]])
        lhs = renyi2_gaussian_magnitudes(R)
        rhs = -math.log1p(-(rho ** 4))
        assert abs(lhs-rhs) < 5e-13
        print(f"rho={rho:.2f}  determinant={lhs:.15g}  closed_form={rhs:.15g}")

def local_check():
    A = np.array([
        [0.0,  0.4, -0.7],
        [0.4,  0.0,  0.2],
        [-0.7, 0.2,  0.0],
    ])
    c4 = sum(A[i,j]**4 for i in range(3) for j in range(i+1,3))
    c6 = 8.0 * (A[0,1]*A[0,2]*A[1,2])**2
    print(f"predicted c4={c4:.15g}, c6={c6:.15g}")
    for eps in (0.08, 0.04, 0.02):
        R = np.eye(3) + eps*A
        d2 = renyi2_gaussian_magnitudes(R)
        scaled4 = d2/eps**4
        scaled6 = (d2-c4*eps**4)/eps**6
        print(f"eps={eps:.2f}  D2/eps^4={scaled4:.15g}  sixth_residual={scaled6:.15g}")

def equicorrelation_check():
    n = 4
    for rho in (0.2, 0.34):
        R = (1-rho)*np.eye(n) + rho*np.ones((n,n))
        lam = np.linalg.eigvalsh(R).max()
        d2 = renyi2_gaussian_magnitudes(R)
        print(f"n=4 rho={rho:.2f} lambda_max={lam:.6g} D2={d2}")

if __name__ == "__main__":
    print("Bivariate identity")
    bivariate_check()
    print("\nLocal expansion")
    local_check()
    print("\nEquicorrelation threshold")
    equicorrelation_check()
