"""Exact finite-state algebra and independent enumeration for complementary triples.

Run with Python 3 and SymPy: python verify.py
The symbolic calculation establishes an identity of rational functions; the
separate enumerations are consistency checks, not substitutes for the identity.
"""
from collections import defaultdict
from itertools import product
import sympy as sp

z = sp.Symbol('z')
num = 1 + z**2 + z**3 + z**4 - 4*z**6 - 2*z**7 - 2*z**8
den = (1-z)*(1-z-z**3)
expected = sp.cancel(num/den)

# Each choice (0,1,2) forbids the smaller three-bit integer,
# its bitwise complement, or both. Inclusion-exclusion has sign (-1)^#2.
result = 0
for choices in product(range(3), repeat=4):
    forbidden = set()
    sign = 1
    for i, c in enumerate(choices):
        if c == 0:
            forbidden.add(i)
        elif c == 1:
            forbidden.add(7-i)
        else:
            forbidden.update((i, 7-i))
            sign *= -1
    T = sp.zeros(4)
    for pair in range(4):
        for letter in range(2):
            triple = (pair << 1) | letter
            if triple not in forbidden:
                T[pair, triple & 3] += 1
    M = sp.eye(4) - z*T
    # Exact adjugate/determinant avoids a floating-point inverse.
    scalar = (sp.ones(1,4)*M.adjugate()*sp.ones(4,1))[0]
    term = sp.cancel(1 + 2*z + z*z*scalar/M.det())
    result = sp.cancel(result + sign*term)
assert sp.cancel(result - expected) == 0

# Independent streaming automaton: tail, set of observed three-grams,
# and length truncated at two.
states = {(0,0,0):1}
observed = []
for n in range(65):
    observed.append(sum(states.values()))
    next_states = defaultdict(int)
    for (tail, seen, length_cap), multiplicity in states.items():
        for letter in range(2):
            triple = (tail << 1) | letter
            if length_cap == 2 and (seen & (1 << (7-triple))):
                continue
            new_seen = seen | (1 << triple) if length_cap == 2 else seen
            next_states[(triple & 3, new_seen, min(2,length_cap+1))] += multiplicity
    states = next_states

# Coefficients of exact proposed rational function, by formal division.
coeff = []
numer_coeff = [int(num.expand().coeff(z,i)) for i in range(65)]
for n in range(65):
    get = lambda k: coeff[k] if k >= 0 else 0
    coeff.append(numer_coeff[n] + 2*get(n-1) - get(n-2) + get(n-3) - get(n-4))
assert observed == coeff

# Third check: direct words, no automaton, with all overlapping triples.
for n in range(16):
    direct = 0
    for w in product((0,1),repeat=n):
        seen = {4*w[i]+2*w[i+1]+w[i+2] for i in range(n-2)}
        if all((7-t) not in seen for t in seen):
            direct += 1
    assert direct == coeff[n], (n,direct,coeff[n])

# A second representation exposes the order-three positive recurrence.
compact = (4/(1-z) + 2*(1+z+z**2)/(1-z-z**3)
           - (5+6*z+6*z**2+4*z**3+2*z**4))
assert sp.cancel(expected - compact) == 0
print('SYMBOLIC IDENTITY VERIFIED: 81 exact transfer matrices')
print('STREAMING AUTOMATON VERIFIED: lengths 0..64')
print('DIRECT WORD ENUMERATION VERIFIED: lengths 0..15')
print('FIRST VALUES:', ', '.join(map(str,coeff[:20])))
print('ALL CHECKS PASSED')
