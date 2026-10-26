#!/usr/bin/env python3
"""Independent integer enumeration and digit-carry verification of a weighted Moser sumset."""

LIMIT = 2 * 4**8

def is_moser(v):
    while v:
        if v % 4 > 1:
            return False
        v //= 4
    return True

M = [i for i in range(LIMIT) if is_moser(i)]
M6 = [i for i in M if 6*i < LIMIT]
counts = [0]*LIMIT
for x in M:
    for y in M6:
        n = x + 6*y
        if n < LIMIT:
            counts[n] += 1
assert max(counts) == 1, "non-unique pair representation"

T = ((0,0,1,1),(2,0,0,1),(2,2,0,0))

def accepted(n):
    c = 0
    while n:
        c = T[c][n%4]
        n //= 4
    return c == 0

for n in range(LIMIT):
    assert bool(counts[n]) == accepted(n), (n, counts[n])

prefix = [0] * (LIMIT + 1)
for i, multiplicity in enumerate(counts):
    prefix[i+1] = prefix[i] + bool(multiplicity)

for L in range(1, 9):
    k = 4**L
    assert prefix[k] == k//2, (L,prefix[k])
    assert prefix[2*k] == (4*k+2)//3, (L,prefix[2*k])
    # Independent complete carry histogram, including both nonaccepting states.
    hist = [0,0,0]
    for n in range(k):
        v=n
        c=0
        for i in range(L):
            c=T[c][v%4]
            v//=4
        hist[c]+=1
    assert hist == [k//2,(k+2)//3,(k-4)//6], (L,hist)

print("VERIFY_OK: unique representations and independent carry decisions for all n<131072; eight exact scale-pair counts and carry histograms")
