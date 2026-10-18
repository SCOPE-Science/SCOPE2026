#!/usr/bin/env python3
"""Finite exact checks of the Pascal-parity covariance identities.

This script tests finite identities only; the asymptotic theorem is proved analytically.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

ASSERTIONS = 0

def check(value):
    global ASSERTIONS
    assert value
    ASSERTIONS += 1

def supp(s):
    return frozenset(k for k in range(s + 1) if comb(s, k) % 2)

def pop(s):
    return s.bit_count()

# Independent check of Lucas' criterion and the crucial separation lemma.
for t in range(1, 256):
    for k in range(t + 1):
        check((k in supp(t)) == ((k & t) == k))
    check(len(supp(t)) == 2 ** pop(t))
    for s in range(t):
        check(len(supp(t) ^ supp(s)) >= 2 ** (pop(t) - 1))

for n in range(1, 10):
    for eps, pseq in [
        (F(1, 3), [F(1, 3)] * (n + 1)),
        (F(1, 4), [F(1, 4) if i % 2 else F(3, 4) for i in range(n + 1)]),
        (F(1, 5), [F(1, 5) if i % 3 == 0 else F(4, 5) for i in range(n + 1)]),
    ]:
        rho = 1 - 2 * eps
        a_n = sum(
            (F(comb(n, r), 2**n) * rho ** (2 ** (pop(r) - 1)))
            for r in range(1, n + 1)
        )
        for m in range(1, n):
            cross = F(0)
            for s in range(m + 1):
                for inc in range(n - m + 1):
                    t = s + inc
                    w = F(comb(m, s) * comb(n - m, inc), 2**n)
                    env_product = F(1)
                    for k in supp(s) ^ supp(t):
                        env_product *= 1 - 2 * pseq[k]
                    cross += w * env_product
            check(abs(cross) <= F(1, 2 ** (n - m)) + a_n)

# Exact direct enumeration of short paths and all frozen coefficient arrays:
# E[Q_N^2] is independently evaluated using path enumeration and covariances.
for n in range(2, 8):
    pp = [F(1, 3) if k % 2 else F(3, 5) for k in range(n)]
    def esign(m):
        return sum(F(comb(m, s), 2**m) *
                   __import__('functools').reduce(lambda a,k: a*(1-2*pp[k]),supp(s), F(1))
                   for s in range(m+1))
    def epair(m,j):
        if m==0:
            return esign(j)
        out=F(0)
        for s in range(m+1):
            for incr in range(j-m+1):
                t=s+incr
                e=F(1)
                for k in supp(s)^supp(t): e *= 1-2*pp[k]
                out+=F(comb(m,s)*comb(j-m,incr), 2**j)*e
        return out
    via_pair = F(n) + 2*sum((epair(m,j) for m in range(n) for j in range(m+1,n)),F(0))
    via_paths=F(0)
    for bb in product((0,1),repeat=n):
        pw=F(1)
        for k,b in enumerate(bb): pw*=pp[k] if b else 1-pp[k]
        for neg in product((0,1),repeat=n):
            s=0
            zz=[1]
            for j in range(1,n):
                s+=neg[j-1]
                zz.append((-1)**sum(bb[k] for k in supp(s)))
            q=sum(zz)
            via_paths += pw * F(q*q,2**n)
    check(via_paths==via_pair)
print(f"PASS: {ASSERTIONS} finite exact assertions (no claim of infinite computational proof)")
