"""Reproduce finite checks for exact continuous-time mixing on a single-edge-deficient balanced biclique.

No external packages are required. The infinite-family result is proved analytically in RESULT.md;
the finite matrix checks here are corroborating evidence, not a substitute for that proof.
"""
from fractions import Fraction as F
from math import sqrt


def weights_at_unit_gap(n):
    m = n - 1
    if 2 <= m <= 6:
        a = (m + 3) / (2 * m * m)
        b = 3 / (2 * m)
        D = (m + 9) / 2
    else:
        disc = sqrt(m*m - 6*m + 1)
        b = (m + 1 - disc) / (4*m)
        a = (1 - b) / m
        D = m * (1 + b)
    return a, b, D


def laplacian(n, a, b):
    N = 2*n
    L = [[0.0 for _ in range(N)] for __ in range(N)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            w = a if i > 0 and j > 0 else b
            k = n + j
            L[i][i] += w
            L[k][k] += w
            L[i][k] -= w
            L[k][i] -= w
    return L


def eigvals_sym_jacobi(A, tol=1e-11, maxsweeps=50):
    N = len(A)
    A = [row[:] for row in A]
    for sweep in range(maxsweeps):
        moved = False
        for p in range(N):
            for q in range(p+1,N):
                if abs(A[p][q]) <= tol:
                    continue
                moved = True
                tau = (A[q][q]-A[p][p])/(2*A[p][q])
                t = (1.0 if tau>=0 else -1.0)/(abs(tau)+sqrt(1+tau*tau))
                c = 1/sqrt(1+t*t)
                s = t*c
                app = A[p][p]
                aqq = A[q][q]
                apq = A[p][q]
                A[p][p] = app - t*apq
                A[q][q] = aqq + t*apq
                A[p][q] = A[q][p] = 0.0
                for r in range(N):
                    if r==p or r==q:
                        continue
                    ar_p,ar_q = A[r][p],A[r][q]
                    A[r][p] = A[p][r] = c*ar_p - s*ar_q
                    A[r][q] = A[q][r] = s*ar_p + c*ar_q
        if not moved:
            break
    return sorted(A[i][i] for i in range(N))


def reduced_eigs(n,a,b):
    m=n-1
    internal = m*a+b
    even=n*b
    tr=m*b+2*m*a+b
    det=(m*b)*(2*m*a+b)-m*b*b
    disc=tr*tr-4*det
    lower=(tr-sqrt(max(0.0,disc)))/2
    upper=(tr+sqrt(max(0.0,disc)))/2
    return [0.0,lower,upper,even]+[internal]*(2*(m-1))


def test():
    # Polynomial and cost identities, exact for rational first branch.
    for m in range(2,7):
        a=F(m+3,2*m*m)
        b=F(3,2*m)
        D=F(m+9,2)
        assert m*m*a+2*m*b == D
        assert (m*b-1)*(2*m*a+b-1)==m*b*b
        assert m*a+b>=1
        assert (m+1)*b>1
        assert m*b>1
    # Candidate second branch lies on both spectral constraints.
    for m in range(7,500):
        disc=sqrt(m*m-6*m+1)
        b=(m+1-disc)/(4*m)
        a=(1-b)/m
        assert abs(m*a+b-1)<1e-11
        assert abs((m*b-1)*(2*m*a+b-1)-m*b*b)<1e-10
        assert m*b>1
        assert abs(m*m*a+2*m*b-(m*(1+b)))<1e-10
    # Direct matrix eigenvalues and budget; multiple graph sizes across transition.
    ns=list(range(3,31))+[35,45]
    for n in ns:
        a,b,D=weights_at_unit_gap(n)
        L=laplacian(n,a,b)
        w=eigvals_sym_jacobi(L)
        exp=sorted(reduced_eigs(n,a,b))
        assert len(w)==len(exp)
        assert max(abs(x-y) for x,y in zip(w,exp)) < 5e-8,(n,w,exp)
        assert abs(w[1]-1.0)<5e-8,(n,w[1])
        assert abs((n-1)**2*a +2*(n-1)*b-D)<1e-9
    # Independent finite search: random two-orbit design cannot beat proven D.
    import random
    R=random.Random(3097)
    for n in [3,4,6,7,8,9,13,30]:
        m=n-1
        _,_,D=weights_at_unit_gap(n)
        for _ in range(200):
            a=10**R.uniform(-2,2)
            b=10**R.uniform(-2,2)
            lam=min(sorted(reduced_eigs(n,a,b))[1],m*a+b)
            normalized=(m*m*a+2*m*b)/lam
            assert normalized>=D-1e-8,(n,normalized,D)
    print('PASS: exact rational identities for m=2..6; 493 radical-branch identities;'
          ' 30 dense matrix spectra; 1,600 sampled two-orbit designs')


if __name__=='__main__':
    test()
