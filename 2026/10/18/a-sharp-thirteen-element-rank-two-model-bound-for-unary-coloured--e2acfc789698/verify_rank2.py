#!/usr/bin/env python3
"""Exact rank-two census of finite unary-coloured equivalence structures.
Run with Python >=3.9: python3 verify_rank2.py. No external dependencies.
This is a finite, exhaustive computation with a mathematically justified
bounded-profile reduction described in the accompanying proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import product

# Each E-class has the indicated number of red / blue elements, capped at 2.
CLASS_TYPES = tuple((red, blue) for red in range(3)
                    for blue in range(3) if red + blue > 0)


def profiles():
    """All 3^8-1 nonempty capped profiles of E-class multiplicities."""
    for numbers in product(range(3), repeat=len(CLASS_TYPES)):
        if any(numbers):
            yield numbers


def size(numbers):
    return sum((r+b)*m for (r,b),m in zip(CLASS_TYPES,numbers))


def local_signature(numbers):
    """Rank-two complete type via the set of all pointed rank-one types."""
    global_counts = tuple(sum(t[color]*m for t,m in zip(CLASS_TYPES,numbers))
                          for color in (0,1))
    local = set()
    for members, multiplicity in zip(CLASS_TYPES,numbers):
        if multiplicity == 0:
            continue
        for colour in (0,1):
            if members[colour] == 0:
                continue
            # Move: (colour of y, y equals x, E(x,y)).
            witnesses = {(colour, True, True)}
            for y_colour in (0,1):
                if members[y_colour] - (y_colour == colour) > 0:
                    witnesses.add((y_colour,False,True))
                if global_counts[y_colour] - members[y_colour] > 0:
                    witnesses.add((y_colour,False,False))
            local.add((colour,frozenset(witnesses)))
    return frozenset(local)


def direct_recursive_signature(numbers):
    """Independent FO rank-two recursion on the actual finite structure."""
    universe = []
    for typ, ((r,b), multiplicity) in enumerate(zip(CLASS_TYPES,numbers)):
        for copy in range(multiplicity):
            block = (typ,copy)
            universe.extend((block,True) for _ in range(r))
            universe.extend((block,False) for _ in range(b))

    @lru_cache(maxsize=None)
    def node(chosen, depth):
        atom = (tuple(universe[z][1] for z in chosen),
                tuple((chosen[i] == chosen[j],
                       universe[chosen[i]][0] == universe[chosen[j]][0])
                      for i in range(len(chosen)) for j in range(i+1,len(chosen))))
        if depth == 0:
            return (atom,)
        return (atom,frozenset(node(chosen + (i,),depth-1)
                               for i in range(len(universe))))
    return node((),2)


def run():
    profile_list = list(profiles())
    assert len(CLASS_TYPES) == 8
    assert len(profile_list) == 6560

    classes, independent = {}, {}
    for numbers in profile_list:
        fast = local_signature(numbers)
        slow = direct_recursive_signature(numbers)
        classes.setdefault(fast,[]).append(numbers)
        # The two independently specified logical semantics must agree on
        # the entire canonical universe (not just a handful of examples).
        if slow in independent:
            assert independent[slow] == fast
        else:
            independent[slow] = fast
    assert len(classes) == 207, len(classes)
    assert len(independent) == 207, len(independent)

    minimum = [min(g, key=lambda p:(size(p),p)) for g in classes.values()]
    distribution = Counter(size(p) for p in minimum)
    expected = {1:2,2:6,3:10,4:17,5:22,6:28,7:30,
                8:29,9:26,10:18,11:12,12:5,13:2}
    assert dict(distribution) == expected, distribution
    assert max(size(p) for p in minimum) == 13

    # Exactly two different rank-two types require 13 points.
    extremal = sorted(p for p in minimum if size(p)==13)
    assert extremal == [(1,1,1,0,0,1,1,1),(1,1,1,0,1,1,0,1)]
    assert sum(len(g) for g in classes.values())==6560

    print('class_patterns:', CLASS_TYPES)
    print('canonical_profiles:',len(profile_list))
    print('rank_2_types:',len(classes))
    print('minimum_size_histogram:',sorted(distribution.items()))
    print('sharp_model_size:',max(distribution))
    print('extremal_13_vertex_profiles:',extremal)
    print('independent_signature_agreement: all 6560 profiles')

if __name__=='__main__':
    run()
