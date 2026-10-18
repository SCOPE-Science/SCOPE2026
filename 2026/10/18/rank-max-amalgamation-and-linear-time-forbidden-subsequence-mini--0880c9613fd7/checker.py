#!/usr/bin/env python3
"""Subsequence-pattern-rank amalgamation and minimal-supersequence verification.

Run with the Python standard library: python checker.py
"""
from itertools import product
import random


def subseq(a, b):
    it = iter(b)
    return all(any(c == x for c in it) for x in a)


def pattern_rank(w, p):
    """Largest t for which p[:t] is a subsequence of w."""
    if not p:
        return 0
    t = 0
    for c in w:
        if t < len(p) and c == p[t]:
            t += 1
    return t


def amalgamate(words, p):
    """Return P-avoiding common supersequence, or None; O(total input length+len(p))."""
    if not p:
        return None
    groups = [[]]
    T = 0
    for w in words:
        t = 0
        for c in w:
            if t < len(p) and c == p[t]:
                t += 1
                if t == len(p):
                    return None
                while len(groups) <= t:
                    groups.append([])
            else:
                while len(groups) <= t:
                    groups.append([])
                groups[t].append(c)
        T = max(T, t)
    return ''.join(''.join(groups[j]) + (p[j] if j<T else '') for j in range(T+1))


def minimalize_two(a, b, s):
    """One sweep + rightmost embeddings; O(len(s)+len(a)+len(b))."""
    assert subseq(a, s) and subseq(b, s)
    def right_positions(w):
        pos = [-1] * len(w)
        j = len(w)-1
        for z in range(len(s)-1, -1, -1):
            if j>=0 and s[z] == w[j]:
                pos[j] = z
                j -= 1
        assert j == -1
        return pos
    ra, rb = right_positions(a), right_positions(b)
    i=j=0; ans=[]
    for z,c in enumerate(s):
        if (i==len(a) or ra[i]>z) and (j==len(b) or rb[j]>z):
            continue
        ans.append(c)
        if i<len(a) and a[i]==c: i+=1
        if j<len(b) and b[j]==c: j+=1
    assert i==len(a) and j==len(b)
    return ''.join(ans)



def minimalize_k(words, s):
    """Self-contained O(k*len(s)+total input length) greedy reduction for k strings."""
    assert all(subseq(x,s) for x in words)
    right=[]
    for x in words:
        places=[-1]*len(x)
        t=len(x)-1
        for pos in range(len(s)-1,-1,-1):
            if t>=0 and s[pos]==x[t]:
                places[t]=pos
                t-=1
        assert t==-1
        right.append(places)
    matching=[0]*len(words)
    kept=[]
    for pos,c in enumerate(s):
        if all(matching[i]==len(x) or right[i][matching[i]]>pos
               for i,x in enumerate(words)):
            continue
        kept.append(c)
        for i,x in enumerate(words):
            if matching[i]<len(x) and x[matching[i]]==c:
                matching[i]+=1
    assert all(matching[i]==len(x) for i,x in enumerate(words))
    return ''.join(kept)


def minimalize_reference(words, s):
    """Slow deletion-only reference for testing, not the asymptotic algorithm."""
    assert all(subseq(w,s) for w in words)
    i=0
    while i<len(s):
        c=s[:i]+s[i+1:]
        if all(subseq(w,c) for w in words):
            s=c
        else:
            i+=1
    return s


def test_exhaustive():
    words={k:[''.join(x) for x in product('01',repeat=k)] for k in range(8)}
    checks=0
    for a_length in range(4):
        for b_length in range(4):
            universe=sum([words[n] for n in range(a_length+b_length+1)], [])
            for a in words[a_length]:
                for b in words[b_length]:
                    for p_length in range(1,4):
                        for p in words[p_length]:
                            w=amalgamate([a,b],p)
                            brute=any(subseq(a,z) and subseq(b,z) and not subseq(p,z) for z in universe)
                            assert (w is not None)==brute,(a,b,p)
                            expected=max(pattern_rank(a,p),pattern_rank(b,p))
                            if w is not None:
                                assert all(subseq(x,w) for x in (a,b)) and pattern_rank(w,p)==expected
                                z=minimalize_two(a,b,w)
                                assert all(subseq(x,z) for x in (a,b)) and not subseq(p,z)
                                assert all(not(all(subseq(x,z[:i]+z[i+1:]) for x in (a,b))) for i in range(len(z)))
                                reference=minimalize_reference([a,b],w)
                                assert z==reference, (a,b,p,w,z,reference)
                            else:
                                assert expected==len(p)
                            checks+=1
    print('exhaustive_binary_two_input_pattern_cases:',checks)
    multi=0
    for k in range(1,5):
        # Exhaustive input families with each length 0..2; patterns length 1..3.
        base=sum((words[j] for j in range(3)),[])
        for inputs in product(base,repeat=k):
            for r in range(1,4):
                for p in words[r]:
                    w=amalgamate(inputs,p)
                    expected=max((pattern_rank(x,p) for x in inputs),default=0)
                    assert (w is None)==(expected==r),(inputs,p)
                    if w is not None:
                        assert all(subseq(x,w) for x in inputs)
                        assert pattern_rank(w,p)==expected
                        v=minimalize_k(inputs,w)
                        assert all(subseq(x,v) for x in inputs) and not subseq(p,v)
                        assert all(not(all(subseq(x,v[:j]+v[j+1:]) for x in inputs)) for j in range(len(v)))
                        assert v==minimalize_reference(inputs,w)
                    multi+=1
    print('exhaustive_binary_up_to_four_inputs_cases:',multi)
    rng=random.Random(4813)
    for _ in range(2000):
        inputs=[''.join(rng.choices('0123',k=rng.randrange(25))) for j in range(rng.randrange(1,7))]
        p=''.join(rng.choices('0123',k=rng.randrange(1,25)))
        w=amalgamate(inputs,p)
        exp=max(pattern_rank(x,p) for x in inputs)
        assert (w is None)==(exp==len(p))
        if w is not None:
            assert pattern_rank(w,p)==exp and all(subseq(x,w) for x in inputs)
            z=minimalize_k(inputs,w)
            assert all(subseq(x,z) for x in inputs) and not subseq(p,z)
    print('random_quaternary_family_cases:',2000)
    for m in [2,3,4,5,9]:
        a,b,p='0'*m+'1','1'+'0'*m,'11'
        w=amalgamate([a,b],p)
        z=minimalize_two(a,b,w)
        assert z=='0'*m+'1'+'0'*m,(m,z)
        print(f'separation_m={m}: shortest_unconstrained={m+2}, unique_minimal_avoiding={z}, length={len(z)}')
    print('PASS')

if __name__=='__main__':
    test_exhaustive()
