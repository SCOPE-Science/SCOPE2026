#!/usr/bin/env python3
"""Two direct checks of finite certificates for completely unclustered BWT extrema.

Input: BWT_WITNESSES.tsv (tab-separated length and last-column word).
Requires Python 3 standard library only.
"""
from pathlib import Path

def stable_LF(last):
    n=len(last)
    first=''.join(sorted(last))
    offsets={a:first.index(a) for a in set(last)}
    occ={a:0 for a in offsets}
    mapping=[]
    for a in last:
        mapping.append(offsets[a]+occ[a])
        occ[a]+=1
    assert sorted(mapping)==list(range(n))
    return mapping

def invert(last):
    pi=stable_LF(last)
    n=len(last)
    seen=set(); p=0; backwards=[]
    for _ in range(n):
        assert p not in seen, ('short LF cycle',n,p)
        seen.add(p)
        backwards.append(last[p])
        p=pi[p]
    assert p==0 and len(seen)==n, ('not one cycle',n)
    return ''.join(reversed(backwards))

def direct_bwt(word):
    shifts=sorted(word[i:]+word[:i] for i in range(len(word)))
    return ''.join(row[-1] for row in shifts)

def circular_runs(word):
    return sum(word[i]!=word[(i+1)%len(word)] for i in range(len(word)))

def main():
    p=Path(__file__).with_name('BWT_WITNESSES.tsv')
    lines=p.read_text(encoding='utf8').splitlines()
    assert lines[0]=='n\tL'
    assert len(lines)==81
    seen=set()
    for line in lines[1:]:
        n_text,L=line.split('\t')
        n=int(n_text)
        assert 81<=n<=160 and n not in seen and len(L)==n and set(L)<=set('012')
        seen.add(n)
        assert all(L[i]!=L[i+1] for i in range(n-1)),('adjacent BWT equality',n)
        # Certificate condition from the standard-permutation formula.
        h=sum(a!=b for a,b in zip(L,sorted(L)))
        assert h==(n+1)//2,('Hamming run condition',n,h)
        # Independent full BWT inversion, input cyclic runs and direct rotation check.
        word=invert(L)
        assert len(set(word[i:]+word[:i] for i in range(n)))==n,('periodic necklace',n)
        assert circular_runs(word)==(n+1)//2,('cyclic run discrepancy',n)
        assert direct_bwt(word)==L,('direct BWT mismatch',n)
    assert seen==set(range(81,161))
    print('VERIFIED: 80 consecutive ternary BWT last columns, lengths 81..160')
    print('VERIFIED: 80 single LF cycles, 80 direct inverse-necklace BWT calculations')
    print('VERIFIED: 80 exact cyclic-run optima ceil(n/2), each with BWT run count n')

if __name__=='__main__':main()
