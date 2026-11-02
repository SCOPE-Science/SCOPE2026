#!/usr/bin/env python3
"""Exact, standalone finite-field and symbolic checks for a symmetric plane sextic.

Only Python's standard library is required. The proof of the universal
geometric claims is supplied in RESULT.md; this program checks critical
coefficient and rank calculations, not the validity of the cited general
Hasse--Witt formula.
"""
from math import factorial

P=5
# Coefficients of the six monomials of f_t in order.
MONOMIALS=[(6,0,0),(0,6,0),(0,0,6),(3,3,0),(0,3,3),(3,0,3)]
BASIS=[(i,j,6-i-j) for i in range(1,5) for j in range(1,6-i) if 6-i-j>=1]
assert len(BASIS)==10


def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for i in range(n+1):
            for suffix in compositions(n-i,k-1):
                yield (i,)+suffix


def poly_add(a,b):
    r=[0]*max(len(a),len(b))
    for i,x in enumerate(a):r[i]=(r[i]+x)%P
    for i,x in enumerate(b):r[i]=(r[i]+x)%P
    return tuple(r)


def poly_mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]=(r[i+j]+x*y)%P
    return tuple(r)


def trunc(a,n=5):
    return tuple((list(a)+[0]*n)[:n])


# Expand f_t^4 by the multinomial theorem, collecting all coefficients
# as polynomials in the indeterminate t over F_5.
COEFF={}
for counts in compositions(4,6):
    exp=tuple(sum(counts[i]*MONOMIALS[i][j] for i in range(6)) for j in range(3))
    k=sum(counts[3:])
    den=1
    for count in counts:
        den *= factorial(count)
    scalar=(factorial(4)//den)%P
    coeff=list(COEFF.get(exp,(0,)*5))
    coeff[k]=(coeff[k]+scalar)%P
    COEFF[exp]=tuple(coeff)

M=[]
for i in BASIS:
    row=[]
    for j in BASIS:
        exp=tuple(5*i[z]-j[z] for z in range(3))
        row.append(COEFF.get(exp,(0,)*5))
    M.append(row)

# All entries are determined symbolically, not by finite-field sampling.
# A=-t(t-2)^2(t+2), B=2t(t+2), D=2t(t-2)^3 in F_5[t].
A=trunc(poly_mul((0,-1),poly_mul(poly_mul((-2,1),(-2,1)),(2,1))))
B=trunc(poly_mul((0,2),(2,1)))
D=trunc(poly_mul((0,2),poly_mul((-2,1),poly_mul((-2,1),(-2,1)))))
ZERO=(0,)*5
EXPECTED=[[ZERO for _ in range(10)] for _ in range(10)]
for i,j in [(1,4),(4,1),(2,6),(6,2),(7,8),(8,7)]: EXPECTED[i][j]=A
for i in (0,3,9): EXPECTED[i][5]=B
for j in (0,3,9): EXPECTED[5][j]=D
assert M==EXPECTED, 'symbolic Hasse coefficient matrix does not match'
assert A==(0,2,4,2,4),A
assert B==(0,4,2,0,0),B
assert D==(0,4,4,3,2),D

# F_25 = F_5[s]/(s^2+2), s^2=3 (3 is a nonsquare in F_5).
ZERO25=(0,0); ONE25=(1,0)
def add(a,b):return ((a[0]+b[0])%5,(a[1]+b[1])%5)
def neg(a):return ((-a[0])%5,(-a[1])%5)
def mul(a,b):return ((a[0]*b[0]+3*a[1]*b[1])%5,(a[0]*b[1]+a[1]*b[0])%5)
def power(a,n):
    z=ONE25
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z

def evaluation(poly,a):
    z=ZERO25
    for coeff in reversed(poly):z=add(mul(z,a),(coeff%5,0))
    return z


def rank(matrix):
    R=[[v for v in row] for row in matrix]
    nr=len(R); nc=len(R[0]); pivot=0
    for j in range(nc):
        nxt=next((i for i in range(pivot,nr) if R[i][j]!=ZERO25),None)
        if nxt is None:continue
        R[pivot],R[nxt]=R[nxt],R[pivot]
        inv=power(R[pivot][j],23)
        assert mul(R[pivot][j],inv)==ONE25
        R[pivot]=[mul(a,inv) for a in R[pivot]]
        for i in range(nr):
            if i==pivot:continue
            q=R[i][j]
            if q!=ZERO25:
                R[i]=[add(u,neg(mul(q,v))) for u,v in zip(R[i],R[pivot])]
        pivot+=1
        if pivot==nr:break
    return pivot


def matrix_mul(U,V):
    return [[sum25(mul(U[i][k],V[k][j]) for k in range(len(V))) for j in range(len(V[0]))] for i in range(len(U))]

def sum25(values):
    s=ZERO25
    for v in values:s=add(s,v)
    return s

vals=[]
for aa in range(5):
  for bb in range(5):
    t=(aa,bb)
    if t in [(2,0),(3,0),(4,0)]:continue # singular fibers
    T=[[evaluation(x,t) for x in row] for row in M]
    target=0 if t==ZERO25 else 8
    assert rank(T)==target,(t,'Hasse rank',rank(T),target)
    # Frobenius linearization. The Hasse matrix is the transpose of M;
    # since all entries are in the same invariant blocks, stable ranks agree.
    comp=T
    for k in range(1,5):
        # compose with the p^k twist, testing stable rank of semilinear Frobenius.
        twisted=[[power(x,5**k) for x in row] for row in T]
        comp=matrix_mul(comp,twisted)
        assert rank(comp)==target,(t,k,rank(comp),target)
    vals.append(t)
assert len(vals)==22
print('SYMMETRIC_SEXTIC_CHAR5_HASSE_AND_STABLE_RANK_ALL_F25_SMOOTH_PARAMETERS_PASS')
print('symbolic matrix: six A entries, three B entries, three D entries')
print('A=-t(t-2)^2(t+2), B=2t(t+2), D=2t(t-2)^3')
print('22 smooth F_25 parameters: 1 zero Hasse matrix and 21 stable rank-8 matrices')
