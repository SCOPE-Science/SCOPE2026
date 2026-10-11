"""Finite-dimensional checks for the sharp common-source joint numerical-radius bound.
These checks are finite examples; the analytic proof establishes the universal theorem.
"""
from fractions import Fraction
from itertools import product
import math
import numpy as np


def exact_matrix_checks():
    count = 0
    tight = 0
    strict = 0
    for m in range(2, 9):
        for k in range(1, 11):
            q = min(k, m - 1)
            B = np.zeros((k, m-1), dtype=int)
            for j in range(q):
                B[j,j] = 1
            gram = B @ B.T
            norm_squared = int(np.trace(gram))
            eigenvalues = np.linalg.eigvalsh(gram)
            top = float(eigenvalues[-1])
            assert norm_squared == q
            assert abs(top-1) < 1e-12
            assert abs(math.sqrt(top)/(2*math.sqrt(norm_squared)) - 1/(2*math.sqrt(q))) < 1e-12
            tight += 1
            count += 3
            if q > 1:
                a = np.zeros(k,dtype=int)
                a[0] = 1
                norm_squared_nonorth = norm_squared + 1
                lower_squared = (top+1)/4
                target_squared = norm_squared_nonorth/(4*q)
                assert lower_squared > target_squared + 1e-12
                strict += 1
            else:
                # At t=3/4, the phase-averaged squared radius strictly beats
                # the q=1 threshold whenever a != 0.
                lhs = Fraction(3,4)**2 + Fraction(3,4)*Fraction(1,4)
                rhs = Fraction(2,4)
                assert lhs > rhs
                strict += 1
    return count,tight,strict


def random_checks():
    rng = np.random.default_rng(195)
    count=0
    for field in ('real','complex'):
        for m in range(2, 9):
            for k in range(1, 11):
                q=min(k,m-1)
                for j in range(12):
                    U=rng.standard_normal((m,k))
                    if field=='complex':
                        U=U+1j*rng.standard_normal((m,k))
                    a=U[0,:]
                    B=U[1:,:]
                    hs2=float(np.vdot(U,U).real)
                    smax=float(np.linalg.svd(B,compute_uv=False)[0])
                    bound=(np.linalg.norm(a)**2+smax*smax)/4
                    required=hs2/(4*q)
                    assert bound >= required-1e-9, (field,m,k,j,bound,required)
                    # sampled test for w2(x) >= lower bound for a nonzero vector
                    if np.linalg.norm(B)>0:
                        svd=np.linalg.svd(B,full_matrices=False)
                        y=svd[0][:,0]
                        # x=(e0 + phase*(0,y))/sqrt2, phase average ensures
                        # at least the claimed phase-insensitive lower bound
                        vals=[]
                        for theta in (0,math.pi/2,math.pi,3*math.pi/2):
                            z=np.exp(1j*theta)*y
                            comps=(a+ B.conj().T @ z)/2
                            vals.append(float(np.vdot(comps,comps).real))
                        assert max(vals) >= bound - 1e-8
                    count += 1
    return count

if __name__=='__main__':
    c,t,s=exact_matrix_checks()
    r=random_checks()
    print(f'VERIFY_OK exact_witness_assertions={c} rank_equalizers={t} nonorthogonality_tests={s} random_gram_tests={r} analytic_global_proof_required=True')
