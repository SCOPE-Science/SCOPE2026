"""Exact character-count checks and independent matrix checks for the Hamming mixing spectrum."""
from itertools import product
from fractions import Fraction
from math import comb, factorial
import numpy as np


def spectral_factor(q, j):
    coeff = sum(factorial(j) // (factorial(a)**2 * factorial(j-2*a)) *
                (q-2)**(j-2*a) for a in range(j//2+1))
    return Fraction(coeff, q**j)


def count_character_pairs(q,d,j):
    """Count equal-Hamming-weight ordered character pairs of difference eta."""
    eta = (1,)*j + (0,)*(d-j)
    count = 0
    for x in product(range(q),repeat=d):
        y = tuple((xi-ei)%q for xi,ei in zip(x,eta))
        if sum(a!=0 for a in x)==sum(b!=0 for b in y):
            count += 1
    return count


def exact_tests():
    cases=0
    for q in range(2,7):
        for d in range(1,4):
            for j in range(d+1):
                direct=Fraction(count_character_pairs(q,d,j),q**d)
                formula=spectral_factor(q,j)
                assert direct==formula,(q,d,j,direct,formula)
                cases+=1
            expected_rank=sum(comb(d,j)*(q-1)**j for j in range(d+1)
                              if spectral_factor(q,j)>0)
            assert expected_rank==(q**d if q>=3 else 2**(d-1))
    return cases


def independent_projector_test():
    runs=0
    max_err=0.0
    for q,d in [(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(5,2)]:
        points=list(product(range(q),repeat=d))
        n=len(points)
        w=np.exp(2j*np.pi/q)
        # Independently construct the projectors from the character columns.
        P=[np.zeros((n,n),complex) for _ in range(d+1)]
        for k in points:
            j=sum(v!=0 for v in k)
            v=np.array([w**(sum(a*b for a,b in zip(k,x))%q)
                        for x in points])
            P[j]+=np.outer(v,v.conj())/n
        # Verify spectral decomposition for the simple graph.
        A=np.zeros((n,n),float)
        for u,x in enumerate(points):
            for v,y in enumerate(points):
                A[u,v]=int(sum(a!=b for a,b in zip(x,y))==1)
        assert np.max(np.abs(sum(P)-np.eye(n)))<2e-12
        for j in range(d+1):
            assert np.max(np.abs(A@P[j]-(d*(q-1)-q*j)*P[j]))<2e-11
        M=sum((E.real)**2 for E in P)
        assert np.max(np.abs(M.sum(axis=1)-1))<2e-12
        exact_eigs=[]
        for j in range(d+1):
            exact_eigs.extend([float(spectral_factor(q,j))]*
                              (comb(d,j)*(q-1)**j))
        eigs=np.linalg.eigvalsh(M)
        err=max(abs(a-b) for a,b in zip(eigs,sorted(exact_eigs)))
        max_err=max(err,max_err)
        assert err<1e-10,(q,d,err)
        runs+=1
    return runs,max_err


if __name__=='__main__':
    count=exact_tests()
    runs,error=independent_projector_test()
    print(f'VERIFY_OK exact_pair_count_cases={count} matrix_projector_cases={runs} max_eigen_error={error:.3e}')
