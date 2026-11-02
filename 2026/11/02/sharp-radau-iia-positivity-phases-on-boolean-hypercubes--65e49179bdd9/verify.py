#!/usr/bin/env python3
"""Exact arithmetic checks for two-stage Radau IIA positivity on Boolean cubes.

Only the Python standard library is required.
"""
from fractions import Fraction as F
from math import comb

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1] == 0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); z=[0]*n
    for i,v in enumerate(a): z[i]+=v
    for i,v in enumerate(b): z[i]+=v
    return trim(z)

def scale(a,c): return trim([c*x for x in a])

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return trim(z)

def prod(polys):
    p=[1]
    for q in polys:p=mul(p,q)
    return p

def evalp(a,x):
    y=0
    for v in reversed(a): y=y*x+v
    return y

def desc(*a):return list(reversed(a))

def factor(*arr):return prod(arr)

# Each pair (numerator, denominator) is an exact Hamming-distance kernel.
A=[3,4,2]; B=[1,4,6]; C=[3,8,8]; D=[3,16,32]; E=[3,20,50]
FORM={
 1:[(desc(1,1,3), A), (mul([0,1],[3,1]),A)],
 2:[(desc(4,2,17,18,9),mul(A,C)),
    (mul([0,1],[3,2]),C),
    (mul([0,0,1],desc(4,18,9)),mul(A,C))],
 3:[(desc(12,-14,22,83,98,45,9),mul(A,mul(B,C))),
    (mul([0,1],desc(12,42,92,95,45,9)),mul(A,mul(B,C))),
    (mul([0,0,1],desc(12,58,76,45,9)),mul(A,mul(B,C))),
    (scale(mul([0,0,0,1],desc(4,22,18,3)),3),mul(A,mul(B,C)))],
 4:[(desc(192,-848,-1300,168,2242,2216,1050,252,27),prod([A,B,C,D])),
    (mul([0,1],desc(24,50,168,163,60,9)),prod([A,B,D])),
    (mul([0,0,1],desc(16,36,9)),prod([C,D])),
    (scale(mul([0,0,0,1],desc(8,38,24,3)),3),prod([A,B,D])),
    (scale(mul([0,0,0,0,1],desc(32,200,210,60,3)),6),prod([A,B,C,D]))],
 5:[(desc(4800,-49040,-126924,-119100,-2890,78470,71146,31950,8325,1215,81),prod([A,B,C,D,E])),
    (mul([0,1],desc(4800,10480,45540,98956,114450,77674,32400,8298,1215,81)),prod([A,B,C,D,E])),
    (mul([0,0,1],desc(4800,22960,57676,79040,61358,28530,7884,1215,81)),prod([A,B,C,D,E])),
    (scale(mul([0,0,0,1],desc(1600,9360,17860,17504,9450,2850,450,27)),3),prod([A,B,C,D,E])),
    (scale(mul([0,0,0,0,1],desc(800,5160,7846,5250,1755,255,9)),6),prod([A,B,C,D,E])),
    (scale(mul([0,0,0,0,0,1],desc(160,1096,1350,510,45,-3)),30),prod([A,B,C,D,E]))]
}

def spectral_coeff(d,r,k):
    return sum((-1)**j*comb(r,j)*comb(d-r,k-j)
               for j in range(max(0,k-d+r),min(r,k)+1))

def raw_polynomials(d,r):
    q=[ [6,8*k,4*k*k] for k in range(d+1)]
    q[0]=[6]
    denominator=scale(prod(q),2**d)
    numerator=[0]
    for k in range(d+1):
        c=spectral_coeff(d,r,k)
        term=scale(mul([6,-4*k],prod(q[:k]+q[k+1:])),c)
        numerator=add(numerator,term)
    return numerator,denominator

for d in range(1,6):
    for r,(n,p) in enumerate(FORM[d]):
        N,Q=raw_polynomials(d,r)
        check(mul(N,p)==mul(n,Q),f'polynomial identity d={d} r={r}')
        check(evalp(p,F(1,2))>0, f'denominator d={d} r={r}')

