"""Reconstructible finite certificate for balanced DNA non-overlapping codes.
Usage: python verify.py [certificate.json]
Standard-library Python only.
"""
import itertools
import json
import pathlib
import sys
from collections import Counter

ALPHABET = 'ACGT'
PAIR = dict(A='T', T='A', C='G', G='C')
LENGTH = 5

def rc(word):
    return ''.join(PAIR[letter] for letter in word[::-1])

def is_balanced(word):
    return len(word)==LENGTH and sum(letter in 'CG' for letter in word) in (2,3)

def no_overlap(u, v):
    return all(u[:k] != v[-k:] for k in range(1, LENGTH))

def family_compatible(words):
    return all(no_overlap(u,v) for u in words for v in words)

def run(path):
    doc=json.loads(pathlib.Path(path).read_text('utf-8'))
    assert doc['domain'] == {'length':5,'alphabet':'ACGT','gc_allowed':[2,3],
                             'watson_crick_complement':PAIR}
    balanced={''.join(t) for t in itertools.product(ALPHABET, repeat=LENGTH)
              if is_balanced(''.join(t))}
    assert len(balanced)==640
    assert all(rc(rc(w))==w and rc(w)!=w for w in balanced)
    canonical={min(w,rc(w)) for w in balanced}
    assert len(canonical)==320
    admissible={w for w in canonical if family_compatible([w,rc(w)])}
    assert len(admissible)==120

    rows=doc['candidate_orbits']
    reps=[row['representative'] for row in rows]
    assert len(rows)==len(set(reps))==120
    assert set(reps)==admissible
    colors={row['representative']:row['color_class'] for row in rows}
    assert all(type(c) is int and 0<=c<12 for c in colors.values())
    assert set(colors.values())==set(range(12))

    # Every class is a clique in the INCOMPATIBILITY graph. Thus a valid
    # code containing whole reverse-complement orbits selects <=1 per class.
    group=Counter(colors.values())
    for x,y in itertools.combinations(admissible, 2):
        if colors[x]==colors[y]:
            assert not family_compatible([x,rc(x),y,rc(y)])
    # All 640 input DNA words are either excluded by an internal overlap
    # or form exactly one of these 120 admissible orbits.
    selected=doc['witness_representatives']
    assert len(selected)==len(set(selected))==12
    assert all(w in admissible for w in selected)
    witness={z for w in selected for z in (w,rc(w))}
    assert len(witness)==24
    assert all(is_balanced(w) for w in witness)
    assert {rc(w) for w in witness}==witness
    assert family_compatible(witness)
    assert Counter(sum(c in 'CG' for c in w) for w in witness)==Counter({2:12,3:12})

    # Finiteness of the partition proves <=2*12 = 24;
    # the 24 distinct witness words prove equality.
    print('VERIFY_OK: balanced=640, initial_orbits=320, admissible_orbits=120, classes=12, witness=24')
    print('class_sizes='+str([group[k] for k in range(12)]))

if __name__=='__main__':
    run(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).with_name('certificate.json'))
