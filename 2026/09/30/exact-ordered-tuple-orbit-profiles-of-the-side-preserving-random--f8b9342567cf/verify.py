#!/usr/bin/env python3
from itertools import product
from math import comb

def rank_masks(a,b,kind):
    masks=set()
    if kind=="A":
        masks={0, (1<<(a*b))-1}
    elif kind=="L":
        for rs in range(1<<a):
            m=0
            for i in range(a):
                if (rs>>i)&1:
                    for j in range(b):
                        m ^= 1<<(i*b+j)
            masks.add(m)
    elif kind=="R":
        for cs in range(1<<b):
            m=0
            for j in range(b):
                if (cs>>j)&1:
                    for i in range(a):
                        m ^= 1<<(i*b+j)
            masks.add(m)
    elif kind=="LR":
        for rs in range(1<<a):
            for cs in range(1<<b):
                m=0
                for i in range(a):
                    for j in range(b):
                        if ((rs>>i)&1) ^ ((cs>>j)&1):
                            m ^= 1<<(i*b+j)
                masks.add(m)
    return masks

def brute_orbits(a,b,kind):
    N=1<<(a*b)
    masks=rank_masks(a,b,kind)
    seen=set()
    orbits=0
    for x in range(N):
        if x in seen:
            continue
        orbits += 1
        seen.update(x^m for m in masks)
    return orbits

def closed(a,b,kind):
    if a==0 or b==0:
        return 1
    if kind=="A":  return 1<<(a*b-1)
    if kind=="L":  return 1<<(a*(b-1))
    if kind=="R":  return 1<<((a-1)*b)
    if kind=="LR": return 1<<((a-1)*(b-1))
    raise ValueError(kind)

for a in range(1,4):
    for b in range(1,4):
        if a*b <= 8:
            for kind in ("A","L","R","LR"):
                assert brute_orbits(a,b,kind)==closed(a,b,kind), (a,b,kind)

def f(k,kind):
    if k==0:
        return 1
    if kind=="SYM":
        return 1<<k
    ans=2
    for a in range(1,k):
        b=k-a
        ans += comb(k,a)*closed(a,b,kind)
    return ans

expected={
"A":[1,2,4,14,82,722,9154,165314],
"L":[1,2,4,11,46,287,2584,33161],
"R":[1,2,4,11,46,287,2584,33161],
"LR":[1,2,4,8,22,92,574,5168],
"SYM":[1,2,4,8,16,32,64,128],
}
for kind,row in expected.items():
    assert [f(k,kind) for k in range(8)]==row

# Stirling numbers of the second kind and all-tuple orbit counts.
S=[[0]*9 for _ in range(9)]
S[0][0]=1
for n in range(1,9):
    for k in range(1,n+1):
        S[n][k]=S[n-1][k-1]+k*S[n-1][k]

def o(n,kind):
    return sum(S[n][k]*f(k,kind) for k in range(n+1))

expected_all={
"A":[1,2,6,28,196,1954,26700,491796],
"L":[1,2,6,25,142,1084,10995,147270],
"R":[1,2,6,25,142,1084,10995,147270],
"LR":[1,2,6,22,100,574,4230,40464],
"SYM":[1,2,6,22,94,454,2430,14214],
}
for kind,row in expected_all.items():
    assert [o(n,kind) for n in range(8)]==row

assert all(f(k,"L")==f(k,"R") for k in range(50))
print("VERIFY_OK")
