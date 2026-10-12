#!/usr/bin/env python3
import json
from collections import Counter
from hashlib import sha256
from pathlib import Path

N=5
L=1<<N

def minrot(s):
    return min(s[i:]+s[:i] for i in range(len(s)))

def complement(s):
    return ''.join('1' if c=='0' else '0' for c in s)

def discrepancy_prefix(s):
    z=lo=hi=0
    for c in s:
        z += 1 if c=='1' else -1
        lo=min(lo,z); hi=max(hi,z)
    return hi-lo

def discrepancy_bruteforce(s):
    n=len(s); ss=s+s; best=0
    for i in range(n):
        z=0
        for j in range(1,n+1):
            z += 1 if ss[i+j-1]=='1' else -1
            best=max(best,abs(z))
    return best

def is_debruijn(s):
    return len(s)==L and len({
        ''.join(s[(i+j)%L] for j in range(N))
        for i in range(L)
    })==L

# Engine A: generate rooted cycles as Eulerian circuits in B(2,4).
def engine_eulerian():
    V=1<<(N-1); mask=V-1
    used=[False]*(1<<N)
    used[0]=True
    bits=['0']
    out=set()
    def rec(v,depth):
        if depth==L:
            if v==0:
                out.add(minrot(''.join(bits)))
            return
        for b in (0,1):
            e=(v<<1)|b
            if not used[e]:
                used[e]=True; bits.append(str(b))
                rec(((v<<1)|b)&mask,depth+1)
                bits.pop(); used[e]=False
    rec(0,1)
    return sorted(out)

# Engine B: grow from the unique factor 00000, forbidding repeated length-5 factors.
def engine_factor_backtrack():
    pref='0'*N
    used={pref}
    out=set()
    def rec(s):
        if len(s)==L+N-1:
            if s[-(N-1):]=='0'*(N-1):
                out.add(minrot(s[:L]))
            return
        for c in "01":
            q=s+c
            f=q[-N:]
            if f not in used:
                used.add(f); rec(q); used.remove(f)
    rec(pref)
    return sorted(out)

A=engine_eulerian()
B=engine_factor_backtrack()
assert A==B
assert len(A)==2048
assert len(A)==2**(2**(N-1)-N)
assert all(is_debruijn(s) for s in A)

for s in A:
    assert s.count('0')==s.count('1')==16
    assert discrepancy_prefix(s)==discrepancy_bruteforce(s)

hist=Counter(discrepancy_prefix(s) for s in A)
assert hist=={5:224,6:688,7:912,8:224}

mins=sorted(s for s in A if discrepancy_prefix(s)==5)
assert len(mins)==224
assert sha256(("\n".join(mins)+"\n").encode()).hexdigest()==json.loads(
    (Path(__file__).resolve().parent/"certificate.json").read_text()
)["minimum_cycles_sha256_newline_sorted"]

M=set(mins)
def orbit(s):
    return {minrot(x) for x in (s,complement(s),s[::-1],complement(s[::-1]))}
seen=set(); od=[]
for s in mins:
    if s in seen: continue
    o=sorted(orbit(s)&M)
    od.append((o[0],len(o)))
    seen.update(o)
assert len(od)==60 and len(seen)==224
assert Counter(z for _,z in od)=={4:52,2:8}

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text())
assert cert["discrepancy_histogram"]=={"5":224,"6":688,"7":912,"8":224}
assert cert["minimum_fraction"]=="7/64"
assert [(x["representative"],x["orbit_size"]) for x in cert["minimum_orbit_representatives"]]==od
assert cert["lexicographically_least_minimum_cycle"]==mins[0]
mx=sorted(s for s in A if discrepancy_prefix(s)==8)
assert cert["lexicographically_least_maximum_cycle"]==mx[0]

print(
    "VERIFY_OK order=5 cycles=2048 histogram=5:224,6:688,7:912,8:224 "
    "minimum=5 minimizers=224 fraction=7/64 symmetry_orbits=60 "
    "orbit_sizes=2:8,4:52 engines=2 discrepancy_checks=2"
)
