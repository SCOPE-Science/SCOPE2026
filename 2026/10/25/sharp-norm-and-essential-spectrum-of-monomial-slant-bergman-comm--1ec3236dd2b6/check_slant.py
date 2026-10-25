"""Deterministic finite checks for the slant Bergman monomial commutator.
Theorems concerning infinite operators follow from the accompanying proof,
not from these finite checks.
"""
from math import sqrt
from fractions import Fraction
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import svds

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def action(r, a, b, n):
    terms = {}
    for sign, shift in ((1,b+r*a),(-1,a+r*b)):
        if (n+shift) % (r*r):
            continue
        m=(n+shift)//(r*r)
        v=sign*sqrt((n+1)/(m+1))
        terms[m]=terms.get(m,0.)+v
    return {m:v for m,v in terms.items() if abs(v)>1e-12}

def two_steps(r,a,b,n):
    terms={}
    for sign,first,second in ((1,b,a),(-1,a,b)):
        if (n+first)%r: continue
        k=(n+first)//r
        if (k+second)%r: continue
        m=(k+second)//r
        value=sign*sqrt((n+1)/(k+1))*sqrt((k+1)/(m+1))
        terms[m]=terms.get(m,0.)+value
    return {m:v for m,v in terms.items() if abs(v)>1e-12}

def finite_matrix(r,a,b,N):
    rows=[];cols=[];vals=[]
    for n in range(N):
        for m,v in action(r,a,b,n).items():
            if m<N:
                rows.append(m);cols.append(n);vals.append(v)
    return coo_matrix((vals,(rows,cols)),shape=(N,N)).tocsr()

for r in range(2,8):
    for a in range(0,14):
        for b in range(0,14):
            d1=b+r*a; d2=a+r*b
            coincident=((a-b)%(r*r)==0)
            check(((d1-d2)%(r*r)==0)==coincident,'congruence identity')
            for n in (0,1,2,3,5,11,30,93,272,650):
                x=action(r,a,b,n)
                y=two_steps(r,a,b,n)
                check(x.keys()==y.keys(),'two-step support')
                for m in x:
                    check(abs(x[m]-y[m])<1.e-12,'telescoping coefficient')
                    check(abs(x[m])<=2*r+1.e-12,'universal two-term bound')
            if a!=b:
                for m in (31,103,1001):
                    for d in (d1,d2):
                        n=r*r*m-d
                        if n<0: continue
                        weight_sq=Fraction(n+1,m+1)
                        check(weight_sq<r*r,'strict weight inequality')
                        check(abs(float(weight_sq)-r*r)<r*r*(max(d1,d2)+r*r)/(m+1),'limit inequality')

# Direct finite-section tests at small slant orders. The finite sections
# are lower bounds only; they do not prove the infinite-dimensional norms.
examples=((2,0,1),(2,0,4),(2,2,10),(3,0,1),(3,0,9),(4,3,19),(5,0,25))
for r,a,b in examples:
    C=finite_matrix(r,a,b,900)
    measured=float(svds(C,k=1,return_singular_vectors=False,tol=1e-9,maxiter=8000)[0])
    target=r*(2 if (a-b)%(r*r)==0 else sqrt(2))
    check(measured<=target+1e-8,'finite norm exceeds analytic upper bound')
    check(measured>target*.90,'finite section too far from limit')
    print(f'r={r} a={a} b={b} finite_norm={measured:.9f} target={target:.9f}')

print(f'PASS {checks} deterministic assertions')
