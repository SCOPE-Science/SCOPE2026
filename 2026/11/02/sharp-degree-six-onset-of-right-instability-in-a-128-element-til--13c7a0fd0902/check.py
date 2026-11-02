#!/usr/bin/env python3
"""Exact degree-cutoff certificate for a tiled matrix ring over Z/4Z.

Requires Python 3 standard library only. All calculations are integral.
"""
from itertools import product

MOD=4
ZERO=(0,0,0,0)
ONE=(1,0,0,1)
E11=(1,0,0,0)
E21=(0,0,1,0)
E22=(0,0,0,1)
MATRIX_BASIS=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
RING=tuple(product(range(4),(0,2),range(4),range(4)))


def mul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return ((a*e+b*g)%4,(a*f+b*h)%4,(c*e+d*g)%4,(c*f+d*h)%4)


def powers(x,degree):
    ans=[ONE]
    for _ in range(degree):ans.append(mul(ans[-1],x))
    return ans


def eval_poly(coefficients,x):
    ans=[0,0,0,0]
    for c,p in zip(coefficients,powers(x,len(coefficients)-1)):
        z=mul(c,p)
        ans=[(u+v)%4 for u,v in zip(ans,z)]
    return tuple(ans)


def eval_coordinate_row(x,v):
    row=[]
    for p in powers(x,5):
        for c in MATRIX_BASIS:
            row.append(mul(c,p)[v])
    return row


def determinant_bareiss(matrix):
    a=[list(map(int,row)) for row in matrix]
    n=len(a)
    assert all(len(row)==n for row in a)
    sign=1
    prev=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((j for j in range(k+1,n) if a[j][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*p-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
        for i in range(k+1,n):a[i][k]=0
        prev=p
    return sign*a[-1][-1]


def rank_mod_2(matrix):
    a=[[int(x)&1 for x in row] for row in matrix]
    n=len(a[0]);p=0
    for j in range(n):
        i=next((i for i in range(p,len(a)) if a[i][j]),None)
        if i is None:continue
        a[i],a[p]=a[p],a[i]
        for i in range(p+1,len(a)):
            if a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[p])]
        p+=1
        if p==len(a):break
    return p


def main():
    assert len(RING)==128 and len(set(RING))==128
    assert all(mul(x,y) in RING for x in RING for y in RING)
    # The 24 necessary evaluation constraints for a degree-five null polynomial.
    probes=[
      ((0,0,0,0),(0,1,2,3)),
      ((1,0,0,1),(0,1,2,3)),
      ((0,2,1,0),(0,1,2,3)),
      ((1,2,1,1),(0,1,2,3)),
      ((0,0,1,0),(0,2)),
      ((1,0,1,1),(0,2)),
      ((0,0,1,2),(2,)),
      ((1,0,1,3),(2,)),
    ]
    cert=[eval_coordinate_row(x,v) for x,entries in probes for v in entries]
    for i in (2,3):
        row=[0]*24
        row[4*i+1]=2
        cert.append(row)
    assert len(cert)==24 and all(len(x)==24 for x in cert)
    determinant=determinant_bareiss(cert)
    rank=rank_mod_2(cert)
    assert determinant==4096 and rank==12,(determinant,rank)
    print('DEGREE_5_CERTIFICATE: determinant=4096, rank_mod_2=12, size=24')

    # The ring element r has r^2=2 I and r^4=0.
    r=(0,2,1,0)
    r2=mul(r,r)
    r4=mul(r2,r2)
    assert r2==(2,0,0,2) and r4==ZERO
    # F=E21*(X^2-X^4)+E22*(X^3-X^4-X^5+X^6).
    F=(ZERO,ZERO,E21,E22,(0,0,3,3),(0,0,0,3),E22)
    assert all(x in RING for x in F)
    assert all(eval_poly(F,x)==ZERO for x in RING)
    Fe=tuple(mul(c,E11) for c in F)
    got=eval_poly(Fe,r)
    assert got==(0,0,2,0),got
    print('DEGREE_6_WITNESS: 128/128 evaluations zero, (F*E11)(r)=2*E21')
    print('VERIFY_OK')

if __name__=='__main__':main()
