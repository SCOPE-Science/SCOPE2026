"""Exact finite-field and rational tests for the one-edge weighted sunlet controllability theorem."""
from math import gcd
from fractions import Fraction

PRIMES = (1000003, 1000033)

def laplacian(n, a, b, c):
    d=2*n
    L=[[0]*d for _ in range(d)]
    def edge(i,j,w):
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    for i in range(n):
        edge(i,(i+1)%n,a)
        edge(i,n+i,c if i==0 else b)
    return L

def rank_mod(mat,prime):
    A=[[x%prime for x in row] for row in mat]
    rows=len(A);cols=len(A[0]);r=0
    for j in range(cols):
        piv=next((i for i in range(r,rows) if A[i][j]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][j],-1,prime)
        for k in range(j,cols):A[r][k]=(A[r][k]*inv)%prime
        for i in range(r+1,rows):
            mul=A[i][j]
            if mul:
                for k in range(j,cols):A[i][k]=(A[i][k]-mul*A[r][k])%prime
        r+=1
        if r==rows:break
    return r

def krylov_rank(L,root,p):
    d=len(L)
    cols=[];v=[int(i==root) for i in range(d)]
    for t in range(d):
        cols.append(v)
        v=[sum(L[i][j]*v[j] for j in range(d))%p for i in range(d)]
    return rank_mod([[cols[j][i] for j in range(d)] for i in range(d)],p)

def rank_rat(mat):
    A=[[Fraction(v) for v in row] for row in mat]
    rows=len(A);cols=len(A[0]);r=0
    for j in range(cols):
        piv=next((i for i in range(r,rows) if A[i][j]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=1/A[r][j]
        for k in range(j,cols):A[r][k]*=inv
        for i in range(r+1,rows):
            mul=A[i][j]
            if mul:
                for k in range(j,cols):A[i][k]-=mul*A[r][k]
        r+=1
    return r

def krylov_rank_rat(L,root):
    d=len(L)
    cols=[];v=[int(i==root) for i in range(d)]
    for _ in range(d):
        cols.append(v)
        v=[sum(L[i][j]*v[j] for j in range(d)) for i in range(d)]
    return rank_rat([[cols[j][i] for j in range(d)] for i in range(d)])

def main():
    count=0
    for n in range(3,13):
        M=n//gcd(n,2)
        for p in PRIMES:
            for c in (1,2,3):
                L=laplacian(n,1,1,c)
                for j in range(n):
                    for root in (j,n+j):
                        rank=krylov_rank(L,root,p)
                        if c==1:assert rank<2*n,(n,c,j,root,p,rank)
                        elif gcd(j,M)>1:assert rank<2*n,(n,c,j,root,p,rank)
                        else:assert rank==2*n,(n,c,j,root,p,rank)
                        count+=1
    for n in range(3,9):
        M=n//gcd(n,2)
        for c in (1,3,5):
            L=laplacian(n,2,2,c)
            for root in range(2*n):
                j=root%n
                if c==2:assert krylov_rank_rat(L,root)<2*n
                elif gcd(j,M)>1:assert krylov_rank_rat(L,root)<2*n
                count+=1
    n=5
    L=laplacian(n,2,2,1)
    assert krylov_rank_rat(L,1)<10
    assert krylov_rank_rat(L,2)==10
    count+=2
    print('VERIFY_OK',count,'controllability-rank checks over finite fields and exact rationals')

if __name__=='__main__':main()
