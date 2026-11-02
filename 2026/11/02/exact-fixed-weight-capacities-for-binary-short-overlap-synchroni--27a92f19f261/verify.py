#!/usr/bin/env python3
"""Stand-alone exact checks for the binary three-short-overlap fixed-weight theorem.

All operations use integer arithmetic; no external packages or remote services.
"""
from itertools import product, combinations
from math import comb

K = 3
BLOCKS = tuple(''.join(x) for x in product('01', repeat=K))
P = (('000',), ('000','001'), ('000','001','010'), ('000','001','010','011'))
S = (('001','011','101','111'), ('011','101','111'), ('011','111'), ('111',))

def bad(u, v, tmax=3):
    return any(u[:t] == v[-t:] for t in range(1, tmax+1))

def binom(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0

def predicted(n, w):
    a = binom(n-4,w-1)
    b = 2*binom(n-5,w-2)+binom(n-5,w-3)
    c = binom(n-5,w-2)+2*binom(n-5,w-3)
    d = binom(n-4,w-3)
    return max(a,b,c,d)

def template_words(n, j):
    return [p+''.join(mid)+s for p in P[j] for mid in product('01',repeat=n-6) for s in S[j]]

def cross_overlap_safe(words):
    return all(not bad(u,v) for u in words for v in words)

def compatible_suffixes(ps):
    return tuple(s for s in BLOCKS if all(not bad(p,s) for p in ps))

# Exact neighborhood and nesting identity, the nonstandard structural lemma.
assert [compatible_suffixes((p,)) for p in P[-1]] == list(S)
assert all(set(S[j+1]) <= set(S[j]) for j in range(3))
for j in range(4):
    assert not any(bad(p,s) for p in P[j] for s in S[j])

# Complete 8-prefix-subset enumeration, no stochastic search.
nonempty_allowed = 0
for mask in range(1,1<<len(BLOCKS)):
    ps = tuple(BLOCKS[i] for i in range(len(BLOCKS)) if mask>>i&1)
    ss = compatible_suffixes(ps)
    if not ss:
        continue
    nonempty_allowed += 1
    # Every feasible prefix/suffix rectangle must embed in an orientated
    # four-template rectangle. For the opposite orientation, complement.
    cands = [(P[j], S[j]) for j in range(4)]
    flip = lambda b: ''.join('1' if ch=='0' else '0' for ch in b)
    cands += [(tuple(map(flip,P[j])),tuple(map(flip,S[j]))) for j in range(4)]
    assert any(set(ps)<=set(pp) and set(ss)<=set(s) for pp,s in cands), (ps,ss)
assert nonempty_allowed == 30

# Two independent exact ways of evaluating attainable code sizes:
# (1) weight enumerators of all feasible full rectangles;
# (2) the four closed binomial expressions.
checked_parameters = 0
for n in range(6,31):
    for w in range(n+1):
        brute_rectangle_opt = 0
        for mask in range(1,1<<len(BLOCKS)):
            ps = tuple(BLOCKS[i] for i in range(len(BLOCKS)) if mask>>i&1)
            ss = compatible_suffixes(ps)
            if not ss:
                continue
            count = sum(binom(n-6, w-p.count('1')-s.count('1')) for p in ps for s in ss)
            brute_rectangle_opt = max(brute_rectangle_opt, count)
        assert brute_rectangle_opt == predicted(n,w), (n,w,brute_rectangle_opt,predicted(n,w))
        checked_parameters += 1

# Literal word families, distinct from coefficient evaluation.
checked_words = 0
for n in range(6,12):
    for j in range(4):
        words = template_words(n,j)
        assert cross_overlap_safe(words), (n,j)
        checked_words += len(words)
        for w in range(n+1):
            expected = [binom(n-4,w-1),
                        2*binom(n-5,w-2)+binom(n-5,w-3),
                        binom(n-5,w-2)+2*binom(n-5,w-3),
                        binom(n-4,w-3)][j]
            assert sum(x.count('1')==w for x in words)==expected,(n,w,j)

# Independent maximum-clique search on all literal weight-w words.
def exact_literal_maximum(n,w):
    words=[''.join(x) for x in product('01',repeat=n) if sum(t=='1' for t in x)==w]
    words=[x for x in words if not bad(x,x)]
    allowed=[sum((1<<j) for j,v in enumerate(words) if i!=j and not bad(u,v) and not bad(v,u))
             for i,u in enumerate(words)]
    best=0
    def dfs(chosen, options):
        nonlocal best
        if chosen+options.bit_count()<=best: return
        if not options:
            best=max(best,chosen)
            return
        v=(options & -options).bit_length()-1
        dfs(chosen+1, (options & ~(1<<v)) & allowed[v])
        dfs(chosen, options & ~(1<<v))
    dfs(0,(1<<len(words))-1)
    return best

literal_cases=0
for n in range(6,9):
    for w in range(n+1):
        a=exact_literal_maximum(n,w)
        assert a == predicted(n,w), (n,w,a,predicted(n,w))
        literal_cases+=1

print('VERIFY_OK exact_prefix_subsets=255 viable_subsets=30 rectangle_parameter_cases=%d literal_template_words=%d literal_clique_cases=%d n_range=6..30' %
      (checked_parameters,checked_words,literal_cases))
