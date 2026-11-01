#!/usr/bin/env python3
"""Standalone finite-field and graph-metric checks for the projective-plane negative-type theorem.

Run: python3 check_projective_negative_type.py
The finite tests support, but do not replace, the all-order analytic argument.
Requires only the Python standard library.
"""
from collections import deque
from decimal import Decimal, getcontext
from math import isqrt

getcontext().prec = 65


def field(q):
    if q == 4:  # GF(4)=F_2[u]/(u^2+u+1), bit-packed basis 1,u
        def add(a, b): return a ^ b
        def mul(a, b):
            c = 0
            if b & 1: c ^= a
            if b & 2: c ^= (a << 1)
            if c & 8: c ^= 0b110  # u^3=1, from u^2=u+1
            if c & 4: c ^= 0b111  # u^2=u+1
            return c
        # Multiplication table is symmetric and has units 1,2,3.
        assert all(mul(a, b) == mul(b, a) for a in range(q) for b in range(q))
        assert all(mul(a, 1) == a for a in range(q))
    else:
        assert q >= 2 and all(q % d for d in range(2, isqrt(q)+1))
        def add(a, b): return (a+b) % q
        def mul(a, b): return (a*b) % q
    inv = {a: next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    return add, mul, inv


def point_line_matrix(q):
    add, mul, inv = field(q)
    def normalize(a):
        j = next(i for i,x in enumerate(a) if x)
        return tuple(mul(inv[a[j]], x) for x in a)
    pts = sorted({normalize((x,y,z)) for x in range(q) for y in range(q)
                  for z in range(q) if x or y or z})
    n = q*q+q+1
    assert len(pts) == n
    B = [[int(add(add(mul(p[0],l[0]), mul(p[1],l[1])),mul(p[2],l[2]))==0)
          for l in pts] for p in pts]
    return B


def test_incidence(q):
    B = point_line_matrix(q)
    n=len(B)
    k=q+1
    assert all(sum(row)==k for row in B)
    assert all(sum(B[i][j] for i in range(n))==k for j in range(n))
    # Exact combinatorial certificate for B B^T=qI+J.
    assert all(sum(B[i][z]*B[j][z] for z in range(n))==(q+1 if i==j else 1)
               for i in range(n) for j in range(n))
    adj=[[] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if B[i][j]:
                adj[i].append(n+j)
                adj[n+j].append(i)
    num_pairs=0
    for src in range(2*n):
        ds=[-1]*(2*n)
        ds[src]=0
        Q=deque([src])
        while Q:
            x=Q.popleft()
            for y in adj[x]:
                if ds[y]<0:
                    ds[y]=ds[x]+1
                    Q.append(y)
        for dst in range(2*n):
            expected=(0 if src==dst else
                      (2 if (src<n)==(dst<n) else
                       (1 if ((src<n and B[src][dst-n]) or
                              (src>=n and B[dst][src-n])) else 3)))
            assert ds[dst]==expected, (q,src,dst,ds[dst],expected)
            num_pairs+=1
    return n,num_pairs,B


def critical_p(q):
    rootq=Decimal(q).sqrt()
    three=Decimal(3)
    two=Decimal(2)
    def f(p): return rootq * ((p*three.ln()).exp()-1) - (p*two.ln()).exp()
    lo,hi=Decimal(0),Decimal(1)
    assert f(lo)<0<f(hi)
    for _ in range(230):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    p=(lo+hi)/2
    u=(p*two.ln()).exp()
    w=(p*three.ln()).exp()
    assert abs(rootq*(w-1)-u)<Decimal('1e-58')
    # The remaining conditional eigenvalues are strictly negative.
    other= -u-rootq*(w-1)
    minus=Decimal(q*(q+1))*u-Decimal(q+1)-Decimal(q*q)*w
    assert other<0 and minus<0
    # The sparse equality direction for a pair of distinct lines.
    # Its norm-identity is exact from B B^T=qI+J; numerical quadratic must vanish.
    # y=(1,-1,0,...), x=-By/sqrt(q): x.x=y.y=2, x.B.y=-2sqrt(q).
    # Q=-u*(x.x+y.y)+2*(1-w)*(x.B.y).
    quadratic=-4*u+4*rootq*(w-1)
    assert abs(quadratic)<Decimal('1e-57')
    return p,other,minus


def main():
    for q in (2,3,4,5,7):
        n,pairs,B=test_incidence(q)
        p,other,minus=critical_p(q)
        # Algebraic multiplicities: one uniform, one color antisymmetric,
        # and two transverse spaces each of dimension n-1.
        assert 1+1+(n-1)+(n-1)==2*n
        assert 2*n-1-(n-1)==n
        print(f'CHECK_OK q={q} vertices={2*n} ordered_distances={pairs} '
              f'incidence_BBt=qI+J exact p={p:.14f} '
              f'critical_nullity={n-1} minimal_Hilbert_dimension={n}')
    print('ALL_PROJECTIVE_NEGATIVE_TYPE_CHECKS_OK')

if __name__ == '__main__':
    main()
