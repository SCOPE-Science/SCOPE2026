#!/usr/bin/env python3
"""Exact characteristic-seven checks for the genus-ten elementary abelian triple cover.
Only Python's standard library is used. No external files or services are needed.
"""
from itertools import product
from math import comb
P=7

def add(A,B):
    C=dict(A)
    for k,v in B.items():
        C[k]=(C.get(k,0)+v)%P
    return {k:v for k,v in C.items() if v}

def mul(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            z=(i+k,j+l)
            C[z]=(C.get(z,0)+a*b)%P
    return {k:v for k,v in C.items() if v}

def powpoly(A,n):
    B={(0,0):1}
    for _ in range(n): B=mul(B,A)
    return B

X={(1,0):1}; Xm1={(1,0):1,(0,0):6}; Xmt={(1,0):1,(0,1):6}
FACTORS=(X,Xm1,Xmt)

def dimensions(a,j):
    total=sum(a)
    d=sum(z==2 for z in a) if j==2 else 0
    infinity=(-total)%3
    maxdegree=(j*total-(6 if infinity==0 else 4))//3
    return max(0,maxdegree-d+1),d

def calc_by_multiplication(a,j,d):
    F={(0,0):1}
    for i in range(3): F=mul(F,powpoly(FACTORS[i],2*j*a[i]+(j==2 and a[i]==2)))
    N=6+7*d
    return tuple(F.get((N,e),0) for e in range(15))

def calc_by_binomial(a,j,d):
    e=[2*j*a[i]+(j==2 and a[i]==2) for i in range(3)]
    N=6+7*d
    vals=[0]*15
    for u in range(e[1]+1):
        v=N-e[0]-u
        if 0<=v<=e[2]:
            deg=e[2]-v
            vals[deg]=(vals[deg]+comb(e[1],u)*(-1)**(e[1]-u)*comb(e[2],v)*(-1)**deg)%P
    return tuple(vals)

def poly(*coeff):
    return tuple((list(coeff)+[0]*15)[:15])

def convolve(A,B):
    out=[0]*15
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            if i+j<15:out[i+j]=(out[i+j]+a*b)%7
    return tuple(out)

A=poly(6,6,1)       # t^2-t-1
B=poly(6,1,1)       # t^2+t-1
C=poly(1,4,1)       # t^2-3t+1
neg=lambda x:tuple((-v)%7 for v in x)
t=poly(0,1);tm1=poly(6,1)
expected={
 ((0,1,1),2):neg(convolve(tm1,tm1)),
 ((1,0,1),2):neg(convolve(t,t)),
 ((1,1,0),2):poly(6),
 ((1,1,1),2):neg(convolve(convolve(t,t),convolve(tm1,tm1))),
 ((1,1,2),1):neg(A),((1,1,2),2):neg(A),
 ((1,2,1),1):B,((1,2,1),2):convolve(convolve(t,t),B),
 ((1,2,2),1):convolve(convolve(tm1,tm1),C),((1,2,2),2):C,
}

reps=[]; seen=set(); forms=[]
for a in product(range(3),repeat=3):
    if a==(0,0,0):continue
    opposite=tuple((-z)%3 for z in a)
    if a in seen or opposite in seen:continue
    seen.update((a,opposite))
    reps.append(a)
    for j in (1,2):
        dimension,d=dimensions(a,j)
        assert dimension in (0,1), (a,j,dimension)
        if dimension:
            via_expansion=calc_by_multiplication(a,j,d)
            via_comb=calc_by_binomial(a,j,d)
            assert via_expansion==via_comb, (a,j,via_expansion,via_comb)
            assert via_expansion==expected[(a,j)],(a,j,via_expansion,expected.get((a,j)))
            forms.append((a,j))
assert len(reps)==13 and len(forms)==10
assert set(forms)==set(expected)

# Euclidean polynomial arithmetic verifies irreducibility, pairwise gcds, and j-locus identity.
def strip(f):
    r=list(f)
    while len(r)>1 and r[-1]==0: r.pop()
    return r

def divrem(f,g):
    f=strip([v%7 for v in f]); g=strip([v%7 for v in g]); rem=f[:]
    while len(rem)>=len(g) and rem!=[0]:
        q=rem[-1]*pow(g[-1],-1,7)%7;shift=len(rem)-len(g)
        for i,v in enumerate(g):rem[i+shift]=(rem[i+shift]-q*v)%7
        rem=strip(rem)
    return rem

def gcd(f,g):
    f=strip(f);g=strip(g)
    while g!=[0]: f,g=g,divrem(f,g)
    inv=pow(f[-1],-1,7)
    return [(v*inv)%7 for v in f]
q=[list(A[:3]),list(B[:3]),list(C[:3])]
assert all(gcd(z,[0,1])==[1] and gcd(z,[6,1])==[1] for z in q)
assert all(gcd(q[i],q[j])==[1] for i in range(3) for j in range(i+1,3))
# x^7=x holds in F7 and irreducible quadratic divides x^49-x in F7[x].
def polymodmul(f,g,m):
    prod=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):prod[i+j]=(prod[i+j]+a*b)%7
    return divrem(prod,m)
def polymodpow(f,n,m):
    r=[1]
    while n:
        if n&1:r=polymodmul(r,f,m)
        f=polymodmul(f,f,m);n>>=1
    return r
for z in q:
    assert polymodpow([0,1],49,z)==[0,1]
    assert polymodpow([0,1],7,z)!=[0,1]

# 256(t^2-t+1)^3 - 4t^2(t-1)^2 = 4 A B C in F7[t].
D=poly(1,6,1)
L=convolve(poly(4),convolve(convolve(D,D),D))
R=convolve(poly(4),convolve(convolve(t,t),convolve(tm1,tm1)))
ABC=convolve(A,convolve(B,C))
assert tuple((x-y)%7 for x,y in zip(L,R)) == convolve(poly(4),ABC)

# The Hasse-Witt determinant equals t^6 (t-1)^6 (ABC)^2.
det=poly(1)
for qform in expected.values():det=convolve(det,qform)
t2=convolve(t,t)
t3=convolve(t2,t)
t6=convolve(t3,t3)
s2=convolve(tm1,tm1)
s3=convolve(s2,tm1)
s6=convolve(s3,s3)
canonical=convolve(convolve(t6,s6),convolve(ABC,ABC))
assert det==canonical, (det,canonical)
# The p-rank at any geometric parameter !=0,1 is 8 if ABC=0, else 10.
# Each root gives precisely 2 zero Cartier eigenlines.
assert [sum(1 for (aa,j) in forms if aa==a) for a in [(1,1,2),(1,2,1),(1,2,2)]]==[2,2,2]
print('VERIFY_OK: 13 character pairs, 10 holomorphic eigenlines, all ten Cartier scalars agree by two exact expansions.')
print('STRATA_OK: three disjoint separable quadratic divisors, six F49 parameters, ranks 8/10 and a-numbers 2/0.')
print('MODULI_OK: the exceptional locus is j=4, a single unordered branch-configuration class, with Hasse divisor multiplicity two.')
