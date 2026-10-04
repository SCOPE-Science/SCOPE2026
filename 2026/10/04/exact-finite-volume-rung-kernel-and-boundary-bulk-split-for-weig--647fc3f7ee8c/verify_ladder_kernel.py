#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import math

def edges(n):
    E=[]
    for i in range(n): E.append((i,n+i,"r",i))
    for i in range(n-1):
        E.append((i,i+1,"h",None))
        E.append((n+i,n+i+1,"h",None))
    return E

def is_tree(n,S):
    N=2*n
    if len(S)!=N-1: return False
    p=list(range(N))
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for e in S:
        a,b=f(e[0]),f(e[1])
        if a==b: return False
        p[b]=a
    r=f(0)
    return all(f(v)==r for v in range(N))

def inv(A):
    n=len(A)
    M=[A[i][:]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        q=next(r for r in range(c,n) if M[r][c])
        M[c],M[q]=M[q],M[c]
        d=M[c][c]; M[c]=[x/d for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                z=M[r][c]
                M[r]=[M[r][k]-z*M[c][k] for k in range(2*n)]
    return [r[n:] for r in M]

def det(A):
    A=[r[:] for r in A]; n=len(A); out=Fraction(1)
    for c in range(n):
        q=next((r for r in range(c,n) if A[r][c]),None)
        if q is None: return Fraction(0)
        if q!=c: A[c],A[q]=A[q],A[c]; out=-out
        d=A[c][c]; out*=d
        for r in range(c+1,n):
            if A[r][c]:
                z=A[r][c]/d
                for k in range(c,n): A[r][k]-=z*A[c][k]
    return out

def kernel(n,c):
    if n==1: return [[Fraction(1)]]
    B=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        B[i][i]=1+2*c if i in (0,n-1) else 2+2*c
        if i+1<n: B[i][i+1]=B[i+1][i]=-1
    Q=inv(B)
    return [[2*c*Q[i][j] for j in range(n)] for i in range(n)]

def main():
    checks=0
    for n in range(1,6):
        for c in (Fraction(1),Fraction(2),Fraction(3,2)):
            E=edges(n)
            R=[next(k for k,e in enumerate(E) if e[2]=="r" and e[3]==i) for i in range(n)]
            trees=[]; Z=Fraction(0)
            for I in combinations(range(len(E)),2*n-1):
                S=[E[k] for k in I]
                if is_tree(n,S):
                    w=c**sum(E[k][2]=="r" for k in I)
                    trees.append((set(I),w)); Z+=w
            K=kernel(n,c)
            for r in range(1,n+1):
                for S in combinations(range(n),r):
                    prob=sum(w for T,w in trees if all(R[i] in T for i in S))/Z
                    assert prob==det([[K[i][j] for j in S] for i in S])
                    checks+=1
            a=float(c)+1-math.sqrt(float(c*c+2*c)); rho=(1-a)/(1+a)
            for i0 in range(n):
                for j0 in range(n):
                    i,j=sorted((i0+1,j0+1))
                    x=rho*a**(j-i)*(1+a**(2*i-1))*(1+a**(2*(n-j)+1))/(1-a**(2*n))
                    assert abs(float(K[i0][j0])-x)<2e-12
                    checks+=1
    print("VERIFY_OK")
    print("checks =",checks)

if __name__=="__main__": main()
