#!/usr/bin/env python3
"""Exact integer replay for the uncentered maximal graph-ball norm on C5."""
from itertools import product
from fractions import Fraction

N = 5

def row_options(v):
    sets = [(v,)]
    for center in ((v-1)%N,v,(v+1)%N):
        sets.append(tuple(sorted(((center-1)%N,center,(center+1)%N))))
    sets.append(tuple(range(N)))
    assert len(sets)==len(set(sets))==5
    return [tuple(15//len(s) if j in s else 0 for j in range(N)) for s in sets]

ROWS = [row_options(v) for v in range(N)]

def determinant(mat):
    a=[list(row) for row in mat]
    n=len(a)
    if not n: return 1
    sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]!=0),None)
            if j is None: return 0
            a[k],a[j]=a[j],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot - a[i][k]*a[k][j]
                assert num%prev==0,(num,prev,k)
                a[i][j]=num//prev
        for i in range(k+1,n): a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def gram(b):
    return [[sum(b[k][i]*b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def leading_positive(mat):
    return all(determinant([row[:k] for row in mat[:k]])>0 for k in range(1,N+1))

# threshold for the squared norm is exactly 5/3.  Since B=15A,
# lambda_max(A^T A)<5/3 iff 375 I-B^T B is positive definite.
exceptional=[]
for idx in product(range(5),repeat=N):
    b=[ROWS[v][idx[v]] for v in range(N)]
    g=gram(b)
    c=[[(375 if i==j else 0)-g[i][j] for j in range(N)] for i in range(N)]
    if not leading_positive(c): exceptional.append(idx)

EXPECTED={
    (3,0,1,1,3), (1,1,3,3,0), (3,3,0,1,1),
    (1,3,3,0,1), (0,1,1,3,3)
}
assert set(exceptional)==EXPECTED,exceptional
assert len(exceptional)==5

winning=[ROWS[v][(3,0,1,1,3)[v]] for v in range(N)]
assert winning==[
    (5,5,5,0,0),
    (0,15,0,0,0),
    (5,5,5,0,0),
    (0,5,5,5,0),
    (5,5,0,0,5)
]

def poly(z): return 81*z**3-171*z**2+62*z-4
assert poly(Fraction(1670,1000))<0<poly(Fraction(1671,1000))
assert poly(Fraction(5,3))<0
# Characteristic polynomial of H=(3A)^T(3A) is
# u(u-2)(u^3-19u^2+62u-36).
H=[[v//25 for v in r] for r in gram(winning)]
assert all(x%25==0 for r in gram(winning) for x in r)
# Five exact evaluations of the monic degree-5 characteristic polynomial.
def det_shift(u):
    return determinant([[(u if i==j else 0)-H[i][j] for j in range(N)] for i in range(N)])
for u in (0,1,2,5,10,20):
    assert det_shift(u)==u*(u-2)*(u**3-19*u**2+62*u-36)
# The cubic has just one root greater than 5/3 in the original z variable,
# because p'(z)=243z^2-342z+62>0 for z>=5/3.
assert 243*Fraction(5,3)**2-342*Fraction(5,3)+62>0
# Exact positive eigenvector formulas: x=(a,1,a,c,c) with
# a=(27z-2)/(81z^2-54z+4), c=(9z-2)/same.
# Verify row-selection inequalities using rational interval bounds on z.
lo,hi=Fraction(1670,1000),Fraction(1671,1000)
# Bounds derived from monotonic interval arithmetic.
def iv_add(A,B): return A[0]+B[0],A[1]+B[1]
def iv_sub(A,B): return A[0]-B[1],A[1]-B[0]
def iv_mul(A,B):
    p=[x*y for x in A for y in B]
    return min(p),max(p)
def iv_div(A,B):
    assert 0<B[0]
    return iv_mul(A,(1/B[1],1/B[0]))
Z=(lo,hi); ONE=(Fraction(1),Fraction(1))
den=iv_add(iv_sub(iv_mul((81,81),iv_mul(Z,Z)),iv_mul((54,54),Z)),(4,4))
a=iv_div(iv_sub(iv_mul((27,27),Z),(2,2)),den)
c=iv_div(iv_sub(iv_mul((9,9),Z),(2,2)),den)
x=[a,ONE,a,c,c]
for v in range(N):
    expected=(3,0,1,1,3)[v]
    ave_expected=(sum(ROWS[v][expected][i]*x[i][0] for i in range(N))/15,
                  sum(ROWS[v][expected][i]*x[i][1] for i in range(N))/15)
    for k in range(5):
        if k==expected: continue
        ave_comp=(sum(ROWS[v][k][i]*x[i][0] for i in range(N))/15,
                  sum(ROWS[v][k][i]*x[i][1] for i in range(N))/15)
        assert ave_expected[0]>ave_comp[1],(v,k,ave_expected,ave_comp)
print('CERTIFICATE_OK selections=3125 strict=3120 exceptional=5 characteristic=exact active=20')
