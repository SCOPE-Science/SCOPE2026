#!/usr/bin/env python3
"""Independent GF(25) Cartier census for a genus-14 Artin-Schreier pencil.

F_25=F_5[w]/(w^2-3). All 625 coefficient-marked curves are checked.
"""
from math import comb
from collections import Counter
P=5
Z=(0,0);ONE=(1,0)
def plus(u,v):return ((u[0]+v[0])%P,(u[1]+v[1])%P)
def neg(u):return ((-u[0])%P,(-u[1])%P)
def prod(u,v):return ((u[0]*v[0]+3*u[1]*v[1])%P,(u[0]*v[1]+u[1]*v[0])%P)
def power(u,n):
    out=ONE
    while n:
        if n&1:out=prod(out,u)
        u=prod(u,u);n//=2
    return out
def scalar(u,c):return prod(u,(c%P,0))
def pol_mul(f,g):
    out={}
    for i,a in f.items():
        for j,b in g.items():out[i+j]=plus(out.get(i+j,Z),prod(a,b))
    return {i:c for i,c in out.items() if c!=Z}
def cartier_matrix(d,coefficients):
    bound=(5-1)*(d-1)-2
    basis=[(i,j) for j in range(4) for i in range((bound-d*j)//5+1)]
    powers=[{0:ONE}]
    for h in range(3):powers.append(pol_mul(powers[-1],coefficients))
    M=[[Z for _ in basis] for _ in basis]
    loc={pair:i for i,pair in enumerate(basis)}
    for col,(i,j) in enumerate(basis):
        for k in range(j+1):
            coeff=(comb(j,k)*(-1)**(j-k))%5
            for e,val in powers[j-k].items():
                if (e+i)%5!=4:continue
                row=loc[((e+i-4)//5,k)]
                M[row][col]=plus(M[row][col],scalar(power(val,5),coeff))
    return M,basis

def rank(M):
    A=[row.copy() for row in M];R=0;nr=len(A);nc=len(A[0]);
    for col in range(nc):
        pivot=next((i for i in range(R,nr) if A[i][col]!=Z),None)
        if pivot is None:continue
        A[R],A[pivot]=A[pivot],A[R]
        inv=power(A[R][col],23)
        A[R]=[prod(v,inv) for v in A[R]]
        for i in range(R+1,nr):
            if A[i][col]!=Z:
                c=A[i][col]
                A[i]=[plus(v,neg(prod(c,w))) for v,w in zip(A[i],A[R])]
        R+=1
    return R

F=[(a,b) for a in range(5) for b in range(5)]
assert len({power(z,5) for z in F})==25
counts=Counter()
for a in F:
    for b in F:
        M,basis=cartier_matrix(8,{8:ONE,4:a,6:b})
        assert len(basis)==14
        actual=rank(M)
        predicted=4 if (a,b)==(Z,Z) else (5 if a==Z or plus(scalar(a,2),prod(b,b))==Z else 6)
        assert actual==predicted,(a,b,actual,predicted)
        counts[actual]+=1
        Q,qbasis=cartier_matrix(4,{4:ONE,3:b,2:a})
        assert len(qbasis)==6 and rank(Q)==2,(a,b)
assert counts=={4:1,5:48,6:576},counts
# Independent prime-field census inside the same field model.
c5=Counter()
for a in range(5):
    for b in range(5):
        M,_=cartier_matrix(8,{8:ONE,4:(a,0),6:(b,0)})
        c5[rank(M)]+=1
assert c5=={4:1,5:8,6:16},c5
print('GF25_ALL_625_CARTIER_AND_QUOTIENT_OK')
print('GF5_ALL_25_CARTIER_OK')
