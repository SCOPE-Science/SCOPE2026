#!/usr/bin/env python3
"""Standalone exhaustive checks for product ranks of twisted-code idempotents."""
from itertools import product
from collections import Counter
from math import prod


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return a*b % q
    z = 0
    aa, bb = a, b
    while bb:
        if bb & 1:
            z ^= aa
        bb >>= 1
        aa <<= 1
        if aa & 4:
            aa ^= 7  # t^2+t+1=0 over F_2
    return z


def matrix_mul(A, B, n, q):
    out = [0]*(n*n)
    for i in range(n):
        for j in range(n):
            v = 0
            for k in range(n):
                v = add(v, mul(A[i*n+k], B[k*n+j], q), q)
            out[i*n+j] = v
    return tuple(out)


def rank(A, rows, cols, q):
    M = [[A[i*cols+j] for j in range(cols)] for i in range(rows)]
    r = 0
    for col in range(cols):
        pivot = next((i for i in range(r, rows) if M[i][col]), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        pv = M[r][col]
        inverse = next(v for v in range(1, q) if mul(v, pv, q) == 1)
        M[r] = [mul(v, inverse, q) for v in M[r]]
        for i in range(rows):
            if i == r or M[i][col] == 0:
                continue
            coefficient = M[i][col]
            # In characteristic 2, additive inverse equals itself.
            minus = coefficient if q == 4 else (-coefficient)%q
            M[i] = [add(M[i][j], mul(minus, M[r][j], q), q) for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def gaussian(n, r, q):
    if r < 0 or r > n:
        return 0
    numerator = prod(q**(n-i)-1 for i in range(r))
    denominator = prod(q**(r-i)-1 for i in range(r))
    return numerator // denominator


def gl(n, q):
    return prod((q**n-q**i) for i in range(n))


def invariants(A, n, q):
    k = n - rank(A,n,n,q)
    A2 = matrix_mul(A,A,n,q)
    # dim(ker A cap im A) = rank A - rank A^2
    s = rank(A,n,n,q)-rank(A2,n,n,q)
    t = k - s
    assert s >= 0 and t >= 0
    return (t,s)


def predicted(t,s,q):
    out=Counter()
    for r in range(t+1):
        for u in range(t+1):
            for v in range(max(0,r+u-t),min(r,u)+1):
                out[(r,u,v)]=(gaussian(t,r,q)*gaussian(t-r,u-v,q)*gaussian(r,v,q)
                              *q**(r*(t-r)+u*(t-u)+(t-r-u+v)*v+2*s*(r+u)))
    return out


def ambient_check(A,n,q,lambdas,name):
    t,s=invariants(A,n,q)
    zero=(0,)*(n*n)
    expected=predicted(t,s,q)
    for la in lambdas:
        idempotents=[]
        for X in product(range(q),repeat=n*n):
            if matrix_mul(X,X,n,q)!=X:
                continue
            AX=matrix_mul(A,X,n,q)
            XA=matrix_mul(X,A,n,q)
            if AX!=tuple(mul(la,v,q) for v in XA):
                continue
            assert AX==XA==zero
            idempotents.append((X,rank(X,n,n,q)))
        actual=Counter()
        for X,r in idempotents:
            for Y,u in idempotents:
                v=rank(matrix_mul(X,Y,n,q),n,n,q)
                actual[(r,u,v)]+=1
        assert actual==expected,(name,q,la,actual,expected)
        assert sum(actual.values())==len(idempotents)**2
        print('PASS',name,'q',q,'lambda',la,'n',n,'t',t,'s',s,'idempotents',len(idempotents),'pairs',sum(actual.values()))


def sandwich_check(t,s,q):
    n=t+s
    star=lambda X,Y:tuple(sum(X[i*n+k]*Y[k*n+j] for k in range(t))%q
                           for i in range(n) for j in range(n))
    idems=[X for X in product(range(q),repeat=n*n) if star(X,X)==X]
    actual=Counter()
    for X in idems:
        rx=rank(X,n,n,q)
        for Y in idems:
            actual[(rx,rank(Y,n,n,q),rank(star(X,Y),n,n,q))]+=1
    assert actual==predicted(t,s,q)
    print('PASS sandwich',q,t,s,'idempotents',len(idems),'pairs',sum(actual.values()))
    return actual


def main():
    # Full ambient matrix enumeration checks, without imposing predicted block forms.
    cases=[
       ('zero_3',3,3,(0,)*9,[2]),
       ('diagonal_rank1_3',3,3,(1,0,0,0,0,0,0,0,0),[2]),
       ('J2_plus_J1_3',3,3,(0,1,0,0,0,0,0,0,0),[2]),
       ('J3_3',3,3,(0,1,0,0,0,1,0,0,0),[2]),
       ('diagonal_rank2_3',3,3,(1,0,0,0,2,0,0,0,0),[2]),
       ('mixed_J2_nonzero_3',3,3,(0,1,0,0,0,0,0,0,1),[2]),
       ('invertible_3',3,3,(1,0,0,0,1,0,0,0,2),[2]),
       ('zero_2',2,5,(0,0,0,0),[2,3,4]),
       ('J2_2',2,5,(0,1,0,0),[2,3,4]),
       ('diagonal_2',2,5,(1,0,0,0),[2,3,4]),
       ('extension_zero_2',2,4,(0,0,0,0),[2,3]),
       ('extension_J2_2',2,4,(0,1,0,0),[2,3]),
       ('extension_diagonal_2',2,4,(1,0,0,0),[2,3]),
       ('extension_J2_plus_J1',3,4,(0,1,0,0,0,0,0,0,0),[2,3]),
    ]
    for name,n,q,A,lambdas in cases:
        ambient_check(A,n,q,lambdas,name)
    p=sandwich_check(2,1,3)
    assert sum(p.values())==36100
    assert p[(1,1,0)]==2916 and p[(1,1,1)]==8748
    print('ALL_EXACT_CHECKS_PASSED:',sum(len(c[-1]) for c in cases),'ambient field-twist cases, plus full Munn case')


if __name__=='__main__':
    main()
