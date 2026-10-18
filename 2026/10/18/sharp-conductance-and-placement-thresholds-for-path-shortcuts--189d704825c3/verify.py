"""Reproducible checks for one-shortcut spectral saturation on paths.

Needs numpy and Python standard library. Numerical checks support, but do not
replace, the arbitrary-order analytical proof in RESULT.md.
"""
import math
import numpy as np


def laplacian(n):
    L = np.zeros((n, n), dtype=float)
    for k in range(n - 1):
        L[k, k] += 1
        L[k + 1, k + 1] += 1
        L[k, k + 1] -= 1
        L[k + 1, k] -= 1
    return L


def second(L, i, j, weight):
    d = np.zeros(L.shape[0]); d[i] = 1.; d[j] = -1.
    return np.linalg.eigvalsh(L + weight * np.outer(d, d))[1]


def threshold(n, i):
    theta = 2 * math.pi / n
    s = math.sin((2 * i + 1) * theta)
    return (math.sin(theta) / s) if s > 1e-13 else math.inf


def verify():
    count = 0
    for n in range(4, 34):
        L = laplacian(n)
        ceiling = 2 - 2 * math.cos(2 * math.pi / n)
        admissible = [(i, j) for i in range(n) for j in range(i + 2, n)]
        for i, j in admissible:
            e = second(L, i, j, 1.)
            expect = (i + j == n - 1 and i < n // 4)
            if expect:
                assert abs(e - ceiling) < 2e-9, (n,i,j,e,ceiling)
            else:
                assert e < ceiling - 2e-11, (n,i,j,e,ceiling)
            count += 1
        for i in range((n - 2) // 2):
            j = n - 1 - i
            if j - i < 2: continue
            critical = threshold(n, i)
            if not math.isfinite(critical):
                assert second(L,i,j,1000.) < ceiling - 1e-9
            else:
                assert abs(second(L,i,j,critical)-ceiling) < 1e-8
                assert second(L,i,j,critical * .97) < ceiling - 1e-11
            count += 2
    # Symbolically evaluate the exactly computable dimension-four threshold.
    # P4+one diagonal {0,3} closes a cycle; lambda2=2 when weight=1.
    assert abs(second(laplacian(4),0,3,1.)-2.) < 1e-12
    # Crosscheck the antisymmetric shifted resolvent with its explicit formula.
    for n in range(4, 55):
        L = laplacian(n)
        theta=2*math.pi/n; lam=2-2*math.cos(theta)
        for i in range((n-2)//2):
            j=n-1-i
            if j-i<2: continue
            b=np.zeros(n); b[i]=1; b[j]=-1
            # Project away the symmetric k=2 eigenspace and the constant.
            spectral, basis = np.linalg.eigh(L)
            y = np.zeros(n)
            for k in range(1,n):
                if abs(spectral[k]-lam) > 1e-7:
                    y += (basis[:,k] @ b) * basis[:,k] / (spectral[k]-lam)
            analytic = -math.sin((2*i+1)*theta)/math.sin(theta)
            assert abs(b @ y - analytic) < 3e-8, (n,i,b@y,analytic)
            count += 1
    print('VERIFY_OK',count,'numerical eigenvalue, threshold and shifted-resolvent checks')


if __name__ == '__main__':
    verify()
