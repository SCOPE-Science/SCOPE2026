#!/usr/bin/env python3
import json
from pathlib import Path

def suffix_cube(w):
    n=len(w)
    for h in range(1,n//3+1):
        if w[n-3*h:n-2*h]==w[n-2*h:n-h]==w[n-h:n]:
            return True
    return False

def has_cube(w):
    n=len(w)
    for i in range(n):
        for h in range(1,(n-i)//3+1):
            if w[i:i+h]==w[i+h:i+2*h]==w[i+2*h:i+3*h]:
                return True
    return False

def engine_suffix():
    levels=[[""]]
    for _ in range(1,23):
        nxt=[]
        for w in levels[-1]:
            for c in "01":
                q=w+c
                if not suffix_cube(q):
                    nxt.append(q)
        levels.append(sorted(nxt))
    return levels

def engine_direct():
    levels=[[""]]
    for _ in range(1,23):
        nxt=[]
        for w in levels[-1]:
            for c in "01":
                q=w+c
                if not has_cube(q):
                    nxt.append(q)
        levels.append(sorted(nxt))
    return levels

def delicate(w):
    if has_cube(w):
        return False
    for i,c in enumerate(w):
        q=w[:i]+("1" if c=="0" else "0")+w[i+1:]
        if not has_cube(q):
            return False
    return True

def comp(w):
    return "".join("1" if c=="0" else "0" for c in w)

def orbit(w):
    return {w,w[::-1],comp(w),comp(w)[::-1]}

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
A=engine_suffix()
B=engine_direct()
assert A==B
assert [len(x) for x in A]==cert["cube_free_counts_by_length_0_to_22"]
D={n:sorted(w for w in A[n] if delicate(w)) for n in range(1,23)}
assert [len(D[n]) for n in range(1,23)]==cert["delicate_counts_by_length_1_to_22"]
assert all(len(D[n])==0 for n in range(1,20))
for n in (20,21,22):
    e=sorted(cert["delicate_words"][str(n)])
    assert D[n]==e
    assert orbit(e[0])==set(e)
    for w in e:
        assert not has_cube(w)
        for i,c in enumerate(w):
            q=w[:i]+("1" if c=="0" else "0")+w[i+1:]
            assert has_cube(q)
print("VERIFY_OK first=20 counts20_21_22=2,4,2 orbits=1,1,1 orbit_sizes=2,4,2 engines=2 cubefree20_21_22="+",".join(str(len(A[n])) for n in (20,21,22)))
