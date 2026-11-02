#!/usr/bin/env python3
"""Exact 4-pattern witness minima in prime quadratic-residue tournaments.

Mathematical certificate: affine-square automorphisms normalize a selected
ordered pair of each four-set to (0,1). The finite census is exhaustive in
that normalization. No external dependencies.
"""
import json
from math import isqrt


def primes(a, b):
    for n in range(a, b + 1):
        if n < 2: continue
        if all(n % d for d in range(2, isqrt(n)+1)):
            yield n


def minimum_extensions(p):
    assert p % 4 == 3 and p > 4
    quadratic = {(k*k)%p for k in range(1,p)}
    assert len(quadratic) == (p-1)//2 and p-1 not in quadratic
    universe=(1<<p)-1
    # outgoing[a] consists of z such that a -> z.
    outgoing=[]
    incoming=[]
    for a in range(p):
        o=sum(1<<z for z in range(p) if z != a and ((z-a)%p) in quadratic)
        outgoing.append(o)
        incoming.append(universe & ~(o | (1<<a)))
    minimum=p
    min_example=None
    representative_count=0
    for x in range(2,p):
        for y in range(x+1,p):
            a=(0,1,x,y)
            possibilities=[universe]
            for vertex in a:
                possibilities=[m & n for m in possibilities for n in (outgoing[vertex],incoming[vertex])]
            assert len(possibilities)==16
            representative_count+=1
            for mask,m in enumerate(possibilities):
                count=m.bit_count()
                if count<minimum:
                    minimum=count
                    min_example={'four_set':list(a),'pattern_mask':mask,'witness_count':count,
                                 'witnesses':[z for z in range(p) if m>>z&1]}
    assert representative_count==(p-2)*(p-3)//2
    return {'p':p,'minimum_witnesses':minimum,
            'normalized_four_sets':representative_count,'minimizer':min_example}


def main():
    entries=[minimum_extensions(p) for p in primes(7,211) if p % 4 == 3]
    assert entries[0]['p']==7 and entries[-1]['p']==211
    assert {d['p']:d['minimum_witnesses'] for d in entries if d['p']<107 and d['minimum_witnesses']>=2}=={}
    assert all(d['minimum_witnesses']>=2 for d in entries if d['p']>=107)
    assert next(d for d in entries if d['p']==107)['minimum_witnesses']==2
    # Character estimate N >= (q - 38 - 11 sqrt(q))/16. For q>=223 this exceeds 1.
    assert 223-38-11*(223**0.5)>16
    assert 223 > (11/2)**2  # ensures increasing bound for q>=223
    result={'specification':'minimum 4-extension witnesses of QR(p), modulo affine-square normalization',
            'prime_records':entries,
            'small_prime_powers_below_223_not_prime':[3,27],
            'small_prime_power_exclusion':'q<36 cannot have 2 witnesses for every one of 16 patterns on four fixed vertices',
            'large_field_bound':'N >= (q-38-11*sqrt(q))/16 > 1 whenever q>=223',
            'conclusion':'For prime powers q=3 modulo 4, 2-fold 4-extension holds exactly when q>=107.'}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__': main()
