#!/usr/bin/env python3
"""Exact independent finite checks of a rank-two matroid polytope graph spectrum.

Requires Python 3 and SymPy. Finite checks corroborate, but do not replace,
the invariant-subspace proof in RESULT.md.
"""
from itertools import combinations
from math import comb
import sympy as sp

x = sp.symbols('x')
p_sym, q_sym = sp.symbols('p q', integer=True, positive=True)


def matrices_from_bases(p, q):
    # Reconstruct the one-skeleton from the basis-exchange condition.
    bases = [pair for pair in combinations(range(p + q), 2)
             if not (pair[0] < p and pair[1] < p)]
    mat = sp.zeros(len(bases))
    for a, first in enumerate(bases):
        for b in range(a + 1, len(bases)):
            if len(set(first) & set(bases[b])) == 1:
                mat[a, b] = mat[b, a] = -1
                mat[a, a] += 1
                mat[b, b] += 1
    return bases, mat


def factored_predicted_poly(p, q):
    T, S, U = p + 2*q - 1, p + q - 1, 2*p + 2*q - 2
    W = x**2 - (2*p + 3*q - 1)*x + q*(3*p + 2*q - 1)
    return (x * (x - 2*p - q + 1) * (x - T)**((p-1)*(q-1))
            * (x - S)**(p-1) * (x - U)**(q*(q-3)//2) * W**(q-1))


def predicted_trees(p, q):
    E = p*q + comb(q, 2)
    numerator = ((2*p+q-1) * (p+2*q-1)**((p-1)*(q-1))
                 * (p+q-1)**(p-1) * (2*p+2*q-2)**(q*(q-3)//2)
                 * (q*(3*p+2*q-1))**(q-1))
    assert numerator % E == 0
    return numerator // E


def finite_checks():
    count = 0
    for p, q in [(2, 3), (3, 3), (2, 4), (3, 4),
                 (4, 3), (2, 5), (3, 5)]:
        bases, laplacian = matrices_from_bases(p, q)
        assert len(bases) == p*q + comb(q, 2)
        assert sp.expand(laplacian.charpoly(x).as_expr()
                         - factored_predicted_poly(p, q)) == 0
        assert laplacian[1:, 1:].det() == predicted_trees(p, q)
        print('EXACT_CHECK', p, q, len(bases), predicted_trees(p, q))
        count += 1
    return count


def phase_identity():
    S = p_sym + q_sym - 1
    W_S = sp.expand(S**2 - (2*p_sym+3*q_sym-1)*S
                    + q_sym*(3*p_sym+2*q_sym-1))
    assert sp.expand(W_S - (q_sym-p_sym*(p_sym-1))) == 0
    assert sp.expand((2*p_sym+3*q_sym-1)**2
                     - 4*q_sym*(3*p_sym+2*q_sym-1)
                     - ((q_sym-1)**2 + 4*p_sym*(p_sym-1))) == 0
    for p in range(3, 15):
        q = p*(p-1)
        assert factored_predicted_poly(p, q).subs(x, p+q-1) == 0
        assert sp.expand((p+q-1)**2 - (2*p+3*q-1)*(p+q-1)
                         + q*(3*p+2*q-1)) == 0
    print('SYMBOLIC_PHASE_IDENTITY_OK')


if __name__ == '__main__':
    tested = finite_checks()
    phase_identity()
    print('VERIFY_OK', tested, 'finite cofactor+characteristic polynomial cases')
