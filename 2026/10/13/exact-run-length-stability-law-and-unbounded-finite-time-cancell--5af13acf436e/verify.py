#!/usr/bin/env python3
"""Standalone checks for the deterministic periodically delayed scalar recurrence."""
from itertools import product
import sympy as S

t=S.symbols('t',real=True)
T0=S.Matrix([[1-t,0],[1,0]])
T1=S.Matrix([[1,-t],[1,0]])

def p(L):
    a,b=1-t,1-2*t
    if L==0: return a
    if L==1: return b
    for k in range(2,L+1):
        a,b=b,S.expand(b-t*a)
    return b

def monodromy(word):
    M=S.eye(2)
    for x in word:
        M=(T0 if x==0 else T1)*M
    return M

def cyclic_run_lengths(word):
    n=len(word)
    zeros=[j for j,v in enumerate(word) if v==0]
    assert zeros
    if len(zeros)==1: return [n-1]
    return [ (zeros[(i+1)%len(zeros)]-z-1)%n for i,z in enumerate(zeros)]

count=0
for n in range(1,9):
    for word in product((0,1),repeat=n):
        if 0 not in word: continue
        M=monodromy(word)
        expected=S.prod(p(L) for L in cyclic_run_lengths(word))
        assert S.expand(S.trace(M)-expected)==0
        assert S.expand(M.det())==0
        count+=1
assert count==502

for L in range(0,9):
    m=L+2
    A=S.zeros(m)
    for j in range(m-1):
        A[j,j+1]=A[j+1,j]=1
    u=S.symbols('u')
    # This determinant has only even powers and equals p_L(u^2).
    det=S.expand((S.eye(m)-u*A).det())
    assert S.expand(det-p(L).subs(t,u*u))==0
    roots=[1/(4*S.cos(S.pi*j/(L+3))**2) for j in range(1,(L+2)//2+1)]
    reconstructed=S.prod((1-t/r) for r in roots)
    assert all(abs(complex(S.N(c,30)))<1e-9 for c in S.Poly(S.expand(reconstructed)-p(L),t).all_coeffs())

assert p(2)==t*t-3*t+1
big=(3+S.sqrt(5))/2
M=T1*T1*T0
assert S.simplify(M.subs(t,big)**2)==S.zeros(2)
assert p(2).subs(t,S.Rational(5,2))==-S.Rational(1,4)
assert p(2).subs(t,S.Rational(3,2))==-S.Rational(5,4)
print('VERIFY_OK 502 exact periodic words, 9 path determinants/root products, and exact nilpotence')
