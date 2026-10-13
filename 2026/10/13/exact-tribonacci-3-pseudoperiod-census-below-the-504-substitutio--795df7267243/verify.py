#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, time
root=Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
listed=[]
for line in (root/'triples.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    if line.strip(): listed.append(tuple(map(int,line.split('\t'))))
assert len(listed)==9352 and len(set(listed))==9352
assert hashlib.sha256((root/'triples.tsv').read_bytes()).hexdigest()==cert['triples_tsv_sha256']

def morph(w): return ''.join('01' if c=='0' else '02' if c=='1' else '0' for c in w)
W=['0']
for _ in range(15): W.append(morph(W[-1]))
prefix=W[15]
assert len(prefix)==10609
assert [len(W[i]) for i in range(11)]==[1,2,4,7,13,24,44,81,149,274,504]

def factors(m): return sorted({prefix[i:i+m] for i in range(len(prefix)-m+1)})
# Check every factor-language size required by the proof.
for m in range(1,505):
    assert len(factors(m))==2*m+1,(m,len(factors(m)))
# Exhaustive census via mismatch bitsets.
A=[]
for c in range(3,504):
    fs=factors(c+1)
    bad=[0]*(c+1)
    for j,x in enumerate(fs):
        bit=1<<j; x0=x[0]
        for d in range(1,c+1):
            if x[d]!=x0: bad[d]|=bit
    bc=bad[c]
    for a in range(1,c-1):
        ba=bad[a]
        for b in range(a+1,c):
            if ba & bad[b] & bc == 0: A.append((a,b,c))
assert A==listed
# Independent positive-certificate replay directly on strings.
byc={}
for t in listed: byc.setdefault(t[2],[]).append(t)
for c,ts in byc.items():
    fs=factors(c+1)
    for a,b,_ in ts:
        assert all(x[0] in (x[a],x[b],x[c]) for x in fs),(a,b,c)
cum={str(Q):sum(c<Q for a,b,c in listed) for Q in (7,13,24,44,81,149,274,504)}
assert cum=={'7':0,'13':2,'24':9,'44':42,'81':172,'149':676,'274':2402,'504':9352}
first9=[x for x in listed if x[2]<24]
assert first9==[(4,6,7),(6,7,11),(4,7,13),(7,11,13),(11,13,14),(6,7,17),(7,13,17),(6,11,20),(11,13,20)]
print('VERIFY_OK factors_m=1..504 p=2m+1 triples_c<504=9352 exhaustive=mismatch positive_replay=9352 cumulative=0,2,9,42,172,676,2402,9352 first9=checked')
