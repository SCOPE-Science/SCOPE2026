#!/usr/bin/env python3
"""Exact finite-state checks for random two-cylinder escape laws.

Requires Python 3 and SymPy. Numerical sampling is not used as a proof of
infinite-time claims; it supplements the algebraic calculation.
"""
import itertools
from fractions import Fraction
import sympy as sp

p, d, x, z = sp.symbols('p d x z')
half = sp.Rational(1, 2)
u = sp.Matrix([[half, half]])
one = sp.ones(2, 1)
words = [(0, 0), (0, 1), (1, 0), (1, 1)]

def matrix(a, b, prob):
    M = sp.ones(2, 2) / 2
    M[a[0], a[1]] -= prob / 2
    M[b[0], b[1]] -= (1 - prob) / 2
    return M

representatives = {
    'A': ((0, 0), (0, 1)),
    'B': ((0, 0), (1, 1)),
    'C': ((0, 1), (1, 0)),
    'D': ((0, 1), (1, 1)),
}
traces = {'A': 1-p/2, 'B': half, 'C': 1, 'D': (1+p)/2}
determinants = {
    'A': (1-2*p)/4,
    'B': -(1-p+p**2)/4,
    'C': (1-p+p**2)/4,
    'D': (2*p-1)/4,
}
polys = {}
for label, (a, b) in representatives.items():
    M = matrix(a, b, p)
    t, det = traces[label], determinants[label]
    assert sp.simplify(M.trace()-t) == 0
    assert sp.simplify(M.det()-det) == 0
    P = x**2 - t*x + det
    assert sp.simplify(M.charpoly(x).as_expr()-P) == 0
    polys[label] = P
    assert sp.factor((u*M*one)[0]-sp.Rational(3, 4)) == 0
    G = sp.factor((u*(sp.eye(2)-z*M).inv()*one)[0])
    G_proof = (1+(sp.Rational(3,4)-t)*z)/(1-t*z+det*z*z)
    assert sp.cancel(G-G_proof)==0

# Characteristic polynomial resultants in delta=p-1/2.
expected = {
  ('A','B'): -d*(2*d-1)**2/sp.Integer(32),
  ('B','C'): d**2*(4*d**2+3)/sp.Integer(16),
  ('C','D'): d*(2*d-1)**3/sp.Integer(64),
}
for (a,b), value in expected.items():
    got = sp.resultant(polys[a].subs(p, half+d), polys[b].subs(p, half+d), x)
    assert sp.factor(got-value)==0, (a,b,got,value)

# Every pair has exact geometric survival for a fair independent choice.
for a, b in itertools.combinations(words, 2):
    M = matrix(a, b, half)
    assert all(sp.factor((u*(M**n)*one)[0]-sp.Rational(3,4)**n)==0
               for n in range(14)), (a,b)
    # A direct algebraic certificate: either a constant right eigenvector
    # or rank-one with A^2=(3/4)A. Together with S_1=3/4 this proves all n.
    good = (M*one == sp.Rational(3,4)*one or
            M**2 == sp.Rational(3,4)*M)
    assert good, (a,b,M)

# The four classes partition all ordered distinct word pairs for p>1/2.
def kind(a,b):
    loop_a = a[0] == a[1]
    loop_b = b[0] == b[1]
    if loop_a and not loop_b: return 'A'
    if loop_a and loop_b: return 'B'
    if not loop_a and not loop_b: return 'C'
    return 'D'
for a,b in itertools.permutations(words,2):
    M=matrix(a,b,p)
    k=kind(a,b)
    assert sp.simplify(M.trace()-traces[k]) == 0
    assert sp.simplify(M.det()-determinants[k]) == 0

# Independent exhaustive path enumeration at finite horizons and several
# nontrivial exact rational biases, distinct from matrix multiplication.
for prob in (Fraction(1,2), Fraction(3,5), Fraction(3,4), Fraction(9,10)):
    for a,b in itertools.permutations(words,2):
        M=matrix(a,b,sp.Rational(prob.numerator,prob.denominator))
        for n in range(1,9):
            brute=Fraction(0)
            for seq in itertools.product((0,1),repeat=n+1):
                survival=Fraction(1,1<< (n+1))
                for j in range(n):
                    block=seq[j:j+2]
                    if block==a: survival *= 1-prob
                    if block==b: survival *= prob
                brute += survival
            mat=(u*M**n*one)[0]
            assert mat==sp.Rational(brute.numerator,brute.denominator), (a,b,n,prob,brute,mat)

# The ordering at p=3/4 is exact; the three adjacent pair resultants
# above exclude every crossing for 1/2 < p < 1.
root = {}
for label in representatives:
    pp=polys[label].subs(p,sp.Rational(3,4))
    roots=sp.solve(pp,x)
    root[label]=max(roots,key=lambda t:float(t))
assert all(sp.N(root[a]-root[b],30)>0 for a,b in [('A','B'),('B','C'),('C','D')])
print('VERIFY_OK')
