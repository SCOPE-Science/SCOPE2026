#!/usr/bin/env python3
"""Exact first-order rank-profile certificate for directed successor cycles.

Only Python's standard library is required. The universal result at sizes >=32
is supplied by the separate gap-splitting lemma in RESULT.md; this program
certifies all finite comparisons through 32.
"""
from collections import defaultdict
from functools import lru_cache
import json

MAX_N = 32
MAX_RANK = 5

# IDs are names for mathematically defined finite hereditarily-nested types.
# Global interning (rather than per-cycle numbering) makes ID equality exact.
type_ids = {}
def name(tree):
    old = type_ids.get(tree)
    if old is None:
        old = len(type_ids)
        type_ids[tree] = old
    return old

@lru_cache(maxsize=None)
def tp(n, points, q):
    """Complete FO q-type with 'points' as named variables.

    A directed cycle C_n has vertices 0,...,n-1 and R(a,b) iff
    b = a+1 mod n. All nonempty point tuples are rotated so that
    their first coordinate is 0; successive added vertices already
    share this coordinate and need no further normalization.
    """
    if not points:
        if q == 0:
            return name(('empty_atom',))
        # Vertex transitivity: the set of 1-point types is a singleton.
        return name(('empty_quantifier',tp(n,(0,),q-1)))
    atom = tuple((a==b, (a+1)%n == b)
                 for a in points for b in points)
    if q == 0:
        return name(('atom', atom))
    # This set of extensions implements BOTH players' first moves
    # (forth AND back): exact equality of sets is the back-and-forth test.
    extension_types = frozenset(tp(n, points+(v,),q-1)
                                for v in range(n))
    return name(('quantifier',atom,extension_types))

def main():
    all_groups = {q: defaultdict(list) for q in range(1,MAX_RANK+1)}
    for n in range(1,MAX_N+1):
        for q in range(1,MAX_RANK+1):
            all_groups[q][tp(n,(),q)].append(n)
        tp.cache_clear()  # only cross-size canonical type names are retained
    expected = {
        1: [2],
        2: [4],
        3: [7],
        4: [11],
        5: [19],
    }
    report = {'models_checked':list(range(1,MAX_N+1)),
              'max_quantifier_rank':MAX_RANK,
              'type_dictionary_size':len(type_ids),
              'rank_profiles':{}}
    for q in range(1,MAX_RANK+1):
        classes = sorted((sorted(v) for v in all_groups[q].values()),
                         key=lambda s:s[0])
        threshold = expected[q][0]
        reference = ([[n] for n in range(1,threshold)] +
                     [list(range(threshold,MAX_N+1))])
        assert classes == reference, (q, classes)
        report['rank_profiles'][str(q)] = {
            'first_stable_length':threshold,
            'distinct_classes_through_32':len(classes),
            'classes':classes,
        }
    # In particular this checks equivalence of C_19 and C_32; combined
    # with the gap lemma it proves stability for EVERY n >=19.
    print(json.dumps(report,separators=(',',':'),sort_keys=True))

if __name__ == '__main__':
    main()
