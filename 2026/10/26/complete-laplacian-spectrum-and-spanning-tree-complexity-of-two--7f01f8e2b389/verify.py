"""Finite reproducibility checks for the two-token biclique theorem.

The infinite parameter statement is proved by an orthogonal block decomposition,
not by these computations. Requires Python 3 and NumPy for floating point
cross-checks; the modular determinants use the Python standard library.
"""
from itertools import combinations
import math
import numpy as np


def data(m, n):
    V = list(combinations(range(m+n), 2))
    index = {v:i for i,v in enumerate(V)}
    L = [[0]*len(V) for _ in V]
    for i, pair in enumerate(V):
        for x in pair:
            y = next(iter(set(pair)-{x}))
            for dest in range(m+n):
                if (x < m) == (dest < m) or dest == y:
                    continue
                j = index[tuple(sorted((y,dest)))]
                L[i][j] -= 1
                L[i][i] += 1
    return L


def spectrum(m,n):
    N=m+n
    parts = [(0,1), (N,1), (2*(N-1),1), (n,m-1), (m,n-1),
             (m+2*n-2,m-1), (n+2*m-2,n-1), (N-2,(m-1)*(n-1)),
             (2*n,m*(m-3)//2), (2*m,n*(n-3)//2)]
    assert sum(mult for eig,mult in parts) == N*(N-1)//2
    vals=[]
    for eig, mult in parts:
        vals += [eig]*mult
    return sorted(vals)


def trees(m,n):
    N=m+n
    return (4 * n**(m-1)*m**(n-1)
            *(m+2*n-2)**(m-1)*(n+2*m-2)**(n-1)
            *(N-2)**((m-1)*(n-1))
            *(2*n)**(m*(m-3)//2)*(2*m)**(n*(n-3)//2))


def det_mod(A,p):
    a=[[v%p for v in row] for row in A]
    d=1
    for i in range(len(a)):
        k=next((j for j in range(i,len(a)) if a[j][i]),None)
        if k is None: return 0
        if k != i:
            a[i], a[k] = a[k],a[i]
            d=-d
        v=a[i][i]
        d=d*v%p
        inverse=pow(v,-1,p)
        for j in range(i+1,len(a)):
            f=a[j][i]*inverse%p
            if f:
                for col in range(i+1,len(a)):
                    a[j][col]=(a[j][col]-f*a[i][col])%p
                a[j][i]=0
    return d%p


def main():
    spectral_pairs=0; determinant_pairs=0
    for m in range(3,7):
        for n in range(m,8):
            L=data(m,n)
            eig = np.linalg.eigvalsh(np.asarray(L,dtype=float))
            target=spectrum(m,n)
            assert len(target)==len(eig)
            assert max(abs(float(a)-b) for a,b in zip(eig,target))<1e-7,(m,n)
            spectral_pairs+=1
            if m<=5 and n<=6:
                for p in (1000000007,1000000009):
                    assert det_mod([row[1:] for row in L[1:]],p) == trees(m,n)%p,(m,n,p)
                determinant_pairs+=1
    print(f'VERIFY_OK spectra_pairs={spectral_pairs} exact_modular_matrix_tree_pairs={determinant_pairs}')

if __name__=='__main__': main()
