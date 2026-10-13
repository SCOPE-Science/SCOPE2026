#!/usr/bin/env python3
"""Enumerate reversal-closed length-eight binary comma-free codes.

Every reversal orbit is either present in its entirety or absent.
Pairwise compatibility is a necessary, NOT sufficient, condition:
a third orbit could contribute a forbidden overlapping word. Enumerate maximal
cliques of the pairwise compatibility graph, then check each clique fully.
"""
from itertools import product

N = 8

def comma_free(words):
    seen = set(words)
    return all((x+y)[i:i+N] not in seen
               for x in words for y in words for i in range(1, N))

words = [''.join(bits) for bits in product('01', repeat=N)]
groups = []
for x in words:
    y = x[::-1]
    if x <= y:
        group = tuple(sorted({x, y}))
        if comma_free(group):
            groups.append(group)

adj = [set() for _ in groups]
for i in range(len(groups)):
    for j in range(i):
        if comma_free(groups[i]+groups[j]):
            adj[i].add(j)
            adj[j].add(i)

maximal = 0
pairwise_best = 0
pairwise_opt = 0
true_best = 0
codes = set()

def bron_kerbosch(chosen, possible, excluded):
    global maximal, pairwise_best, pairwise_opt, true_best, codes
    if not possible and not excluded:
        maximal += 1
        weight = sum(len(groups[v]) for v in chosen)
        code = tuple(sorted(x for v in chosen for x in groups[v]))
        if weight > pairwise_best:
            pairwise_best, pairwise_opt = weight, 0
        if weight == pairwise_best:
            pairwise_opt += 1
        if comma_free(code):
            assert all(x[::-1] in code for x in code)
            if weight > true_best:
                true_best, codes = weight, {code}
            elif weight == true_best:
                codes.add(code)
        return
    # All cliques are traversed; the excluded set avoids duplicates.
    for v in tuple(sorted(possible)):
        bron_kerbosch(chosen + (v,), possible & adj[v], excluded & adj[v])
        possible.remove(v)
        excluded.add(v)

bron_kerbosch((), set(range(len(groups))), set())
summary = ('N_GROUPS=%d SINGLE_GROUPS=%d PAIR_GROUPS=%d COMPAT_EDGES=%d '
           'MAXIMAL=%d PAIRWISE_MAX=%d PAIRWISE_OPT=%d TRUE_MAX=%d TRUE_OPT=%d' %
           (len(groups), sum(len(g)==1 for g in groups),
            sum(len(g)==2 for g in groups),
            sum(len(s) for s in adj)//2, maximal, pairwise_best, pairwise_opt, true_best, len(codes)))
assert summary == ('N_GROUPS=56 SINGLE_GROUPS=12 PAIR_GROUPS=44 '
                   'COMPAT_EDGES=929 MAXIMAL=2107 PAIRWISE_MAX=18 '
                   'PAIRWISE_OPT=16 TRUE_MAX=18 TRUE_OPT=12')
out = summary + '\n' + '\n'.join(','.join(code) for code in sorted(codes)) + '\n'
print(out, end='')
