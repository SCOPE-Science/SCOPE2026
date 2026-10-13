#!/usr/bin/env python3
import itertools, json
from pathlib import Path
ALPH="012"

def factors(w):
    return {w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1)}

def bad_A(w):
    fac=factors(w)
    for f in fac:
        L=len(f)
        for a in range(1,(L-1)//2+1):
            if f[:a]==f[-a:]:
                y=f[a:L-a]
                if y and y[::-1] in fac:
                    return True
    return False

def bad_B(w):
    fac=factors(w)
    for x in fac:
        for y in fac:
            if y[::-1] in fac and x+y+x in fac:
                return True
    return False

def build(bad):
    levels=[[""]]
    for _ in range(1,16):
        nxt=[]
        for w in levels[-1]:
            for c in ALPH:
                q=w+c
                if not bad(q):
                    nxt.append(q)
        levels.append(sorted(nxt))
    return levels

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
A=build(bad_A)
B=build(bad_B)
assert A==B
assert [len(x) for x in A]==cert["survivor_counts_by_length_0_to_15"]
assert A[14]==sorted(cert["length_14_extremizers"])
assert len(A[14])==6
assert A[15]==[]

rep=cert["alphabet_permutation_orbit_representative"]
imgs=set()
for p in itertools.permutations(ALPH):
    imgs.add(rep.translate(str.maketrans(dict(zip(ALPH,p)))))
assert sorted(imgs)==A[14]
assert len(imgs)==6
assert sorted(w[::-1] for w in A[14])==A[14]

print("VERIFY_OK max=14 count14=6 count15=0 engines=2 permutation_orbit=6 reversal_closed=1 counts="+",".join(map(str,cert["survivor_counts_by_length_0_to_15"])))
