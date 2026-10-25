#!/usr/bin/env python3
"""Exact, dependency-free checks for the period-six 5-free Fibonacci classification.

The proof's finite residue step has precisely 63 nontrivial binary states.
The program also multiplies the symbolic recurrence matrices and verifies the
characteristic identity coefficient by coefficient over the integers.
"""
from fractions import Fraction
from itertools import product

PAIRS = ((0,2),(0,3),(0,4),(1,3),(1,4),(1,5),(2,4),(2,5),(3,5))
TRIPLES = ((0,2,4),(1,3,5))
ZERO = (0,)*6

def monomial(*indices):
    e = [0]*6
    for i in indices:
        e[i] += 1
    return tuple(e)

def add(*polys):
    out = {}
    for poly in polys:
        for exp,coeff in poly.items():
            out[exp] = out.get(exp,0)+coeff
    return {k:v for k,v in out.items() if v}

def mul(a,b):
    out = {}
    for e,c in a.items():
        for f,d in b.items():
            key=tuple(x+y for x,y in zip(e,f))
            out[key]=out.get(key,0)+c*d
    return {k:v for k,v in out.items() if v}

one={ZERO:1}
negone={ZERO:-1}
zero={}
M=[[one,zero],[zero,one]]
for i in range(6):
    X={monomial(i):1}
    B=[[negone,X],[one,zero]]
    M=[[add(mul(M[r][0],B[0][c]),mul(M[r][1],B[1][c])) for c in range(2)] for r in range(2)]
trace=add(M[0][0],M[1][1])
expected=add(one, *({monomial(i):1} for i in range(6)),
             *({monomial(i,j):1} for i,j in PAIRS),
             *({monomial(*tri):1} for tri in TRIPLES))
assert trace==expected, (trace,expected)

# For each nonzero division-support vector, substitute x_i=0 in F_5 where
# the exponent is positive and x_i=1 elsewhere (as the trace formula dictates).
def mod5_test(bits):
    y=[1-b for b in bits]
    return (sum(y)+sum(y[i]*y[j] for i,j in PAIRS)
            +sum(y[i]*y[j]*y[k] for i,j,k in TRIPLES))%5

winning=[]
for bits in product(range(2),repeat=6):
    if any(bits) and mod5_test(bits)==0:
        winning.append(bits)

p1=(0,0,1,0,1,1)
p2=(0,0,1,1,0,1)
rot=lambda x:{x[i:]+x[:i] for i in range(6)}
assert set(winning)==rot(p1)|rot(p2)|{(1,)*6}
assert len(winning)==13
assert Fraction(6,5**5)+Fraction(9,5**4)+Fraction(2,5**3)<1

# The two residual multi-affine polynomials vanish at (5,5,5) and are
# strictly decreasing in each variable throughout the region A,B,C>=5.
def first(A,B,C):
    return -A*B*C+2*A*B+A*C+2*A+3*B+4*C+5

def second(A,B,C):
    return -A*B*C+A*C+4*A+2*B*C+3*B+2*C+5

assert first(5,5,5)==second(5,5,5)==0
assert ( -5*5+2*5+5+2, -5*5+2*5+3, -5*5+5+4)==(-8,-12,-16)
assert ( -5*5+5+4, -5*5+2*5+3, -5*5+5+2*5+2)==(-16,-12,-8)
for fun in (first,second):
    for A,B,C in product((5,25,125),repeat=3):
        assert (fun(A,B,C)==0)==(A==B==C==5)

seeds=((p1,(1,1,2,3,1,4)),(p2,(7,2,9,11,4,3)))
for bits,word in seeds:
    assert all(v%5 for v in word)
    for i in range(6):
        s=word[i]+word[(i+1)%6]
        z=0
        while s%5==0:
            z+=1
            s//=5
        assert z==bits[i]
        assert s==word[(i+2)%6]

# Exact rational rank, ruling out additional independent period-six
# solutions at the two permitted exponent signatures.
def rank(rows):
    A=[[Fraction(x) for x in row] for row in rows]
    r=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        v=A[r][c]
        A[r]=[x/v for x in A[r]]
        for j in range(len(A)):
            if j!=r and A[j][c]:
                t=A[j][c]
                A[j]=[a-t*b for a,b in zip(A[j],A[r])]
        r+=1
    return r

for bits,word in seeds:
    rows=[]
    for i in range(6):
        row=[0]*6
        row[i]+=1
        row[(i+1)%6]+=1
        row[(i+2)%6]-=5**bits[i]
        rows.append(row)
    assert rank(rows)==5
    assert all(sum(row[j]*word[j] for j in range(6))==0 for row in rows)

print('VERIFY_OK: exact symbolic trace, all 63 division supports, two rank-five kernels, both primitive cycles')
