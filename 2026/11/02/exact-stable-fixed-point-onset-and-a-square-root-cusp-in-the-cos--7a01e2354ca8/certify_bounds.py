"""Exact rational alternating-series certificates for derivative inequalities used in the proof.
No floating-point arithmetic occurs in the tests.
"""
from fractions import Fraction as F
from math import factorial

def exp_negative(t):
    # exp(-t) alternating for 0<=t<=1; odd partial sum lower, even upper.
    def S(n): return sum(((-t)**k/F(factorial(k))) for k in range(n+1))
    return S(19),S(20)
def sin_partial(x,n): return sum((-1)**k*x**(2*k+1)/F(factorial(2*k+1)) for k in range(n+1))
def cos_partial(x,n): return sum((-1)**k*x**(2*k)/F(factorial(2*k)) for k in range(n+1))
def sin_bound(x):return sin_partial(x,9),sin_partial(x,8) # odd index lower
def cos_bound(x):return cos_partial(x,9),cos_partial(x,8)
def sinus(X):return sin_bound(X[0])[0],sin_bound(X[1])[1]
def cosinus(X):return cos_bound(X[1])[0],cos_bound(X[0])[1]
def add(X,Y):return X[0]+Y[0],X[1]+Y[1]
def sub(X,Y):return X[0]-Y[1],X[1]-Y[0]
def mul(X,Y):
    z=[a*b for a in X for b in Y]
    return min(z),max(z)
def div(X,Y):
    assert Y[0]>0
    return mul(X,(1/Y[1],1/Y[0]))
def bounds(q,L,U):return F(str(L))<q[0] and q[1]<F(str(U))
V=exp_negative(F(1))
W=exp_negative(F(2,5))
D=sub(cosinus(V),cosinus((F(1),F(1))))
hp0=div(mul(V,sinus(V)),D)
hp1=div(sinus((F(1),F(1))),D)
h6=div(sub(cosinus(V),cosinus(W)),D)
hp6=div(mul(W,sinus(W)),D)
assert bounds(D,'0.39278','0.39280')
assert bounds(hp0,'0.3368','0.3369')
assert bounds(hp1,'2.1422','2.1424')
assert h6[1]+F(3,5)<F('0.981')
assert hp6[0]>F('1.06')
print('PASS 5 exact-rational Taylor enclosure certificates')
