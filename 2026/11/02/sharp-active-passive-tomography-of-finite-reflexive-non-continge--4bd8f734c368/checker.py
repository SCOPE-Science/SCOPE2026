#!/usr/bin/env python3
"""Direct finite tests of the non-contingency successor-set and tomography theorem.
No external dependencies; integer bit masks encode finite relations and valuations.
"""
from itertools import combinations
from random import Random
from itertools import product
from fractions import Fraction
from math import comb

def delta_row(s, x):
    return (s & x == 0) or (s & ~x == 0)

def row_observations(rows, n, x):
    return sum(1 << w for w,s in enumerate(rows) if delta_row(s,x))

def arbitrary_relations(n):
    for code in range(1 << (n*n)):
        yield tuple((code >> (n*w)) & ((1<<n)-1) for w in range(n))

def reflexive_relations(n):
    positions = [(w,v) for w in range(n) for v in range(n) if w!=v]
    for code in range(1 << len(positions)):
        rows = [1<<w for w in range(n)]
        for i,(w,v) in enumerate(positions):
            if code>>i & 1: rows[w] |= 1<<v
        yield tuple(rows)

def quotient_tag(s,n):
    return s if s.bit_count() >= 2 else -1

def test_arbitrary():
    for n in range(1,4):
        maps = {}
        for rows in arbitrary_relations(n):
            signature = tuple(row_observations(rows,n,x) for x in range(1<<n))
            tag = tuple(quotient_tag(s,n) for s in rows)
            if signature in maps: assert maps[signature] == tag
            else: maps[signature] = tag
        predicted = (2**n - n)**n
        assert len(maps)==predicted, (n,len(maps),predicted)
        print('ALL_ROWS', n, 'operators',len(maps))

def test_reflexive():
    for n in range(1,5):
        frames=list(reflexive_relations(n))
        tests = list(range(1, 1 << (n-1))) # representatives of X, its complement
        patterns={x:[row_observations(rows,n,x) for rows in frames] for x in tests}
        all_sigs=[tuple(patterns[x][i] for x in tests) for i in range(len(frames))]
        assert len(set(all_sigs))==len(frames), ('not_identifiable',n)
        # Verify the finite minimum exhaustively over all test families.
        minimum=None; best=None
        for k in range(len(tests)+1):
            for comb in combinations(tests,k):
                keys=[tuple(patterns[x][i] for x in comb) for i in range(len(frames))]
                if len(set(keys))==len(frames): minimum=k;best=comb; break
            if minimum is not None: break
        predicted=0 if n==1 else (1 if n==2 else n)
        assert minimum==predicted,(n,minimum,predicted,best)
        # n singleton valuations give a straightforward reconstruction rule
        for rows in frames:
            recover=[1<<w for w in range(n)]
            for v in range(n):
                y=row_observations(rows,n,1<<v)
                for w in range(n):
                    if w!=v and not (y>>w & 1): recover[w] |= 1<<v
            assert tuple(recover)==rows
        print('REFLEXIVE',n,'frames',len(frames),'min_queries',minimum,'example_tests',best)

    rng=Random(1472)
    n=5
    for i in range(1200):
        rows=tuple((1<<w)|rng.randrange(1<<n) for w in range(n))
        recover=[1<<w for w in range(n)]
        for v in range(n):
            y=row_observations(rows,n,1<<v)
            for w in range(n):
                if w!=v and not (y>>w & 1): recover[w] |= 1<<v
        assert tuple(recover)==rows
    print('RANDOM_REFLEXIVE_5',1200)

def test_adversary():
    for n in range(3,8):
        base = tuple((1<<n)-1 for w in range(n))
        for v in range(n):
            w=(v+1)%n
            alt=list(base); alt[w]&=~(1<<v);alt=tuple(alt)
            sensitive=[]
            for x in range(1<<n):
                if row_observations(base,n,x)!=row_observations(alt,n,x):
                    sensitive.append(x)
            assert set(sensitive)=={1<<v,((1<<n)-1)^(1<<v)}
        print('ADVERSARIAL',n,'verified')


def test_random_coupon():
    for n in range(3,5):
        frames=list(reflexive_relations(n))
        xs=list(range(1,1<<(n-1)))
        patterns={x:[row_observations(rows,n,x) for rows in frames] for x in xs}
        specials={min(1<<v,((1<<n)-1)^(1<<v)) for v in range(n)}
        assert len(specials)==n
        # Every choice of nonconstant complement-pair tests is injective
        # on all reflexive frames iff it contains all singleton tests.
        for mask in range(1<<len(xs)):
            used=[x for i,x in enumerate(xs) if mask>>i & 1]
            keys=[tuple(patterns[x][i] for x in used) for i in range(len(frames))]
            works=len(set(keys))==len(frames)
            assert works == specials.issubset(used), (n,used)
        print('COUPON_CHARACTERIZATION',n,'families',1<<len(xs))
        # Direct enumeration of independently random subsets, counting every
        # full valuation sequence rather than sampling.
        for m in range(0,5 if n==3 else 4):
            total=(1<<n)**m
            success=sum(1 for values in product(range(1<<n),repeat=m)
                        if specials.issubset(
                          min(x,((1<<n)-1)^x) for x in values))
            pred=sum(((-1)**j)*comb(n,j)*(2**n-2*j)**m for j in range(n+1))
            # 0**0 counts as 1, matching empty sequence convention.
            assert success==pred, (n,m,success,pred)
            print('COUPON_EXACT',n,m,success,total)

if __name__=='__main__':
    test_arbitrary()
    test_reflexive()
    test_adversary()
    test_random_coupon()
    print('ALL_CHECKS_OK')
