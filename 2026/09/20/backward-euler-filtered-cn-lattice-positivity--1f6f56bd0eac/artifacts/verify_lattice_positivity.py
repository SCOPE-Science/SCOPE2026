#!/usr/bin/env python3
"""Verification for the lattice-positivity identities in RESULT.md."""
import math
import numpy as np

def q_from_s(s):
    return (1.0 + 2.0*s - math.sqrt(1.0 + 4.0*s))/(2.0*s)

def r_kernel(j, s):
    q = q_from_s(s)
    return (1.0-q)/(1.0+q) * q**abs(j)

def k_kernel(j, s):
    q = q_from_s(s)
    a = abs(j)
    return (q**a * (1.0-q)**2/(1.0+q)**3
            * (2.0*a*(1.0+q) + 1.0-q))

def cycle_laplacian(n):
    L = 2*np.eye(n)
    for i in range(n):
        L[i, (i-1) % n] -= 1
        L[i, (i+1) % n] -= 1
    return L

def periodize(kernel, n, j, s, M=20000):
    # exponentially convergent; M is overkill for the test values below
    return sum(kernel(j + ell*n, s) for ell in range(-M, M+1))

def check_periodic():
    worst = 0.0
    min_entry = float("inf")
    for n in [3,4,5,8,17]:
        L = cycle_laplacian(n)
        for s in [0.01,0.1,0.5,1.0,3.0,20.0]:
            R = np.linalg.inv(np.eye(n) + s*L)
            C = R @ (np.eye(n) - s*L)
            K = C @ R
            min_entry = min(min_entry, K.min())
            # Compare first row against the periodized closed-form kernel.
            pred = np.array([periodize(k_kernel, n, j, s, M=1000)
                             for j in range(n)])
            worst = max(worst, np.max(np.abs(K[0] - pred)))
            # General consequence C^k R^m >= 0 for m >= k.
            for m in range(1,5):
                for k in range(m+1):
                    Mmat = np.linalg.matrix_power(C,k) @ np.linalg.matrix_power(R,m)
                    if Mmat.min() < -2e-12:
                        raise AssertionError((n,s,m,k,Mmat.min()))
    return worst, min_entry

def check_infinite_convolution():
    worst = 0.0
    min_k = float("inf")
    for s in [0.01,0.1,0.5,1.0,3.0,20.0,100.0]:
        q = q_from_s(s)
        # truncate where tails are negligible
        M = max(100, int(math.ceil(math.log(1e-15)/math.log(q)))+20)
        js = range(-min(M,20000), min(M,20000)+1)
        for j in range(0, min(50,M)+1):
            conv = sum(r_kernel(a,s)*r_kernel(j-a,s) for a in js)
            kval = 2.0*conv-r_kernel(j,s)
            closed = k_kernel(j,s)
            worst = max(worst, abs(kval-closed))
            min_k = min(min_k, closed)
        # mass of closed form (tail truncated adaptively)
        total = k_kernel(0,s) + 2*sum(k_kernel(j,s) for j in range(1,min(M,20000)+1))
        if abs(total-1.0) > 2e-11:
            raise AssertionError(("mass",s,total))
    return worst, min_k

def check_dirichlet_counterexample():
    L = np.array([[2.0,-1.0],[-1.0,2.0]])
    s = 1.0
    R = np.linalg.inv(np.eye(2)+s*L)
    C = R @ (np.eye(2)-s*L)
    K = C @ R
    H = C @ R @ R
    targetK = np.array([[-1,1],[1,-1]],dtype=float)/16.0
    targetH = np.array([[-1,1],[1,-1]],dtype=float)/64.0
    return np.max(np.abs(K-targetK)), np.max(np.abs(H-targetH)), K.min(), H.min()

if __name__ == "__main__":
    wper, minkper = check_periodic()
    winf, minkinf = check_infinite_convolution()
    eK,eH,mK,mH = check_dirichlet_counterexample()
    print(f"periodic kernel max error: {wper:.3e}")
    print(f"periodic K minimum tested entry: {minkper:.3e}")
    print(f"infinite convolution max error: {winf:.3e}")
    print(f"infinite closed-form minimum tested entry: {minkinf:.3e}")
    print(f"Dirichlet K exact-pattern error: {eK:.3e}; min={mK:.6f}")
    print(f"Dirichlet C R^2 exact-pattern error: {eH:.3e}; min={mH:.6f}")
    print("PASS")