# Non-diagonal numerators are coefficientwise positive after removing h^r,
# except the fifth-distance numerator, whose constant term is negative.
for d in range(1,6):
    for r,(n,_) in enumerate(FORM[d]):
        if r==0: continue
        check(n[:r]==[0]*r, f'zero order d={d} r={r}')
        if d==5 and r==5:
            check(n[r]<0 and all(x>0 for x in n[r+1:]),'fifth shell sign')
        else:
            check(all(x>0 for x in n[r:]),f'positive coefficients d={d} r={r}')

# Three-dimensional diagonal: h^4(12 h^2 - 14 h + 22) plus a positive remainder.
check((-14)**2-4*12*22<0,'positive quadratic')
# Exact positive-root counts follow from Descartes' rule plus sign witnesses.
def sign_changes(p):
    s=[1 if v>0 else -1 for v in reversed(p) if v]
    return sum(s[i]!=s[i+1] for i in range(len(s)-1))
q4=FORM[4][0][0]
q5=FORM[5][0][0]
g5=desc(160,1096,1350,510,45,-3)
check(sign_changes(q4)==2 and evalp(q4,0)>0 and evalp(q4,F(3,2))<0 and q4[-1]>0,'four-cube root count')
check(sign_changes(q5)==2 and evalp(q5,F(1,2))>0 and evalp(q5,F(3,2))<0 and q5[-1]>0,'five-cube root count')
check(sign_changes(g5)==1 and evalp(g5,0)<0 and evalp(g5,F(1,10))>0,'five-cube antipode root')
check(all(x>0 for x in g5[1:]),'antipodal polynomial strictly increasing')

# A distance-5 entry starts at -(5!)/108 * h^5 = -10/9*h^5.
coeff=[F(1),F(-1)]
for k in range(2,6):coeff.append(-(4*coeff[-1]+coeff[-2])/6)
check(coeff[5]==F(1,108),'order-five stability coefficient')
check(-120*coeff[5]==F(-10,9),'distance-five short-path obstruction')

# All high-dimensional cubes have a negative diagonal at h=3/2.
def r(z):return (F(6)-2*z)/(z*z+4*z+6)
S4=sum(comb(4,k)*(-r(F(3*k))) for k in range(2,5))
check(S4==F(463,451),'universal diagonal negative witness')
for d in range(4,15):
    value=sum(comb(d,k)*r(F(3*k)) for k in range(d+1))/2**d
    check(value<0,f'diagonal negativity in dimension {d}')

# Compare spectral entries with directly inverted endpoint matrices.
def invert(A):
    n=len(A)
    T=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if T[i][col])
        T[col],T[pivot]=T[pivot],T[col]
        v=T[col][col]
        T[col]=[z/v for z in T[col]]
        for i in range(n):
            if i==col: continue
            f=T[i][col]
            if f:T[i]=[a-f*b for a,b in zip(T[i],T[col])]
    return [row[n:] for row in T]

def endpoint(d,h):
    n=2**d
    L=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        L[i][i]=F(d)
        for k in range(d):L[i][i^(1<<k)]=-1
    LL=[[sum(L[i][k]*L[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    DD=[[(h*h*LL[i][j]+4*h*L[i][j]+6*(i==j)) for j in range(n)] for i in range(n)]
    inv=invert(DD)
    return [[sum((6*(i==k)-2*h*L[i][k])*inv[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def shell(d,r,h):
    return sum(F(spectral_coeff(d,r,k))*rfun(F(2*k)*h) for k in range(d+1))/2**d
rfun=r
for d in range(1,6):
    for h in ([F(1,10),F(1,2),F(3,2),F(6)] if d<=4 else [F(1,100),F(1,10),F(1),F(13)]):
        M=endpoint(d,h)
        for i in range(2**d):
            check(sum(M[i])==1,'row stochastic')
            for j in range(2**d):
                rr=(i^j).bit_count()
                v=shell(d,rr,h)
                check(M[i][j]==v,f'matrix versus Walsh spectrum d={d} h={h} r={rr}')

# Independent sampled positivity signs of the complete small-dimensional phase diagram.
for d in range(1,6):
    for i in range(1,401):
        h=F(i,100)
        for r in range(d+1):
            val=shell(d,r,h)
            if d<=3: check(val>0,f'unconditional positivity d={d}')
            if d==4 and r>0:check(val>0,'four-cube offdiagonal')
            if d==5 and r in range(1,5):check(val>0,'five-cube intermediate shells')
print(f'VERIFY_OK {checks} exact assertions')
