"""Standalone finite checks for cyclic scattered-01 dispersion theorem.

Run with Python 3: python check.py
Only the mathematical enumeration and constructions are checked; the general
proof is given separately.
"""
from itertools import combinations
from math import comb, gcd


def scattered01(w):
    zeros=0
    total=0
    for bit in w:
        if bit==0:
            zeros+=1
        else:
            total+=zeros
    return total


def rotations(w):
    n=len(w)
    return tuple(w[i:]+w[:i] for i in range(n))


def spectrum(w):
    return tuple(scattered01(r) for r in rotations(w))


def predicted_word(n,b,second):
    assert n>=5 and 2<=b<=n-2 and gcd(n,b)==1
    h=[]
    for i in range(n+1):
        residue=(-b*i)%n
        h.append(n+1 if (second and residue==1) else residue)
    w=tuple((h[i+1]-h[i]+b)//n for i in range(n))
    assert h[0]==h[-1]==0
    assert all(h[i+1]-h[i]+b in (0,n) for i in range(n))
    assert sum(w)==b
    return w


def check():
    cases=0
    necklaces=0
    words_checked=0
    rotations_checked=0
    for n in range(5,16):
        for b in range(2,n-1):
            if gcd(n,b)!=1:
                continue
            a=n-b
            lo0=(a*b-n+1)//2
            lo2=(a*b-n-1)//2
            assert (a*b-n+1)%2==0
            assert (a*b-n-1)%2==0
            expected0=set(range(lo0,lo0+n))
            expected2=set(range(lo2,lo2+n+2))-{lo2+1,lo2+n}
            m=predicted_word(n,b,False)
            e=predicted_word(n,b,True)
            assert set(spectrum(m))==expected0
            assert set(spectrum(e))==expected2
            assert len(set(rotations(m)))==len(set(rotations(e)))==n
            assert set(rotations(m)).isdisjoint(set(rotations(e)))
            count0=count2=0
            observed=set()
            for idx in combinations(range(n),b):
                w=tuple(int(i in idx) for i in range(n))
                S=spectrum(w)
                assert len(set(S))==n  # distinct residues, coprime content
                d=max(S)-min(S)
                assert d>=n-1 and d!=n
                if d==n-1:
                    count0+=1
                    assert w in rotations(m) and set(S)==expected0
                if d==n+1:
                    count2+=1
                    assert w in rotations(e) and set(S)==expected2
                observed.add(d)
                words_checked+=1
                rotations_checked+=n
            assert count0==count2==n, (n,b,count0,count2)
            assert len(observed)>1
            cases+=1
            necklaces+=2
    print('CYCLIC_2_BINOMIAL_SPREAD_PASS',
          f'n_range=5..15',f'coprime_classes={cases}',
          f'full_words_checked={words_checked}',
          f'rotations_checked={rotations_checked}',
          f'extremal_necklaces_checked={necklaces}')

if __name__=='__main__':
    check()
