#!/usr/bin/env python3
"""Exact group-orbit certificates for the Thue-Morse factor family."""
from itertools import permutations
from collections import Counter

def mu(s):
    return ''.join('01' if c == '0' else '10' for c in s)

def factors(n):
    m = 0
    while (1 << m) < n:
        m += 1
    blocks = ['00','01','10','11']
    for _ in range(m):
        blocks = [mu(w) for w in blocks]
    return frozenset(w[i:i+n] for w in blocks for i in range(len(w)-n+1))

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def subgroup(generators, n):
    ident = tuple(range(n))
    found = {ident}
    todo = [ident]
    while todo:
        x = todo.pop()
        for g in generators:
            y = compose(x,g)
            if y not in found:
                found.add(y)
                todo.append(y)
    return found

def classes(facts, permutations_):
    n = len(next(iter(facts)))
    d = {}
    for word in facts:
        image = min(''.join(word[g[i]] for i in range(n)) for g in permutations_)
        d.setdefault(image, []).append(word)
    return sorted([tuple(sorted(v)) for v in d.values()])

# One-line cycle notation below is the list of images of 1,...,n, not cycles.
W4 = {
 3: [[1,3,4,2],[2,1,4,3]],
 4: [[1,3,4,2]],
 5: [[1,3,2,4],[4,2,3,1]],
 6: [[1,3,2,4]],
 7: [[1,2,4,3],[2,1,3,4]],
 8: [[1,2,4,3]],
 10: []
}
W6 = {
 3: [[1,2,3,5,6,4],[4,5,6,1,2,3]],
 4: [[1,2,3,5,6,4],[2,3,1,4,5,6]],
 5: [[2,3,6,1,4,5]],
 6: [[1,3,4,6,2,5]],
 7: [[2,3,6,5,4,1]],
 8: [[2,3,1,5,6,4]],
 9: [[2,1,4,5,6,3]],
 10: [[1,3,2,4,6,5]],
 11: [[6,3,2,5,4,1]],
 12: [[1,3,2,5,4,6]],
 13: [[2,1,4,3,6,5]],
 14: [[1,2,3,4,6,5]],
 16: []
}

for n, expected, witness in [(4,{3,4,5,6,7,8,10},W4),
                              (6,set(range(3,15))|{16},W6)]:
    F=factors(n)
    actual_all=[]
    singleton = []
    for p in permutations(range(n)):
        c=classes(F,subgroup([p],n))
        actual_all.append(len(c))
        if len(c) == len(F)-1:
            singleton.append(p)
    assert not singleton, (n, singleton)
    assert len(F)=={4:10,6:16}[n]
    assert len({w.count('1') for w in F})==3
    assert set(witness)==expected
    for target, gens in witness.items():
        g=[tuple(x-1 for x in p) for p in gens]
        got=len(classes(F,subgroup(g,n)))
        assert got==target,(n,target,got)
    assert max(actual_all)==len(F)
    print('n=',n,'factors=',len(F),'cyclic_subgroups_checked=',len(actual_all),
          'cyclic_counts=',sorted(Counter(actual_all).items()),
          'attainable_values=',sorted(expected),'all_witnesses_valid=True')

n=8
F=factors(n)
g=tuple(x-1 for x in [2,1,8,5,4,7,6,3])
c=classes(F,subgroup([g],n))
merged=[z for z in c if len(z)>1]
assert len(F)==22
assert len(c)==21
assert merged==[('01001011','10110100')],merged
print('n=8 factors=22 classes=21 unique_merged_pair=',merged,
      'involution_order=',len(subgroup([g],n)))
print('ALL CHECKS PASS')
