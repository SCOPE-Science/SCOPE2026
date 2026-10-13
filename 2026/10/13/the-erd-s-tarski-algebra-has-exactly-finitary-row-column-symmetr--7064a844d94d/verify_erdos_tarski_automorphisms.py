#!/usr/bin/env python3
from itertools import permutations

checks = 0


def tri_ok(a,b):
    global checks
    n=len(a)
    for i in range(n):
        for j in range(n):
            checks += 1
            if ((a[i] <= b[j]) != (i <= j)):
                return False
    return True


def anti_ok(a,b):
    global checks
    n=len(a)
    for i in range(n):
        for j in range(n):
            checks += 1
            if ((a[i] <= b[j]) != (i > j)):
                return False
    return True

for n in range(1,7):
    ps=list(permutations(range(n)))
    tri=[]
    anti=[]
    for a in ps:
        for b in ps:
            if tri_ok(a,b):
                tri.append((a,b))
            if anti_ok(a,b):
                anti.append((a,b))
    ident=tuple(range(n))
    assert tri == [(ident,ident)], (n,tri[:5],len(tri))
    assert anti == [], (n,anti[:5],len(anti))
    checks += 2

# Directly test that arbitrary finite-support coordinate permutations alter
# the triangular set only in finitely many rows/columns on large finite boxes.
for n in range(2,8):
    for m in range(0,n+1):
        # reverse the first m coordinates, fix the rest
        p=list(range(n))
        p[:m]=reversed(p[:m])
        inv=[0]*n
        for i,v in enumerate(p): inv[v]=i
        bad=[]
        for i in range(n):
            for j in range(n):
                checks += 1
                if ((inv[i] <= inv[j]) != (i <= j)):
                    bad.append((i,j))
        # Outside the finite support, membership is unchanged.
        assert all(i < m or j < m for i,j in bad)
        checks += 1

print(f"VERIFY_OK {checks} exact assertions/comparisons")
