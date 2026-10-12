#!/usr/bin/env python3
"""Standalone exact verifier: finite two-level complete S4 frames.
No external modules, no external files, deterministic exhaustive tests.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def onto(n,k):
    return sum((-1)**j*comb(k,j)*(k-j)**n for j in range(k+1))


def onto_with_sink(n,k):
    return sum((-1)**j*comb(k,j)*(k+1-j)**n for j in range(k+1))


def forest(N,r):
    assert N >= r >= 1
    return 1 if N==r else r*N**(N-r-1)


def predicted(p,q):
    E,I,A = Counter(), Counter(), Counter()
    if q>=2:
        E[2]=q;I[2]=q;A[2]=q
        for k in range(1,p+1):
            rank=2**(q+k)
            E[rank]+=factorial(q)*comb(p,k)*onto(p,k)
            I[rank]+=comb(p,k)*k**(p-k)
            A[rank]+=factorial(q)*comb(p,k)*factorial(k)*forest(p,k)
    else:
        for k in range(p+1):
            rank=2**(k+1)
            E[rank]+=comb(p,k)*onto_with_sink(p,k)
            I[rank]+=comb(p,k)*(k+1)**(p-k)
            A[rank]+=comb(p,k)*factorial(k)*forest(p+1,k+1)
    return E,I,A


def bounded(f,p,q):
    n=p+q
    for x in range(n):
        successors=([x]+list(range(p,n))) if x<p else [x]
        y=f[x]
        target=({y}|set(range(p,n))) if y<p else {y}
        if {f[z] for z in successors} != target:
            return False
    return True


def eventual_image(f):
    g=tuple(f)
    seen=set()
    while g not in seen:
        seen.add(g)
        h=tuple(f[g[x]] for x in range(len(f)))
        if len(set(h))==len(set(g)):
            return len(set(h))
        g=h
    raise AssertionError('image cardinality must stabilize')


def direct_modal_preserved(f,p,q):
    n=p+q
    def diamond(subset):
        return frozenset(x for x in range(n) if ((x in subset or bool(set(range(p,n)) & subset)) if x<p else x in subset))
    for b in range(1<<n):
        S=frozenset(i for i in range(n) if b>>i&1)
        pre=lambda U: frozenset(i for i in range(n) if f[i] in U)
        if diamond(pre(S))!=pre(diamond(S)):
            return False
    return True


def run():
    candidates=bounded_maps=direct_checks=comparisons=0
    cases=[]
    for n in range(2,7):
        for p in range(1,n):
            q=n-p
            E,I,A=(Counter() for _ in range(3))
            for f in product(range(n),repeat=n):
                candidates+=1
                b=bounded(f,p,q)
                if n<=4:
                    assert b==direct_modal_preserved(f,p,q),(p,q,f)
                    direct_checks+=1
                if not b:continue
                bounded_maps+=1
                E[2**len(set(f))]+=1
                if all(f[f[x]]==f[x] for x in range(n)):
                    I[2**len(set(f))]+=1
                A[2**eventual_image(f)]+=1
            e,i,a=predicted(p,q)
            assert E==e,(p,q,'E',E,e)
            assert I==i,(p,q,'I',I,i)
            assert A==a,(p,q,'A',A,a)
            comparisons+=3
            cases.append((p,q,sum(E.values()),sum(I.values()),sum(A.values())))
    for p in range(1,20):
        for q in range(1,8):
            E,I,A=predicted(p,q)
            assert sum(E.values())==((p+1)**p if q==1 else factorial(q)*p**p+q)
            assert sum(I.values())== (sum(comb(p,k)*(k+1)**(p-k) for k in range(p+1)) if q==1 else q+sum(comb(p,k)*k**(p-k) for k in range(1,p+1)))
            assert sum(A.values())==sum(E.values())
            comparisons+=3
    print('VERIFY_OK',f'cases={len(cases)}',f'candidate_functions={candidates}',f'bounded_maps={bounded_maps}',f'direct_modal_checks={direct_checks}',f'exact_comparisons={comparisons}')
    for c in cases: print('CASE',*c)

if __name__=='__main__':run()
