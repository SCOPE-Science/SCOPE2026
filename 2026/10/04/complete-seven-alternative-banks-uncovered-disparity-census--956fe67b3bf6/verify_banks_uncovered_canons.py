#!/usr/bin/env python3
from itertools import permutations

CANONS = (4642, 4705, 9387, 11371)
EXPECTED = {
    4642: ((0,1,4,5,6),(0,1,3,4,5,6), (2,2,2,3,3,4,5)),
    4705: ((0,4,5,6),(0,3,4,5,6), (2,2,2,3,3,4,5)),
    9387: ((0,1,2,3,5,6),(0,1,2,3,4,5,6), (2,2,2,3,4,4,4)),
    11371: ((0,5,6),(0,4,5,6), (2,2,2,3,4,4,4)),
}

def outsets(bits,n=7):
    out=[set() for _ in range(n)]
    k=0
    for i in range(n):
        for j in range(i+1,n):
            if (bits>>k)&1:
                out[i].add(j)
            else:
                out[j].add(i)
            k+=1
    return out

def transitive_order(out,S):
    S=set(S)
    if not S:
        return ()
    for x in sorted(S):
        if all(y in out[x] for y in S if y!=x):
            rest=transitive_order(out,S-{x})
            if rest is not None:
                return (x,)+rest
    return None

def banks(out):
    n=len(out)
    trans={}
    for mask in range(1,1<<n):
        S=[i for i in range(n) if (mask>>i)&1]
        order=transitive_order(out,S)
        if order is not None:
            trans[mask]=order
    B=set()
    for mask,order in trans.items():
        if not any(mask!=m and (mask&m)==mask for m in trans):
            B.add(order[0])
    return B

def uncovered(out):
    n=len(out)
    U=set()
    for x in range(n):
        covered=False
        for y in range(n):
            if y==x:
                continue
            if x in out[y] and out[x] <= out[y]:
                covered=True
                break
        if not covered:
            U.add(x)
    return U

for bits in CANONS:
    out=outsets(bits)
    B=tuple(sorted(banks(out)))
    U=tuple(sorted(uncovered(out)))
    deg=tuple(sorted(len(s) for s in out))
    assert (B,U,deg)==EXPECTED[bits], (bits,B,U,deg)

print("VERIFY_OK")
for bits in CANONS:
    B,U,deg=EXPECTED[bits]
    print(bits, "BA", B, "UC", U, "scores", deg, "extra", tuple(sorted(set(U)-set(B))))
