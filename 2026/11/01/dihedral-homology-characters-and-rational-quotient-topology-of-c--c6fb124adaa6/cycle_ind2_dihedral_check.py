#!/usr/bin/env python3
"""Exact finite corroboration for dihedral homology characters of two-independence cycle complexes.
The all-order proof is in RESULT.md; the tests below do not replace it.
"""
from math import gcd


def admissible(mask, n):
    return all(not ((mask >> j) & 1 and (mask >> ((j+1)%n)) & 1 and
                    (mask >> ((j+2)%n)) & 1) for j in range(n))


def orbits(perm):
    seen=set(); out=[]
    for i in range(len(perm)):
        if i not in seen:
            o=[]; j=i
            while j not in seen:
                seen.add(j);o.append(j);j=perm[j]
            out.append(o)
    return out


def z_direct(perm):
    n=len(perm); oo=orbits(perm); masks=[]
    for o in oo:
        mask=sum(1<<i for i in o)
        masks.append(mask)
    total=0
    for choice in range(1<<len(oo)):
        subset=0
        for i,part in enumerate(masks):
            if (choice>>i)&1: subset |= part
        if admissible(subset,n):
            total += -1 if choice.bit_count()%2 else 1
    return total


def predicted(n,a,reflection):
    assert n>=4
    if not reflection:
        if n%4==0:
            return (3 if a%4==0 else -1 if a%4==2 else 1)
        if n%4==2:
            return (-1)**a
        return 1
    if n%4==0:
        return (-1)**(n//4)
    if n%2:
        return (-1)**((n+1)//4)
    return (-1)**(((n-2)//4)+a)


def homology_degree(n):
    k,t=divmod(n,4)
    return 2*k-1 if t in (0,1) else 2*k if t==2 else 2*k+1


def matrix_multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def check_transfer():
    M=[[1,-1,0,0],[0,0,1,-1],[1,-1,0,0],[0,0,1,0]]
    v=[[1,-1,-1,0]]
    identity=[[int(i==j) for j in range(4)] for i in range(4)]
    mm=matrix_multiply(M,M)
    assert matrix_multiply(v,[[mm[i][j]+identity[i][j] for j in range(4)] for i in range(4)]) == [[0,0,0,0]]
    Bv=v
    w=[[1],[1],[1],[0]]
    for L in range(2,37):
        b=matrix_multiply(Bv,w)[0][0]
        assert b==(-1)**(L//2),(L,b)
        Bv=matrix_multiply(Bv,M)
    # Characteristic polynomial: t(t-1)(t^2+1), checked by Cayley-Hamilton.
    M2=matrix_multiply(M,M);M3=matrix_multiply(M2,M);M4=matrix_multiply(M3,M)
    assert all(M4[i][j]-M3[i][j]+M2[i][j]-M[i][j]==0 for i in range(4) for j in range(4))


def check_all():
    check_transfer()
    cases=0
    for n in range(4,17):
        d=homology_degree(n)
        rank=3 if n%4==0 else 1
        for a in range(n):
            for reflection in (False,True):
                perm=[((a-i)%n if reflection else (i+a)%n) for i in range(n)]
                direct=(-1)**(d+1)*z_direct(perm)
                claim=predicted(n,a,reflection)
                assert direct==claim,(n,a,reflection,direct,claim)
                cases+=1
        assert predicted(n,0,False)==rank
        inv=sum(predicted(n,a,ref) for a in range(n) for ref in (False,True))//(2*n)
        expected_inv=int(n%8 in (0,1,7))
        assert inv==expected_inv,(n,inv,expected_inv)
    print(f'PASS: {cases} signed fixed-face Lefschetz traces (n=4..16), transfer identities and quotient invariants')
    print('CYCLE_IND2_DIHEDRAL_CHARACTER_EXACT_CHECK_OK')


if __name__=='__main__': check_all()
