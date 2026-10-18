#!/usr/bin/env python3
"""Finite semantic cross-check of bounded-width PINL arity identities.

Set-valued clauses are implemented directly, independently from the proof.
No third-party libraries are required. This checks finite instances only.
"""
from itertools import product
from random import Random


def transitive_closure(n, cover):
    rel = [[i == j for j in range(n)] for i in range(n)]
    for i,j in cover: rel[i][j] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                rel[i][j] |= rel[i][k] and rel[k][j]
    assert all(not(rel[i][j] and rel[j][i]) for i in range(n) for j in range(n) if i!=j)
    return rel


def is_upset(S, rel):
    n=len(rel)
    return all(not ((S>>i)&1) or not rel[i][j] or ((S>>j)&1)
               for i in range(n) for j in range(n))


def width(n, rel):
    return max(s.bit_count() for s in range(1<<n)
               if all(not(rel[i][j] or rel[j][i])
                      for i in range(n) for j in range(i+1,n)
                      if (s>>i)&1 and (s>>j)&1))


def max_antichain(n, rel):
    w=width(n,rel)
    return next(s for s in range(1<<n) if s.bit_count()==w and all(
         not(rel[i][j] or rel[j][i]) for i in range(n) for j in range(i+1,n)
         if (s>>i)&1 and (s>>j)&1))


def partitions(n, limit):
    """Nonempty unlabeled blocks, represented by tuples of index tuples."""
    if n == 0:
        yield ()
        return
    rgs=[0]*n
    def rec(i,m):
        if i==n:
            blocks=tuple(tuple(j for j in range(n) if rgs[j]==a) for a in range(m+1))
            yield blocks
        else:
            for a in range(min(m+1,limit-1)+1):
                rgs[i]=a
                yield from rec(i+1,max(m,a))
    yield from rec(1,0)


def witness(U,As,B):
    return (U & ~B)==0 and all(U&A for A in As)


def co_witness(U,As,B):
    return bool(U&B) or any((U & ~A)==0 for A in As)


def group_meet(As,p,allbits):
    return tuple(__import__('functools').reduce(lambda a,b:a&b,(As[i] for i in block),allbits) for block in p)


def group_join(As,p):
    return tuple(__import__('functools').reduce(lambda a,b:a|b,(As[i] for i in block),0) for block in p)


def all_ups(n,rel):
    return [s for s in range(1<<n) if is_upset(s,rel)]


def test_one(name,n,cover, exhaustive=True):
    rel=transitive_closure(n,cover)
    ups=all_ups(n,rel)
    w=width(n,rel)
    allbits=(1<<n)-1
    rr=Random(131067+n)
    comparisons=0
    for k in range(w+1,min(w+2,6)):
        pp=list(partitions(k,w))
        # Too large cases use deterministic random sample.
        raw=len(ups)**(k+1)
        cases=product(ups,repeat=k+1) if exhaustive and raw<=110000 else (
            tuple(rr.choice(ups) for _ in range(k+1)) for _ in range(2500 if k>=5 else 12000))
        for tup in cases:
            As=tup[:-1];B=tup[-1]
            meets=[group_meet(As,p,allbits) for p in pp]
            joins=[group_join(As,p) for p in pp]
            for U in ups:
                lhs=witness(U,As,B)
                rhs=any(witness(U,bs,B) for bs in meets)
                assert lhs==rhs,('BOX',name,k,U,As,B)
                lhs=co_witness(U,As,B)
                rhs=all(co_witness(U,bs,B) for bs in joins)
                assert lhs==rhs,('DIAMOND',name,k,U,As,B)
                comparisons+=2
    # Sharpness on every fixed carrier P: add generated upset Ustar.
    anti=max_antichain(n,rel)
    Ustar=0
    for i in range(n):
        if anti>>i&1:
            Ustar|=sum(1<<j for j in range(n) if rel[i][j])
    assert Ustar in ups
    low=[U for U in ups if U!=Ustar and U&~Ustar==0]
    high=low+[Ustar]
    low_tests=0
    for k in range(w):
        raw=len(ups)**(k+1)
        cases=product(ups,repeat=k+1) if raw<=170000 else (
            tuple(rr.choice(ups) for _ in range(k+1)) for _ in range(17000))
        for tup in cases:
            As=tup[:-1];B=tup[-1]
            dlow=all(co_witness(U,As,B) for U in low)
            dhigh=all(co_witness(U,As,B) for U in high)
            assert dlow==dhigh,(name,'lower mismatch',k,As,B)
            low_tests+=1
    A=list(i for i in range(n) if anti>>i&1)
    Ai=tuple(Ustar&~(1<<i) for i in A)
    assert len(Ai)==w and all(a in ups for a in Ai)
    assert all(co_witness(U,Ai,0) for U in low)
    assert not all(co_witness(U,Ai,0) for U in high)
    print(f'{name}: |P|={n} width={w} upsets={len(ups)} identities={comparisons} lower={low_tests} SHARP_OK')
    return comparisons,low_tests


def main():
    samples={
      'point':(1,[]),
      'chain4':(4,[(0,1),(1,2),(2,3)]),
      'fork4':(4,[(0,1),(0,2),(2,3)]),
      'diamond4':(4,[(0,1),(0,2),(1,3),(2,3)]),
      'two_chains4':(4,[(0,1),(2,3)]),
      'antichain3':(3,[]),
      'antichain4':(4,[]),
      'crown6':(6,[(0,3),(0,4),(1,4),(1,5),(2,5),(2,3)]),
    }
    c=l=0
    for name,(n,edges) in samples.items():
        cc,ll=test_one(name,n,edges)
        c+=cc;l+=ll
    print(f'PINL_WIDTH_VERIFY_OK comparisons={c} lower_checks={l}')

if __name__=='__main__': main()
