#!/usr/bin/env python3
"""Independent finite-field checks for a graded quadratic-multiplication theorem."""
from itertools import product
from math import comb
from collections import Counter
import random

def add(a,b,q):
    if q==3:return (a+b)%3
    return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def neg(a,q):
    if q==3:return (-a)%3
    return (-(a%3))%3+3*((-(a//3))%3)
def mul(a,b,q):
    if q==3:return a*b%3
    aa,ab=a%3,a//3;ba,bb=b%3,b//3
    return (aa*ba+2*ab*bb)%3+3*((aa*bb+ab*ba)%3)
def inv(a,q):
    if q==3:return pow(a,1,3)
    for b in range(1,9):
        if mul(a,b,9)==1:return b
    raise ZeroDivisionError

def rref_rank(mat,q):
    if not mat:return 0
    aa=[row[:] for row in mat]; R=len(aa);C=len(aa[0]);r=0
    for j in range(C):
        k=next((k for k in range(r,R) if aa[k][j]),None)
        if k is None:continue
        aa[r],aa[k]=aa[k],aa[r]
        t=inv(aa[r][j],q)
        aa[r][j:]=[mul(t,x,q) for x in aa[r][j:]]
        for k in range(r+1,R):
            s=aa[k][j]
            if s:
                aa[k][j:]=[add(a,neg(mul(s,b,q),q),q) for a,b in zip(aa[k][j:],aa[r][j:])]
        r+=1
        if r==R:break
    return r

def polynomial_mul(A,B,n,q):
    out={}
    for a,ca in A.items():
        for b,cb in B.items():
            z=tuple(x+y for x,y in zip(a,b))
            if max(z)>=3:continue
            out[z]=add(out.get(z,0),mul(ca,cb,q),q)
    return {k:v for k,v in out.items() if v}

def monoms(n):
    m=list(product(range(3),repeat=n))
    return [[a for a in m if sum(a)==d] for d in range(2*n+1)]

def operator_ranks(Q,n,q,ms):
    square=polynomial_mul(Q,Q,n,q)
    a={};b={}
    for power,P,target in [(2,Q,a),(4,square,b)]:
        for d in range(2*n+1):
            if d+power>2*n:target[d]=0;continue
            src=ms[d];dst=ms[d+power]; di={z:i for i,z in enumerate(dst)}
            M=[[0]*len(src) for _ in dst]
            for j,z in enumerate(src):
                for exponent,coef in P.items():
                    zz=tuple(z[k]+exponent[k] for k in range(n))
                    if max(zz)<3:
                        M[di[zz]][j]=add(M[di[zz]][j],coef,q)
            target[d]=rref_rank(M,q)
    return a,b

def graded_strings_from_ranks(a,b,ms,n):
    p1={};p2={};p3={}
    for d in range(2*n+1):
        p3[d]=b[d]
        p2[d]=a[d]-p3[d]-p3.get(d-2,0)
        p1[d]=len(ms[d])-p2[d]-p2.get(d-2,0)-p3[d]-p3.get(d-2,0)-p3.get(d-4,0)
    return [{d:v for d,v in p.items() if v} for p in (p1,p2,p3)]

def shiftmul(X,Y):
    z={}
    for i,a in X.items():
        for j,b in Y.items():z[i+j]=z.get(i+j,0)+a*b
    return {k:v for k,v in z.items() if v}

def addpoly(*Xs):
    Z={}
    for X in Xs:
        for i,a in X.items():Z[i]=Z.get(i,0)+a
    return {k:v for k,v in Z.items() if v}

def expected_strings(n,r):
    if r==0:
        p={0:1}
        for _ in range(n):p=shiftmul(p,{0:1,1:1,2:1})
        return [p,{},{}]
    p1={r:2**(r-1)};p2={r-1:2**(r-1)};p3={}
    for j in range(r-1):
        poly={0:1}
        for _ in range(r-2-j):poly=shiftmul(poly,{0:1,1:1,2:1})
        poly=shiftmul(poly,{j:2**j})
        p3=addpoly(p3,poly)
    scale={0:1}
    for _ in range(n-r):scale=shiftmul(scale,{0:1,1:1,2:1})
    return [shiftmul(p,scale) for p in (p1,p2,p3)]

def quad_basis(n):
    return [tuple(2 if j==i else 0 for j in range(n)) for i in range(n)]+[
      tuple(int(j==i or j==k) for j in range(n)) for i in range(n) for k in range(i+1,n)]

def form_matrix(coeff,n,q):
    # For char 3, Q(x)=x^T B x: off-diagonal B_ij=2 * coefficient(x_i x_j).
    B=[[0]*n for _ in range(n)]
    for i in range(n):B[i][i]=coeff[i]
    c=n
    for i in range(n):
        for j in range(i+1,n):
            B[i][j]=B[j][i]=mul(2,coeff[c],q);c+=1
    return B

def verify_case(coeff,n,q,ms,basis):
    Q={a:c for a,c in zip(basis,coeff) if c}
    r=rref_rank(form_matrix(coeff,n,q),q)
    a,b=operator_ranks(Q,n,q,ms)
    real=graded_strings_from_ranks(a,b,ms,n)
    predicted=expected_strings(n,r)
    assert real==predicted,(n,q,coeff,r,real,predicted)
    return r

def nondeg_count(r,q):
    if r==0:return 1
    m=r//2
    e=m*(m+1)
    stop=m if r%2==0 else m+1
    a=q**e
    for j in range(1,stop+1):a*=q**(2*j-1)-1
    return a

def gaussian(n,r,q):
    a=b=1
    for j in range(r):a*=q**(n-j)-1;b*=q**(r-j)-1
    return a//b

def main():
    n=3;q=3;ms=monoms(n);basis=quad_basis(n)
    freq=Counter()
    for coeff in product(range(q),repeat=len(basis)):
        freq[verify_case(coeff,n,q,ms,basis)]+=1
    expected={r:gaussian(n,r,q)*nondeg_count(r,q) for r in range(n+1)}
    assert dict(freq)==expected,(freq,expected)
    assert dict(freq)=={0:1,1:26,2:234,3:468}
    print('EXHAUSTIVE_GF3_N3_OK',sum(freq.values()),dict(sorted(freq.items())))
    rng=random.Random(20261013)
    for n,q,trials in [(3,9,90),(4,3,90),(5,3,25)]:
        ms=monoms(n);basis=quad_basis(n)
        for _ in range(trials):
            coeff=[rng.randrange(q) for __ in basis]
            verify_case(coeff,n,q,ms,basis)
        print('SAMPLED_OK',n,q,trials)
    for n in range(3,10):
        assert sum(gaussian(n,r,3)*nondeg_count(r,3) for r in range(n+1))==3**(n*(n+1)//2)
    print('FREQUENCY_IDENTITY_OK')
    print('VERIFY_OK')
if __name__=='__main__':main()
