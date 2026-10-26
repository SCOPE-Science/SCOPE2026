#!/usr/bin/env python3
"""Supplementary finite checks for alternating-adjoint paths and rank-range recovery.

All computations use Python's standard library. These checks do not replace
proof of the all-dimension statements.
"""
import math


def product_multiset(m, singular):
    factors = [math.cos(j * math.pi / (m + 1)) for j in range(1, (m // 2) + 1)]
    return sorted([c * s for s in singular for c in factors], reverse=True)


def recover(m, d, values):
    """Greedy exact-data inversion; small errors are tolerated only in this test."""
    factors = [math.cos(j * math.pi / (m + 1)) for j in range(1, (m // 2) + 1)]
    present = list(values)
    found = []
    for _ in range(d):
        if not present or present[0] < 1e-11:
            found.extend([0.0] * (d - len(found)))
            break
        s = present[0] / factors[0]
        found.append(s)
        for c in factors:
            target = c * s
            if present:
                j = min(range(len(present)), key=lambda z: abs(present[z] - target))
                if abs(present[j] - target) <= 1e-9 * max(1.0, target):
                    present.pop(j)
    return found


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def zero(n):
    return [[0j for _ in range(n)] for _ in range(n)]


def block_diagonal(blocks):
    dim = sum(len(b) for b in blocks)
    out = zero(dim)
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                out[off+i][off+j] = b[i][j]
        off += len(b)
    return out


def path(m, t):
    d = len(t)
    out = zero(m*d)
    for i in range(m-1):
        edge = t if i % 2 == 0 else dagger(t)
        for p in range(d):
            for q in range(d):
                out[i*d+p][(i+1)*d+q] = edge[p][q]
    return out


def test():
    count = 0
    for m in range(2, 11):
        l = m // 2
        for d in range(1, 7):
            k = (d-1)*l+1
            for spectral in (
                [2.0**(-j) for j in range(d)],
                [1.0]*d,
                [1.0]*(d-1)+[0.0],
                [1.0]*(d-1)+[1e-4],
            ):
                positives = product_multiset(m, spectral)
                r = recover(m, d, (positives+[0.0]*k)[:k])
                assert len(r) == d, (m,d,k,spectral,r)
                assert max(abs(x-y) for x,y in zip(r, spectral)) < 1e-8, (m,d,k,spectral,r)
                count += 1
            if d >= 2:
                factors = [math.cos(j*math.pi/(m+1)) for j in range(1,l+1)]
                p = factors[-1]/factors[0]
                s1 = [1.0]*(d-1)+[p/4]
                s2 = [1.0]*(d-1)+[p/2]
                a = product_multiset(m,s1)
                b = product_multiset(m,s2)
                assert all(abs(x-y)<1e-11 for x,y in zip(a[:k-1],b[:k-1]))
                assert abs(a[k-1]-b[k-1])>1e-7
                count += 1
    rt = math.sqrt(.5)
    u = [[rt,rt],[rt,-rt]]
    v = [[0j,1j],[1+0j,0j]]
    diag = [[3+0j,0j],[0j,1+0j]]
    t = multiply(multiply(u,diag),dagger(v))
    for m in range(2,9):
        change = block_diagonal([u if i%2==0 else v for i in range(m)])
        lhs = multiply(multiply(dagger(change),path(m,t)),change)
        rhs = path(m,diag)
        err = max(abs(lhs[i][j]-rhs[i][j]) for i in range(2*m) for j in range(2*m))
        assert err < 1e-12, (m,err)
        count += 1
    print('PASS: %d finite recovery, sharpness and unitary-block checks' % count)

if __name__ == '__main__':
    test()
