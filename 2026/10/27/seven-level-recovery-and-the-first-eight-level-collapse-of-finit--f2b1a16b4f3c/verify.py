#!/usr/bin/env python3
"""Exact rank-three first-order types of finite weak-order posets.

Run: python3 verify.py low; python3 verify.py eight; python3 verify.py game
Only the strict order relation is present; no level predicates or constants.
"""
import sys
from functools import lru_cache
from itertools import product
from collections import defaultdict


def points(word):
    return tuple((level, copy) for level, count in enumerate(word)
                 for copy in range(count))


def relation(a, b):
    if a == b:
        return 0                  # equality
    if a[0] < b[0]:
        return 1                  # strict less-than
    if a[0] > b[0]:
        return 2                  # strict greater-than
    return 3                      # distinct incomparable


@lru_cache(None)
def rank_three_type(word):
    """An exact Hintikka invariant: set of pointed rank-two types."""
    vertices = points(word)
    pointed_types = set()
    for x in vertices:
        successor_types = set()
        for y in vertices:
            xy = relation(x, y)
            # Three-point atomic diagrams: xy, xz, yz.
            diagrams = frozenset((xy, relation(x,z), relation(y,z))
                                 for z in vertices)
            successor_types.add((xy, diagrams))
        pointed_types.add(frozenset(successor_types))
    return frozenset(pointed_types)


@lru_cache(None)
def orbit_rank_three_type(word):
    """Independent enumeration by automorphism orbits of one- and two-tuples."""
    vertices = points(word)
    pointed_types = set()
    for level_x in range(len(word)):
        x = (level_x, 0)
        successor_types = set()
        for level_y in range(len(word)):
            possibilities = [0]
            if level_y == level_x and word[level_y] >= 2:
                possibilities.append(1)
            for copy_y in possibilities:
                y = (level_y, copy_y)
                xy = relation(x, y)
                diagrams = frozenset((xy, relation(x,z), relation(y,z))
                                     for z in vertices)
                successor_types.add((xy, diagrams))
        pointed_types.add(frozenset(successor_types))
    return frozenset(pointed_types)


def expected_merger(a,b):
    if a == b: return True
    if len(a) != 8 or len(b) != 8: return False
    if a[:3] != b[:3] or a[5:] != b[5:]: return False
    if sorted(a[3:5]) != [2,3] or sorted(b[3:5]) != [2,3]: return False
    if a[3] == b[3]: return False
    return all(a[i] >= 2 for i in (1,2,5,6))


def phase_low():
    seen = {}
    total = 0
    for length in range(1,8):
        for word in product((1,2,3),repeat=length):
            s = rank_three_type(word)
            assert s not in seen, (seen.get(s),word)
            assert s == orbit_rank_three_type(word),word
            seen[s] = word
            total += 1
        print('RECOVERABLE_LEVELS_OK',length,'cumulative_types',len(seen),flush=True)
    assert total == 3279
    assert max(sum(w) for w in seen.values()) == 21
    assert rank_three_type((1,)*6)!=rank_three_type((1,)*7)
    assert rank_three_type((1,)*7)==rank_three_type((1,)*8)
    print('UP_TO_SEVEN_LEVEL_THEORIES_OK',total)
    print('SHARP_WITHIN_FAMILY_BOUND_OK',21)
    print('SEVEN_TO_EIGHT_ORDER_CUTOFF_OK')
    print('LOW_VERIFY_OK')


def phase_eight():
    classes = defaultdict(list)
    for word in product((1,2,3),repeat=8):
        classes[rank_three_type(word)].append(word)
    assert len(classes) == 6417, len(classes)
    assert max(min(sum(w) for w in fiber) for fiber in classes.values()) == 24
    pairs = [v for v in classes.values() if len(v)==2]
    assert len(pairs)==144
    assert all(len(v)<=2 for v in classes.values())
    assert all(expected_merger(*v) for v in pairs)
    expected=set()
    for prefix in product((1,2,3), (2,3), (2,3)):
        for suffix in product((2,3), (2,3), (1,2,3)):
            w1=prefix+(2,3)+suffix
            w2=prefix+(3,2)+suffix
            expected.add(frozenset((w1,w2)))
    actual={frozenset(pair) for pair in pairs}
    assert len(expected)==144 and expected==actual
    print('EIGHT_LEVEL_WORDS_OK',3**8)
    print('EIGHT_LEVEL_CLASSES_OK',len(classes))
    print('EIGHT_LEVEL_EXACT_MERGERS_OK',len(pairs))
    print('EIGHT_LEVEL_WITHIN_STRATUM_BOUND_OK',24)
    print('CENTRAL_SWAP_CHARACTERIZATION_OK')
    print('EIGHT_VERIFY_OK')


def independent_game(a,b,rounds=3):
    A=points(a);B=points(b)
    @lru_cache(None)
    def win(selA,selB,k):
        for i,ai in enumerate(selA):
            for j,aj in enumerate(selA):
                if relation(A[ai],A[aj])!=relation(B[selB[i]],B[selB[j]]):
                    return False
        if k==0:return True
        for source in (0,1):
            src=A if source==0 else B
            dest=B if source==0 else A
            for v in range(len(src)):
                responses=False
                for w in range(len(dest)):
                    na=(selA+(v,)) if source==0 else (selA+(w,))
                    nb=(selB+(w,)) if source==0 else (selB+(v,))
                    if win(na,nb,k-1):
                        responses=True;break
                if not responses:return False
        return True
    return win((),(),rounds)


def phase_game():
    examples=[((1,1,1,1,1,1,1),(1,1,1,1,1,1,1,1)),
      ((1,2,2,2,3,2,2,1),(1,2,2,3,2,2,2,1)),
      ((1,2,2,2,3,2,2,1),(1,2,2,2,2,3,2,1)),
      ((1,2,2),(1,2,3)), ((3,2,1),(3,2,1)),
      ((1,1,3),(1,1,4)), ((2,2,2),(2,2,5)),
      ((1,2,1),(1,1,2))]
    for a,b in examples:
        direct=independent_game(a,b)
        symbolic=rank_three_type(a)==rank_three_type(b)
        assert direct==symbolic,(a,b,direct,symbolic)
        print('DIRECT_GAME_AGREEMENT_OK',a,b,'equivalent',symbolic,flush=True)
    for a,b in [((1,2,3,1),(1,2,4,1)),
                ((2,5,2),(2,3,2)),
                ((4,3,3),(3,3,3)),
                ((1,1,2,3,1),(1,1,2,8,1)),
                ((1,4,2,3,2),(1,3,2,3,2))]:
        assert rank_three_type(a)==rank_three_type(b)
    print('UNCAPPED_CLASS_SIZE_SAMPLES_OK',5)
    print('GAME_VERIFY_OK')


if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in {'low','eight','game'}:
        raise SystemExit('usage: python3 verify.py low|eight|game')
    globals()['phase_'+sys.argv[1]]()
