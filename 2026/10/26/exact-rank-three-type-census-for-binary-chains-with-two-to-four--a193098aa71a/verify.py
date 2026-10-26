#!/usr/bin/env python3
"""Exact finite rank-three profiles of sparse two-colour chains.

Dependencies: Python 3 standard library. Run: python3 verify.py
The infinite cap reduction is proved separately; this script checks its finite remainder.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
import hashlib
import json

B, R = 0, 1

@lru_cache(maxsize=None)
def two_character(w):
    """Definition directly from left- and right-hand colour sets."""
    return frozenset((v, frozenset(w[:i]), frozenset(w[i+1:]))
                     for i, v in enumerate(w))

@lru_cache(maxsize=None)
def three_character(w):
    """First-move type obtained from independently computed prefix/suffix types."""
    return frozenset((v, two_character(w[:i]), two_character(w[i+1:]))
                     for i, v in enumerate(w))

def append_two(bits, mask, a):
    """Independent bit-packed right-append transition for rank two."""
    old = bits
    nxt = 1 << (a * 16 + 4 * mask)
    while old:
        least = old & -old
        idx = least.bit_length()-1
        old -= least
        v = idx // 16
        lmask = (idx // 4) & 3
        rmask = idx & 3
        nxt |= 1 << (v * 16 + 4 * lmask + (rmask | (1 << a)))
    return nxt, mask | (1 << a)

def incremental_three(w):
    """Second implementation: process the word from left to right."""
    t2 = 0
    mask = 0
    t3 = frozenset()
    for a in w:
        t3 = frozenset(
            [(v,l,append_two(r, (1 if (r & ((1 << 16) - 1)) else 0) | (2 if (r >> 16) else 0), a)[0]) for (v,l,r) in t3]
            +[(a,t2,0)]
        )
        t2,mask = append_two(t2,mask,a)
    return t3

def encode_two(s):
    bits = 0
    for a,left,right in s:
        lm = sum(1<<x for x in left)
        rm = sum(1<<x for x in right)
        bits |= 1 << (a * 16 + 4 * lm + rm)
    return bits

def encode_three(s):
    return frozenset((a,encode_two(l),encode_two(r)) for a,l,r in s)

def word(gaps):
    k=len(gaps)-1
    return tuple(v for i,n in enumerate(gaps)
                 for v in ([B]*n+([R] if i<k else [])))

def main():
    totals={}
    for k, expected_count, expected_longest, expected_witness in [
        (1, 51, 13, (6,6)),
        (2, 310, 19, (6,5,6)),
        (3, 1865, 25, (6,5,5,6)),
        (4, 11196, 31, (6,5,5,5,6)),
    ]:
        reps={}
        checked=0
        for gaps in product(range(8),repeat=k+1):
            w=word(gaps)
            canonical=encode_three(three_character(w))
            alternate=incremental_three(w)
            assert canonical==alternate, ('implementations-disagree',k,gaps)
            checked+=1
            if canonical not in reps or (len(w),gaps)<(sum(reps[canonical])+k,reps[canonical]):
                reps[canonical]=gaps
        length_counts=Counter(sum(t)+k for t in reps.values())
        largest=max(length_counts)
        witnesses=sorted(x for x in reps.values() if sum(x)+k==largest)
        assert len(reps)==expected_count, (k,len(reps))
        assert largest==expected_longest, (k,largest)
        assert witnesses==[expected_witness], (k,witnesses)
        # By construction every equivalence type over this stratum occurs
        # in the finite 7-capped universe. All finite cases are checked.
        totals[k]={
            'capped_parameters':checked,
            'distinct_rank_three_types':len(reps),
            'sharp_shortest_representative_length':largest,
            'unique_extremal_canonical_gaps':witnesses[0],
            'minimal_length_histogram':dict(sorted(length_counts.items())),
        }
        print('STRATUM_OK',k,'capped_cases',checked,'types',len(reps),
              'sharp_bound',largest,'unique_extremal_gaps',witnesses[0],flush=True)
    # Independent sanity checks at and above the monochromatic 7-point cap.
    for k in (2,3):
        for other in product(range(8),repeat=k):
            for position in range(k+1):
                arr=list(other)
                arr.insert(position,7)
                a=encode_three(three_character(word(tuple(arr))))
                arr[position]=8
                b=encode_three(three_character(word(tuple(arr))))
                assert a==b, (k,position,other)
    print('BOUNDARY_FINITE_CHECK_OK thresholds_7_to_8 k=2,3',flush=True)
    js=json.dumps(totals,sort_keys=True,separators=(',',':'))
    print('COUNTS_SHA256',hashlib.sha256(js.encode('utf-8')).hexdigest(),flush=True)
    print('VERIFY_OK',flush=True)

if __name__=='__main__':main()
