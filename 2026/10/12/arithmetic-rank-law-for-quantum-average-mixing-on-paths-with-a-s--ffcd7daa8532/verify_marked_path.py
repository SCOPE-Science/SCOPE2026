#!/usr/bin/env python3
"""Exact checks for a single-site potential on finite path Hamiltonians."""
from math import gcd
from fractions import Fraction


def add(a, b):
    z = [0] * max(len(a), len(b))
    for i, x in enumerate(a): z[i] += x
    for i, x in enumerate(b): z[i] += x
    return trim(z)


def scale(a, c): return trim([c*x for x in a])


def mul(a,b):
    z = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j,y in enumerate(b): z[i+j] += x*y
    return trim(z)


def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a


def path_polys(n):
    u=[[1],[0,1]]
    for k in range(1,n): u.append(add(mul(u[-1],[0,1]),scale(u[-2],-1)))
    return u


def deleted_minor(n,i,j,t,u):
    if j == i: return mul(u[j-1],u[n-j])
    if j < i:
        return mul(u[j-1],add(u[n-j],scale(mul(u[i-j-1],u[n-i]),-t)))
    return mul(add(u[j-1],scale(mul(u[i-1],u[j-i-1]),-t)),u[n-j])


def rank(M):
    if not M: return 0
    A=[[Fraction(x) for x in row] for row in M]
    n=len(A); k=len(A[0]); r=0
    for j in range(k):
        pivot=next((i for i in range(r,n) if A[i][j]!=0),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        pr=A[r][j]
        for i in range(r+1,n):
            if A[i][j]:
                f=A[i][j]/pr
                for h in range(j+1,k): A[i][h]-=f*A[r][h]
                A[i][j]=Fraction(0)
        r+=1
        if r==n: break
    return r


def moment_matrix(n,site,t):
    H=[[0]*n for _ in range(n)]
    for j in range(n-1): H[j][j+1]=H[j+1][j]=1
    H[site-1][site-1]=t
    P=[[int(i==j) for j in range(n)] for i in range(n)]
    W=[]
    for _ in range(n):
        W.append([P[j][j] for j in range(n)])
        P=[[sum(P[i][k]*H[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return W


def predicted(n,i):
    d=gcd(i,n+1)
    if n%2 and i==(n+1)//2: return (n+1)//2
    return n-(d-1)//2


def main():
    differences=0; pairs=0; symmetries=0; negatives=0
    for n in range(2,19):
        u=path_polys(n)
        m=n//2
        for i in range(1,n+1):
            # Symbolic coefficient witness for the claimed two-case formula.
            q=[None]+[deleted_minor(n,i,j,1,u) for j in range(1,n+1)]
            for j in range(1,m+1):
                lhs=add(q[j],scale(q[n+1-j],-1))
                ii=min(i,n+1-i)
                if n%2 and i==(n+1)//2:
                    rhs=[0]
                elif j<=ii:
                    rhs=mul(u[n-2*ii],mul(u[j-1],u[j-1]))
                else:
                    rhs=mul(mul(u[ii-1],u[ii-1]),u[n-2*j])
                # Under spatial reflection, sign reverses.
                if i>n+1-i: rhs=scale(rhs,-1)
                assert lhs==rhs, ('MINOR_IDENTITY',n,i,j,lhs,rhs)
                differences+=1
            for t in (-2,Fraction(3,2),1,3):
                r=rank(moment_matrix(n,i,t))
                assert r==predicted(n,i), ('RANK',n,i,t,r,predicted(n,i))
                pairs+=1
                if t<0: negatives+=1
            symmetries+=1
    print(f'VERIFY_OK symbolic_antisymmetric_minor_identities={differences} exact_moment_rank_instances={pairs} negative_potential_instances={negatives} site_cases={symmetries} path_orders=2..18')

if __name__=='__main__': main()
