"""Finite exact checks for binary Toeplitz block-phase incidence and simplex contractions.
Run with Python 3 standard library only. These tests supplement, not replace, the proof.
"""
from fractions import Fraction
from itertools import product

def base_word(p):
    assert p >= 6
    return '11' + '0' * (p - 3)

def next_word(w, q):
    assert q >= 4
    return (w + '0') * (q - 3) + w + '1' + w + '1' + w

def block_parities(w, q):
    p = len(w) + 1
    W = next_word(w, q)
    assert len(W) + 1 == p * q
    assert W.count('1') % 2 == 0
    assert all(W[i*p:i*p+p-1] == w for i in range(q))
    return [W[:i*p].count('1') % 2 for i in range(q)]

def mm(q):
    return ((Fraction(q-1, q), Fraction(1, q)),
            (Fraction(1, q), Fraction(q-1, q)))

def matmul(a, b):
    return tuple(tuple(sum(a[i][t] * b[t][j] for t in range(2)) for j in range(2)) for i in range(2))

count = 0
for p, q in product(range(6, 13), range(4, 14)):
    w = base_word(p)
    parities = block_parities(w, q)
    assert parities == [0] * (q-2) + [1, 0], (p, q, parities)
    m = mm(q)
    assert m[0][0] == Fraction(parities.count(0), q)
    assert m[1][0] == Fraction(parities.count(1), q)
    assert m[0][0]-m[0][1] == Fraction(q-2, q)
    count += 4

for tup in product(range(4, 8), repeat=4):
    m = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    for q in tup:
        m = matmul(m, mm(q))
    beta = Fraction(1)
    for q in tup:
        beta *= Fraction(q-2,q)
    assert m[0][0] - m[0][1] == beta
    assert m[0][0] + m[0][1] == 1
    count += 2

for qs in ([4]*20, [5,6,7,8,9,10,11,12], [9,16,25,36,49,64,81]):
    w = base_word(6)
    for q in qs[:4]:
        assert block_parities(w,q).count(1) == 1
        w = next_word(w,q)
        count += 1
print(f'PASS {count} exact assertions; all sampled incidence matrices and symbolic blocks agree')
