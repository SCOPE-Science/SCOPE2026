#!/usr/bin/env python3
"""Independent direct-word backtracking census and maximum symmetry classes.

No adjacency matrix or memoization. Each extension is tested against actual
codewords; every codebook has one strictly increasing orbit-index sequence.
"""
from collections import Counter
from itertools import product, permutations

BASES = 'ACGT'
COMP = {'A':'T','T':'A','C':'G','G':'C'}
EXPECTED = (1,12,88,288,584,760,688,424,160,32)

def reverse_complement(w):
    return ''.join(COMP[b] for b in reversed(w))

def code_ok(code):
    for u in code:
        for v in code:
            if any(u[:k] == v[-k:] for k in range(1,4)):
                return False
            if u != v and sum(a != b for a,b in zip(u,v)) < 2:
                return False
    return True

def main():
    orbits = sorted({tuple(sorted(set((w, reverse_complement(w)))))
                     for w in map(''.join, product(BASES, repeat=4))})
    eligible = [o for o in orbits if code_ok(o)]
    assert len(orbits) == 136 and len(eligible) == 56
    counts = Counter()
    maxima = []

    def backtrack(code, future):
        counts[len(code)] += 1
        if len(code) == 9:
            maxima.append(tuple(sorted(code)))
        for offset, i in enumerate(future):
            trial = code + list(eligible[i])
            next_candidates = [j for j in future[offset+1:]
                               if code_ok(trial + list(eligible[j]))]
            backtrack(trial, next_candidates)

    backtrack([], list(range(len(eligible))))
    spectrum = tuple(counts.get(k,0) for k in range(10))
    assert spectrum == EXPECTED
    assert not any(k > 9 for k in counts)
    assert len(maxima) == 32 and len(set(maxima)) == 32
    group = []
    for seq in permutations(BASES):
        p = dict(zip(BASES,seq))
        if all(p[COMP[x]] == COMP[p[x]] for x in BASES):
            group.append(p)
    assert len(group) == 8
    def image(code, permutation):
        return tuple(sorted(''.join(permutation[x] for x in w) for w in code))
    outstanding = set(maxima)
    representatives = []
    while outstanding:
        sample = min(outstanding)
        orbit = {image(sample,g) for g in group}
        assert orbit <= outstanding and len(orbit) == 8
        representatives.append(sample)
        outstanding -= orbit
    assert len(representatives) == 4
    types = Counter((sum(w == reverse_complement(w) for w in c),
                     sum(w != reverse_complement(w) for w in c)//2)
                    for c in maxima)
    assert types == {(5,2):24,(1,4):8}
    print('DIRECT_CROSSCHECK_OK', spectrum, 'sum', sum(spectrum),
          'maximum', max(counts), 'maximizers', len(maxima),
          'symmetry_orbits', len(representatives), 'types', dict(types))
    for i,c in enumerate(representatives,1):
        print('MAX_ORBIT',i,','.join(c))
    return representatives

if __name__ == '__main__':
    main()
