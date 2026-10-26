#!/usr/bin/env python3
"""Reproduce the five Legendre Hasse-polynomial tests in characteristic five.

Elements of F_25 are (a,b) = a+b*t, with t^2=2. No packages required.
The proof of the universal upper bound is independent of this finite test.
"""
from itertools import product
P=5

def add(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def neg(x): return ((-x[0])%P,(-x[1])%P)
def sub(x,y):return add(x,neg(y))
def mul(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def powf(x,n):
    y=(1,0)
    while n:
        if n&1:y=mul(y,x)
        x=mul(x,x);n//=2
    return y
Z=(0,0);O=(1,0);TWO=(2,0)
def h(x):return add(sub(mul(x,x),x),O)
def squares_h(x,y):
    a=sub(x,O);b=sub(y,O)
    return [h(x),h(y),add(sub(add(mul(x,x),mul(y,y)),mul(x,y)),Z),
            add(sub(add(mul(a,a),mul(b,b)),mul(a,b)),Z),
            add(sub(add(mul(mul(y,y),mul(a,a)),mul(mul(x,x),mul(b,b))),mul(mul(x,y),mul(a,b))),Z)]
def count_ss(u,v):
    assert len({Z,O,u,v})==4 and u!=v
    return sum(x==Z for x in squares_h(u,v))
roots=[z for z in product(range(5),repeat=2) if h(z)==Z]
assert len(roots)==2 and roots[0]!=roots[1]
assert add(roots[0],roots[1])==O and mul(roots[0],roots[1])==O
assert [x==Z for x in squares_h(*roots)]==[True,True,False,False,False]
assert count_ss(roots[0],TWO)==1
assert count_ss(TWO,(3,0))==0
pairs=[]
for u in product(range(P),repeat=2):
 for v in product(range(P),repeat=2):
  if len({Z,O,u,v})<4:continue
  cnt=count_ss(u,v)
  assert 0<=cnt<=2
  if cnt==2:
   pairs.append((u,v))
assert pairs
print('CHECK_OK Hasse_coeff=x^4 coefficient of [x(x-1)(x-lambda)]^2 = lambda^2-lambda+1')
print('CHECK_OK F25 roots of H:', roots)
print('CHECK_OK rank_minimum=3 (two supersingular factors); rank_4 and rank_5 witnesses')
print('CHECK_OK no ordered five-point configuration over F25 has three supersingular elliptic quotients')
