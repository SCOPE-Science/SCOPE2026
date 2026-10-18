#!/usr/bin/env python3
"""Exact checks for the Lucas/Fibonacci cubic-window gcd transfer."""
from math import gcd
from itertools import permutations
K=320
F=[0,1]
L=[2,1]
for i in range(2,K+12):
    F.append(F[-2]+F[-1])
    L.append(L[-2]+L[-1])

def windows(U,k):
    return [sum(U[n+j]**3 for j in range(k)) for n in range(4)]

def vector_gcd(x):
    out=0
    for v in x:out=gcd(out,v)
    return out

M=[[-6,3,1,-3],[24,3,6,-8],[8,6,-3,24],[-3,-1,3,6]]
def det(A):
    z=0
    for q in permutations(range(4)):
        crossings=sum(q[i]>q[j] for i in range(4) for j in range(i+1,4))
        term=(-1)**crossings
        for i in range(4):term*=A[i][q[i]]
        z+=term
    return z
assert det(M)==5**6
for n in range(K):
    assert L[n]**3 == -6*F[n]**3+24*F[n+1]**3+8*F[n+2]**3-3*F[n+3]**3
for U in [F,L]:
    for n in range(K):
        a=lambda i:U[n+i]**3
        assert a(4)-3*a(3)-6*a(2)+3*a(1)+a(0)==0
assert [v%125 for v in windows(F,20)]==[30,30,65,120]
assert [v%125 for v in windows(L,20)]==[75,75,0,75]
assert {k: [v%25 for v in windows(L,k)] for k in [4,8,12,16]}=={
    4:[0,10,15,20],8:[20,10,10,0],12:[10,0,10,15],16:[20,5,15,15]}
assert (L[20]%25,L[21]%25)==(2,1)
for k in range(1,K+1):
    Hf=vector_gcd(windows(F,k))
    Hl=vector_gcd(windows(L,k))
    assert Hl == (5 if k%4==0 else 1)*Hf, (k,Hf,Hl)
    for p in [2,3,7,11,13,17,19]:
        def valuation(v,p):
            t=0
            while v%p==0:
                t+=1;v//=p
            return t
        assert valuation(Hf,p)==valuation(Hl,p)
print('VERIFY_OK')
print(f'window_lengths=1..{K}; directly_evaluated_windows={8*K}; recurrence_checks={2*K}; transfer_identities={K}')
print('transfer_matrix_determinant=15625; base_20_residues_mod_125: Fibonacci=[30,30,65,120]; Lucas=[75,75,0,75]')
print('example: k=4 Fibonacci_gcd=1 Lucas_gcd=5; k=8 Fibonacci_gcd=9 Lucas_gcd=45; k=20 Fibonacci_gcd=55 Lucas_gcd=275')
