#!/usr/bin/env python3
"""Independent exact-arithmetic checks for a two-qubit Pauli-flat contrast bound.
Uses the Python standard library. No external data or packages are needed.
"""
from itertools import product

I = ((1, 0), (0, 1))
X = ((0, 1), (1, 0))
Y = ((0, -1j), (1j, 0))
Z = ((1, 0), (0, -1))
SINGLE = {'I': I, 'X': X, 'Y': Y, 'Z': Z}
IDENT = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
LABELS = tuple(''.join(pair) for pair in product('IXYZ', repeat=2) if pair != ('I','I'))

def multiply(a, b):
    n = len(a)
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)) for i in range(n))

def tensor(a, b):
    return tuple(tuple(a[i//2][j//2]*b[i%2][j%2] for j in range(4)) for i in range(4))

def scale(a, c):
    return tuple(tuple(c*x for x in row) for row in a)

def add(a, b):
    return tuple(tuple(x+y for x,y in zip(row_a,row_b)) for row_a,row_b in zip(a,b))

def tr(a):
    return sum(a[i][i] for i in range(len(a)))

PAULI = {word:tensor(SINGLE[word[0]], SINGLE[word[1]]) for word in LABELS}
CONTEXTS = (
    (('XI','IX','XX'),1),
    (('IY','YI','YY'),1),
    (('XY','YX','ZZ'),1),
    (('XI','IY','XY'),1),
    (('IX','YI','YX'),1),
    (('XX','YY','ZZ'),-1),
)
for words, eps in CONTEXTS:
    a,b,c=(PAULI[w] for w in words)
    assert multiply(a,b) == multiply(b,a)
    assert multiply(b,c) == multiply(c,b)
    assert multiply(multiply(a,b),c) == scale(IDENT,eps)
assert {w for words,_ in CONTEXTS for w in words} == {'XI','IX','XX','IY','YI','YY','XY','YX','ZZ'}
assert all(sum(w in words for words,_ in CONTEXTS)==2 for w in {'XI','IX','XX','IY','YI','YY','XY','YX','ZZ'})

# Exhaust every choice of signs on all 15 nonidentity two-qubit Paulis.
# For a frustrated context, (-r_A A,-r_B B) are joint +1 stabilizers,
# with third operator's expectation forced to -r_C.
contexts_witnessed = 0
for mask in range(1 << 15):
    sign = {w:(-1 if mask >> k & 1 else +1) for k,w in enumerate(LABELS)}
    violated = [(w,e) for w,e in CONTEXTS if sign[w[0]]*sign[w[1]]*sign[w[2]] != e]
    assert violated
    contexts_witnessed += len(violated)
    if mask % 127 == 0:
        (a,b,c),eps=violated[0]
        # projectors on the joint (-r_a,-r_b)-eigenspace
        pr = scale(multiply(add(IDENT, scale(PAULI[a],-sign[a])),
                            add(IDENT, scale(PAULI[b],-sign[b]))), 1)
        assert tr(pr) == 4
        for w in LABELS:
            val=tr(multiply(pr,PAULI[w]))
            expected=-4*sign[w] if w in (a,b,c) else 0
            assert val == expected, (mask, a,b,c, w, val, expected)

# Verify the explicit all-positive density operator at contrast 1/3.
H = scale(IDENT,0)
for w in LABELS:
    H=add(H,PAULI[w])
Q=add(scale(IDENT,3),H)  # Q = 12*rho, integer Gaussian entries
assert tr(Q)==12
assert all(tr(multiply(Q,PAULI[w]))==4 for w in LABELS)
assert tr(multiply(Q,Q))==96  # purity is 96/144 = 2/3
# Exact characteristic polynomial via traces/eigenvalues:
# H has eigenvalues -3,-3,3+2sqrt(3),3-2sqrt(3).
# Check the resulting polynomial annihilates H and has correct coefficients.
H2=multiply(H,H)
assert tr(H)==0
assert tr(H2)==60
# Polynomial (t+3)^2*(t^2-6t-3)=t^4-30t^2-72t-27.
H4=multiply(H2,H2)
Hpol=add(add(H4,scale(H2,-30)),add(scale(H,-72),scale(IDENT,-27)))
assert Hpol==scale(IDENT,0)
print('VERIFY_OK: 32768 sign vectors,', contexts_witnessed, 'frustrated contexts, exact rank-one witnesses, 15 Pauli expectations, and characteristic identity')
