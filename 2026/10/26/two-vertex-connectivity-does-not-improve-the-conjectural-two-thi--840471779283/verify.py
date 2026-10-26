"""Standalone exact Pieri and independent seminormal-matrix checks.

Run: python verify.py (requires Python 3 and numpy).
"""
from functools import lru_cache
from itertools import combinations
import numpy as np


def partition_boxes(p):
    return {(i + 1, j + 1) for i, r in enumerate(p) for j in range(r)}


def smaller_partition_shapes(p, steps=2):
    out = {p}
    for _ in range(steps):
        new = set()
        for shape in out:
            for i in range(len(shape)):
                if i == len(shape)-1 or shape[i] > shape[i+1]:
                    a = list(shape)
                    a[i] -= 1
                    new.add(tuple(v for v in a if v))
        out = new
    return out


def pieri_eigen(p):
    n = sum(p)
    scores = []
    for beta in smaller_partition_shapes(p):
        skew = partition_boxes(p) - partition_boxes(beta)
        assert len(skew) == 2
        contents = sum(j-i for i,j in skew)
        if len({j for _,j in skew}) == 2:  # horizontal strip, S_2-trivial
            scores.append((contents - 1, beta, 'horizontal', tuple(sorted(skew))))
        if len({i for i,_ in skew}) == 2:  # vertical strip, S_2-sign
            scores.append((contents + 1, beta, 'vertical', tuple(sorted(skew))))
    best = max(scores)
    return 2*(n-2)-best[0], best, scores


def tableaux(p):
    n = sum(p)
    results = []
    def append(shape, positions):
        k = len(positions)+1
        if k > n:
            results.append(tuple(positions))
            return
        for i, cap in enumerate(p):
            a = shape[i] if i < len(shape) else 0
            if i > len(shape) or a == cap or (i > 0 and a >= shape[i-1]):
                continue
            newshape = list(shape)
            if i == len(newshape):
                newshape.append(1)
            else:
                newshape[i] += 1
            append(tuple(newshape), positions + [(i+1,a+1)])
    append((), [])
    return results


def matrix_eigen(p):
    n = sum(p)
    tab = tableaux(p)
    d = len(tab)
    lookup = {t:i for i,t in enumerate(tab)}
    matrices=[]
    for k in range(n-1):
        mat = np.zeros((d,d))
        for idx,t in enumerate(tab):
            a,b=t[k],t[k+1]
            diff=(b[1]-b[0])-(a[1]-a[0])
            mat[idx,idx]=1.0/diff
            if abs(diff)>1:
                arr=list(t)
                arr[k],arr[k+1]=arr[k+1],arr[k]
                j=lookup[tuple(arr)]
                mat[j,idx]=(1-1.0/(diff*diff))**0.5
        assert np.max(np.abs(mat@mat-np.eye(d))) < 1e-10
        matrices.append(mat)
    identity=np.eye(d)
    L=np.zeros((d,d))
    for a in (0,1):
        for b in range(2,n):
            trans=identity.copy()
            for k in list(range(a,b))+list(range(b-2,a-1,-1)):
                trans=trans@matrices[k]
            assert np.max(np.abs(trans-trans.T)) < 1e-10
            L+=identity-trans
    return np.linalg.eigvalsh(L)[0],d


def dominance(p,q):
    return all(sum(p[:k])>=sum(q[:k]) for k in range(1,max(len(p),len(q))+1))


def run():
    n_exact = 0
    n_matrix = 0
    for n in range(6,21):
        tau = (2,2) + (1,)*(n-4)
        if n % 2 == 0:
            sigma = (2,)*(n//2)
            sig_eig = 3*n-10
        else:
            sigma = (2,)*((n-1)//2)+(1,)
            sig_eig = 3*n-11
        assert dominance(sigma,tau)
        lam_tau,best_tau,_=pieri_eigen(tau)
        lam_sig,best_sig,_=pieri_eigen(sigma)
        assert lam_tau == 2*n-6, (n,lam_tau)
        assert lam_sig == sig_eig, (n,lam_sig)
        assert (3*lam_tau - 2*lam_sig)>0
        print(f'n={n} tau={lam_tau}, sigma={lam_sig}, ratio={lam_tau/lam_sig:.12f}; scores {best_tau[0]},{best_sig[0]}')
        n_exact+=1
        if n <= 10:
            a,da=matrix_eigen(tau)
            b,db=matrix_eigen(sigma)
            assert abs(a-lam_tau)<1e-8,(n,a,lam_tau)
            assert abs(b-lam_sig)<1e-8,(n,b,lam_sig)
            print(f'  seminormal matrix dimensions {da},{db}, min eigenvalues {a:.12g},{b:.12g}')
            n_matrix+=1
    print(f'PASS: {n_exact} exact finite-parameter checks, {n_matrix*2} independent full representation checks')

if __name__=='__main__':
    run()
