#!/usr/bin/env python3
"""Checks exact ternary size-relational quotients and depth-one countermodels.
Self-contained; only Python 3 standard library.
"""
from itertools import product

def klass(n,k,m):
    return n if n<k else k+(n-k)%m

def theoretical_rel(k,m):
    q=k+m
    R=set()
    for a in range(q):
        for b in range(q):
            if a<k and b<k:
                vals=range(max(a,b),a+b+1)
                R.update((a,b,klass(c,k,m)) for c in vals)
            elif a<k:
                # choose b-tail representative with n congruent to b-k modulo m
                R.update((a,b,klass(b+t,k,m)) for t in range(a+1))
            elif b<k:
                R.update((a,b,klass(a+t,k,m)) for t in range(b+1))
            else:
                R.update((a,b,c) for c in range(k,q))
    return R

def reachable_at_a(a,k,m,cap):
    res=set()
    for b in range(cap+1):
        for c in range(max(a,b),a+b+1):
            res.add((klass(b,k,m),klass(c,k,m)))
    return res

def check():
    checked=0
    for m in range(1,8):
        for k in range(0,8):
            cap=5*(k+m)+20
            rows={}
            for a in range(cap+1):
                ra=reachable_at_a(a,k,m,cap)
                cls=klass(a,k,m)
                if cls in rows and rows[cls]!=ra:
                    stable=False
                    break
                rows[cls]=ra
            else:
                stable=True
            want=(m==1 or k>=m-1)
            assert stable==want,(k,m,stable,want)
            if want:
                R=theoretical_rel(k,m)
                for a in range(3*(k+m)+3):
                    rel={(b,c) for x,b,c in R if x==klass(a,k,m)}
                    assert rel==reachable_at_a(a,k,m,cap),(k,m,a,rel,reachable_at_a(a,k,m,cap))
                    checked+=1
            else:
                # Explicit implication separates equal-typed X with cardinalities k and k+m.
                # p(y) iff y lies in tail class k (residue k modulo m).
                # q(z) iff z avoids tail class k+(k+1)%m.
                a0=k
                a1=k+m
                source=k
                bad=k+(k+1)%m
                assert source!=bad
                def impl_at(a):
                    for b in range(cap+1):
                        if klass(b,k,m)!=source: continue
                        for c in range(max(a,b),a+b+1):
                            if klass(c,k,m)==bad:
                                return False
                    return True
                assert klass(a0,k,m)==klass(a1,k,m)
                assert impl_at(a0) and not impl_at(a1),(k,m,a0,a1,bad)
                checked+=1
    # Independently enumerate real subsets of small finite universes to
    # confirm the elementary interval-of-union-sizes lemma.
    for N in range(1,8):
        universe=range(1<<N)
        by_size=[[] for _ in range(N+1)]
        for Y in universe: by_size[Y.bit_count()].append(Y)
        for X in universe:
            a=X.bit_count()
            for b in range(N+1):
                got={(X|Y).bit_count() for Y in by_size[b]}
                wanted=set(range(max(a,b),min(N,a+b)+1))
                assert got==wanted,(N,X,b,got,wanted)
                checked+=1
    print('CARDINALITY_QUOTIENT_VERIFY_OK',checked)

if __name__=='__main__': check()
