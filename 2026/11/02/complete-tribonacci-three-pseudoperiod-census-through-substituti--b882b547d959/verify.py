#!/usr/bin/env python3
"""Exact, reproducible check of the bounded Tribonacci pseudoperiod census.

Usage: python3 verify.py triples.csv
The theorem's factor-boundary lemma is mathematically proved in RESULT.md;
the checks below recompute its finite cases from distinct constructions.
"""
import csv
import hashlib
import pathlib
import sys

CUT=1705
SUB={'0':'01','1':'02','2':'0'}
PAIRS={'00','01','02','10','20'}

def sub(word):
    return ''.join(SUB[ch] for ch in word)

def factor_family():
    blocks={x:x for x in '012'}
    exponent=0
    while min(map(len,blocks.values()))<CUT+1:
        blocks={x:sub(blocks[x]) for x in '012'}
        exponent+=1
    assert exponent==14
    assert sorted(len(v) for v in blocks.values())==[3136,4841,5768]
    w=set()
    for xy in PAIRS:
        pair=blocks[xy[0]]+blocks[xy[1]]
        w.update(pair[i:i+CUT+1] for i in range(len(pair)-CUT))
    assert len(w)==3413
    return w

def independent_factors():
    # Deliberately different from adjacent-supertiles construction.
    word='0'
    for _ in range(18):
        word=sub(word)
    factors={word[i:i+CUT+1] for i in range(len(word)-CUT)}
    assert len(factors)==3413
    return factors

def independent_census(windows):
    # Recompute shift-matching masks from an independently generated long prefix.
    full=(1<<(CUT+1))-2
    good=[]
    for w in windows:
        m=0
        first=w[0]
        for j in range(1,CUT+1):
            if w[j]!=first:
                m|=1<<j
        good.append(full ^ m)
    good=tuple(set(good))
    out=[]
    for a in range(1,CUT-1):
        one=1<<a
        for b in range(a+1,CUT):
            bit=one | (1<<b)
            possibilities=full & ~((1<<(b+1))-1)
            for matching_positions in good:
                if not (matching_positions>>a&1 or matching_positions>>b&1):
                    possibilities &= matching_positions
                    if possibilities==0:
                        break
            while possibilities:
                smallest=possibilities & -possibilities
                out.append((a,b,smallest.bit_length()-1))
                possibilities^=smallest
    return sorted(out)

def main():
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python3 verify.py triples.csv')
    csv_path=pathlib.Path(sys.argv[1]); raw=csv_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='03a725ce29a938e5315b6d4f164a788f1b8f90ddde93db8f32fe0f99a2c65c74'
    assert raw.startswith(b'a,b,c\n')
    tuples=[tuple(map(int,row)) for row in csv.reader(raw.decode('ascii').splitlines()[1:])]
    assert len(tuples)==145217
    assert len(set(tuples))==len(tuples)
    assert tuples==sorted(tuples)
    assert all(1<=a<b<c<=CUT for a,b,c in tuples)
    f1=factor_family()
    f2=independent_factors()
    assert f1==f2
    recomputed=independent_census(f2)
    assert tuples==recomputed
    cutoff_counts={7:1,13:4,24:15,44:55,81:207,149:801,274:2648,504:9604,927:37596,1705:145217}
    for upper,expected in cutoff_counts.items():
        assert sum(c<=upper for _,_,c in tuples)==expected
    # Direct tests on a nontrivial independent prefix.
    prefix='0'
    for _ in range(17):
        prefix=sub(prefix)
    for triple in (tuples[0],tuples[1000],tuples[len(tuples)//2],tuples[-1]):
        a,b,c=triple
        assert all(prefix[i] in (prefix[i+a],prefix[i+b],prefix[i+c]) for i in range(len(prefix)-c))
    for t in ((1,2,3),(4,6,8),(13,14,15)):
        a,b,c=t
        assert t not in tuples
        assert any(prefix[i] not in (prefix[i+a],prefix[i+b],prefix[i+c]) for i in range(len(prefix)-c))
    print('VERIFY_OK; factor_set=3413; pseudoperiod_triples=145217; two_independent_factor_enumerations; independent mismatch_census; CSV_hash_OK')

if __name__=='__main__':
    main()
