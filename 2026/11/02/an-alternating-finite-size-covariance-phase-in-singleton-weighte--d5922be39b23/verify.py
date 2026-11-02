#!/usr/bin/env python3
"""Exact finite-polynomial verification for singleton-weighted noncrossing partitions.

Uses ordinary set-partition generation and a crossing test, independently of the
block-profile coefficient formula used in the proof. All arithmetic is integer.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial

# Ascending coefficients of polynomials P_n in Cov(X_2,X_3)=-n P_n/Z_n^2.
P = {
 5: [-1,5,0,40,0,19],
 6: [21,60,30,145,15,200,0,45],
 7: [-20,252,741,1190,560,1218,126,694,0,90],
 8: [547,1442,3752,8939,10486,11424,4340,6174,581,1918,0,161],
}
Z = {
 5: [6,15,10,10,0,1],
 6: [15,36,45,20,15,0,1],
 7: [36,105,126,105,35,21,0,1],
 8: [91,288,420,336,210,56,28,0,1],
}

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def partitions(n):
    seq=[((1,),)]
    for x in range(2,n+1):
        nxt=[]
        for p in seq:
            for k in range(len(p)):
                arr=list(p)
                arr[k]=arr[k]+(x,)
                nxt.append(tuple(arr))
            nxt.append(p+((x,),))
        seq=nxt
    return seq

def noncrossing(p,n):
    idx=[-1]*(n+1)
    for j,b in enumerate(p):
        for a in b:idx[a]=j
    for a in range(1,n-2):
        for b in range(a+1,n-1):
            for c in range(b+1,n):
                if idx[a]!=idx[c]:continue
                for d in range(c+1,n+1):
                    if idx[b]==idx[d] and idx[b]!=idx[a]:
                        return False
    return True

def counts(n):
    z=[0]*(n+1);a=z.copy();b=z.copy();m=z.copy()
    profiles=Counter()
    for p in partitions(n):
        if not noncrossing(p,n): continue
        h=sum(len(v)==1 for v in p)
        two=sum(len(v)==2 for v in p)
        three=sum(len(v)==3 for v in p)
        z[h]+=1;a[h]+=two;b[h]+=three;m[h]+=two*three
        profiles[tuple(sorted(map(len,p)))]+=1
    return z,a,b,m,profiles

def equal_poly(a,b):
    k=max(len(a),len(b))
    return a+[0]*(k-len(a)) == b+[0]*(k-len(b))

def polyval(poly,q):
    return sum((v*q**i for i,v in enumerate(poly)),Fraction(0))

def main():
    checks=0
    cats={5:42,6:132,7:429,8:1430}
    for n in range(5,9):
        z,a,b,m,profiles=counts(n)
        assert sum(z)==cats[n];checks+=1
        assert equal_poly(z,Z[n]);checks+=1
        D=mul(m,z);AB=mul(a,b)
        target=[-n*x for x in P[n]]
        D=[(D[i] if i<len(D) else 0)-(AB[i] if i<len(AB) else 0) for i in range(max(len(D),len(AB)))]
        assert equal_poly(D,target),(n,D,target);checks+=1
        # Independently validate the Kreweras profile formula for every observed type.
        for prof,ct in profiles.items():
            mlen=len(prof)
            zfac=1
            for v in Counter(prof).values():zfac*=factorial(v)
            expct=factorial(n)//(factorial(n-mlen+1)*zfac)
            assert ct==expct,(n,prof,ct,expct)
            checks+=1
        for q in map(Fraction,['0','1/20','1/10','1/2','1','2','10']):
            zz=polyval(z,q)
            cov=polyval(D,q)/zz**2
            reconstructed=polyval(m,q)/zz-polyval(a,q)*polyval(b,q)/zz**2
            assert cov==reconstructed;checks+=1
            assert cov==-n*polyval(P[n],q)/zz**2;checks+=1
    q=Fraction(1,20)
    signs=[]
    for n in range(5,9):
        p=polyval(P[n],q)
        signs.append(1 if p<0 else (-1 if p>0 else 0))
    assert signs==[1,-1,1,-1];checks+=1
    assert P[5][0]<0 and all(v>=0 for v in P[5][1:]);checks+=1
    assert P[7][0]<0 and all(v>=0 for v in P[7][1:]);checks+=1
    assert all(v>=0 for v in P[6]) and all(v>=0 for v in P[8]);checks+=1
    print('VERIFIED', checks, 'independent exact checks; alternating q=1/20 signs +,-,+,-')

if __name__=='__main__':main()
