#!/usr/bin/env python3
"""Separate finite checks of the two-row rectangular-band Schur partition theorem."""
from math import comb, factorial
from functools import lru_cache

def partitions(n):
    if n == 0:
        yield ()
        return
    a=[0]*n
    def go(k, mx):
        if k==n:
            yield tuple(a)
            return
        for val in range(mx+2):
            a[k]=val
            yield from go(k+1, max(mx,val))
    yield from go(1,0)

def class_data(p,m):
    k=1+max(p)
    rows=[[0,0] for _ in range(k)]
    cols=[[0]*m for _ in range(k)]
    elems=[[] for _ in range(k)]
    for i,x in enumerate(p):
        rr=i//m; cc=i%m
        rows[x][rr]+=1; cols[x][cc]+=1;elems[x].append((rr,cc))
    return rows,cols,elems

def direct_schur(p,m):
    rows,cols,elems=class_data(p,m)
    for x in range(len(rows)):
        for y in range(len(rows)):
            for z in elems:
                if len({rows[x][i]*cols[y][j] for i,j in z})>1:
                    return False
    return True

def profile_schur(p,m):
    rows,cols,elems=class_data(p,m)
    for block in elems:
        if any(tuple(r[i] for r in rows)!=tuple(r[block[0][0]] for r in rows) or
               tuple(c[j] for c in cols)!=tuple(c[block[0][1]] for c in cols)
               for i,j in block):
            return False
    return True


def orbit_certificate(p,m):
    """Construct subgroup generators of S_2 x S_m with precisely these orbits."""
    rows,cols,blocks=class_data(p,m)
    balanced=all(r[0]==r[1] for r in rows)
    gens=[]
    def col_swap(a,b):
        perm=list(range(m));perm[a]=b;perm[b]=a
        gens.append((0,perm))
    if not balanced:
        for block in blocks:
            if block[0][0]!=0:continue
            C=sorted(j for i,j in block)
            for j in range(len(C)-1):col_swap(C[j],C[j+1])
    else:
        signature={}
        for j in range(m):
            signature.setdefault(tuple(c[j] for c in cols),[]).append(j)
        flip=list(range(m))
        for C in signature.values():
            containing=[b for b in range(len(blocks)) if cols[b][C[0]]>0]
            if len(containing)==1:
                for j in range(len(C)-1):col_swap(C[j],C[j+1])
            else:
                A=sorted(j for j in C if p[j]==containing[0])
                B=sorted(j for j in C if p[m+j]==containing[0])
                assert len(A)==len(B)
                for D in (A,B):
                    for j in range(len(D)-1):col_swap(D[j],D[j+1])
                for a,b in zip(A,B):flip[a]=b;flip[b]=a
        gens.append((1,flip))
    # Connected components of generator action coincide with group orbits.
    parent=list(range(2*m))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for rowflip,perm in gens:
        for x in range(2*m):
            y=((x//m)^rowflip)*m+perm[x%m]
            parent[root(x)]=root(y)
    orbits=[root(x) for x in range(2*m)]
    return all((p[i]==p[j])==(orbits[i]==orbits[j]) for i in range(2*m) for j in range(2*m))

@lru_cache(None)
def bell(m):
    if m==0:return 1
    return sum(comb(m-1,k)*bell(k) for k in range(m))

@lru_cache(None)
def weighted_bell(m):
    if m==0:return 1
    # Set partition block containing the distinguished first column.
    return sum(comb(m-1,k-1) * (1+(comb(k,k//2)//2 if k%2==0 else 0)) * weighted_bell(m-k)
               for k in range(1,m+1))

if __name__=='__main__':
    for m in range(1,6):
        total=0; balanced=0; separated=0
        for p in partitions(2*m):
            if m<=4:
                ok=direct_schur(p,m)
                assert ok==profile_schur(p,m),('profile direct mismatch',m,p)
            else:ok=profile_schur(p,m)
            if not ok:continue
            total+=1
            assert orbit_certificate(p,m), ('nonautomorphic',m,p)
            rows,_,_=class_data(p,m)
            if all(r[0]==r[1] for r in rows):balanced+=1
            else:separated+=1
        predicted=bell(m)+weighted_bell(m)
        assert (total,balanced,separated)==(predicted,weighted_bell(m),bell(m)),(m,total,balanced,separated,predicted)
        print('m=%d direct_partition_census=%d balanced=%d separated=%d'%(m,total,balanced,separated))
    print('VERIFY_OK')
