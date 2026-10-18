#!/usr/bin/env python3
"""Exact finite-field certificate for quadratic Waring spans over F_3.

Reproducible using Python 3 standard library only: python VERIFY.py
"""
from collections import Counter
from itertools import combinations, product

F = 3
MON = [(i, j) for i in range(4) for j in range(i, 4)]
assert len(MON) == 10

# Coefficients of the four outputs of (a+bt+ct^2+dt^3)^2 mod t^4.
TARGET = [
    (1,0,0,0,0,0,0,0,0,0),
    (0,2,0,0,0,0,0,0,0,0),
    (0,0,2,0,1,0,0,0,0,0),
    (0,0,0,2,0,2,0,0,0,0),
]

def rref(rows, width):
    """Deterministic reduced row-echelon form over F_3."""
    z = [list(row) for row in rows]
    for row in z:
        assert len(row) == width
    pivots, lead = [], 0
    for col in range(width):
        k = next((j for j in range(lead, len(z)) if z[j][col]), None)
        if k is None:
            continue
        z[lead], z[k] = z[k], z[lead]
        if z[lead][col] == 2:
            z[lead] = [2 * a % 3 for a in z[lead]]
        for j in range(len(z)):
            if j != lead and z[j][col]:
                b = z[j][col]
                z[j] = [(x-b*y) % 3 for x,y in zip(z[j], z[lead])]
        pivots.append(col)
        lead += 1
        if lead == len(z):
            break
    return tuple(tuple(row) for row in z[:lead]), tuple(pivots)

def rank(rows, width):
    return len(rref(rows, width)[0])

sred, spiv = rref(TARGET, 10)
assert spiv == (0, 1, 2, 3) and rank(TARGET, 10) == 4
free = tuple(j for j in range(10) if j not in spiv)
assert len(free) == 6

def quotient(q):
    """Coordinates in Q=Sym^2(F_3^4)^*/span(TARGET)."""
    q = list(q)
    for row, pivot in zip(sred, spiv):
        b = q[pivot]
        if b:
            q = [(u-b*v) % 3 for u,v in zip(q, row)]
    return tuple(q[j] for j in free)

squares = []
for coeff in product(range(F), repeat=4):
    if not any(coeff) or next(v for v in coeff if v) != 1:
        continue
    q = tuple(coeff[i] * coeff[j] * (1 if i == j else 2) % F
              for i,j in MON)
    squares.append((coeff,q,quotient(q)))
assert len(squares) == (3**4-1)//(3-1) == 40

# An eight-square witness.  The four outputs are given in COEFF below.
FORMS = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
         (1,1,0,0),(1,0,1,0),(1,0,0,1),(0,1,1,0)]
COEFF = [
    (1,0,0,0,0,0,0,0),
    (2,2,0,0,1,0,0,0),
    (2,1,2,0,0,1,0,0),
    (2,2,2,2,0,0,1,1),
]
vecs = [next(q for v,q,u in squares if v == x) for x in FORMS]
assert rank(vecs,10) == 8
for t,c in zip(TARGET,COEFF):
    assert all(sum(c[k]*vecs[k][i] for k in range(8)) % 3 == t[i]
               for i in range(10))
for a,b,c,d in product(range(3),repeat=4):
    x=(a,b,c,d)
    lhs=(a*a,2*a*b,b*b+2*a*c,2*a*d+2*b*c)
    rhs=tuple(sum(COEFF[j][k] * (sum(FORMS[k][i]*x[i] for i in range(4))**2)
                  for k in range(8)) % 3 for j in range(4))
    assert tuple(t%3 for t in lhs)==rhs


def echelon_subspaces(k,dim=6):
    """Enumerate each k-plane in F_3^dim exactly once by RREF basis."""
    for piv in combinations(range(dim), k):
        freeplaces=[(i,j) for i in range(k)
                    for j in range(piv[i]+1,dim) if j not in piv]
        for vals in product(range(F),repeat=len(freeplaces)):
            B=[[0]*dim for _ in range(k)]
            for i,j in enumerate(piv):B[i][j]=1
            for (i,j),v in zip(freeplaces,vals):B[i][j]=v
            yield tuple(tuple(row) for row in B)


def gaussian(n,k,q=3):
    numerator=denominator=1
    for i in range(k):
        numerator *= q**(n-i)-1
        denominator *= q**(k-i)-1
    assert numerator%denominator==0
    return numerator//denominator

def contained_in_rowspan(v, basis):
    return rank(basis+(v,),6)==len(basis)

# Lower bound: if <=7 squares span all 4 target quadrics, their images
# in the six-dimensional quotient lie in some three-plane.  For every
# such three-plane, compute the dimension of their span intersect TARGET.
hist3=Counter()
count3=0
for B in echelon_subspaces(3):
    count3+=1
    contained=[q for _,q,u in squares if contained_in_rowspan(u,B)]
    quotient_part=[u for _,q,u in squares if contained_in_rowspan(u,B)]
    intersection=rank(contained,10)-rank(quotient_part,6)
    assert 0 <= intersection <= 4
    hist3[intersection]+=1
assert count3==gaussian(6,3)==33880
assert hist3 == {1:31905, 2:1830, 3:145}
assert max(hist3)<4

# Optimal 8-dimensional support spaces E containing TARGET correspond
# uniquely to four-planes W of Q via E=pi^{-1}(W).  Enumerate W as
# kernels of all RREF two-planes of linear conditions on Q.
count4=0
optimal=Counter()
for normal_basis in echelon_subspaces(2):
    count4+=1
    contained=[q for _,q,u in squares if
               all(sum(ui*ni for ui,ni in zip(u,normal)) % 3 == 0
                   for normal in normal_basis)]
    if rank(contained,10)==8:
        assert rank([quotient(q) for q in contained],6)==4
        optimal[len(contained)]+=1
assert count4==gaussian(6,2)==11011
assert optimal == {10:243,16:9}
assert sum(optimal.values())==252
print('VERIFY_OK: rank=8, 40 projective squares, '
      '33880 three-planes, 11011 four-planes, '
      '252 optimal support spaces (243 with 10 squares, 9 with 16)')
