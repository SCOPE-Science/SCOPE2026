#!/usr/bin/env python3
"""Exact finite checks for the 2-adic residue law of semi-Narayana counts.

The infinite proof is supplied separately; this program checks its finite
matrix identities and seven-case conjugation certificate without dependencies.
"""
from collections import deque
from itertools import product

A = ((1, 0, 0), (0, 1, 1), (0, 1, 0))
B = ((1, 1, 0), (1, 0, 0), (0, 1, 1))
E = ((0, 0, 0), (0, 1, 1), (0, 1, 0))
D = ((0, 0, 0), (0, 1, 0), (0, 0, 1))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def matmul(U, V, modulus):
    return tuple(tuple(sum(U[i][k] * V[k][j] for k in range(3)) % modulus
                       for j in range(3)) for i in range(3))


def mv(U, v, modulus):
    return tuple(sum(U[i][j] * v[j] for j in range(3)) % modulus
                 for i in range(3))


def power(U, exponent, modulus):
    res = I
    while exponent:
        if exponent & 1:
            res = matmul(res, U, modulus)
        U = matmul(U, U, modulus)
        exponent //= 2
    return res


def gf2_rank(vectors):
    rows = [sum(x << j for j, x in enumerate(v)) for v in vectors]
    rank = 0
    for pivot in (4, 2, 1):
        selected = next((i for i in range(rank, len(rows)) if rows[i] & pivot), None)
        if selected is None:
            continue
        rows[rank], rows[selected] = rows[selected], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i] & pivot:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def det(U):
    return (U[0][0]*(U[1][1]*U[2][2]-U[1][2]*U[2][1])
            - U[0][1]*(U[1][0]*U[2][2]-U[1][2]*U[2][0])
            + U[0][2]*(U[1][0]*U[2][1]-U[1][1]*U[2][0]))


assert det(A) == det(B) == -1
assert power(A, 3, 4) == tuple(tuple((I[i][j] + 2*E[i][j]) % 4
                                       for j in range(3)) for i in range(3))
assert power(A, 6, 8) == tuple(tuple((I[i][j] + 4*D[i][j]) % 8
                                       for j in range(3)) for i in range(3))
for r in range(1, 12):
    C = power(A, 3 if r == 1 else 6*2**(r-2), 2**(r+1))
    Q = E if r == 1 else D
    assert C == tuple(tuple((I[i][j] + (2**r)*Q[i][j]) % (2**(r+1))
                              for j in range(3)) for i in range(3))
print('PASS exact lifting matrices A^3 and A^(3*2^(r-1)), levels 1..11')

# All of GL-generated matrices modulo 2 are obtained by short positive words.
group = {I: ''}
queue = deque([I])
while queue:
    U = queue.popleft()
    for char, M in [('0', A), ('1', B)]:
        V = matmul(U, M, 2)
        if V not in group:
            group[V] = group[U] + char
            queue.append(V)
assert len(group) == 21
inverses = {U: next(V for V in group if matmul(U, V, 2) == I)
            for U in group}
by_word = {word: U for U, word in group.items()}
root = (1, 1, 0)
orbit = {root}
queue = deque([root])
while queue:
    v = queue.popleft()
    for M in (A, B):
        w = mv(M, v, 2)
        if w not in orbit:
            orbit.add(w)
            queue.append(w)
assert len(orbit) == 7
assert orbit == set(product(range(2), repeat=3)) - {(0, 0, 0)}
print('PASS seven nonzero initial states modulo 2 and 21-element generated group')

# Fixed explicit word witnesses: for each nonzero v, conjugate effects on v
# contain a basis of F_2^3. The words use products of the matrices A,B.
witnesses = {
    (0,0,1): (('', '1', '101'), ('', '01', '001')),
    (0,1,0): (('', '1', '01'), ('', '1', '11')),
    (0,1,1): (('', '1', '101'), ('', '1', '011')),
    (1,0,0): (('1', '101', '01'), ('1', '11', '011')),
    (1,0,1): (('', '1', '101'), ('', '1', '11')),
    (1,1,0): (('', '101', '01'), ('', '11', '011')),
    (1,1,1): (('', '1', '101'), ('', '1', '11')),
}
for v, (e_words, d_words) in witnesses.items():
    for T, words in ((E, e_words), (D, d_words)):
        vectors = []
        for word in words:
            W = by_word[word]
            C = matmul(matmul(W, T, 2), inverses[W], 2)
            vectors.append(mv(C, v, 2))
        assert gf2_rank(vectors) == 3, (v, T, words, vectors)
print('PASS all fourteen 3-by-3 determinant-one conjugation witnesses')

# Direct reachable residue census is an independent finite diagnostic, not
# the proof at arbitrary modulus: the general case uses the lift lemma above.
for r in range(1, 6):
    q = 1 << r
    seen = {(1,1,0)}
    queue = deque(seen)
    while queue:
        v = queue.popleft()
        for M in (A, B):
            w = mv(M, v, q)
            if w not in seen:
                seen.add(w)
                queue.append(w)
    assert len(seen) == q**3 - (q//2)**3
    assert all(any(v) and any(x % 2 for x in v) for v in seen)
    print(f'PASS modulus {q}: all {len(seen)} primitive triples reachable')

# Numerically test the original restricted-digit counting recursion against
# a truncation of its independent generating-function product.
N = 8192
s = [0]*N
s[0]=s[1]=1
for n in range(2,N):
    s[n] = s[n//2] if n%2 == 0 else s[n//2]+s[n//2-1]
c=[0]*N
c[0]=1
p=1
while p < N:
    out = [0]*N
    for i,value in enumerate(c):
        if value:
            for k in (0,1,3):
                t=i+k*p
                if t<N:out[t]+=value
    c=out
    p*=2
assert c==s
for n in range(1,N//2):
    v=(s[n],s[n-1],s[n-2] if n>=2 else 0)
    assert mv(A,v,10**40)==(s[2*n],s[2*n-1],s[2*n-2])
    assert mv(B,v,10**40)==(s[2*n+1],s[2*n],s[2*n-1])
print('PASS exact generating coefficients and doubling recurrences through 8191')
print('VERIFY_OK')
