"""Independent finite checks for the weighted four-erasure theorem.
Only plain mathematical definitions and reproducible calculations are used.
Run: python3 check_weighted_skew.py
"""
from itertools import combinations
from math import comb, isclose
import numpy as np
import sympy as sp


def paley_skew_conference(q):
    # q is an odd prime, q = 3 mod 4
    def legendre(x):
        x %= q
        return 0 if x == 0 else 1 if pow(x, (q - 1)//2, q) == 1 else -1
    A = np.zeros((q+1, q+1), dtype=int)
    A[0, 1:] = 1
    A[1:, 0] = -1
    for i in range(q):
        for j in range(q):
            A[i+1, j+1] = legendre(j-i)
    assert np.array_equal(A.T, -A)
    assert np.array_equal(A @ A.T, q * np.eye(q+1, dtype=int))
    return A


def pfaffian4(A, subset):
    x = A[np.ix_(subset, subset)]
    return int(x[0,1]*x[2,3] - x[0,2]*x[1,3] + x[0,3]*x[1,2])


def quartic_coeffs(q, ws, pf_sq):
    # Characteristic polynomial of 2 times the positive weighted erasure Gram.
    e = [1]
    for k in range(1,5):
        e.append(sum(np.prod([ws[i] for i in I]) for I in combinations(range(4),k)))
    return [1, -e[1], (1-1/q)*e[2], -(1-3/q)*e[3], (1-6/q+pf_sq/q**2)*e[4]]


def check():
    for q in (7, 11, 19):
        A = paley_skew_conference(q)
        n = q+1
        counts = {1:0, 9:0}
        examples = {}
        for subset in combinations(range(n), 4):
            pf_sq = pfaffian4(A, subset)**2
            assert pf_sq in (1,9)
            counts[pf_sq] += 1
            examples.setdefault(pf_sq, subset)
        expected_one = n*(n-1)*(n-2)*(n-4)//32
        expected_nine = n*n*(n-1)*(n-2)//96
        assert counts == {1:expected_one, 9:expected_nine}
        assert sum(counts.values()) == comb(n,4)
        assert sum(k*v for k,v in counts.items()) == comb(n//2,2)*q*q
        weights = [sp.Integer(1), sp.Integer(2), sp.Integer(3), sp.Integer(5)]
        t = sp.sqrt(q)
        x = sp.symbols('x')
        exact_roots = {}
        for pf_sq,subset in examples.items():
            M = sp.Matrix([[sp.sqrt(weights[i]*weights[j])*(int(A[subset[i],subset[j]])*sp.I/t + (1 if i == j else 0)) for j in range(4)] for i in range(4)])
            actual = sp.Poly(sp.expand((x*sp.eye(4)-M).det()), x)
            es = [sp.Integer(1)] + [sum(sp.prod(weights[i] for i in inds) for inds in combinations(range(4),k)) for k in range(1,5)]
            expected = sp.Poly(x**4-es[1]*x**3+(1-sp.Rational(1,q))*es[2]*x**2-(1-sp.Rational(3,q))*es[3]*x+(1-sp.Rational(6,q)+sp.Rational(pf_sq,q*q))*es[4],x)
            assert sp.simplify(actual.as_expr()-expected.as_expr()) == 0
            eig = np.linalg.eigvalsh(np.array(M.evalf(),dtype=complex)/2)
            assert min(eig)>0
            exact_roots[pf_sq]=eig[-1]
        assert exact_roots[1]>exact_roots[9]
        print('order',n,'pf^2=1',counts[1],'pf^2=9',counts[9], 'weighted maxima',exact_roots)
    print('WEIGHTED_SKEW_CONFERENCE_FOUR_ERASURE_OK')

if __name__=='__main__':check()
