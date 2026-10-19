"""Exact verifier of ternary witnesses to the unclustered-BWT run bound.
Input witnesses.json must be in the same directory. Python 3 stdlib only.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'witnesses.json').read_text('utf8'))['witness_bwt_images']
assert set(DATA)==set(str(n) for n in range(14,81))

def direct_bwt(word):
    length=len(word)
    # Sort all distinct circular rotations lexicographically.
    ordered=sorted(range(length),key=lambda j: word[j:]+word[:j])
    return ''.join(word[(j-1)%length] for j in ordered)

def cyclic_run_count(word):
    return sum(word[i]!=word[(i-1)%len(word)] for i in range(len(word)))

def inverse_bwt(L):
    n=len(L)
    F=''.join(sorted(L))
    first={letter:F.index(letter) for letter in sorted(set(L))}
    occur={letter:0 for letter in first}
    pi=[]
    for x in L:
        pi.append(first[x]+occur[x]);occur[x]+=1
    # Standard LF map must be one orbit, not merely an arbitrary permutation.
    orbit=[];seen=set();i=0
    for _ in range(n):
        assert i not in seen,('premature cycle',n,len(seen))
        seen.add(i);orbit.append(i);i=pi[i]
    assert i==0 and len(seen)==n
    # Traversing LF yields symbols of one inverse rotation backwards.
    word=''.join(F[i] for i in orbit)[::-1]
    return word,F,pi

for n in range(14,81):
    L=DATA[str(n)]
    assert len(L)==n and set(L)<=set('012')
    assert all(L[i]!=L[i+1] for i in range(n-1))
    word,F,pi=inverse_bwt(L)
    assert all(word != word[:d]*(n//d) for d in range(1,n) if n%d==0)
    # Independent direct sorting of all n cyclic rotations, not an LF restatement.
    assert direct_bwt(word)==L,('BWT mismatch',n)
    actual=cyclic_run_count(word)
    assert actual==(n+1)//2,('cyclic runs',n,actual)
    assert sum(L[i]!=F[i] for i in range(n))==actual
print('CERTIFICATE_OK: exactly 67 consecutive lengths 14..80; each primitive, 1 LF cycle, completely unclustered direct BWT, and cyclic runs ceil(n/2).')
