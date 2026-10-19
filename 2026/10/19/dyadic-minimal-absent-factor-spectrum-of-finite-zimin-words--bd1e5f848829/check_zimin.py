#!/usr/bin/env python3
"""Independent direct factor/enumeration check of a dyadic antidictionary formula."""
from collections import defaultdict, Counter


def zimin(k):
    z = ''
    for v in range(1, k+1):
        z = z + chr(64+v) + z
    return z


def predicted(k):
    words = set()
    for j in range(k):
        mid = zimin(j)
        for i in range(j+1,k+1):
            words.add(chr(64+i)+mid+chr(64+i))
        for i in range(j+2,k+1):
            for h in range(j+2,k+1):
                if i!=h:words.add(chr(64+i)+mid+chr(64+h))
    return words


def enumerated(text):
    # Enumerate factors independently of the proposed Zimin structure.
    fac = set()
    left=defaultdict(set);right=defaultdict(set)
    n=len(text)
    for start in range(n):
        for end in range(start+1,n+1):
            block=text[start:end];fac.add(block)
            if start>0: left[block].add(text[start-1])
            if end<n:right[block].add(text[end])
    left[''].update(text);right[''].update(text)
    found=set()
    for core in left.keys() & right.keys():
        for a in left[core]:
            for b in right[core]:
                w=a+core+b
                if w not in fac:found.add(w)
    return found

for k in range(1,9):
    got=enumerated(zimin(k))
    exp=predicted(k)
    assert got == exp, (k, list(got-exp)[:8], list(exp-got)[:8])
    a={length:num for length,num in Counter(map(len,got)).items()}
    expected = {2**j+1:(k-j-1)**2+1 for j in range(k)}
    assert a == expected,(k,a,expected)
    n=k+k*(k-1)*(2*k-1)//6
    assert len(got)==n,(k,len(got),n)
    print(f'k={k} source_length={2**k-1} minimal_absent={len(got)} lengths={sorted(a.items())}')
print('ZIMIN_ANTIDICTIONARY_PASS k=1..8')
