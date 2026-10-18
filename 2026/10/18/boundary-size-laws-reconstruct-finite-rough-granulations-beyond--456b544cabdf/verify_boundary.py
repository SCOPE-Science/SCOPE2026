#!/usr/bin/env python3
"""Exact finite checks of boundary-law factorization and reconstruction.

Usage: python3 check_boundary.py
This checks only finite cases and is not a substitute for the general proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations


def partitions(n, low=1):
    if n == 0:
        yield ()
    else:
        for v in range(low, n + 1):
            for rest in partitions(n-v, v):
                yield (v,) + rest


def direct_law(parts, a, d):
    n = sum(parts)
    blocks = []
    i = 0
    for b in parts:
        blocks.append(((1 << b)-1) << i)
        i += b
    out = [0] * (n+1)
    for mask in range(1 << n):
        size = mask.bit_count()
        weight = a**size * (d-a)**(n-size)
        border = sum(B.bit_count() for B in blocks if mask & B not in (0, B))
        out[border] += weight
    return tuple(Fraction(x, d**n) for x in out)


def multiply(x, y):
    z=[Fraction(0)] * (len(x)+len(y)-1)
    for i, c in enumerate(x):
        for j, e in enumerate(y):
            z[i+j]+=c*e
    return z


def factor_law(parts, a, d):
    p=Fraction(a,d)
    out=[Fraction(1)]
    for b in parts:
        q=p**b + (1-p)**b
        f=[Fraction(0)]*(b+1)
        f[0]=q
        f[b]=1-q
        out=multiply(out, f)
    return tuple(out)


def recover(law, p):
    last=max(i for i, c in enumerate(law) if c)
    norm=[c/law[0] for c in law[:last+1]]
    recovered=[]
    for b in range(2,last+1):
        q=p**b+(1-p)**b
        rho=(1-q)/q
        k=norm[b]/rho
        if k.denominator != 1 or k < 0:
            raise AssertionError(('invalid multiplicity', b, k))
        k=int(k)
        recovered.extend([b]*k)
        # exact formal-series inverse of (1+rho*z^b)^k
        for _ in range(k):
            for j in range(b,last+1):
                norm[j]-=rho*norm[j-b]
    assert norm[0]==1 and all(x==0 for x in norm[1:]), (recovered, norm)
    return tuple(recovered)


def main():
    cases=0; subsets=0; collisions={}
    for n in range(0,10):
        for parts in partitions(n):
            for a,d in ((1,2),(1,3),(2,5)):
                direct=direct_law(parts,a,d)
                formula=factor_law(parts,a,d)
                assert direct==formula, ('factor mismatch',parts,a,d)
                assert recover(direct, Fraction(a,d))==tuple(b for b in parts if b>=2), ('recovery',parts,a,d)
                cases+=1
                subsets+=1<<n
            law=direct_law(parts,1,2)
            sig=tuple(b for b in parts if b>=2)
            prior=collisions.get(law)
            if prior is not None: assert prior==sig, ('non-singleton collision',prior,sig)
            collisions[law]=sig
    # Same universe size: the full uniform law distinguishes every partition shape.
    for n in range(0,10):
        values={}
        for parts in partitions(n):
            law=direct_law(parts,1,2)
            assert law not in values, (parts,values[law])
            values[law]=parts
    # Sharp low-degree ambiguity at fixed n, fixed number of blocks, even including constant.
    for K in range(2,12):
        P=factor_law((K+1,K+3),1,2)
        Q=factor_law((K+2,K+2),1,2)
        assert P[:K+1]==Q[:K+1] and P!=Q
    print(f'VERIFY_OK partition_bias_cases={cases} direct_weighted_subsets={subsets} n_up_to=9 p=1/2,1/3,2/5 full_inverse=PASS fixed_n_uniqueness=PASS prefix_sharpness=PASS')

if __name__=='__main__':main()
