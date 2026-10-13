#!/usr/bin/env python3
import json
from pathlib import Path

def complement(w):
    return "".join("1" if c == "0" else "0" for c in w)

def suffix_has_large_antisquare(w):
    n=len(w)
    for h in range(4,n//2+1):
        s=w[n-2*h:]
        if all(s[j] != s[h+j] for j in range(h)):
            return True
    return False

def suffix_has_eight_thirds_power(w):
    n=len(w)
    # Any newly created forbidden factor must be a suffix.
    for L in range(1,n+1):
        s=w[n-L:]
        for p in range(1,L):
            if 3*L < 8*p:
                continue
            if all(s[j] == s[j-p] for j in range(p,L)):
                return True
    return False

def direct_valid(w):
    n=len(w)
    # Independent whole-word antisquare check.
    for i in range(n):
        for h in range(4,(n-i)//2+1):
            s=w[i:i+2*h]
            if all(s[j] != s[h+j] for j in range(h)):
                return False
    # Independent whole-word exponent check.
    for i in range(n):
        for L in range(1,n-i+1):
            s=w[i:i+L]
            for p in range(1,L):
                if 3*L >= 8*p and all(s[j] == s[j-p] for j in range(p,L)):
                    return False
    return True

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
expected=cert["survivor_counts_by_length"]["0_to_30"]

survivors=[""]
seen=[1]
level29=None
for n in range(1,31):
    nxt=[]
    for w in survivors:
        for c in "01":
            q=w+c
            if suffix_has_large_antisquare(q):
                continue
            if suffix_has_eight_thirds_power(q):
                continue
            nxt.append(q)
    survivors=nxt
    seen.append(len(survivors))
    if n==29:
        level29=sorted(survivors)

assert seen==expected
assert len(level29)==8
assert level29==sorted(cert["length_29_extremizers"])
assert not survivors

# Directly recheck every equality case without incremental assumptions.
assert all(direct_valid(w) for w in level29)

def orbit(w):
    c=complement(w)
    return {w,w[::-1],c,c[::-1]}

remaining=set(level29)
computed=[]
while remaining:
    w=min(remaining)
    o=orbit(w) & set(level29)
    computed.append(sorted(o))
    remaining-=o
computed=sorted(computed)
expected_orbits=sorted(sorted(o) for o in cert["symmetry_orbits"])
assert computed==expected_orbits
assert [len(o) for o in computed]==[4,4]

# The source's displayed witness is one equality case.
assert cert["source_table_representative"] in level29

print("VERIFY_OK max=29 count29=8 count30=0 orbits=2 counts=" +
      ",".join(str(x) for x in seen))
