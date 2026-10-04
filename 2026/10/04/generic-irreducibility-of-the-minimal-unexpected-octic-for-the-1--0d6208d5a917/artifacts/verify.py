#!/usr/bin/env python3
from fractions import Fraction
from math import comb

Z = [
    (0,1,0),(-1,1,0),(-2,1,0),(-3,1,0),(-3,2,0),(4,0,-1),
    (1,1,-1),(2,1,-1),(3,1,-1),(4,1,-1),(0,2,-1),(1,2,-1),
    (2,2,-1),(0,3,-1),(1,3,-1),(-2,3,-1),(-1,3,-1),(-2,4,-1),
]
P0 = (3,5,1)
EXPS = [(i,j,8-i-j) for i in range(9) for j in range(9-i)]
COEFF = [
    24721200,-35757828,-6229440,8397081,-2639385,-560007,318465,1674,0,
    25893900,54701892,-32382945,17755605,2803185,-2045043,-187740,1962,
    -72137100,53528223,-50409975,-12675180,7395780,1206681,-2205,
    -14228375,32803715,44023000,-15659420,-3907645,-7259,
    3115000,-50208305,12756975,7884625,1225,
    13873475,-737709,-8905995,7973,-1136800,4904956,4340,-1122300,684,0,
]
A_EXPECT = {
    (7,0):-1118880,(6,1):4962720,(5,2):-8708280,(4,3):8028720,
    (3,4):-4074420,(2,5):1075200,(1,6):-132300,(0,7):7560,
}

def falling(n,r):
    out = 1
    for t in range(r):
        out *= n-t
    return out

def eval_form(point):
    x,y,z = point
    return sum(c*(x**i)*(y**j)*(z**k) for c,(i,j,k) in zip(COEFF,EXPS))

def interpolation_rows():
    rows=[]
    for x,y,z in Z:
        rows.append([(x**i)*(y**j)*(z**k) for i,j,k in EXPS])
    x0,y0,_ = P0
    for a in range(7):
        for b in range(7-a):
            row=[]
            for i,j,k in EXPS:
                if i<a or j<b:
                    row.append(0)
                else:
                    row.append(falling(i,a)*falling(j,b)*(x0**(i-a))*(y0**(j-b)))
            rows.append(row)
    return rows

def rank_mod(matrix,p):
    a=[[x%p for x in row] for row in matrix]
    n=len(a); m=len(a[0]); r=0
    for c in range(m):
        pivot=None
        for i in range(r,n):
            if a[i][c]:
                pivot=i; break
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c],p-2,p)
        a[r]=[(x*inv)%p for x in a[r]]
        for i in range(n):
            if i!=r and a[i][c]:
                q=a[i][c]
                a[i]=[(a[i][j]-q*a[r][j])%p for j in range(m)]
        r += 1
        if r==n:
            break
    return r

def add_poly(A,B):
    C=dict(A)
    for m,c in B.items():
        C[m]=C.get(m,0)+c
        if C[m]==0:
            del C[m]
    return C

def mul_poly(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            m=(i+k,j+l)
            C[m]=C.get(m,0)+a*b
    return {m:c for m,c in C.items() if c}

def linear(a,b):
    out={}
    if a: out[(1,0)]=a
    if b: out[(0,1)]=b
    return out

def translate():
    T={}
    for c,(i,j,k) in zip(COEFF,EXPS):
        if c==0:
            continue
        # z=1, x=3+u, y=5+v
        for a in range(i+1):
            cx=comb(i,a)*(3**(i-a))
            for b in range(j+1):
                cy=comb(j,b)*(5**(j-b))
                T[(a,b)] = T.get((a,b),0) + c*cx*cy
    return {m:c for m,c in T.items() if c}

def trim(P):
    P=list(P)
    while len(P)>1 and P[-1]==0:
        P.pop()
    return P

def divmod_q(A,B):
    A=trim([Fraction(x) for x in A]); B=trim([Fraction(x) for x in B])
    if len(B)==1 and B[0]==0:
        raise ZeroDivisionError
    Q=[Fraction(0)]*max(1,(len(A)-len(B)+1))
    while not (len(A)==1 and A[0]==0) and len(A)>=len(B):
        d=len(A)-len(B); q=A[-1]/B[-1]; Q[d]+=q
        for i,b in enumerate(B):
            A[d+i]-=q*b
        A=trim(A)
    return trim(Q),trim(A)

def gcd_q(A,B):
    A=trim([Fraction(x) for x in A]); B=trim([Fraction(x) for x in B])
    while not (len(B)==1 and B[0]==0):
        _,R=divmod_q(A,B); A,B=B,R
    lc=A[-1]
    return trim([x/lc for x in A])

assert len(EXPS)==45 and len(COEFF)==45
assert all(eval_form(p)==0 for p in Z)
rows=interpolation_rows()
assert len(rows)==46 and all(len(row)==45 for row in rows)
assert all(sum(a*b for a,b in zip(row,COEFF))==0 for row in rows)
for p in (1000003,1000033,10007,65537):
    assert rank_mod(rows,p)==44
    assert rank_mod(rows[:18],p)==18

T=translate()
degs={i+j for i,j in T}
assert degs=={7,8}
A={m:c for m,c in T.items() if sum(m)==7}
B={m:c for m,c in T.items() if sum(m)==8}
assert A==A_EXPECT

Bfac={(0,0):1}
for fac in [linear(1,0),linear(0,1),linear(1,1),linear(1,2),linear(1,3),linear(2,3),{(2,0):342,(1,1):-395,(0,2):109}]:
    Bfac=mul_poly(Bfac,fac)
assert B==Bfac

# Low-to-high univariate coefficients at v=1.
Au=[A.get((i,7-i),0) for i in range(8)]
Bu=[B.get((i,8-i),0) for i in range(9)]
g=gcd_q(Au,Bu)
assert len(g)==1 and g[0]==1
assert A.get((7,0),0)==-1118880
assert any(A.values())

print('VERIFY_OK')
