#!/usr/bin/env python3
"""Exact full-subset rank certificate for the order-nine harmonic plane frames.

Run: python3 verify_q9_fusion.py
Uses only Python's standard library. Rank lower bounds are certified in F_97;
rank upper bounds at exceptional square configurations use explicit exact
kernel vectors in the integral ring Z[i, omega], omega^2 + omega + 1 = 0.
"""
from collections import Counter
from itertools import combinations

P, PRIMITIVE24 = 97, 4
assert pow(PRIMITIVE24, 24, P) == 1
assert pow(PRIMITIVE24, 12, P) != 1 and pow(PRIMITIVE24, 8, P) != 1
F = [(a,b) for a in range(3) for b in range(3)]
ZERO = (0,0)
ONE = (1,0)
def add(a,b):
    return ((a[0]+b[0])%3,(a[1]+b[1])%3)
def neg(a):
    return ((-a[0])%3,(-a[1])%3)
def mul(a,b):
    return ((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
g = (1,1)
powers = [ONE]
for j in range(1,8):
    powers.append(mul(powers[-1],g))
assert len(set(powers)) == 8 and mul(powers[-1],g) == ONE
log = {x:j for j,x in enumerate(powers)}
assert set(powers) == set(F)-{ZERO}
# The 18 multiplicative squares, transported by translation and scaling.
MU4 = {powers[j] for j in (0,2,4,6)}
squares = {frozenset(add(a,mul(b,x)) for x in MU4)
           for a in F for b in powers}
assert len(squares) == 18

z3 = pow(PRIMITIVE24, 8, P)
z8 = pow(PRIMITIVE24, 3, P)

def rank_mod(matrix):
    A = [row[:] for row in matrix]
    height, width = len(A), len(A[0])
    r = 0
    for j in range(width):
        pivot = next((i for i in range(r,height) if A[i][j] % P),None)
        if pivot is None:
            continue
        A[pivot], A[r] = A[r], A[pivot]
        inv = pow(A[r][j],-1,P)
        for i in range(r+1,height):
            q = A[i][j]*inv % P
            if q:
                for k in range(j+1,width):
                    A[i][k] = (A[i][k]-q*A[r][k])%P
                A[i][j] = 0
        r += 1
        if r == height:
            break
    return r

def plane_matrix(exponent, extra_zero_row, subset):
    cols = []
    for a in subset:
        first = [pow(z3, 2*mul(a,x)[0]%3, P) for x in powers]
        second = [first[j]*pow(z8, -exponent*log[x]%8,P)%P
                  for j,x in enumerate(powers)]
        cols.extend((first,second))
    A = [[col[j] for col in cols] for j in range(8)]
    if extra_zero_row:
        A.insert(0,[1 if j%2==0 else 0 for j in range(2*len(subset))])
    return A

# Elementary exact Gaussian-integer and Eisenstein arithmetic.
# An element is (A,B) = A + B omega with Gaussian integer pairs A,B.
def gi_add(u,v): return (u[0]+v[0],u[1]+v[1])
def gi_neg(u): return (-u[0],-u[1])
def gi_mult_i(u,n):
    for _ in range(n%4):
        u = (-u[1],u[0])
    return u
Z = (0,0)
def ring_add(u,v): return (gi_add(u[0],v[0]),gi_add(u[1],v[1]))
def as_omega_power(u,n):
    n %= 3
    return ((u,Z) if n==0 else ((Z,u) if n==1
            else (gi_neg(u),gi_neg(u))))
def iszero(u): return u[0]==Z and u[1]==Z

T = [powers[6],powers[2],powers[0],powers[4]] # t, -t, 1, -1
assert set(T) == MU4
S = [a for a in F if a not in MU4]
# For each even character, entries (coefficient in first column,
# coefficient in second column) of a nontrivial RIGHT kernel on T.
RIGHT = {
  2: [((0,1),(0,1)),((0,-1),(0,-1)),((1,0),(-1,0)),((-1,0),(1,0))],
  4: [((1,0),(-1,0)),((1,0),(-1,0)),((-1,0),(1,0)),((-1,0),(1,0))],
  6: [((0,-1),(0,-1)),((0,1),(0,1)),((1,0),(-1,0)),((-1,0),(1,0))]
}
# Twice a LEFT kernel on the complement S in row order powers[0..7];
# each tuple (real, imaginary) is a Gaussian integer, and y(0)=0.
LEFT = {
  2: [(-1,-1),(0,-2),(-1,1),(-2,0),(1,1),(0,2),(1,-1),(2,0)],
  4: [(-2,0),Z,(2,0),Z,(-2,0),Z,(2,0),Z],
  6: [(-1,1),(0,2),(-1,-1),(-2,0),(1,-1),(0,-2),(1,1),(2,0)]
}

def check_upper_witnesses(e):
    # For the 4-square T, coefficients of a nonzero column relation.
    for x in [ZERO]+powers:
        total = (Z,Z)
        for a,(u,v) in zip(T,RIGHT[e]):
            if x==ZERO:
                value = u
            else:
                vchi = gi_mult_i(v,-(e//2)*log[x])
                value = gi_add(u,vchi)
            total = ring_add(total,as_omega_power(value,2*mul(a,x)[0]))
        assert iszero(total),('right',e,x,total)
    # For 5-block complement S, a nonzero annihilating row vector.
    assert any(v!=Z for v in LEFT[e])
    for a in S:
        for col in (0,1):
            total=(Z,Z)
            for j,x in enumerate(powers):
                value=gi_mult_i(LEFT[e][j],-(e//2)*j if col else 0)
                total=ring_add(total,as_omega_power(value,2*mul(a,x)[0]))
            assert iszero(total),('left',e,a,col,total)

checked=0
for e in (1,3,5,7):
    for subset in combinations(F,4):
        assert rank_mod(plane_matrix(e,False,subset)) == 8
        checked+=1
    print('8-dimensional odd character %d: all 126 four-block choices have rank 8'%e)
for e in (2,4,6):
    check_upper_witnesses(e)
    for k in range(1,7):
        counts=Counter()
        for subset in combinations(F,k):
            rank=rank_mod(plane_matrix(e,True,subset))
            sq=frozenset(subset)
            if k<=3:
                expected=2*k
            elif k==4:
                expected=7 if sq in squares else 8
            elif k==5:
                complement=frozenset(set(F)-sq)
                expected=8 if complement in squares else 9
            else:
                expected=9
            assert rank==expected,('modular lower bound',e,k,subset,rank,expected)
            counts[rank]+=1
            checked+=1
        print('9-dimensional even character %d, blocks %d: %s'%(
            e,k,sorted(counts.items())))
print('EXACT CERTIFICATE PASSED: %d modular rank computations; six exact kernel identities'%checked)
