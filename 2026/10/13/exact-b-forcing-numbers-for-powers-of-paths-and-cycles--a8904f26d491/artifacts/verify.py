#!/usr/bin/env python3
from itertools import combinations


def path_power(n, k):
    return [{j for j in range(n) if j != i and abs(i-j) <= k} for i in range(n)]


def cycle_power(n, k):
    return [{j for j in range(n) if j != i and min((i-j) % n, (j-i) % n) <= k} for i in range(n)]


def closes(adj, initial, b):
    black=set(initial)
    n=len(adj)
    changed=True
    while changed:
        changed=False
        add=set()
        for u in tuple(black):
            white=adj[u]-black
            if white and len(white) <= b:
                add.update(white)
        if add-black:
            black.update(add)
            changed=True
    return len(black)==n


def exact_number(adj, b):
    n=len(adj)
    global subset_prefixes_checked
    for s in range(1,n+1):
        for comb in combinations(range(n),s):
            subset_prefixes_checked += 1
            if closes(adj,comb,b):
                return s
    raise AssertionError('no forcing set')


def path_formula(n,k,b):
    d=min(k,n-1)
    return max(1,d-b+1)


def cycle_formula(n,k,b):
    d=min(2*k,n-1)
    return max(1,d-b+1)

subset_prefixes_checked=0
profiles=0
for n in range(2,10):
    for k in range(1,8):
        adj=path_power(n,k)
        d=min(len(x) for x in adj)
        for b in range(1,d+3):
            got=exact_number(adj,b)
            want=path_formula(n,k,b)
            assert got==want, ('path',n,k,b,got,want)
            profiles += 1

for n in range(3,10):
    for k in range(1,8):
        adj=cycle_power(n,k)
        d=min(len(x) for x in adj)
        for b in range(1,d+3):
            got=exact_number(adj,b)
            want=cycle_formula(n,k,b)
            assert got==want, ('cycle',n,k,b,got,want)
            profiles += 1

print(f'ALL CHECKS PASSED; exhaustive_profiles={profiles}; subset_prefixes_checked={subset_prefixes_checked}; path_orders=2..9; cycle_orders=3..9; powers=1..7')
