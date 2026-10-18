#!/usr/bin/env python3
"""Exact finite checks for generalized Pitman--Stanley multichain polytope.

Stdlib only. Checks every vertex of small instances by independent active-set
enumeration, every proposed reflected vertex, sharp supporting extrema, and
center equations. The parametric theorem requires its separate analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations


def matrices(n,m,a):
    d=n*m
    A=[]
    total=0
    for v in a:
        total+=v
        A.append(total)
    constraints=[] # coefficient dot x <= bound, label
    for i in range(n):
        for j in range(m):
            row=[F(0)]*d
            row[i*m+j]=-1
            constraints.append((tuple(row),F(0),'nonneg',i,j))
    for i in range(n):
        for j in range(m-1):
            row=[F(0)]*d
            for k in range(i+1):
                row[k*m+j]=-1
                row[k*m+j+1]=1
            constraints.append((tuple(row),F(0),'chain',i,j))
    for i in range(n):
        row=[F(0)]*d
        for k in range(i+1):row[k*m]=1
        constraints.append((tuple(row),F(A[i]),'upper',i,0))
    assert len(constraints)==2*d
    return A,constraints


def solve(rows,bs):
    d=len(bs)
    mat=[[F(v) for v in row]+[F(b)] for row,b in zip(rows,bs)]
    for j in range(d):
        piv=next((i for i in range(j,d) if mat[i][j]),None)
        if piv is None:return None
        if piv!=j:mat[j],mat[piv]=mat[piv],mat[j]
        den=mat[j][j]
        for k in range(j,d+1):mat[j][k]/=den
        for i in range(j+1,d):
            mul=mat[i][j]
            if mul:
                for k in range(j,d+1):mat[i][k]-=mul*mat[j][k]
    x=[F(0)]*d
    for i in range(d-1,-1,-1):
        x[i]=mat[i][d]-sum(mat[i][j]*x[j] for j in range(i+1,d))
    return tuple(x)


def dot(a,x):return sum(q*v for q,v in zip(a,x))


def vertices(d,ineq):
    pts=set()
    for inds in combinations(range(len(ineq)),d):
        x=solve([ineq[i][0] for i in inds],[ineq[i][1] for i in inds])
        if x is None: continue
        if all(dot(row,x)<=b for row,b,*_ in ineq):pts.add(x)
    return pts


def check(n,m,a):
    a=tuple(map(F,a)); A,hs=matrices(n,m,a)
    rho=max(sum(A[:i+1])/A[i] for i in range(n))
    s=m-1+rho
    d=n*m
    center=tuple((A[i]+(m-1-j)*a[i])/(s+1) for i in range(n) for j in range(m))
    assert all(dot(row,center)<b for row,b,*_ in hs), ('not-in-interior',n,m,a,center)
    vs=vertices(d,hs)
    assert vs, ('no-vertices',n,m,a)
    # independently verify claimed extremal values of every displayed inequality
    for row,b,kind,i,j in hs:
        lo=min(dot(row,v) for v in vs)
        hi=max(dot(row,v) for v in vs)
        assert hi==b,('facet-support',kind,i,j,hi,b)
        assert lo==(-A[i] if kind in ('nonneg','chain') else 0),('min',kind,i,j,lo)
    for v in vs:
        reflected=tuple(c-(x-c)/s for c,x in zip(center,v))
        assert all(dot(row,reflected)<=b for row,b,*_ in hs), ('outside',n,m,a,v)
    for i in range(n):
        if sum(A[:i+1])/A[i]==rho:
            y=tuple((s+1)*c for c in center)
            first=sum(y[k*m] for k in range(i+1))
            assert first==s*A[i]
    # Check an exact relative-interior witness for the full center locus.
    tight={i for i in range(n) if sum(A[:i+1])/A[i]==rho}
    L=max(tight)
    h=[F(0) if i in tight else F(1) for i in range(n)]
    eps=F(1,100000)
    y=[]
    for i in range(n):
        prev=h[i-1] if i else F(0)
        for j in range(m):
            y.append(A[i]+(eps if i>L else 0)+(m-1-j)*(a[i]+eps*(h[i]-prev)))
    for i in range(n):
        for j in range(m):
            val=y[i*m+j]-A[i]
            if j==m-1 and i<=L:assert val==0
            else:assert val>0,(n,m,a,'nonneg witness',i,j,val)
    for i in range(n):
        for j in range(m-1):
            diff=sum(y[k*m+j]-y[k*m+j+1] for k in range(i+1))-A[i]
            assert (diff==0 if i in tight else diff>0),(n,m,a,'gap witness',i,j,diff)
        margin=s*A[i]-sum(y[k*m] for k in range(i+1))
        assert (margin==0 if i in tight else margin>0),(n,m,a,'upper witness',i,margin)
    dimension=n*m-(L+1)-(m-1)*len(tight)
    assert dimension>=0
    # Each critical index enforces equality of last-column coordinate floors
    # and all column-prefix differences. Their independent rank is computed
    # analytically in RESULT.md.
    return len(vs),len(vs)*len(hs),rho,s,dimension


def main():
    inputs=[(1,3,(1,)),(2,2,(1,1)),(2,2,(1,3)),(2,2,(3,1)),
            (2,3,(1,1)),(2,3,(3,2)),(3,2,(1,1,1)),
            (3,2,(1,1,4)),(3,2,(1,2,4)),(3,2,(1,1,98))]
    comparisons=vertices_total=0
    for n,m,a in inputs:
        v,k,rho,s,dim=check(n,m,a)
        comparisons+=k;vertices_total+=v
        print('PASS n,m,a=',n,m,a,'vertices=',v,'rho=',rho,'s=',s,'center_dim=',dim)
    print('ALL_VERIFY_OK cases=',len(inputs),'vertices=',vertices_total,'reflected-facet-checks=',comparisons)

if __name__=='__main__':main()
