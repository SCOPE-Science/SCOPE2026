#!/usr/bin/env python3
"""Direct finite-field check of multiplication-rank census for the eight-dimensional free commutative Jacobi algebra."""
from collections import Counter
from itertools import product
from random import Random
from fractions import Fraction

# Basis (x,y,a=x*x,b=x*y,c=y*y,d=(x*x)*y,e=x*(y*y),f=a*c).
# Values are rational coefficients with denominator 2; only odd fields considered.
TABLE = {
(0,0):[(2,1)],(0,1):[(3,1)],(1,1):[(4,1)],
(0,3):[(5,-0.5)],(0,4):[(6,1)],(1,2):[(5,1)],(1,3):[(6,-0.5)],
(2,4):[(7,1)],(3,3):[(7,-0.5)],(0,6):[(7,-0.5)],(1,5):[(7,-0.5)],
}

def structure(q):
    inverse2=pow(2,-1,q)
    t=[[[0]*8 for _ in range(8)] for _ in range(8)]
    for (i,j),items in TABLE.items():
        for k,c in items:
            v=(1 if c==1 else -inverse2)%q
            t[i][j][k]=v;t[j][i][k]=v
    return t

def prod(x,y,t,q):
    out=[0]*8
    for i,xi in enumerate(x):
        if xi:
            for j,yj in enumerate(y):
                if yj:
                    for k,c in enumerate(t[i][j]):
                        out[k]+=xi*yj*c
    return tuple(z%q for z in out)

def rank_mod(matrix,q):
    a=[list(row) for row in matrix]; n=len(a);m=len(a[0]);r=0
    for col in range(m):
        pivot=next((i for i in range(r,n) if a[i][col]%q),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][col]%q,-1,q)
        for j in range(col,m): a[r][j]=(a[r][j]*inv)%q
        for i in range(r+1,n):
            if a[i][col]%q:
                factor=a[i][col]
                for j in range(col,m): a[i][j]=(a[i][j]-factor*a[r][j])%q
        r+=1
        if r==n:break
    return r

def actual_rank(x,t,q):
    m=[[sum(x[k]*t[k][i][j] for k in range(8))%q for i in range(8)] for j in range(8)]
    return rank_mod(m,q)

def prediction(x,q):
    u,v,a,b,c,d,e,f=x
    if u or v:return 5
    if a or b or c:return 2 if (b*b-4*a*c)%q==0 else 3
    if d or e:return 1
    return 0

def expected_counts(q):
    return {0:q,1:(q*q-1)*q,2:(q*q-1)*q**3,3:q**5*(q-1),5:(q*q-1)*q**6}

def main():
    # Exact rational verification of every structure-constant Jacobi identity.
    rat=[[[Fraction(0) for _ in range(8)] for _ in range(8)] for _ in range(8)]
    for (i,j),items in TABLE.items():
        for k,c in items:
            rat[i][j][k]=Fraction(c)
            rat[j][i][k]=Fraction(c)
    for i,j,k in product(range(8),repeat=3):
        for out in range(8):
            value=sum(rat[i][j][h]*rat[h][k][out]+rat[j][k][h]*rat[h][i][out]+rat[k][i][h]*rat[h][j][out] for h in range(8))
            assert value==0,(i,j,k,out,value)
    print('EXACT_RATIONAL_JACOBI_OK 512')
    rng=Random(731211)
    for q in (5,7,11):
        t=structure(q)
        for i,j,k in product(range(8),repeat=3):
            left=[sum(t[i][j][h]*t[h][k][l] for h in range(8))%q for l in range(8)]
            mid=[sum(t[j][k][h]*t[h][i][l] for h in range(8))%q for l in range(8)]
            right=[sum(t[k][i][h]*t[h][j][l] for h in range(8))%q for l in range(8)]
            assert all((left[l]+mid[l]+right[l])%q==0 for l in range(8)),(q,i,j,k)
        # Exhaustively vary all coefficients impacting L_z over F5, holding f=0.
        # Over other primes check 5000 independently constructed samples.
        if q==5:
            counts=Counter()
            for seven in product(range(q),repeat=7):
                x=seven+(0,)
                r=actual_rank(x,t,q)
                assert r==prediction(x,q),(q,x,r,prediction(x,q))
                counts[r]+=q # last coordinate f is arbitrary and has no effect
            assert dict(counts)==expected_counts(q),(counts,expected_counts(q))
            print('EXHAUSTIVE q=5',dict(sorted(counts.items())))
        else:
            for _ in range(5000):
                x=tuple(rng.randrange(q) for _ in range(8))
                r=actual_rank(x,t,q)
                assert r==prediction(x,q),(q,x,r,prediction(x,q))
            print('RANDOM q=',q,'5000 independent ranks')
    print('FREE_JJ_MULTIPLICATION_RANK_OK q5_exhaustive q7_5000 q11_5000 jacobi_512_each')

if __name__=='__main__': main()
