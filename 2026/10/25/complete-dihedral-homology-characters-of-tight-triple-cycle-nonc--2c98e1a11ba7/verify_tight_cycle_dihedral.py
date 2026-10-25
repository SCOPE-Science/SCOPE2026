#!/usr/bin/env python3
"""Reproducible finite checks for cyclic triple noncover dihedral characters.
Requires only Python 3 standard library; exact integer arithmetic.
"""
from math import gcd

def dimension(n):
    k, t = divmod(n,4)
    return (2*k-2) if t == 0 else (2*k-1)

def character(n, a, reflection):
    k,t = divmod(n,4)
    if reflection:
        if t == 0:
            return (-1)**(k+1+a)
        return (-1)**k
    if t == 0:
        return 3 if a % 4 == 0 else -1
    return 1

def orbital_sum(n, perm):
    seen=set(); blocks=[]
    for i in range(n):
        if i in seen: continue
        j=i; bm=0
        while j not in seen:
            seen.add(j); bm |=1<<j; j=perm[j]
        blocks.append(bm)
    edges=[sum(1<<((i+k)%n) for k in range(3)) for i in range(n)]
    out=0
    for idx in range(1<<len(blocks)):
        selected=0
        for j,block in enumerate(blocks):
            if (idx>>j)&1:selected |=block
        if all((selected&triple)!=triple for triple in edges):
            out += -1 if idx.bit_count()%2 else 1
    return len(blocks),out

def mask_sign(mask,perm):
    # sign of permutation restricted to the selected vertices
    vertices=[i for i in range(len(perm)) if mask>>i&1]
    images=[perm[i] for i in vertices]
    return -1 if sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))%2 else 1

def direct_character(n, perm):
    # Reduced Lefschetz trace: the empty face contributes -1.
    edges=[sum(1<<((i+k)%n) for k in range(3)) for i in range(n)]
    trace=0
    for mask in range(1<<n):
        if not any((mask&edge)==0 for edge in edges):continue
        image=0
        for i in range(n):
            if mask>>i&1:image|=1<<perm[i]
        if mask!=image:continue
        # alternating face trace with dimension popcount(mask)-1
        sign=(-1)**(mask.bit_count()-1)*mask_sign(mask,perm)
        trace+=sign
    return (-1)**dimension(n)*trace

def matvec(mat, v):
    return [sum(mat[i][j]*v[j] for j in range(4)) for i in range(4)]
M=[[1,-1,0,0],[0,0,1,-1],[1,-1,0,0],[0,0,1,0]]

def mult(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def trans_trace_power(h):
    P=[[int(i==j) for j in range(4)] for i in range(4)]
    for _ in range(h):P=mult(P,M)
    return sum(P[i][i] for i in range(4))

def path_weight(L):
    v=[1,-1,-1,0]; P=v[:]
    for _ in range(L-2): P=[sum(P[i]*M[i][j] for i in range(4)) for j in range(4)]
    return sum(P[i] for i in [0,1,2])

def verify():
    # Validate Cayley–Hamilton by exact 4x4 arithmetic, not sampling.
    P1=M
    P2=mult(P1,M)
    P3=mult(P2,M)
    P4=mult(P3,M)
    assert all(P4[i][j]-P3[i][j]+P2[i][j]-P1[i][j]==0
               for i in range(4) for j in range(4))
    # Exact transfer identities for the range; the characteristic polynomial
    # x(x-1)(x^2+1) and Cayley-Hamilton justify all larger exponents.
    for h in range(1,101):
        assert trans_trace_power(h)==(3 if h%4==0 else -1 if h%4==2 else 1)
    for L in range(2,101):assert path_weight(L)==(-1)**(L//2)
    tested_direct=tested_orbits=0
    for n in range(6,15):
        for reflection in (False,True):
            for a in range(n):
                p=[(a-i)%n if reflection else (a+i)%n for i in range(n)]
                want=character(n,a,reflection)
                c,F=orbital_sum(n,p)
                assert (-1)**(c+dimension(n))*F==want,(n,a,reflection,c,F,want)
                tested_orbits+=1
                if n<=12:
                    assert direct_character(n,p)==want,(n,a,reflection,'direct')
                    tested_direct+=1
    print('TIGHT_CYCLIC_NONCOVER_DIHEDRAL_CHECKS_OK', tested_orbits, tested_direct)

if __name__=='__main__':verify()
