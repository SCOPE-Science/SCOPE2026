#!/usr/bin/env python3
from itertools import product

# Tiny exact finite fields used only for separate replay checks.
# Elements are integers 0..q-1. q=4 uses F2[t]/(t^2+t+1), bits encode coefficients.

def add(a,b,q):
    if q==4: return a ^ b
    return (a+b)%q

def mul(a,b,q):
    if q!=4: return (a*b)%q
    # polynomial multiplication over F2, modulus x^2+x+1 (0b111)
    r=0; aa=a; bb=b
    while bb:
        if bb&1: r ^= aa
        bb >>= 1
        aa <<= 1
    # reduce degrees >=2
    for k in range(4,1,-1):
        if r & (1<<k):
            r ^= 0b111 << (k-2)
    return r & 0b11

def madd(acc,a,b,q):
    return add(acc,mul(a,b,q),q)

def mm(A,B,q):
    C=[[0]*3 for _ in range(3)]
    for i in range(3):
        for k in range(3):
            aik=A[i][k]
            if aik==0: continue
            for j in range(3):
                C[i][j]=madd(C[i][j],aik,B[k][j],q)
    return C

def identity(q):
    return [[1,0,0],[0,1,0],[0,0,1]]

def iter_mats(q):
    for v in product(range(q), repeat=9):
        yield [list(v[0:3]),list(v[3:6]),list(v[6:9])]

def is_involution(U,q):
    return mm(U,U,q)==identity(q)

def formulas(q):
    if q%2:
        return 4*q**3+2*q**2+2, 2*q*(q**2-1)
    return 2*q**3-q, q*(q**2-1)

def replay(q):
    # For A=E12, tr(AU)=U21; for A=E11, tr(AU)=U11.
    total=0; nil_count=0; semi_count=0
    for U in iter_mats(q):
        if is_involution(U,q):
            total += 1
            if U[1][0]==0: nil_count += 1
            if U[0][0]==0: semi_count += 1
    expected_nil, expected_semi=formulas(q)
    assert nil_count==expected_nil,(q,nil_count,expected_nil)
    assert semi_count==expected_semi,(q,semi_count,expected_semi)
    return q,total,nil_count,semi_count

if __name__=='__main__':
    for q in (2,3,4):
        q,total,n,s=replay(q)
        print(f'q={q}: involutions={total}; trace-zero-rank1 factors={n}; nonzero-trace-rank1 factors={s}; OK')
