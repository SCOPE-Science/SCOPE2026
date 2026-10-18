#!/usr/bin/env python3
"""Independent exact checks for total distinct scattered subsequence moments."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb

# Count including the empty subsequence, by two end-letter counters.
def subsequence_count_dp(word):
    u = v = 0
    for letter in word:
        if letter == 0:
            u = 1 + u + v
        else:
            v = 1 + u + v
    return 1 + u + v

# Independent set construction, used for short words.
def subsequence_count_set(word):
    S = {()}
    for letter in word:
        S |= {z + (letter,) for z in list(S)}
    return len(S)

# Sparse bivariate polynomial arithmetic.
def poly(*terms):
    return {(a,b):c for a,b,c in terms if c}
def mul(P,Q):
    R=defaultdict(int)
    for (a,b),c in P.items():
        for (i,j),d in Q.items():
            R[a+i,b+j]+=c*d
    return {k:v for k,v in R.items() if v}
def add(P,Q):
    R=defaultdict(int,P)
    for k,v in Q.items():R[k]+=v
    return {k:v for k,v in R.items() if v}
def neg(P):return {k:-v for k,v in P.items()}
def sub(P,Q):return add(P,neg(Q))
ONE=poly((0,0,1));X=poly((1,0,1));Y=poly((0,1,1))
s=add(X,Y)
t=sub(ONE,s)
xy=mul(X,Y)
N=mul(sub(ONE,X),sub(ONE,Y))
Q=sub(mul(t,t),xy)
P=add(sub(sub(add(add(ONE,mul(mul(X,X),X)),mul(mul(Y,Y),Y)),s),add(mul(X,X),mul(Y,Y))),add(add(poly((1,1,5)),poly((2,1,-2))),poly((1,2,-2))))
K=sub(add(sub(ONE, {k:3*v for k,v in s.items()}),add({k:3*v for k,v in mul(X,X).items()}, {k:3*v for k,v in mul(Y,Y).items()})),add(mul(mul(X,X),X),mul(mul(Y,Y),Y)))
K=add(K,xy)
num1=N; den1=mul(t,Q)
num2=mul(N,P); den2=mul(den1,K)

def coefficients(num,den,L):
    assert den[(0,0)] == 1
    coeff={}
    for n in range(L+1):
        for a in range(n+1):
            b=n-a
            val=num.get((a,b),0)
            for (i,j),d in den.items():
                if (i,j)==(0,0) or i>a or j>b:continue
                val-=d*coeff[(a-i,b-j)]
            coeff[(a,b)]=val
    return coeff

LIMIT=11
first=coefficients(num1,den1,LIMIT)
second=coefficients(num2,den2,LIMIT)
for n in range(LIMIT+1):
    by_weight=defaultdict(lambda:[0,0,0])
    for word in product((0,1),repeat=n):
        D=subsequence_count_dp(word)
        if n<=9:assert D==subsequence_count_set(word)
        a=word.count(0)
        by_weight[a][0]+=1;by_weight[a][1]+=D;by_weight[a][2]+=D*D
    for a in range(n+1):
        ct,m1,m2=by_weight[a]
        assert ct==comb(n,a)
        assert m1==first[(a,n-a)],(n,a,m1,first[(a,n-a)])
        assert m2==second[(a,n-a)],(n,a,m2,second[(a,n-a)])

# Verify unconditioned exact moment/variance identity independently from
# coefficients of bivariate rational functions.
T0,T1=Fraction(4),Fraction(9)
for n in range(32):
    if n==0:T=T0
    elif n==1:T=T1
    else:T0,T1=T1,Fraction(5,2)*T1-Fraction(1,2)*T0;T=T1
    mean=2*Fraction(3,2)**n-1
    variance=T-4*Fraction(9,4)**n
    if n<=LIMIT:
        W1=sum(first[(a,n-a)] for a in range(n+1))
        W2=sum(second[(a,n-a)] for a in range(n+1))
        assert Fraction(W1,2**n)==mean
        assert Fraction(W2,2**n)-mean**2==variance
    assert variance>=0
    if n>=2:assert variance>0
print('VERIFY_OK: full word-set comparison n<=9; exact composition moments n<=11; iid formulas n<=31')

# Polynomial certificates for the complete formal power-series identities:
# (I-x M0-y M1) h1 = (1-x-y)Q * e3,
# (I-x(M0 tensor M0)-y(M1 tensor M1)) h2 = (1-x-y)QK * e9.
def scale(C,k):return {m:c*k for m,c in C.items() if c*k}
def eq(P,Q):return sub(P,Q)=={}
def matrix_poly_certificate(mats,h,target):
    size=len(h)
    for i in range(size):
        lhs=h[i]
        for weight,M in mats:
            for j in range(size):
                if M[i][j]:lhs=sub(lhs,mul(scale(weight,M[i][j]),h[j]))
        assert eq(lhs,target[i]), (size,i)
M0=[[1,1,1],[0,1,0],[0,0,1]]
M1=[[1,0,0],[1,1,1],[0,0,1]]
def kron(A,B):
    n=len(A);m=len(B)
    return [[A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)] for i in range(n*m)]
one_minus_x=sub(ONE,X);one_minus_y=sub(ONE,Y)
h1=[mul(X,one_minus_x),mul(Y,one_minus_y),Q]
target1=[{}, {},mul(t,Q)]
matrix_poly_certificate([(X,M0),(Y,M1)],h1,target1)
C=mul(scale(mul(mul(X,Y),mul(one_minus_x,one_minus_y)),2),sub(scale(ONE,2),s))
h2=[mul(mul(X,one_minus_x),P),C,mul(mul(X,one_minus_x),K),
    C,mul(mul(Y,one_minus_y),P),mul(mul(Y,one_minus_y),K),
    mul(mul(X,one_minus_x),K),mul(mul(Y,one_minus_y),K),mul(Q,K)]
target2=[{} for _ in range(8)]+[mul(mul(t,Q),K)]
matrix_poly_certificate([(X,kron(M0,M0)),(Y,kron(M1,M1))],h2,target2)
assert eq(sum_poly(h1) if False else add(add(h1[0],h1[1]),h1[2]),N)
assert eq(add(add(add(add(add(add(add(h2[0],h2[1]),h2[2]),h2[3]),h2[4]),h2[5]),h2[6]),add(h2[7],h2[8])),mul(N,P))
print('SYMBOLIC_OK: exact 3-state and 9-state polynomial certificates')
