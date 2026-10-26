#!/usr/bin/env python3
"""Independent finite-closure certificate for Tribonacci three-pseudoperiods.
Run with Python 3 standard library from the directory containing census.json.
"""
import itertools
import json
from pathlib import Path

MORPH = {'0':'01', '1':'02', '2':'0'}
B = 44
K = B + 1
LEVEL = 9

def image(w):
    return ''.join(MORPH[c] for c in w)

def factors(w, n):
    return set(w[i:i+n] for i in range(len(w)-n+1))

def all_triples(factor_set):
    return sorted((a,b,c) for a,b,c in itertools.combinations(range(1,B+1),3)
                  if all(x[0] in (x[a],x[b],x[c]) for x in factor_set))

def verify():
    spec = json.loads(Path(__file__).with_name('census.json').read_text(encoding='utf-8'))
    assert spec['bound'] == B and spec['morphism_level'] == LEVEL
    w = '0'
    for _ in range(LEVEL):
        w = image(w)
    assert len(w) == 274
    S = factors(w,K)
    assert len(S) == 91
    assert S == set(spec['length_45_factors'])
    # The closure certificate proves that *all* length-45 factors of the
    # infinite fixed point belong to S, without making a finite-prefix leap.
    for v in S:
        for x in factors(image(v),K):
            assert x in S
    positives = all_triples(S)
    assert positives == [tuple(x) for x in spec['positive_triples']]
    assert len(positives) == 55
    assert len(list(itertools.combinations(range(1,B+1),3))) == 13244
    # Distinct independent direct-position realization of the same triples:
    # no factor set or morphic-closure logic is used for this comparison.
    longer = w
    for _ in range(3):
        longer = image(longer)
    cutoff = 500
    via_positions = sorted((a,b,c) for a,b,c in itertools.combinations(range(1,B+1),3)
                           if all(longer[i] in (longer[i+a], longer[i+b], longer[i+c])
                                  for i in range(cutoff)))
    assert via_positions == positives
    # Certificate from lexicographically first violating length-45 factor:
    # every rejected triple has an actual finite occurrence in the fixed point.
    for a,b,c in itertools.combinations(range(1,B+1),3):
        if (a,b,c) not in set(positives):
            assert any(v[0] not in (v[a],v[b],v[c]) for v in S)
    print('TRIBONACCI_PSEUDOPERIOD_CENSUS_PASS',
          'factors=',len(S),'triples=',13244,'valid=',len(positives))

if __name__ == '__main__':
    verify()
