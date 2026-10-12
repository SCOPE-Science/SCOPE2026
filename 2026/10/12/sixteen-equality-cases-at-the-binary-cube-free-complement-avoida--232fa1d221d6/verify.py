#!/usr/bin/env python3
import json
from pathlib import Path

def comp(s):
    return "".join("1" if c=="0" else "0" for c in s)

def cube_suffix(w):
    n=len(w)
    for p in range(1,n//3+1):
        if w[n-3*p:n-2*p] == w[n-2*p:n-p] == w[n-p:n]:
            return True
    return False

def new_complement_violation(w):
    if len(w)<6:
        return False
    s=w[-6:]
    return comp(s) in w[:-1]

def engine_incremental():
    levels=[[""]]
    for _ in range(1,52):
        nxt=[]
        for w in levels[-1]:
            for c in "01":
                q=w+c
                if cube_suffix(q):
                    continue
                if new_complement_violation(q):
                    continue
                nxt.append(q)
        levels.append(sorted(nxt))
    return levels

def contains_cube(w):
    n=len(w)
    for i in range(n):
        for p in range(1,(n-i)//3+1):
            if w[i:i+p] == w[i+p:i+2*p] == w[i+2*p:i+3*p]:
                return True
    return False

def no_complement_pair6(w):
    fs={w[i:i+6] for i in range(max(0,len(w)-5))}
    return all(comp(x) not in fs for x in fs)

def engine_direct():
    levels=[[""]]
    for _ in range(1,52):
        nxt=[]
        for w in levels[-1]:
            for c in "01":
                q=w+c
                if not contains_cube(q) and no_complement_pair6(q):
                    nxt.append(q)
        levels.append(sorted(nxt))
    return levels

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
A=engine_incremental()
B=engine_direct()
assert A==B
assert [len(x) for x in A] == cert["survivor_counts_by_length_0_to_51"]
assert A[50] == sorted(cert["length_50_extremizers"])
assert len(A[50]) == 16
assert A[51] == []

# Full boundary recheck.
assert all((not contains_cube(w)) and no_complement_pair6(w) for w in A[50])

# Length 6 suffices for all longer complementary pairs:
# if x and comp(x) of length >=6 both occur, their length-6 prefixes do too.
for w in A[50]:
    for L in range(6,len(w)+1):
        fs={w[i:i+L] for i in range(len(w)-L+1)}
        assert all(comp(x) not in fs for x in fs)

def orbit(w):
    c=comp(w)
    return {w,w[::-1],c,c[::-1]}

remaining=set(A[50])
computed=[]
while remaining:
    w=min(remaining)
    o=sorted(orbit(w)&set(A[50]))
    computed.append(o)
    remaining-=set(o)
computed=sorted(computed)
assert computed == sorted(sorted(o) for o in cert["symmetry_orbits"])
assert [len(o) for o in computed] == [4,4,4,4]
assert cert["source_displayed_witness"] in A[50]

print(
    "VERIFY_OK max=50 count50=16 count51=0 engines=2 "
    "symmetry_orbits=4 orbit_sizes=4,4,4,4 counts="
    + ",".join(str(x) for x in cert["survivor_counts_by_length_0_to_51"])
)
