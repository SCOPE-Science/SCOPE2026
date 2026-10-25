#!/usr/bin/env python3
"""Exact, dependency-free checks of a planar quartic Cox witness."""
from fractions import Fraction

# A homogeneous polynomial in s,t, represented by monomial/exponent dictionary.
def mon(i,j,c=1):
    return {(i,j): int(c)} if c else {}
def add(a,b):
    r=a.copy()
    for k,v in b.items():r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v}
def neg(a):return {k:-v for k,v in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    r={}
    for (i,j),u in a.items():
        for (k,l),v in b.items():r[(i+k,j+l)]=r.get((i+k,j+l),0)+u*v
    return {k:v for k,v in r.items() if v}
def deriv(a,k):
    r={}
    for (i,j),u in a.items():
        if k==0 and i:r[(i-1,j)]=i*u
        if k==1 and j:r[(i,j-1)]=j*u
    return r
def coeffs(a,d):return [a.get((d-j,j),0) for j in range(d+1)]
def minor3(rows):
    a,b,c=rows
    return add(sub(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),
                   mul(a[1],sub(mul(b[0],c[2]),mul(b[2],c[0])))),
               mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))

def T(a,deg,m):
    c=coeffs(a,deg)
    return [[c[j-i] if 0<=j-i<=deg else 0 for j in range(m)] for i in range(m-deg)]

def rank(rows):
    a=[[Fraction(x) for x in row] for row in rows]
    ncol=len(a[0]); r=0
    for j in range(ncol):
        piv=next((i for i in range(r,len(a)) if a[i][j]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        q=a[r][j]
        for col in range(j,ncol):a[r][col]/=q
        for i in range(r+1,len(a)):
            f=a[i][j]
            if f:
                for col in range(j,ncol):a[i][col]-=f*a[r][col]
        r+=1
    return r

# Fixed-source class (4,2) tuple (u0,u1,v2,v3,w).
s2,t2=mon(2,0),mon(0,2)
w=add(s2,t2);v2=s2;v3=t2
u0=mul(w,v2)
u1=add(add(mon(3,1),mon(1,3)),mon(0,4))
q=[u0,u1,v2,v3,w]
assert coeffs(u0,4)==[1,0,1,0,0]
assert coeffs(u1,4)==[0,1,0,1,1]
assert coeffs(v2,2)==[1,0,0] and coeffs(v3,2)==[0,0,1]
# The first column below is -A_E, the last two are homogeneous derivatives.
psi=[[{},deriv(q[i],0),deriv(q[i],1)] for i in range(2)]
psi += [[q[i],deriv(q[i],0),deriv(q[i],1)] for i in (2,3)]
psi += [[neg(w),deriv(w,0),deriv(w,1)]]
D124=minor3([psi[j] for j in (1,2,4)])
D134=minor3([psi[j] for j in (1,3,4)])
A=add(add(add(add(mon(5,0),mon(3,2,2)),mon(2,3,4)),mon(1,4)),mon(0,5,2))
B=add(add(add(mon(4,0),mon(2,2,2)),mon(1,3,-2)),mon(0,4))
assert D124 == mul(mon(1,0,4),A)
assert D134 == mul(mon(0,2,-4),B)
# In the chart t!=0, the univariate gcd is 1, and at t=0 D124=4*s^6 is nonzero.
from fractions import Fraction as F
def trim(v):
    while v and v[-1]==0:v.pop()
    return v
def remainder(a,b):
    a=trim([F(x) for x in a]);b=trim([F(x) for x in b])
    while len(a)>=len(b):
        factor=a[-1]/b[-1]; k=len(a)-len(b)
        for i,c in enumerate(b):a[k+i]-=factor*c
        trim(a)
    return a
def gcdpoly(a,b):
    while b:a,b=b,remainder(a,b)
    return [u/a[-1] for u in a]
# A(s,1), B(s,1) coefficient vectors ascending in s.
assert gcdpoly([2,1,4,2,0,1],[1,-2,2,0,1]) == [F(1)]
# For rank of Theta_{O(-7)} use Iwasaki Appendix A, Eq. (A.1).
blocks=[]
for i,f in enumerate(q):
    deg=4 if i<2 else 2
    aa=[[0]*6 for _ in range(6-deg)] if i<2 else [[-v for v in row] if i==4 else row for row in T(f,deg,6)]
    bs=T(deriv(f,0),deg-1,5)
    cs=T(deriv(f,1),deg-1,5)
    blocks += [a+b+c for a,b,c in zip(aa,bs,cs)]
assert len(blocks)==16 and all(len(row)==16 for row in blocks)
assert rank(blocks)==14
print('VERIFY_OK: Cox regularity, two coprime immersion minors, 16x16 rank 14')
