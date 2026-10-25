#!/usr/bin/env python3
"""Exhaustive small-alphabet check of exact prefix/suffix Parikh fibers.
No data files or third-party dependencies are needed.
"""
from collections import defaultdict, Counter
from itertools import product, combinations
from math import comb


def full_deck(word, q):
    """Directly construct the multiset of Parikh vectors of all prefixes/suffixes."""
    z=[]
    n=len(word)
    for ell in range(1, n+1):
        for segment in (word[:ell], word[n-ell:]):
            z.append(tuple(segment.count(c) for c in range(q)))
    return tuple(sorted(z))


def shell_deck(word, q):
    """Independent representation: unordered pair at each outer length."""
    l=[0]*q
    r=[0]*q
    result=[]
    for a,b in zip(word, reversed(word)):
        l[a]+=1; r[b]+=1
        result.append(tuple(sorted((tuple(l), tuple(r)))))
    return tuple(result)


def expected_four_fibers(q):
    out = set()
    for outer in combinations(range(q),2):
        for middle in combinations(range(q),2):
            a,b = outer; c,d = middle
            out.add(frozenset(((a,b,c,d,a,b), (a,b,d,c,a,b),
                               (b,a,c,d,b,a), (b,a,d,c,b,a))))
    return out


def census(q,n):
    buckets=defaultdict(set)
    for word in product(range(q),repeat=n):
        k=full_deck(word,q)
        assert tuple(sorted(pair for stage in shell_deck(word,q) for pair in stage))==k
        buckets[k].add(word)
    palindrome=q**((n+1)//2)
    rev_orbits=(q**n + palindrome)//2
    if n<=5:
        assert len(buckets)==rev_orbits
        assert all(v=={next(iter(v)), next(iter(v))[::-1]} for v in buckets.values())
        assert all(len(v) in (1,2) for v in buckets.values())
        return (len(buckets),0)
    assert n==6
    c=comb(q,2)**2
    expected=expected_four_fibers(q)
    fours={frozenset(v) for v in buckets.values() if len(v)>2}
    assert fours==expected,(q,len(fours),len(expected))
    assert all(len(v) in (1,2,4) for v in buckets.values())
    assert sum(len(v)==1 for v in buckets.values())==palindrome
    assert sum(len(v)==4 for v in buckets.values())==c
    assert sum(len(v)==2 for v in buckets.values())==(q**6-palindrome-4*c)//2
    assert len(buckets)==rev_orbits-c
    return len(buckets),len(fours)


def main():
    for q in range(2,8):
        vals=[census(q,n) for n in range(1,7)]
        print('q=',q,'classes=',[v[0] for v in vals],
              'four-fibers-at-six=',vals[-1][1],flush=True)
    print('PREFIX_SUFFIX_FIRST_COLLISION_PASS alphabets=2..7 lengths=1..6 methods=two-deck-representations all-fibers=classified')

if __name__=='__main__':main()
