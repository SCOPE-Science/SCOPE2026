#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

# a+b*w with w^2+w+1=0
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)
def scale(q,x): return (q*x[0],q*x[1])
def neg(x): return (-x[0],-x[1])
def eq0(x): return x==(Fraction(0),Fraction(0))
ONE=(Fraction(1),Fraction(0)); W=(Fraction(0),Fraction(1)); W2=(-Fraction(1),-Fraction(1))
roots=[ONE,W,W2]
def evalp(coef,X,Y):
    a,b,c,e=coef
    return add(add(add(a,mul(b,X)),mul(c,mul(X,X))),mul(e,Y))
def zeros(coef):
    return [(i,j) for i,X in enumerate(roots) for j,Y in enumerate(roots) if eq0(evalp(coef,X,Y))]
Q=Fraction
witnesses=[
 (ONE,ONE,ONE,ONE),
 (ONE,ONE,ONE,(Q(-3),Q(0))),
 ((Q(1,3),Q(0)), scale(Q(4,3),W), scale(Q(4,3),W2), ONE),
 (scale(Q(1,3),add((Q(-2),Q(0)),neg(W))), scale(Q(1,3),add(ONE,scale(Q(2),W))), scale(Q(1,3),add((Q(-2),Q(0)),neg(W))), ONE)
]
for expected,c in enumerate(witnesses):
    assert all(not eq0(z) for z in c)
    z=zeros(c)
    assert len(z)==expected,(expected,z)
    print(f'witness_zero_count={expected} zeros={z}')
# Any 4 grid points have two with the same X-coordinate (3 rows only).
grid=list(range(9))
for S in combinations(grid,4):
    rows=[s//3 for s in S]
    assert len(set(rows))<4
print('four_zero_row_obstruction=126/126')
print('VERIFY_OK')
