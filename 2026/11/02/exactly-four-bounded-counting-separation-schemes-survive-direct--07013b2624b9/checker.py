#!/usr/bin/env python3
"""Independent finite-semigroup checks for bounded counting predicates.
Scientific checks only. Finite exhaustive computation does not replace the proof.
"""
from itertools import product


def cross_bad(cutoff, mask):
    """Return a 2x2 pattern obstructing a rectangular truth set, if any.

    Inputs are finite cardinality classes 0,1,...,cutoff; the final class
    represents every cardinality >= cutoff, including infinite ones.
    """
    def test(a,b):
        return (mask >> min(a*b, cutoff)) & 1
    for a,b,c,d in product(range(cutoff+1), repeat=4):
        if test(a,b) and test(c,d) and not test(a,d):
            return (a,b,c,d)
    return None


def expected_safe_masks(cutoff):
    full=(1 << (cutoff+1))-1
    pos=full ^ 1
    singleton=1 << 1
    return {0,full,pos,singleton}


def exhaustive():
    # Testing cutoffs at least two ensures singleton is distinguishable.
    masks_tested=0
    witnessed=0
    for cutoff in range(2,9):
        safe=expected_safe_masks(cutoff)
        found={}
        for mask in range(1 << (cutoff+1)):
            witness=cross_bad(cutoff,mask)
            masks_tested+=1
            if witness is None:
                found[mask]=True
            else:
                witnessed+=1
                a,b,c,d=witness
                def v(x,y): return bool(mask & (1 << min(x*y,cutoff)))
                assert v(a,b) and v(c,d) and not v(a,d)
                # The same witness is a 2 x 2 parent-box obstruction:
                # any Cartesian rectangle containing (a,b) and (c,d)
                # must contain the mixed point (a,d).
                assert a!=c and b!=d
        assert set(found)==safe, (cutoff,found,safe)
    print('CUTOFFS_2_TO_8_OK', 'masks=',masks_tested,'witnessed=',witnessed)


def exhaustive_three_factors():
    # In three coordinates the four safe predicates factor exactly;
    # every unsafe predicate already fails on a padded 2 x 2 face.
    cases=0
    for cutoff in range(2,6):
        for mask in expected_safe_masks(cutoff):
            for a,b,c in product(range(cutoff+1), repeat=3):
                target=bool(mask & (1 << min(a*b*c,cutoff)))
                if mask==0:
                    want=False
                elif mask==(1 << (cutoff+1))-1:
                    want=True
                elif mask==(1 << 1):
                    want=(a==b==c==1)
                else:
                    want=(a>0 and b>0 and c>0)
                assert target==want, (cutoff,mask,a,b,c)
                cases+=1
    print('THREE_FACTOR_OK', 'tuples=',cases)


def explicit_examples():
    # >=2: the two accepted cardinality pairs (2,1),(1,2)
    # force the rejected (1,1).  The parent contains 4 members.
    def ge2(a,b): return a*b>=2
    assert ge2(2,1) and ge2(1,2) and not ge2(1,1)
    # Zero members: (0,1) and (1,0) force rejected (1,1).
    def zero(a,b): return a*b==0
    assert zero(0,1) and zero(1,0) and not zero(1,1)
    # Exactly two: same obstruction as >=2.
    def exactly2(a,b): return a*b==2
    assert exactly2(2,1) and exactly2(1,2) and not exactly2(1,1)
    print('EXPLICIT_4_MEMBER_WITNESSES_OK')


if __name__=='__main__':
    exhaustive()
    exhaustive_three_factors()
    explicit_examples()
    print('ALL_CHECKS_OK')
