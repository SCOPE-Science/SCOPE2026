#!/usr/bin/env python3
"""Exact finite certificates for Rule 73's one-step spatial image language.
Run: python3 verify.py. Requires only the Python standard library.
"""
from itertools import product
from collections import deque
from fractions import Fraction

RULE = 73
D = [1, -4, 5, -2, 1, -4, 9, -13, 12, -7, 1, 4, -6, 4, -2, 0]
N = [1, -2, 1, 0, 1, -2, 3, -4, 1, 3, -4, 4, -2, 1, 0]

def step(mask, bit):
    out = 0
    for a, b, c in product((0, 1), repeat=3):
        old = 2*a+b
        new = 2*b+c
        if mask & (1 << old) and (RULE >> (4*a+2*b+c)) & 1 == bit:
            out |= 1 << new
    return out

trans = {s:(step(s,0),step(s,1)) for s in range(16)}
assert trans[0] == (0,0)
expected = {
    0:(0,0),1:(2,1),2:(4,8),3:(6,9),4:(3,0),5:(3,1),
    6:(7,8),7:(7,9),8:(8,4),9:(10,5),10:(12,12),
    11:(14,13),12:(11,4),13:(11,5),14:(15,12),15:(15,13)
}
assert trans == expected

# All 16 subset states reachable from the all-states initial subset.
reach = {15:''}
queue = deque([15])
while queue:
    s = queue.popleft()
    for b in (0,1):
        nxt = trans[s][b]
        if nxt not in reach:
            reach[nxt] = reach[s]+str(b)
            queue.append(nxt)
assert len(reach) == 16

def initial_support(word):
    mask = 0
    for initial in range(4):
        s = 1 << initial
        for bit in word:
            s = trans[s][int(bit)]
        if s: mask |= 1 << initial
    return mask

# Four suffix experiments recover each possible pair-state from any subset.
singletons = ['111', '11001', '0111', '10011']
assert [initial_support(w) for w in singletons] == [1,2,4,8]
# Hence all 16 subsets have different right languages (minimal DFA).

def read(word, start=15):
    s = start
    for b in word: s = trans[s][int(b)]
    return s

assert read('11001') == 8
assert trans[8][0] == 8 and trans[8][1] == 4 and trans[4][1] == 0
assert read('1001') == 12
assert [read('0'*k,12) for k in range(1,6)] == [11,14,15,15,15]
assert [read('11', s) for s in [11,14,15]] == [5,4,5]
for k in range(1,256):
    w = '11001'+'0'*k+'11'
    assert read(w) == 0 and read(w[:-1]) != 0 and read(w[1:]) != 0

# Integer matrix for the 15 live DFA states. Rows count output-symbol arcs.
states = list(range(1,16))
m = len(states)
A = [[0]*m for _ in states]
for a in states:
    for b in (0,1):
        c = trans[a][b]
        if c: A[a-1][c-1] += 1

def multiply(X,Y):
    n = len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def trace(X): return sum(X[i][i] for i in range(len(X)))

def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]

# Exact Faddeev-LeVerrier characteristic polynomial of A.
B = eye(m)
char = [1]
for k in range(1,m+1):
    V = multiply(A,B)
    t = trace(V)
    assert t % k == 0
    ck = -t//k
    char.append(ck)
    B = [[V[i][j] + (ck if i==j else 0) for j in range(m)] for i in range(m)]
assert char == D
assert all(all(x==0 for x in row) for row in B)

# Prove rational generating function, not just finite-term matching.
ones = [1]*m
V = ones
numerator=[]
for k in range(m):
    numerator.append(V[14])  # initial mask 15 corresponds to row 14.
    V = [sum(A[i][j]*V[j] for j in range(m)) + D[k+1] for i in range(m)]
assert numerator == N
assert V == [0]*m  # implies (I-z A) Q(z)=D(z) 1 exactly.

# Independent block-level comparison for every word through length 12.
for n in range(13):
    generated = set()
    for bits in product((0,1),repeat=n+2):
        w = ''.join(str((RULE >> (4*bits[i]+2*bits[i+1]+bits[i+2])) & 1) for i in range(n))
        generated.add(w)
    dfa_generated = {''.join(bits) for bits in product('01',repeat=n) if read(bits)}
    assert generated == dfa_generated

# Positive power certifies strongly connected + aperiodic live adjacency,
# implying a unique, simple positive Perron eigenvalue.
T = eye(m)
positive_at = None
for k in range(1,100):
    T = multiply(T,A)
    if all(v > 0 for row in T for v in row):
        positive_at = k
        break
assert positive_at is not None
print(f'VERIFY_OK: 16 reachable and distinguishable states; 4 distinguishing suffixes; '
      f'255 exact minimal forbidden words; characteristic polynomial degree 15; '
      f'15 exact numerator coefficients; independent blocks length 0..12; A^{positive_at}>0')
