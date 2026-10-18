#!/usr/bin/env python3
"""Reproducibility checks for positive graded rooted-star profiles.

Usage: python3 artifacts/verify.py
The all-size conclusions additionally require the proof in RESULT.md.
"""
from itertools import product
from math import comb
from functools import lru_cache
import random


def observable(k, a, b, c, d):
    return tuple(min(k, x) for x in (d, b+d, c+d, b+c+d, a+b+c+d))


def reduce_counts(k, a, b, c, d):
    small_d = min(d, k)
    small_b = min(b, max(0, k-small_d))
    small_c = min(c, max(0, k-small_d))
    small_a = 0 if b+c+d >= k else min(a, k-(b+c+d))
    return (small_a, small_b, small_c, small_d)


def enumerate_spectrum(k):
    observed = set()
    for quadruple in product(range(k+1), repeat=4):
        observed.add(observable(k,*quadruple))
    return len(observed)


def eval_at_world(formula, world_bits, leaf_bits, k, is_root=True):
    op=formula[0]
    if op=='p': return bool(world_bits&1)
    if op=='q': return bool(world_bits&2)
    if op=='top': return True
    if op=='bot': return False
    if op=='and': return eval_at_world(formula[1],world_bits,leaf_bits,k,is_root) and eval_at_world(formula[2],world_bits,leaf_bits,k,is_root)
    if op=='or': return eval_at_world(formula[1],world_bits,leaf_bits,k,is_root) or eval_at_world(formula[2],world_bits,leaf_bits,k,is_root)
    if op=='ge':
        if not is_root: return False
        r=formula[1]
        return sum(eval_at_world(formula[2], w, (), k, False) for w in leaf_bits)>=r
    raise ValueError(formula)



def symmetric_chains(m):
    chains=[[0]]
    for bit in range(m):
        new=[]
        for chain in chains:
            new.append(chain+[chain[-1] | (1<<bit)])
            if len(chain)>1:
                new.append([v|(1<<bit) for v in chain[:-1]])
        chains=new
    assert len(chains)==comb(m,m//2)
    flat=[v for c in chains for v in c]
    assert sorted(flat)==list(range(1<<m))
    assert all(all((u&v)==u for u,v in zip(c,c[1:])) for c in chains)
    return chains


def chain_compress(counts,chains,k):
    new=[0]*len(counts)
    for chain in chains:
        remaining=k
        for mask in reversed(chain):
            retained=min(remaining,counts[mask])
            new[mask]=retained
            remaining-=retained
    return new


def monotone_upsets(m):
    size=1<<m
    for up in range(1<<size):
        if all(not ((up>>v)&1) or all((up>>w)&1 for w in range(size) if (v&w)==v) for v in range(size)):
            yield [v for v in range(size) if (up>>v)&1]


def generic_width_test():
    rng=random.Random(761156)
    checked=0
    for m in range(0,5):
        chains=symmetric_chains(m)
        ups=list(monotone_upsets(m))
        for k in range(1,5):
            examples=[[k if v.bit_count()==m//2 else 0 for v in range(1<<m)],
                      [2*k+2]*(1<<m),[0]*(1<<m)]
            examples.extend([[rng.randrange(2*k+3) for _ in range(1<<m)] for _ in range(32)])
            for counts in examples:
                reduced=chain_compress(counts,chains,k)
                assert sum(reduced)<=k*comb(m,m//2)
                assert all(0<=x<=y for x,y in zip(reduced,counts))
                for up in ups:
                    lhs=min(k,sum(counts[v] for v in up))
                    rhs=min(k,sum(reduced[v] for v in up))
                    assert lhs==rhs,(m,k,counts,reduced,up)
                    checked+=1
    print('SPERNER_WIDTH_SHARP_COMPRESSION_OK',checked)


def main():
    for k in range(1,11):
        computed=enumerate_spectrum(k)
        closed=comb(k+3,4)+comb(k+2,3)+comb(k+3,3)
        assert computed==closed, (k,computed,closed)
        print('PROFILE_SPECTRUM_OK',k,computed,'pointed',4*computed)
    generic_width_test()
    checked=0
    for k in range(1,7):
        for counts in product(range(k+3),repeat=4):
            reduced=reduce_counts(k,*counts)
            assert all(0<=r<=old for r,old in zip(reduced,counts))
            assert sum(reduced)<=2*k
            assert observable(k,*reduced)==observable(k,*counts), (k,counts,reduced)
            checked+=1
    print('SHARP_CORE_UPPER_BOUND_OK',checked)
    for k in range(1,101):
        goal=observable(k,0,k,k,0)
        for b in range(k):
            # Since the p-count cannot be met below k 10-only leaves while d=0.
            assert observable(k,0,b,k,0)!=goal
        for c in range(k):
            assert observable(k,0,k,c,0)!=goal
        print_end=k
    print('SHARP_CORE_LOWER_BOUND_OK',print_end)
    rng=random.Random(260201856)
    def generate(depth):
        if depth==0 or rng.randrange(5)==0:
            return (rng.choice(['p','q','top','bot']),)
        operator=rng.choice(['and','or','ge'])
        if operator=='ge': return ('ge',rng.randint(1,3),generate(depth-1))
        return (operator,generate(depth-1),generate(depth-1))
    # An independent evaluator processes actual terminal labels and modal syntax.
    # For each signature group, randomly nested formulas must agree.
    k=3
    groups={}
    for a,b,c,d in product(range(5),repeat=4):
        sig=observable(k,a,b,c,d)
        groups.setdefault(sig,[]).append(([0]*a+[1]*b+[2]*c+[3]*d,(a,b,c,d)))
    formulas=[generate(4) for _ in range(240)]
    compared=0
    for root in range(4):
        for cases in groups.values():
            # Test all representatives in a signature class on nested syntax.
            for f in formulas:
                vals={eval_at_world(f,root,leaves,k) for leaves,_ in cases}
                assert len(vals)==1,(f,root,cases)
                compared+=len(cases)
    print('NESTED_POSITIVE_GRADED_EQUIVALENCE_OK',compared)
    print('POSITIVE_GRADED_STAR_CLASSIFICATION_OK')


if __name__=='__main__':
    main()
