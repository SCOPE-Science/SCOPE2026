#!/usr/bin/env python3
"""Exact characteristic-11 Cartier and smooth-parameter checks for cyclic trigonal genus-four curves."""
import math
from collections import Counter
p=11

def comb3(n,u,v):
    return math.factorial(n)//(math.factorial(u)*math.factorial(v)*math.factorial(n-u-v))

def coeff(n,k,a,b):
    return sum(comb3(n,u,v)*pow(a,v,p)*pow(b,n-u-v,p)
               for u in range(n+1) for v in range(n-u+1)
               if 5*u+v == k) % p

def mat(a,b):
    # Basis [dx/y, dx/y^2, x dx/y^2, x^2 dx/y^2].
    # Nonzero input->output columns computed by the exponent-selection Cartier formula.
    # Entries take pth roots, trivial on F11.
    M=[[0]*4 for _ in range(4)]
    for ell in range(3):M[1+ell][0]=coeff(7, 11*(ell+1)-1,a,b)
    for i in range(3):M[0][1+i]=coeff(3,10-i,a,b)
    return M

def rank(A):
    m=[r[:] for r in A]; rows=len(m); cols=len(m[0]);rank0=0
    for j in range(cols):
        h=next((i for i in range(rank0,rows) if m[i][j]%p),None)
        if h is None:continue
        m[rank0],m[h]=m[h],m[rank0]
        inv=pow(m[rank0][j]%p,-1,p)
        m[rank0]=[x*inv%p for x in m[rank0]]
        for i in range(rows):
            if i!=rank0:
                c=m[i][j]%p
                m[i]=[(z-c*w)%p for z,w in zip(m[i],m[rank0])]
        rank0+=1
    return rank0

def multiply(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4))%p for j in range(4)] for i in range(4)]

def stable_rank(M):
    A=M
    for _ in range(6):A=multiply(A,M)
    return rank(A)
assert coeff(7,10,2,3)==(10*pow(3,5,11)+9*pow(2,5,11)*3)%11
for a in range(11):
    for b in range(11):
        smooth=((pow(b,4,11)+3*pow(a,5,11))%11!=0)
        if not smooth:continue
        M=mat(a,b);r=rank(M);f=stable_rank(M)
        if b==0: expected=(0,4)
        elif (pow(b,4,11)-9*pow(a,5,11))%11==0:expected=(0,2)
        else:expected=(2,2)
        assert (f,4-r)==expected,(a,b,M,f,r,expected)
counts=Counter()
for a in range(11):
    for b in range(11):
        if (pow(b,4,11)+3*pow(a,5,11))%11==0:continue
        M=mat(a,b)
        counts[(stable_rank(M),4-rank(M))]+=1
print('F11 smooth parameter counts:',dict(counts))
assert counts=={(0,4):10,(0,2):10,(2,2):90}
print('CARTIER_VERIFY_OK')
