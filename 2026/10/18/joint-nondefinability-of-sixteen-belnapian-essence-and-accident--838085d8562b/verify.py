#!/usr/bin/env python3
"""Finite semantic checks for a non-definability theorem in four-valued essence/accident logic.

Truth values use two bits: 1 for positive truth support and 2 for falsity support.
All modal clauses below reproduce the semantics in Petrukhin (2026), Definition 2.6.
This checker confirms finite instances, not all formulas or all models.
"""
from itertools import product
from random import Random

N, T, F, B = 0, 1, 2, 3
VALUES = {'t': T, 'f': F, 'b': B, 'n': N}
TARGETS = {'t': T, 'f': F, 'T': 1, 'F': 2}
STARS = ('ess', 'acc', 'ness', 'nacc')
BASE = tuple((s,j) for s in STARS for j in ('b','n'))


def has(v, bit): return bool(v & bit)
def val(z): return VALUES[z]
def star(v, xs, kind, j):
    if j in ('T','F'):
        bit = 1 if j == 'T' else 2
        other = 3 ^ bit
        a = has(v,bit)
        bs = [has(z,bit) for z in xs]
        os = [has(z,other) for z in xs]
        if kind == 'ess':
            tr = (not a) or all(bs)
            fa = a and any(os)
        elif kind == 'ness':
            tr = a or not any(bs)
            fa = (not a) and not all(os)
        elif kind == 'acc':
            tr = a and not all(bs)
            fa = has(v,other) or not any(os)
        elif kind == 'nacc':
            tr = (not a) and any(bs)
            fa = (not has(v,other)) or all(os)
        else: raise AssertionError(kind)
    else:
        q = val(j)
        c = B if j == 'n' else N if j == 'b' else q
        a = v == q
        bs = [z==q for z in xs]
        os = [z==c for z in xs]
        if kind == 'ess':
            tr = (not a) or all(bs)
            fa = a and not all(os)
        elif kind == 'ness':
            tr = a or not any(bs)
            fa = (not a) and any(os)
        elif kind == 'acc':
            tr = a and not all(bs)
            fa = (v != c) or all(os)
        elif kind == 'nacc':
            tr = (not a) and any(bs)
            fa = (v == c) or not any(os)
        else: raise AssertionError(kind)
    return (1 if tr else 0) | (2 if fa else 0)


def local_unary(kind,j,w):
    # The defining invariant on consistent, complete (t/f-only) models.
    return (T if kind in ('ess','ness') else F)


def evaluate(node, points, world):
    op = node[0]
    if op == 'var': return points[world][node[1]]
    if op == 'neg':
        v = evaluate(node[1],points,world)
        return ((v&1)<<1) | ((v&2)>>1)
    if op == 'boolneg': return 3 ^ evaluate(node[1],points,world)
    if op in ('and','or','impl'):
        v=evaluate(node[1],points,world); u=evaluate(node[2],points,world)
        if op=='and': return ((v&u)&1)|((v|u)&2)
        if op=='or': return ((v|u)&1)|((v&u)&2)
        return (1 if (not(v&1)) or (u&1) else 0) | (2 if (v&1) and (u&2) else 0)
    if op == 'modal':
        kind,j,sub=node[1:]
        vals=[evaluate(sub,points,k) for k in range(len(points))]
        return star(vals[world],vals,kind,j)
    raise ValueError(op)


def run():
    # Fundamental eight-modal collapse verified on all crisp truth patterns on up to 5 worlds.
    modal_cases=0
    for n in range(1,6):
        for bits in product((T,F),repeat=n):
            for s,j in BASE:
                for w in range(n):
                    assert star(bits[w],bits,s,j) == local_unary(s,j,bits[w])
                    modal_cases+=1

    # Each of the sixteen target connectives differs on a two-point pointed pair.
    witnesses=[]
    for kind in STARS:
        for j in TARGETS:
            q = T if j in ('t','T') else F
            p = F if q==T else T
            atroot=q if kind in ('ess','acc') else p
            other=p if kind in ('ess','acc') else q
            one=star(atroot,[atroot],kind,j)
            two=star(atroot,[atroot,other],kind,j)
            assert (one,two) in ((T,F),(F,T)),(kind,j,one,two)
            witnesses.append((kind,j,one,two))

    # Nontrivial composition stresses: all eight source modalities together,
    # unlimited alternation permitted by the syntax, with sampled finite terms.
    rng=Random(762118)
    def random_formula(depth):
        if depth==0 or rng.randrange(6)==0:
            return ('var',rng.randrange(3))
        k=rng.randrange(5)
        if k==0:return ('neg',random_formula(depth-1))
        if k==1:return ('boolneg',random_formula(depth-1))
        if k==2:
            x,y=BASE[rng.randrange(8)]
            return ('modal',x,y,random_formula(depth-1))
        return (('and','or','impl')[rng.randrange(3)],random_formula(depth-1),random_formula(depth-1))
    termcases=0
    for _ in range(12000):
        term=random_formula(5)
        root=[rng.choice((T,F)) for z in range(3)]
        other=[rng.choice((T,F)) for z in range(3)]
        third=[rng.choice((T,F)) for z in range(3)]
        singleton=[root]; double=[root,other]; triple=[root,other,third]
        assert evaluate(term,singleton,0)==evaluate(term,double,0)==evaluate(term,triple,0)
        assert evaluate(term,singleton,0) in (T,F)
        termcases+=1
    print('VERIFY_OK')
    print('eight_modal_collapse_checks',modal_cases)
    print('two_world_target_separations',len(witnesses))
    print('sampled_reduct_term_comparisons',termcases)
    for (s,j,u,v) in witnesses:
        print('target',s,j,'singleton',u,'two_world',v)

if __name__=='__main__': run()
