#!/usr/bin/env python3
"""Exact finite-field checks for a binary moving-corner cycle census.

The logical theorem is proved algebraically; finite checks are regression tests.
"""

def advance(z, d, e):
    out = 0
    for i in range(d):
        for j in range(e):
            bit = (z >> (i*e+j)) & 1
            if i >= 2: bit ^= (z >> ((i-2)*e+j)) & 1
            if j >= 2: bit ^= (z >> (i*e+j-2)) & 1
            if i >= 2 and j >= 2: bit ^= (z >> ((i-2)*e+j-2)) & 1
            out |= bit << (i*e+j)
    return out


def rank_columns(cols):
    basis = {}
    for x in cols:
        while x:
            i = x.bit_length()-1
            if i in basis: x ^= basis[i]
            else:
                basis[i] = x
                break
    return len(basis)


def kernel_dim_direct(d, e, q):
    cols = []
    for k in range(d*e):
        b = 1 << k
        z = b
        for _ in range(q): z = advance(z, d, e)
        cols.append(z ^ b)
    return d*e-rank_columns(cols)


def formula(d, e, q):
    a = 2*q
    return sum(min(a,max(0,d-t*a))*min(a,max(0,e-t*a))
               for t in range(max(d,e)//a+1))


def test():
    cases = 0
    for d in range(1,10):
        for e in range(1,10):
            for r in range(5):
                q = 1 << r
                calc = kernel_dim_direct(d,e,q)
                expect = formula(d,e,q)
                assert calc == expect, (d,e,q,calc,expect)
                cases+=1
    small = 0
    for d in range(1,5):
        for e in range(1,5):
            if d*e > 12: continue
            for r in range(4):
                q=1<<r
                count = 0
                for z in range(1 << (d*e)):
                    v=z
                    for _ in range(q): v=advance(v,d,e)
                    count += v==z
                assert count == (1 << formula(d,e,q)),(d,e,q,count)
                small+=1
    for k in range(2,5):
        for j in range(0,k+1):
            d,e=1<<k,1<<j
            q=(1<<(k-1))
            kprev=formula(d,e,q//2)
            assert 2*kprev==d*e,(d,e,kprev)
    print('PASS: {} exact matrix-rank comparisons and {} exhaustive fixed-point counts; dyadic half-rank checks passed'.format(cases,small))

if __name__=='__main__':test()
