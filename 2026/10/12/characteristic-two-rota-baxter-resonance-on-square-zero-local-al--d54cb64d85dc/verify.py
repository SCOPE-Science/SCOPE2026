#!/usr/bin/env python3
"""Exhaustive small finite-field verification of the weight-zero Rota--Baxter classification.
No third-party dependencies. Run: python3 verify.py
"""
from itertools import product
from math import prod


def add(a, b, q):
    return a ^ b if q in (2, 4) else (a+b) % q


def mul(a, b, q):
    if q == 4:
        a0, a1 = a & 1, (a >> 1) & 1
        b0, b1 = b & 1, (b >> 1) & 1
        return (a0 & b0 ^ a1 & b1) | ((a0 & b1 ^ a1 & b0 ^ a1 & b1) << 1)
    return (a * b) % q


def dot(v, w, q):
    s = 0
    for a, b in zip(v, w):
        s = add(s, mul(a, b, q), q)
    return s


def vec_add(v, w, q):
    return tuple(add(a, b, q) for a, b in zip(v, w))


def algebra_mul(v, w, q):
    out = [mul(v[0], w[0], q)]
    for i in range(1, len(v)):
        out.append(add(mul(v[0], w[i], q), mul(w[0], v[i], q), q))
    return tuple(out)


def transform(cols, v, q):
    n = len(cols)
    out = [0]*n
    for a, col in zip(v, cols):
        if a:
            for j, b in enumerate(col):
                out[j] = add(out[j], mul(a, b, q), q)
    return tuple(out)


def rank_columns(cols, q):
    n = len(cols)
    a = [[col[i] for col in cols] for i in range(n)]
    r = 0
    for j in range(n):
        ip = next((i for i in range(r, n) if a[i][j]), None)
        if ip is None:
            continue
        a[r], a[ip] = a[ip], a[r]
        inv = next(b for b in range(1,q) if mul(b,a[r][j],q)==1)
        a[r] = [mul(inv,z,q) for z in a[r]]
        for i in range(n):
            if i != r and a[i][j]:
                f=a[i][j]
                a[i] = [add(a[i][k], mul(f,a[r][k],q), q) if q in (2,4)
                        else (a[i][k]-mul(f,a[r][k],q))%q for k in range(n)]
        r+=1
        if r==n: break
    return r


def is_rb(cols, q):
    n = len(cols)
    zero = (0,)*n
    # Linear-bilinear identity: it suffices to test all ordered basis pairs.
    for i in range(n):
        for j in range(n):
            lhs = algebra_mul(cols[i], cols[j], q)
            # e_i P(e_j)+P(e_i)e_j. Products with basis i,j.
            if i == 0:
                r1=cols[j]
            elif cols[j][0]:
                r1=tuple(cols[j][0] if k==i else 0 for k in range(n))
            else:
                r1=zero
            if j == 0:
                r2=cols[i]
            elif cols[i][0]:
                r2=tuple(cols[i][0] if k==j else 0 for k in range(n))
            else:
                r2=zero
            rhs=transform(cols,vec_add(r1,r2,q),q)
            if lhs != rhs:
                return False
    return True


def is_squarezero_L(cols, q):
    n = len(cols)-1
    if any(col[0] for col in cols):
        return False
    for j in range(1,n+1):
        if transform(cols, cols[j], q) != (0,)*(n+1):
            return False
    if q % 2:
        if transform(cols,cols[0],q) != (0,)*(n+1):
            return False
    return True


def is_zero(cols):
    return all(not any(col) for col in cols)


def exponent_index(cols,q):
    if is_zero(cols):return 1
    # Operator square and cube; the theorem predicts index <= 3.
    p2=[transform(cols,v,q) for v in cols]
    if not any(any(col) for col in p2): return 2
    p3=[transform(cols,v,q) for v in p2]
    assert not any(any(col) for col in p3)
    return 3


def formula_count(n,q):
    def choose_gauss(n,k):
        if k<0 or k>n: return 0
        acc=1
        for i in range(k):
            acc*=q**(n-i)-1
        den=prod(q**i-1 for i in range(1,k+1))
        return acc//den
    def gl(r):
        return prod(q**r-q**i for i in range(r))
    by_rank={}
    by_index={1:1,2:0,3:0}
    for r in range(n//2+1):
        m=choose_gauss(n,r)*choose_gauss(n-r,r)*gl(r)
        by_rank[r] = m
        if q%2==0:
            by_index[3]+=m*(q**n-q**(n-r))
            by_index[2]+=m*q**n
        else:
            by_index[2]+=m*q**(n-r)
    by_index[2]-=1 + by_index[3]
    return by_rank,by_index


def check(n,q):
    d=n+1
    total=0
    by_index={1:0,2:0,3:0}
    diff=0
    for entries in product(range(q), repeat=d*d):
        cols=[entries[i*d:(i+1)*d] for i in range(d)]
        rb=is_rb(cols,q)
        predicted=is_squarezero_L(cols,q)
        assert rb==predicted,(n,q,cols,rb,predicted)
        if not rb:continue
        total+=1
        ix=exponent_index(cols,q)
        by_index[ix]+=1
    _,expect=formula_count(n,q)
    assert by_index==expect,(n,q,by_index,expect)
    print(f'field={q} dimension_radical={n} enumerated={q**(d*d)} RB={total} indexes={by_index} PASS',flush=True)

if __name__=='__main__':
    for n,q in [(1,2),(1,3),(2,2),(2,3),(3,2),(2,4)]:
        check(n,q)
    print('VERIFY_OK')
