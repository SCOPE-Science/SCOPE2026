#!/usr/bin/env python3
"""Reproduce finite enumeration for simultaneous non-overlap and one-deletion codes.
Standard-library Python 3; all words and candidate codebooks are generated afresh.
"""
from itertools import product
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
EXPECTED_CAPACITIES = {2:1,3:1,4:1,5:1,6:2,7:2,8:4,9:6,10:9}
EXPECTED_OPTIMA = {2:2,3:4,4:6,5:12,6:4,7:60,8:4,9:4,10:12}

def border_free(w):
    return all(w[:s] != w[-s:] for s in range(1,len(w)))

def overlap_free(u,v):
    n=len(u)
    return all(u[:s] != v[n-s:] and v[:s] != u[n-s:] for s in range(1,n))

def delete_outputs(w):
    return {w[:j]+w[j+1:] for j in range(len(w))}

def orientation_words(n):
    # Any nonempty binary non-overlapping code has the same starting bit
    # in every word, and the opposite ending bit. The complement symmetry
    # permits restricting the census to first bit 0, last bit 1.
    return [''.join(p) for p in product('01', repeat=n)
            if p[0]=='0' and p[-1]=='1' and border_free(''.join(p))]

def compute(n):
    words=orientation_words(n); k=len(words)
    balls=[delete_outputs(w) for w in words]
    later=[0]*k
    for i in range(k):
        for j in range(i+1,k):
            if overlap_free(words[i],words[j]) and not balls[i].intersection(balls[j]):
                later[i] |= 1<<j
    counts=Counter()
    biggest=[]
    top=0
    def traverse(candidates,chosen):
        nonlocal top,biggest
        s=len(chosen)
        counts[s]+=1
        if s>top:
            top=s
            biggest=[chosen]
        elif s==top:
            biggest.append(chosen)
        while candidates:
            lb=candidates & -candidates
            v=lb.bit_length()-1
            candidates ^= lb
            traverse(candidates & later[v],chosen+(v,))
    traverse((1<<k)-1,())
    # Each increasing indexed clique is enumerated once, and every clique
    # is either an empty clique or has a unique increasing enumeration.
    codebooks={tuple(words[j] for j in tup) for tup in biggest}
    assert len(codebooks)==len(biggest)
    return words, counts, top, codebooks

def flip(s):
    return ''.join('1' if x=='0' else '0' for x in s)

def transforms(code):
    ss=set(code)
    return {frozenset(ss), frozenset(w[::-1] for w in ss),
            frozenset(flip(w) for w in ss),
            frozenset(flip(w[::-1]) for w in ss)}

def main():
    results={}
    lines=['n\teligible_words_oriented\tmaximum_code_size\tall_labeled_maximum_codebooks\tclique_counts_oriented_by_size']
    for n in range(2,11):
        words,counts,size,book=compute(n)
        results[n]=(words,counts,size,book)
        assert size==EXPECTED_CAPACITIES[n], (n,size)
        assert 2*len(book)==EXPECTED_OPTIMA[n], (n,len(book))
        lines.append('%d\t%d\t%d\t%d\t%s' %
                     (n,len(words),size,2*len(book),','.join(str(counts[i]) for i in range(size+1))))
    census='\n'.join(lines)+'\n'
    assert (BASE/'census.tsv').read_text(encoding='utf8') == census
    n=10
    books=results[n][-1]
    full={frozenset(code) for b in books for code in [b,tuple(flip(w) for w in b)]}
    assert len(full)==12
    listed=set()
    for l in (BASE/'optima.tsv').read_text(encoding='utf8').splitlines():
        if not l: continue
        code=l.split('\t')
        assert len(code)==9 and all(len(w)==10 and set(w)<={'0','1'} for w in code)
        assert len(code)==len(set(code))
        assert all(border_free(w) for w in code)
        assert all(overlap_free(u,v) and not(delete_outputs(u)&delete_outputs(v))
                   for i,u in enumerate(code) for v in code[i+1:])
        listed.add(frozenset(code))
    assert listed==full and len(listed)==12
    orbits=[]
    pending=set(full)
    while pending:
        a=next(iter(pending)); orbit=transforms(a)
        assert orbit<=full
        orbits.append(orbit)
        pending-=orbit
    assert sorted(len(o) for o in orbits)==[4,4,4]
    # Independent full-word check of the 10-bit example, without using the graph.
    representative=min((tuple(sorted(b)) for b in full))
    assert len(representative)==9
    for i,u in enumerate(representative):
        for v in representative[i+1:]:
            assert not(delete_outputs(u)&delete_outputs(v))
            assert overlap_free(u,v)
    print('CAPACITIES',[(n,results[n][2]) for n in range(2,11)])
    print('OPTIMAL_CODEBOOK_COUNTS',[(n,2*len(results[n][3])) for n in range(2,11)])
    print('N10_ORIENTED_CLIQUE_CENSUS',dict(sorted(results[10][1].items())))
    print('N10_SYMMETRY_ORBITS',[len(x) for x in orbits])
    print('VERIFY_OK')

if __name__=='__main__':main()
