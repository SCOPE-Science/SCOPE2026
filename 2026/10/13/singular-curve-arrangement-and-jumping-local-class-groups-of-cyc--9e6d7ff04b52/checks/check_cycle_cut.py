#!/usr/bin/env python3
"""Independent finite checks for toric cycle-cut singular-stratum formulas.

Requires scipy>=1.10 and sympy>=1.12. The general theorem is symbolic;
these bounded tests are not an infinite proof.
"""
from __future__ import annotations
import itertools, json, math
from functools import lru_cache
from scipy.optimize import linprog
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def parity_vertices(n):
    return tuple(v for v in itertools.product((0, 1), repeat=n) if sum(v) % 2 == 0)


def is_edge_by_exposing_functional(vertices, i, j):
    """Find functional strictly maximizing exactly v_i,v_j using an LP."""
    a,b=vertices[i],vertices[j]
    other=[u for k,u in enumerate(vertices) if k not in (i,j)]
    A=[[u[k]-a[k] for k in range(len(a))] for u in other]
    res=linprog([0.]*len(a), A_ub=A, b_ub=[-1.]*len(A),
                A_eq=[[a[k]-b[k] for k in range(len(a))]], b_eq=[0.],
                bounds=[(None,None)]*len(a), method='highs')
    if res.status not in (0,2):
        raise RuntimeError(f'Unresolved LP status {res.status}: {res.message}')
    return res.status==0


def check_edges(n):
    V=parity_vertices(n)
    actual=set()
    predicted=set()
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            d=sum(x!=y for x,y in zip(V[i],V[j]))
            if d==2: predicted.add((i,j))
            if is_edge_by_exposing_functional(V,i,j): actual.add((i,j))
    assert actual==predicted, (n, len(actual),len(predicted),actual^predicted)
    assert len(actual)==2**(n-2)*math.comb(n,2)
    return len(V),len(actual)

@lru_cache(None)
def representable(degrees):
    if all(x==0 for x in degrees):return True
    for i,j in itertools.combinations(range(len(degrees)),2):
        if degrees[i] and degrees[j]:
            v=list(degrees);v[i]-=1;v[j]-=1
            if representable(tuple(v)):return True
    return False


def comps(total,n):
    if n==1:
        yield (total,)
    else:
        for z in range(total+1):
            for v in comps(total-z,n-1):yield (z,)+v


def check_semigroup(n,max_degree=10):
    trials=0
    for s in range(0,max_degree+1,2):
        for x in comps(s,n):
            predicted=(max(x,default=0)*2<=s)
            found=representable(x)
            assert found==predicted,(n,x,predicted,found)
            trials+=1
    return trials


def class_snf(n):
    # Basis of the parity lattice: e_i-e_n, 2e_n.
    B=Matrix.eye(n)
    for i in range(n-1):B[n-1,i]=-1
    B[n-1,n-1]=2
    def evals(x):
        h=sum(x)//2
        assert 2*h==sum(x)
        return list(x)+[h-x[i] for i in range(n)]
    M=Matrix.hstack(*[Matrix(evals(list(B[:,i]))) for i in range(n)])
    D=smith_normal_form(M,domain=ZZ)
    elementary=[abs(int(D[i,i])) for i in range(n)]
    assert elementary==[1]*n,(n,elementary)
    return {'rank':2*n-n,'torsion_invariants':elementary}


def check_minors(n):
    # Finite-field Jacobian rank of 2xm minors on rank-one matrices.
    # At a nonzero matrix, rank of ideal's Jacobian equals m-1.
    p=101;m=n-2
    minors=list(itertools.combinations(range(m),2))
    def rank_mod(A):
        A=[row[:] for row in A];r=0
        for c in range(len(A[0]) if A else 0):
            piv=next((k for k in range(r,len(A)) if A[k][c]%p),None)
            if piv is None:continue
            A[r],A[piv]=A[piv],A[r]
            inv=pow(A[r][c]%p,-1,p)
            A[r]=[(z*inv)%p for z in A[r]]
            for k in range(len(A)):
                if k==r:continue
                mult=A[k][c]
                A[k]=[(a-mult*b)%p for a,b in zip(A[k],A[r])]
            r+=1
            if r==len(A):break
        return r
    trials=0
    for aa,bb in ((1,1),(1,3),(2,0),(0,4)):
        for vec in itertools.product((0,1,2),repeat=m):
            if not any(vec):continue
            first=[aa*x%p for x in vec];second=[bb*x%p for x in vec]
            Jac=[]
            for i,j in minors:
                row=[0]*(2*m)
                row[i]=second[j];row[j]=-second[i]
                row[m+i]=-first[j];row[m+j]=first[i]
                Jac.append(row)
            assert rank_mod(Jac)==m-1,(n,aa,bb,vec)
            trials+=1
    return trials


def main():
    result={'edge_checks':{},'semigroup_checks':{},'local_class_checks':{},'jacobian_checks':{}}
    for n in range(3,8):
        result['edge_checks'][n]=check_edges(n)
    for n in range(3,8):
        result['semigroup_checks'][n]=check_semigroup(n)
    for n in range(4,11):
        result['local_class_checks'][n]=class_snf(n)
    for n in range(4,9):
        result['jacobian_checks'][n]=check_minors(n)
    result['status']='PASS'
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
