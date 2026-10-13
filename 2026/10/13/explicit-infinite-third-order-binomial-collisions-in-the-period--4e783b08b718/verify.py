#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json

def choose_count(w,p):
    dp=[0]*(len(p)+1)
    dp[0]=1
    for ch in w:
        for j in range(len(p)-1,-1,-1):
            if p[j]==ch:
                dp[j+1]+=dp[j]
    return dp[-1]

def sig(w,k):
    return {
        p:choose_count(w,p)
        for L in range(1,k+1)
        for p in map("".join,product("01",repeat=L))
    }

def morph(w,h):
    return "".join(h[ch] for ch in w)

PD={"0":"01","1":"00"}

def sigma(w):
    return morph(w,PD)

def iterate(w,t):
    for _ in range(t):
        w=sigma(w)
    return w

u="0101010001"
v="1000101010"
seed=iterate("0",4)
assert seed=="0100010101000100"
assert seed.find(u)==4
assert seed.find(v)==1
assert u!=v
assert sig(u,3)==sig(v,3)
assert choose_count(u,"0001")==21
assert choose_count(v,"0001")==15

expected={
    "0":6,"1":4,
    "00":15,"01":12,"10":12,"11":6,
    "000":20,"001":19,"010":22,"011":10,
    "100":19,"101":16,"110":10,"111":4
}
assert sig(u,3)==expected

# Direct iterated stress test.  Uniformity gives factor inheritance, while
# direct searches independently confirm it through t=10.
for t in range(11):
    U=iterate(u,t)
    V=iterate(v,t)
    source=iterate("0",t+4)
    assert len(U)==len(V)==10*(2**t)
    assert U!=V
    assert source.find(U)>=0 and source.find(V)>=0
    assert sig(U,3)==sig(V,3)

# Independently validate the morphism-transfer identity used in the proof.
# An occurrence of x in h(w) is grouped by the source blocks from which it
# takes at least one letter.
def compositions(word,r):
    L=len(word)
    if r==1:
        yield (word,)
        return
    for cuts in product(range(1,L),repeat=r-1):
        if tuple(sorted(cuts))!=cuts or len(set(cuts))<r-1:
            continue
        pts=(0,)+cuts+(L,)
        if all(pts[i]<pts[i+1] for i in range(r)):
            yield tuple(word[pts[i]:pts[i+1]] for i in range(r))

def transferred_count(w,h,x):
    total=0
    for r in range(1,len(x)+1):
        for letters in product("01",repeat=r):
            cw=choose_count(w,"".join(letters))
            if not cw:
                continue
            inner=0
            for pieces in compositions(x,r):
                z=1
                for a,piece in zip(letters,pieces):
                    z*=choose_count(h[a],piece)
                inner+=z
            total+=cw*inner
    return total

images=["0","1","00","01","10","11"]
transfer_checks=0
for h0 in images:
    for h1 in images:
        h={"0":h0,"1":h1}
        for n in range(0,6):
            for w in map("".join,product("01",repeat=n)):
                hw=morph(w,h)
                for L in range(1,4):
                    for x in map("".join,product("01",repeat=L)):
                        assert transferred_count(w,h,x)==choose_count(hw,x)
                        transfer_checks+=1

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["seed_factors"]["u"]==u and cert["seed_factors"]["v"]==v
assert cert["source_primary_msc"]=="68R15"

print(
    "VERIFY_OK seed_level4_positions=4,1 seed_3binomial_equal=1 "
    "fourth_order_0001=21_vs_15 iterates_t=0..10 "
    f"transfer_identity_checks={transfer_checks} "
    "conclusion=infinite_strict_b3_vs_factor"
)
