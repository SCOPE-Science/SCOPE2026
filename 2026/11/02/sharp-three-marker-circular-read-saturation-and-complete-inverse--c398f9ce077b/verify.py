#!/usr/bin/env python3
"""Direct factor-spectrum verification of a three-marker circular classification.

Stdlib-only; run: python3 verify.py. This is a finite check, not a proof for all k,n.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def observed_profile(n, k, positions):
    """Read actual bit positions, without using gaps or predicted profile labels."""
    bit = [0]*n
    for p in positions:
        bit[p] = 1
    hist = [0]*(1 << k)
    for start in range(n):
        factor = 0
        for j in range(k):
            factor = 2*factor + bit[(start+j) % n]
        hist[factor] += 1
    return tuple(hist)


def class_label(n, k, positions):
    p, q, r = positions
    ds = (q-p, r-q, n-r+p)
    short_indices = [i for i,d in enumerate(ds) if d < k]
    if len(short_indices) == 0:
        return ('A',)
    if len(short_indices) == 1:
        return ('B', ds[short_indices[0]])
    assert len(short_indices) == 2
    i = (short_indices[0])
    if (i + 1) % 3 == short_indices[1]:
        a, b = ds[i], ds[short_indices[1]]
    else:
        a, b = ds[short_indices[1]], ds[i]
    if a+b < k:
        return ('D', a, b)
    return ('C', min(a,b), max(a,b))


def label_from_multispectrum(k, spectrum):
    """Recover gap class from observed factors alone, by inclusion correlations."""
    three = []
    for a in range(1, k):
        for b in range(1, k-a):
            mask = (1 << (k-1)) | (1 << (k-1-a)) | (1 << (k-1-a-b))
            f = sum(m for word, m in enumerate(spectrum) if word & mask == mask)
            if f:
                assert f == 1, (k, a, b, f)
                three.append((a,b))
    if three:
        assert len(three) == 1, (k, three)
        return ('D', *three[0])
    short = []
    for d in range(1,k):
        mask = (1 << (k-1)) | (1 << (k-1-d))
        f = sum(m for word,m in enumerate(spectrum) if word & mask == mask)
        short.extend([d]*f)
    if not short:
        return ('A',)
    if len(short)==1:
        return ('B', short[0])
    assert len(short)==2,(k,short)
    return ('C',*sorted(short))


def predicted_count(k, n):
    s = k-1
    return k+s*s-(s*s//4)-(n == 3*k-1)


def predicted_fiber(k, n, label):
    t = label[0]
    if t == 'A':
        return n*comb(n-3*k+2, 2)//3
    if t == 'B':
        a = label[1]
        return n*(n-a-2*k+1)
    if t == 'C':
        return n*(1 if label[1] == label[2] else 2)
    if t == 'D':
        return n
    raise AssertionError(label)


def theoretical_labels(k,n):
    out=set()
    if n >= 3*k: out.add(('A',))
    out.update(('B', a) for a in range(1,k))
    out.update(('C', a,b) for a in range(1,k) for b in range(a,k) if a+b >= k)
    out.update(('D', a,b) for a in range(1,k) for b in range(1,k-a))
    return out


def exhaustive_case(k, n):
    spectra = {}
    label_to_spec = {}
    frequencies=Counter()
    count=0
    for positions in combinations(range(n),3):
        spec=observed_profile(n,k,positions)
        label=class_label(n,k,positions)
        if spec in spectra:
            assert spectra[spec]==label,(n,k,label,spectra[spec])
        else:
            spectra[spec]=label
        if label in label_to_spec:
            assert label_to_spec[label]==spec,(n,k,label)
        else:
            label_to_spec[label]=spec
        frequencies[label]+=1
        count+=1
    # Decode each unique observed spectrum by correlation inversion alone.
    for spec, label in spectra.items():
        assert label_from_multispectrum(k, spec) == label, (n,k,label)
    want=theoretical_labels(k,n)
    assert set(frequencies)==want,(n,k,want-set(frequencies),set(frequencies)-want)
    assert len(spectra)==predicted_count(k,n)
    for label,multiplicity in frequencies.items():
        assert multiplicity==predicted_fiber(k,n,label),(n,k,label,multiplicity)
    assert count==comb(n,3)==sum(frequencies.values())
    return count,len(spectra)


def mathematical_checks():
    for k in range(2,125):
        for n in (3*k-1,3*k,3*k+1,3*k+7):
            labels=theoretical_labels(k,n)
            assert len(labels)==predicted_count(k,n)
            assert sum(predicted_fiber(k,n,p) for p in labels)==comb(n,3)
            for p in labels:
                if p[0]=='C': assert p[1]+p[2]>=k
                if p[0]=='D': assert p[1]+p[2]<k
    return 123*4


def main():
    cases=[]
    for k in range(2,11):
        for n in (3*k-1,3*k,3*k+1,3*k+3):
            cases.append((k,n))
    checked = 0
    for k,n in cases:
        source, profiles = exhaustive_case(k,n)
        checked += source
        print(f'k={k:2d} n={n:2d} words={source:5d} profiles={profiles:3d}')
    theory = mathematical_checks()
    print(f'VERIFY_OK {len(cases)} direct cases, {checked} indexed source words, '
          f'{theory} large-parameter combinatorial identities')


if __name__=='__main__':
    main()
