#!/usr/bin/env python3
"""Exact finite checks of circular three-marker k-mer reconstruction thresholds."""
from itertools import combinations
from collections import defaultdict, Counter

def canonical(word):
    return min(word[i:] + word[:i] for i in range(len(word)))

def all_classes(n):
    output = set()
    for support in combinations(range(n), 3):
        word = ''.join('1' if j in support else '0' for j in range(n))
        output.add(canonical(word))
    return sorted(output)

def ordered_gaps(w):
    n = len(w)
    s = [i for i, x in enumerate(w) if x == '1']
    assert len(s) == 3
    return tuple((s[(j+1) % 3] - s[j] - 1) % n for j in range(3))

def predicted(g):
    a,b,c=sorted(g)
    if a<b<c: return a+b+3
    if a==b<c: return a+1 if c==a+1 else a+2
    if a<b==c: return b+1
    return a+1

def spectrum(word,k):
    n=len(word)
    expanded=word + word[:k-1]
    counts=Counter(expanded[i:i+k] for i in range(n))
    return tuple(sorted(counts.items()))

def spectrum_alt(word,k):
    n=len(word)
    return tuple(sorted(''.join(word[(i+j)%n] for j in range(k)) for i in range(n)))

def check(nmax=30):
    total=0; distinct=0; repeated=0; comparisons=0
    for n in range(3,nmax+1):
        classes=all_classes(n)
        max_k=max(predicted(ordered_gaps(w)) for w in classes)
        for k in range(1,max_k+1):
            inv=defaultdict(list)
            for word in classes:
                inv[spectrum(word,k)].append(word)
            for word in classes:
                g=ordered_gaps(word); predicted_k=predicted(g)
                actual_unique=(len(inv[spectrum(word,k)])==1)
                assert actual_unique==(k>=predicted_k),(n,word,g,k,predicted_k,inv[spectrum(word,k)])
                comparisons+=1
                if k==predicted_k:
                    assert spectrum(word,k)==tuple(sorted(Counter(spectrum_alt(word,k)).items())),(n,word,k)
        for w in classes:
            g=ordered_gaps(w)
            if len(set(g))==3:
                distinct+=1
                assert canonical(w[::-1])!=w
                for k in range(1,predicted(g)):
                    assert spectrum(w,k)==spectrum(w[::-1],k)
            else:repeated+=1
        total+=len(classes)
    print('THREE_MARKER_K_SPECTRUM_PASS n=3..%d necklace_classes=%d distinct_gap=%d repeated_gap=%d uniqueness_decisions=%d'%(nmax,total,distinct,repeated,comparisons))

if __name__=='__main__':check()
