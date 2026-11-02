#!/usr/bin/env python3
"""Exact finite-field and formal checks for the cyclic-5 genus-4 Hasse locus.
Python 3; standard library only.  All field coordinates use GF(7)[i]/(i^2+1).
"""
from itertools import product
from math import factorial
P=7

def add(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def neg(x): return ((-x[0])%P,(-x[1])%P)
def mul(x,y): return ((x[0]*y[0]-x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def powf(x,n):
    r=(1,0)
    while n:
        if n&1: r=mul(r,x)
        x=mul(x,x);n//=2
    return r
ZERO=(0,0); ONE=(1,0)
def c(n): return (n%7,0)
def coeff_poly(a):
    # Explicit multinomial expansion of (x^10+a*x^5+1)^3.
    out={}
    for h in range(4):
        for j in range(4-h):
            k=3-h-j
            m=factorial(3)//(factorial(h)*factorial(j)*factorial(k))
            degree=10*h+5*j
            out[degree]=add(out.get(degree,ZERO),mul(c(m),powf(a,j)))
    return out

def matrix(a):
    cf=coeff_poly(a)
    return [[cf.get(7*(i+1)-(j+1),ZERO) for j in range(4)] for i in range(4)]

def matmul(A,B):
    return [[sumf(mul(A[i][k],B[k][j]) for k in range(4)) for j in range(4)] for i in range(4)]
def sumf(xs):
    acc=ZERO
    for x in xs: acc=add(acc,x)
    return acc

def rank(A):
    A=[list(row) for row in A]
    rr=0
    for j in range(len(A[0])):
        p=next((i for i in range(rr,len(A)) if A[i][j]!=ZERO),None)
        if p is None: continue
        A[p],A[rr]=A[rr],A[p]
        pivot=powf(A[rr][j],47) # a^-1 in F49*
        A[rr]=[mul(x,pivot) for x in A[rr]]
        for i in range(len(A)):
            if i==rr:continue
            t=A[i][j]
            A[i]=[add(A[i][k], neg(mul(t,A[rr][k]))) for k in range(len(A[0]))]
        rr+=1
        if rr==len(A):break
    return rr

def determinant(A):
    from itertools import permutations
    ans=ZERO
    for perm in permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        prod=ONE
        for i,j in enumerate(perm): prod=mul(prod,A[i][j])
        ans=add(ans,neg(prod) if inv%2 else prod)
    return ans

# Independent combinatorial coefficient check via the claimed sparse formula.
for ab in product(range(P),repeat=2):
    a=ab
    a2=mul(a,a)
    A=matrix(a)
    u=mul(c(3),a)
    v=mul(c(3),add(a2,ONE))
    assert A==[[ZERO,u,ZERO,ZERO],[ZERO,ZERO,ZERO,v],[v,ZERO,ZERO,ZERO],[ZERO,ZERO,u,ZERO]]
    predicted=neg(mul(mul(u,u),mul(v,v)))
    assert determinant(A)==predicted
    if a==(2,0) or a==(5,0):continue # singular fibers
    exceptional=(a==ZERO or add(a2,ONE)==ZERO)
    assert rank(A)==(2 if exceptional else 4)
    A7=[[powf(x,7) for x in row] for row in A]
    rank_stable=rank(matmul(A,A7))
    assert rank_stable==(0 if exceptional else 4)
print('FORMAL_CARTIER_PATTERN_OK: four-cycle with weights 3a and 3(a^2+1)')
print('FORMAL_HASSE_OK: determinant = -81a^2(a^2+1)^2 = 3a^2(a^2+1)^2 (mod 7)')
print('FORMAL_NILPOTENCE_OK: Cartier x Frobenius-twisted Cartier vanishes at every determinant root')
ordinary=exceptional_count=0
for a in product(range(P),repeat=2):
    if a in ((2,0),(5,0)):continue
    ex=(a==ZERO or add(mul(a,a),ONE)==ZERO)
    ordinary+=not ex
    exceptional_count+=ex
assert (ordinary,exceptional_count)==(44,3)
print('GF49_SMOOTH_FIBERS_OK: 44 ordinary, 3 exceptional of p-rank 0 and a-number 2')
# elementary correctness of invariant quotient rational function: in Laurent ring x+1/x=u,
# (x+1)^2/x=u+2; (x-1)^2/x=u-2; x^5+x^-5=u^5-5u^3+5u.
# Recurrence T_0=2, T_1=u, T_n=u*T_{n-1}-T_{n-2}.
T0=[2]; T1=[0,1]
def pmul_u(P): return [0]+P
def psub(P,Q):
    R=[0]*max(len(P),len(Q))
    for i,x in enumerate(P):R[i]+=x
    for i,x in enumerate(Q):R[i]-=x
    return R
for k in range(2,6):T0,T1=T1,psub(pmul_u(T1),T0)
assert T1==[0,5,0,-5,0,1]
print('INVOLUTION_QUOTIENT_OK: genus-two quotients v^2=(u+2)(u^5-5u^3+5u+a), w^2=(u-2)(u^5-5u^3+5u+a)')
print('VERIFY_OK')
