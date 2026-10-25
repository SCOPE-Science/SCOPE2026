#!/usr/bin/env python3
"""Exact small-zero-sum certificate for order-thirteen multiplicative subgroups."""
from itertools import combinations_with_replacement
from math import comb, isqrt

ORDER = 13
EXPECTED_3 = {53, 2731}
EXPECTED_4 = {53, 79, 131, 157, 1327, 2003, 7229, 398581}

# Each column is the multiplication of an integral basis vector by a sum
# of thirteenth roots of unity, with x^12 = -(1+...+x^11).
def cyclo_matrix(exponents):
    M = [[0]*12 for _ in range(12)]
    for j in range(12):
        for k in exponents:
            e = (j+k) % ORDER
            if e == 12:
                for i in range(12): M[i][j] -= 1
            else:
                M[e][j] += 1
    return M

def bareiss_det(M):
    A = [row[:] for row in M]
    n = len(A)
    den, sign = 1, 1
    for k in range(n-1):
        if A[k][k] == 0:
            for i in range(k+1,n):
                if A[i][k] != 0:
                    A[k],A[i] = A[i],A[k]
                    sign = -sign
                    break
            else: return 0
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = A[i][j]*pivot-A[i][k]*A[k][j]
                assert num % den == 0
                A[i][j] = num // den
            A[i][k] = 0
        den = pivot
    return sign*A[-1][-1]

def factors(n):
    assert n>0
    fs={}
    d=2
    while d*d<=n:
        while n%d==0:
            fs[d]=fs.get(d,0)+1;n//=d
        d=3 if d==2 else d+2
    if n>1: fs[n]=fs.get(n,0)+1
    return fs

def orbit(rep):
    return {tuple(sorted((u*k+v)%ORDER for k in rep))
            for u in range(1,ORDER) for v in range(ORDER)}

def classify(t):
    remaining=set(combinations_with_replacement(range(ORDER),t))
    assert len(remaining)==comb(ORDER+t-1,t)
    rows=[];primes=set()
    while remaining:
        rep=min(remaining)
        eq=orbit(rep)
        assert eq<=remaining
        remaining-=eq
        norm=abs(bareiss_det(cyclo_matrix(rep)))
        fs=factors(norm)
        candidate={p for p in fs if p%ORDER==1}
        primes.update(candidate)
        rows.append((rep,len(eq),norm,fs))
    assert sum(row[1] for row in rows)==comb(ORDER+t-1,t)
    return rows, primes

def primitive_order13(p):
    assert p%13==1
    for h in range(2,p):
        q=pow(h,(p-1)//13,p)
        if q!=1:
            assert pow(q,13,p)==1
            return q
    raise RuntimeError('No generator')

def modular_witness(p,t):
    q=primitive_order13(p)
    vals=[pow(q,i,p) for i in range(13)]
    for exps in combinations_with_replacement(range(13),t):
        if sum(vals[e] for e in exps)%p==0:
            return (q,exps)
    return None

def main():
    rows3,P3=classify(3)
    rows4,P4=classify(4)
    assert len(rows3)==5 and len(rows4)==16
    assert P3==EXPECTED_3,(P3,EXPECTED_3)
    assert P4==EXPECTED_4,(P4,EXPECTED_4)
    for t,rows in ((3,rows3),(4,rows4)):
        print('LENGTH',t,'orbit_count',len(rows),'all_multisets',sum(row[1] for row in rows))
        for rep,sz,norm,fs in rows:
            print(' orbit',rep,'size',sz,'norm',norm,'factors',fs)
    allp=sorted(P3|P4)
    for p in allp:
        q=primitive_order13(p)
        h3=modular_witness(p,3)
        h4=modular_witness(p,4)
        assert bool(h3)==(p in P3)
        assert bool(h4)==(p in P4)
        print('PRIME',p,'order13_generator',q,'3_witness',h3,'4_witness',h4)
    print('PASS: complete affine-orbit census; exact determinant norms; factorizations; direct finite-field witnesses')
    print('m=3:',sorted(P3))
    print('m=4:',sorted(P4-P3))
    print('m>=5: every other prime p with p congruent 1 modulo 13')
if __name__=='__main__':main()
