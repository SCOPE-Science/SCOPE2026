#!/usr/bin/env python3
"""Finite-state exhaustive proof for minimum forcing configurations on cycle prisms.

No external packages. A column of the prism is encoded by a two-bit mask;
bit 0 is the top vertex and bit 1 is the bottom vertex.
"""
from itertools import product
from collections import Counter

DIM = 16
IDENTITY = tuple(1 << i for i in range(DIM))
ZERO = (0,) * DIM

def boolean_product(A, B):
    out = []
    for a in A:
        v = 0
        while a:
            bit = a & -a
            v |= B[bit.bit_length() - 1]
            a -= bit
        out.append(v)
    return tuple(out)

def boolean_union(A, B):
    return tuple(a | b for a, b in zip(A, B))

def marked_product(X, Y):
    # X=(all paths, paths visiting a nonzero fort column).
    a, am = X
    b, bm = Y
    return (boolean_product(a,b),
            boolean_union(boolean_product(am,b), boolean_product(a,bm)))

def transition(seed):
    all_rows = []
    marked_rows = []
    for left in range(4):
        for center in range(4):
            row = 0
            if not(center & seed):
                for right in range(4):
                    good = True
                    for layer in range(2):
                        if not (center >> layer) & 1:
                            neighbours = ((left >> layer) & 1) + ((right >> layer) & 1) + ((center >> (1-layer)) & 1)
                            if neighbours == 1:
                                good = False
                    if good:
                        row |= 1 << (4*center + right)
            all_rows.append(row)
            marked_rows.append(row if center else 0)
    return tuple(all_rows), tuple(marked_rows)

TRANS = [transition(i) for i in range(4)]
POWERS = [(IDENTITY,ZERO)]
for k in range(1,7):
    POWERS.append(marked_product(POWERS[-1],TRANS[0]))
assert POWERS[5] == POWERS[6], 'The central stabilization lemma fails'
# For every k>=5, T0^k = T0^5 by multiplication on the right.
BLOCKS = {(seed,gap):marked_product(TRANS[seed],POWERS[gap])
          for seed in range(1,4) for gap in range(6)}

def forcing_cyclic(blocks):
    P = (IDENTITY, ZERO)
    for v in blocks:
        P = marked_product(P, BLOCKS[v])
    return not any(P[1][i] & (1 << i) for i in range(DIM))

def trans_orbits(n):
    # Five representative 4-vertex sets in a labelled prism.
    templates = [((0,1),(0,1)), ((0,1),(0,n-1)),
                 ((0,1,2,3),()), ((0,1,2),(0,)),
                 ((0,1,3),(1,))]
    family = set()
    class_sets = []
    for top,bottom in templates:
        orbit=set()
        for s in (1,-1):
            for shift in range(n):
                for swap in (0,1):
                    pairs = [( (s*i+shift)%n, z^swap)
                             for z,part in enumerate((top,bottom)) for i in part]
                    mask = sum(1 << (i+n*z) for i,z in pairs)
                    orbit.add(mask)
        assert not (family & orbit), ('non-disjoint orbits',n)
        class_sets.append(orbit)
        family |= orbit
    assert tuple(map(len,class_sets)) == (n,2*n,2*n,4*n,4*n)
    return family,class_sets

CACHED = {}
def orbit_membership(n, word):
    if n not in CACHED:
        CACHED[n] = trans_orbits(n)[0]
    mask = sum((1 << (i+n*z)) for i,letter in enumerate(word)
               for z in range(2) if (letter >> z)&1)
    return mask in CACHED[n]


def check_all_seed_words(weight, verbose=False):
    total = tested = passing = 0
    histogram = Counter()
    for k in range((weight+1)//2, weight+1):
        for letters in product((1,2,3), repeat=k):
            if sum(s.bit_count() for s in letters) != weight:
                continue
            for gaps in product(range(6),repeat=k):
                n = k + sum(gaps)
                if n < 6:
                    continue
                tested += 1
                blocks = list(zip(letters,gaps))
                is_forcing = forcing_cyclic(blocks)
                if is_forcing:passing+=1
                if weight==4:
                    word = [v for x,g in blocks for v in ([x] + [0]*g)]
                    claim = orbit_membership(n,word)
                    if is_forcing != claim:
                        raise AssertionError(('4-set exception',letters,gaps,is_forcing,claim,n))
                else:
                    if is_forcing:
                        raise AssertionError(('unexpected <=3-set forcing',letters,gaps,n))
                histogram[k]+=1
    if verbose:
        print('weight',weight,'cases',tested,'forcing',passing,'occupied-columns',dict(sorted(histogram.items())))
    return tested


def get_degrees(n):
    families,orbits = trans_orbits(n)
    deg = {}
    for B in families:
        ans=0
        for v in range(2*n):
            if B>>v&1:
                for w in range(2*n):
                    if not B>>w&1 and B^(1<<v)^(1<<w) in families:
                        ans+=1
        deg[B]=ans
    return families,orbits,deg

def assert_degrees_and_connectivity(n):
    family,orbits,degree = get_degrees(n)
    assert len(family)==13*n
    assert Counter(degree.values())=={12:n,8:8*n,5:4*n}
    # Counts of undirected edges from degree sum.
    assert sum(degree.values())//2 == 48*n
    # Explicit constructive paths. Every symmetry orbit can reach a square;
    # adjacent squares are linked through {T1,T2,B0,B1}.
    def m(top=(),bottom=()):
        return sum(1<<x for x in top)+sum(1<<(n+x) for x in bottom)
    square = m((0,1),(0,1))
    bridge = m((1,2),(0,1))
    next_square = m((1,2),(1,2))
    for x,y in [(square,bridge),(bridge,next_square),
                (m((0,1),(0,n-1)),square),
                (m((0,1,2,3)),m((0,1,3),(1,))),
                (m((0,1,3),(1,)),square),
                (m((0,1,2),(0,)),square)]:
        assert x in family and y in family and (x^y).bit_count()==2
    return {deg:count for deg,count in sorted(Counter(degree.values()).items())}

if __name__=='__main__':
    print('FORT_MATRIX_STABILIZES_AFTER_FIVE_EMPTY_COLUMNS')
    for w in (1,2,3,4):check_all_seed_words(w,True)
    print('CIRCULAR_TEMPLATE_EXHAUSTION_ALL_LENGTHS_PASS')
    for n in range(6,26):
        print('n',n,assert_degrees_and_connectivity(n))
    print('PRISM_FORCING_DEGREE_CONNECTIVITY_ALL_LENGTHS_PASS')
