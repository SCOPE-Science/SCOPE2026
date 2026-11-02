"""Numerical cross-checks of a sharp column-weight Schur multiplier bound.

Run: python3 verify_sparse_sign.py (requires numpy; cvxpy optional).
The theorem is proved algebraically; tests are finite corroboration only.
"""
from itertools import combinations
from math import comb, sqrt
import numpy as np


def full_incidence(v, k):
    columns=list(combinations(range(v),k))
    z=np.zeros((v,len(columns)),dtype=float)
    for j,c in enumerate(columns):
        z[list(c),j]=1.0
    return z


def sharp(v,k,a,b):
    return abs(a+b*k/v)+abs(b)*sqrt(k*(v-k)*(v-1))/v


def theoretical_upper(M,k,a,b):
    v,n=M.shape
    c=a+b*k/v
    h=np.eye(v)-np.ones((v,v))/v
    z=(M-a)/b
    f=z-(k/v)*np.ones_like(z)
    assert np.max(np.abs(h@f-f))<1e-10
    assert np.max(np.abs(M-(c+b*h@f)))<1e-10
    return sharp(v,k,a,b)


def main():
    tested=0
    for v in range(2,10):
        for k in range(1,v):
            z=full_incidence(v,k)
            nn=z.shape[1]
            assert np.all(z.sum(axis=0)==k)
            r=comb(v-1,k-1)
            lam=comb(v-2,k-2) if k>=2 else 0
            assert np.array_equal((z@z.T).astype(int),((r-lam)*np.eye(v)+lam*np.ones((v,v))).astype(int))
            for a,b in [(1,-2), (1.25,-1.75), (0,1), (-0.4,2.1), (1,-v/k)]:
                M=a+b*z
                target=sharp(v,k,a,b)
                nuc=np.linalg.svd(M,compute_uv=False).sum()/sqrt(v*nn)
                upper=theoretical_upper(M,k,a,b)
                assert abs(nuc-target)<5e-11, (v,k,a,b,target,nuc)
                assert abs(upper-target)<1e-12
                # Explicit polar witness for the nuclear lower bound.
                u,sv,vh=np.linalg.svd(M,full_matrices=False)
                polar=u@vh
                witness=np.linalg.norm(M*polar,ord=2)/np.linalg.norm(polar,ord=2)
                assert witness+2e-10>=target,(v,k,witness,target)
                tested+=1
    print('EXACT_SCHUR_COLUMN_CHECK_OK full_orbit_instances=',tested)
    # Independent random-column examples.  The polar witness with uniform
    # endpoint vectors is a rigorous lower bound for the true multiplier norm.
    rng=np.random.default_rng(825)
    random_cases=0
    for v in range(3,10):
        for k in range(1,v):
            for case in range(11):
                n=2+case
                z=np.zeros((v,n),dtype=float)
                for j in range(n):
                    z[rng.choice(v,k,replace=False),j]=1
                for a,b in ((1,-2),(0,1),(-0.4,2.1)):
                    M=a+b*z
                    lower=np.linalg.svd(M,compute_uv=False).sum()/sqrt(v*n)
                    bound=theoretical_upper(M,k,a,b)
                    assert lower <= bound+2e-10,(v,k,a,b,lower,bound)
                    random_cases+=1
    print('RANDOM_SUPPORT_POLAR_LOWER_CHECK_OK cases=',random_cases)
    # Balanced-column Hadamard boundary: H_4 with removed all-ones column.
    H=np.array([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]],float)
    B=H[:,1:]
    assert np.all(B.sum(axis=0)==0)
    assert np.array_equal(B.T@B,4*np.eye(3))
    assert abs(np.linalg.svd(B,compute_uv=False).sum()/sqrt(12)-sqrt(3))<1e-12
    print('BALANCED_HADAMARD_BOUNDARY_OK')


if __name__=='__main__':main()
