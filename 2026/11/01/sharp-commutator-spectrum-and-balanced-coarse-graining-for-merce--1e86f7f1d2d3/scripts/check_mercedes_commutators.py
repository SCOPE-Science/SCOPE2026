"""Exact-rational small-dimension checks for Mercedes-frame effect commutators.

Run with: python3 check_mercedes_commutators.py
No external dependencies; finite checks complement the proof for arbitrary k.
"""
from fractions import Fraction
from itertools import product
from math import comb

checks = 0

def assert_eq(lhs, rhs):
    global checks
    if lhs != rhs:
        raise AssertionError((lhs, rhs))
    checks += 1

def multiply(A, B):
    n = len(A)
    return [[sum((A[i][s] * B[s][j] for s in range(n)), Fraction(0))
             for j in range(n)] for i in range(n)]

def comm(A, B):
    X, Y = multiply(A, B), multiply(B, A)
    return [[X[i][j] - Y[i][j] for j in range(len(A))]
            for i in range(len(A))]

def one_case(k, A_mask, B_mask, P, cache):
    A, B = cache[A_mask], cache[B_mask]
    C = comm(A, B)
    x = (A_mask & B_mask).bit_count()
    y = (A_mask & ~B_mask & ((1 << k)-1)).bit_count()
    z = (B_mask & ~A_mask & ((1 << k)-1)).bit_count()
    w = k - x - y - z
    e3 = x*y*z+x*y*w+x*z*w+y*z*w
    delta2 = Fraction(e3, k**3)
    assert_eq(sum((C[i][j]*C[i][j] for i in range(k)
                   for j in range(k)), Fraction(0))/2, delta2)
    assert_eq(C, [[-C[j][i] for j in range(k)] for i in range(k)])
    # Direct rank-two exterior-product identity (sign and normalization).
    u = [sum((P[i][s] for s in range(k) if (A_mask >> s) & 1), Fraction(0))
         for i in range(k)]
    v = [sum((P[i][s] for s in range(k) if (B_mask >> s) & 1), Fraction(0))
         for i in range(k)]
    expected = [[(v[i]*u[j]-u[i]*v[j])/k for j in range(k)] for i in range(k)]
    assert_eq(C, expected)
    assert_eq((e3 == 0), (sum(n > 0 for n in (x,y,z,w)) <= 2))
    # Verify cubic spectral identity for every pair (exactly 0 and ±i delta).
    C2 = multiply(C,C)
    C3 = multiply(C2,C)
    assert_eq(C3, [[-delta2*C[i][j] for j in range(k)] for i in range(k)])

for k in (3,4,5):
    P = [[Fraction(int(i==j))-Fraction(1,k) for j in range(k)] for i in range(k)]
    def effect(mask):
        return [[sum((P[i][s]*P[s][j] for s in range(k) if (mask>>s)&1), Fraction(0))
                for j in range(k)] for i in range(k)]
    cache = [effect(mask) for mask in range(1<<k)]
    for a in range(1<<k):
        for b in range(1<<k):
            one_case(k,a,b,P,cache)

# Independent integer-composition optimization for each k (not using masks).
for k in range(3,22):
    triples = [(a,b,c,k-a-b-c)
               for a in range(k+1)
               for b in range(k-a+1)
               for c in range(k-a-b+1)]
    def e3(t):
        return sum(t[i]*t[j]*t[h]
                   for i,j,h in ((0,1,2),(0,1,3),(0,2,3),(1,2,3)))
    q,r = divmod(k,4)
    predicted = 4*q**3+3*r*q*q+r*(r-1)*q+comb(r,3)
    maximum = max(map(e3,triples))
    assert_eq(maximum,predicted)
    assert_eq(all(max(t)-min(t)<=1 for t in triples if e3(t)==maximum),True)
    assert_eq(all(e3(t) < maximum for t in triples if max(t)-min(t)>1),True)

assert_eq(Fraction(4,4**3),Fraction(1,16))  # k=4: commutator norm = 1/4
assert_eq(Fraction(1,3**3),Fraction(1,27))  # k=3: norm = 1/(3sqrt(3))
print(f'PASS {checks} exact rational/integer assertions (n=3,4,5 all binary pairs; k=3..21 all cardinality profiles)')
