#!/usr/bin/env python3
"""Finite checks for the two-state reduction in bilateral exact-truthmaker semantics.

This checks exact recursive set semantics against the four-bit local profile
recurrences, with unrestricted independent positive/negative valuations.
It is a finite corroboration, not a proof for all formulas or all chains.
"""
from itertools import product


def P(i): return ('atom', i)
def N(x): return ('neg', x)
def A(x,y): return ('and',x,y)
def O(x,y): return ('or',x,y)


def explicit(f, atoms, n):
    """Return (positive states, negative states), subsets of 0..n-1."""
    op=f[0]
    if op=='atom': return atoms[f[1]]
    if op=='neg':
        a,b=explicit(f[1],atoms,n)
        return b,a
    a,b=explicit(f[1],atoms,n)
    c,d=explicit(f[2],atoms,n)
    join=lambda x,y: frozenset(max(u,v) for u in x for v in y)
    if op=='and': return join(a,c),b|d
    if op=='or': return a|c,join(b,d)
    raise ValueError(op)


def local(f, atoms, s):
    """Return ((at_plus, at_minus),(prefix_plus,prefix_minus))."""
    op=f[0]
    if op=='atom':
        pp,pm=atoms[f[1]]
        return ((s in pp,s in pm),(any(x<=s for x in pp),any(x<=s for x in pm)))
    if op=='neg':
        (ap,am),(hp,hm)=local(f[1],atoms,s)
        return ((am,ap),(hm,hp))
    (ap,am),(hp,hm)=local(f[1],atoms,s)
    (bp,bm),(kp,km)=local(f[2],atoms,s)
    if op=='and':
        return ((ap and kp or hp and bp,am or bm),(hp and kp,hm or km))
    if op=='or':
        return ((ap or bp,am and km or hm and bm),(hp or kp,hm and km))
    raise ValueError(op)


def compare_profile(f,atoms,n):
    pos,neg=explicit(f,atoms,n)
    for s in range(n):
        (ap,am),(hp,hm)=local(f,atoms,s)
        assert (ap,am)==(s in pos,s in neg),(f,atoms,n,s,'exact')
        assert (hp,hm)==(bool([x for x in pos if x<=s]),bool([x for x in neg if x<=s])),(f,atoms,n,s,'prefix')


def main():
    formulas=[P(0),P(1),N(P(0)),N(P(1)),A(P(0),P(1)),O(P(0),P(1)),
              A(P(0),O(P(0),P(1))),
              N(A(P(0),P(1))),N(O(P(0),P(1))),
              A(N(P(0)),O(P(1),N(P(0)))),
              O(A(P(0),N(P(1))),N(A(P(0),P(1))))]
    formulas += [op(x,y) for op in (A,O) for x,y in product(formulas[:9],repeat=2)]
    formulas += [N(x) for x in formulas[:18]]
    profile_cases=0
    for n,k in [(1,2),(2,2),(3,2),(4,1)]:
        total=2**(2*k*n)
        for bits in range(total):
            sets=[]
            for i in range(2*k):
                v=frozenset(j for j in range(n) if bits & (1<<(i*n+j)))
                sets.append(v)
            atoms=[(sets[2*i],sets[2*i+1]) for i in range(k)]
            subset_formulas=formulas
            if k==1:
                subset_formulas=[P(0),N(P(0)),A(P(0),N(P(0))),O(P(0),N(P(0))),N(A(P(0),P(0))),A(P(0),O(P(0),P(0)))]
            for f in subset_formulas:
                compare_profile(f,atoms,n)
                profile_cases+=1
    # Exhaustively verify the semiring gate recurrence on all subset pairs of chains of size <=6.
    gate_cases=0
    for n in range(1,7):
        subsets=[frozenset(i for i in range(n) if (m>>i)&1) for m in range(1<<n)]
        for Aset,Bset in product(subsets,repeat=2):
            prod=frozenset(max(i,j) for i in Aset for j in Bset)
            for s in range(n):
                ah=s in Aset; bh=s in Bset
                ac=any(i<=s for i in Aset);bc=any(i<=s for i in Bset)
                assert (s in prod)==((ah and bc) or (ac and bh))
                assert any(i<=s for i in prod)==(ac and bc)
                gate_cases+=1
    # Sharpness: absorption valid on 1 point for both positive and negative truthmaking,
    # but fails at top of two-point chain.
    left=A(P(0),O(P(0),P(1)));right=P(0)
    for mask in range(16):
        atoms=[(frozenset({0}) if mask&(1<<(2*i)) else frozenset(),
                frozenset({0}) if mask&(1<<(2*i+1)) else frozenset()) for i in range(2)]
        assert explicit(left,atoms,1)==explicit(right,atoms,1)
    atoms=[(frozenset({0}),frozenset()),(frozenset({1}),frozenset())]
    assert 1 in explicit(left,atoms,2)[0] and 1 not in explicit(right,atoms,2)[0]
    # Incomparable a,b with join t: positive conjunction at t without disjunction at t.
    def join3(i,j): return 2 if i!=j else i
    p,q=frozenset({0}),frozenset({1})
    true_and=frozenset(join3(a,b) for a in p for b in q)
    true_or=p|q
    assert 2 in true_and and 2 not in true_or
    print('TRUTHMAKER_TWO_POINT_CHECK_OK',profile_cases,gate_cases,'SHARP_2','NONCHAIN_3')

if __name__=='__main__':main()
