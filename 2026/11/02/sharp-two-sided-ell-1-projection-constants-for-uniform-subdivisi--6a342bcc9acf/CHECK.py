#!/usr/bin/env python3
"""Exact reproducibility checks for l1 projection constants on uniformly
subdivided complete graphs. No nonstandard dependencies. Tests finite
instances only; the mathematical proof is valid for all permitted integers.
"""
from fractions import Fraction as F


def base_projection(n):
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    m = len(edges)
    idx = {e:k for k,e in enumerate(edges)}
    B=[]
    for i,j in edges:
        v=[F(0)]*n
        v[i]=F(1)
        v[j]=F(-1)
        column=[]
        for k,l in edges:
            # Orient every original edge from the smaller to the larger label.
            value=(F(1) if (k,l)==(i,j) else F(0))-(v[k]-v[l])/n
            column.append(value)
        B.append(column)
    return edges,B


def test(n,r):
    base, B = base_projection(n)
    m=len(base)
    dim=m*r
    d=F(n-2,n)
    lam=F(3*(n-2),n)
    cut=F(1)+lam-F(2*(n-2),n*r)
    # Index (a,t) for path label a and position t=0,...,r-1.
    def at(a,t): return a*r+t
    M=[[B[b][a]/r for b in range(m) for s in range(r)]
       for a in range(m) for t in range(r)]
    checks=0
    for a in range(m):
        for t in range(r):
            j=at(a,t)
            col=[M[i][j] for i in range(dim)]
            assert sum(abs(v) for v in col)==lam
            checks+=1
            other=[(F(1) if i==j else F(0))-M[i][j] for i in range(dim)]
            assert sum(abs(v) for v in other)==cut
            checks+=1
            assert M[j][j]==d/r
            checks+=1
    # Verify idempotence by exact fractional multiplication.
    for i in range(dim):
        for j in range(dim):
            assert sum(M[i][k]*M[k][j] for k in range(dim))==M[i][j]
            checks+=1
    # Range vectors are constant along subdivided paths, are cycle flows.
    for j in range(dim):
        for a in range(m):
            for t in range(1,r):
                assert M[at(a,t)][j]==M[at(a,0)][j]
                checks+=1
        for v in range(n):
            flow=F(0)
            for a,(i,k) in enumerate(base):
                if i==v: flow+=M[at(a,0)][j]
                if k==v: flow-=M[at(a,0)][j]
            assert flow==0
            checks+=1
    # Check covariance under two generators of the vertex-permutation group.
    index={edge:i for i,edge in enumerate(base)}
    perms=[]
    trans=list(range(n)); trans[0],trans[1]=trans[1],trans[0]
    perms.append(trans)
    perms.append([(i+1)%n for i in range(n)])
    for perm in perms:
        action=[]
        for a,(i,j) in enumerate(base):
            u,v=perm[i],perm[j]
            if u<v:
                action.extend([(at(index[(u,v)],t),F(1)) for t in range(r)])
            else:
                action.extend([(at(index[(v,u)],r-1-t),F(-1)) for t in range(r)])
        for i in range(dim):
            for j in range(dim):
                ii,si=action[i]
                jj,sj=action[j]
                assert M[ii][jj] == si*sj*M[i][j]
                checks+=1
    return checks


if __name__=='__main__':
    total=0
    for n in range(3,8):
        for r in range(1,5):
            count=test(n,r)
            total+=count
            print('n=',n,'r=',r,'exact assertions=',count)
    print('CHECK_OK',total,'exact rational assertions, all pairs 3<=n<=7,1<=r<=4')
