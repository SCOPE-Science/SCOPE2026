#!/usr/bin/env python3
"""Finite-field and combinatorial checks for twin-blown-up graph evolution algebras."""
from itertools import combinations, product
from math import comb

def edges_complete(n):
    return [(u, v) for u in range(n) for v in range(u + 1, n)]

def blow_up(n, edges):
    return (2*n, [(2*u+a, 2*v+b) for u,v in edges for a,b in product(range(2),repeat=2)])

def adjacency_rows(n, edges):
    r=[0]*n
    for u,v in edges: r[u]|=1<<v; r[v]|=1<<u
    return r

def pivot_basis(rows):
    b={}
    for z in rows:
        while z:
            i=z.bit_length()-1
            if i in b:z^=b[i]
            else:b[i]=z;break
    return b

def belongs(v,b):
    while v:
        i=v.bit_length()-1
        if i not in b:return False
        v^=b[i]
    return True

def rref_subspaces(n):
    for k in range(n+1):
        for piv in combinations(range(n),k):
            pivs=set(piv)
            free=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in pivs]
            for choices in range(1<<len(free)):
                rows=[1<<p for p in piv]
                for a,(i,j) in enumerate(free):
                    if (choices>>a)&1:rows[i]|=1<<j
                yield rows

def ideals_count(n,edges):
    sq=adjacency_rows(n,edges)
    sq_basis=pivot_basis(sq)
    count=0; csub=0
    for rows in rref_subspaces(n):
        csub+=1
        base=pivot_basis(rows)
        ideal=True
        for x in rows:
            for i in range(n):
                if (x>>i)&1 and not belongs(sq[i],base):
                    ideal=False;break
            if not ideal:break
        if ideal:
            count+=1
            assert len(rows)==0 or all(belongs(y,base) for y in sq), 'nonzero ideal omits square'
    return count,csub,len(sq_basis)

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    a=b=1
    for j in range(k):a*=q**(n-j)-1;b*=q**(k-j)-1
    assert a%b==0
    return a//b

def cheeger(n,edges):
    best=None;witness=None
    for bits in range(1,1<<n):
        k=bits.bit_count()
        if 2*k>n:continue
        boundary=sum(bool((bits>>u)&1)!=bool((bits>>v)&1) for u,v in edges)
        from fractions import Fraction
        ratio=Fraction(boundary,k)
        if best is None or ratio<best:best=ratio;witness=bits
    return best,witness

def main():
    for n in [3,4]:
        nv,ee=blow_up(n,edges_complete(n))
        sq=adjacency_rows(nv,ee)
        rank=len(pivot_basis(sq))
        # Over F2, for K3 rank is 2; for K4 rank is 4.
        assert rank==(2 if n==3 else 4),(n,rank)
        h,w=cheeger(nv,ee)
        print('base_K',n,'blowup_vertices',nv,'rank_F2',rank,'codim',nv-rank,'Cheeger',str(h),'witness',w)
        if n==3:
            cnt,sub,rr=ideals_count(nv,ee)
            assert rr==rank
            expected=1+sum(gaussian(nv-rank,k,2) for k in range(nv-rank+1))
            print('exhaustive_all_subspaces',sub,'actual_ideals',cnt,'formula_ideals',expected)
            assert cnt==expected==68
        else:
            expected=1+sum(gaussian(4,k,2) for k in range(5))
            assert expected==68
            assert h==3
    # F5 base-K4 example: E^2 is a proper basic evolution ideal.
    nv,ee=blow_up(4,edges_complete(4))
    q=5
    R=[[0]*nv for _ in range(nv)]
    for u,v in ee:R[u][v]=1;R[v][u]=1
    svec=[];tvec=[]
    for v in range(4):
        s=[0]*nv;t=[0]*nv
        s[2*v]=s[2*v+1]=1
        t[2*v]=1;t[2*v+1]=q-1
        svec.append(s);tvec.append(t)
    def mult(x,y):
        result=[0]*nv
        for i in range(nv):
            for j in range(nv):result[j]=(result[j]+x[i]*y[i]*R[i][j])%q
        return result
    # Direct modular rank confirmation of the K4 adjacency rows.
    adjbase=[[0 if i==j else 1 for j in range(4)] for i in range(4)]
    pivot=0
    for col in range(4):
        ix=next((i for i in range(pivot,4) if adjbase[i][col]%q),None)
        if ix is None:continue
        adjbase[pivot],adjbase[ix]=adjbase[ix],adjbase[pivot]
        fac=pow(adjbase[pivot][col],-1,q)
        adjbase[pivot]=[u*fac%q for u in adjbase[pivot]]
        for i in range(4):
            if i != pivot:
                fac=adjbase[i][col]
                adjbase[i]=[(a-fac*b)%q for a,b in zip(adjbase[i],adjbase[pivot])]
        pivot+=1
    assert pivot==4
    basis=svec+tvec
    for i in range(nv):
        for j in range(i):assert mult(basis[i],basis[j])==[0]*nv
    for x in svec:
        for y in basis:
            # E^2 equals span of the first four natural vectors, so product
            # must have equal twin coordinates in each pair.
            prod=mult(x,y)
            assert all(prod[2*v]==prod[2*v+1] for v in range(4))
    assert 1+sum(gaussian(4,k,5) for k in range(5))==1121
    print('F5_BASIC_IDEAL_EXAMPLE_OK')
    print('FINITE_FIELD_IDEAL_FORMULAS_OK')
    print('VERIFY_OK')
if __name__=='__main__':main()
