#!/usr/bin/env python3
from itertools import product

def divisors(a,b,c):
    return sorted(3**i * 5**j * 7**k
                  for i in range(a+1)
                  for j in range(b+1)
                  for k in range(c+1))

def stewart(ds):
    if len(ds) < 3 or ds[1:3] != [3,5]:
        return False
    s = 0
    partial = []
    for d in ds:
        s += d
        partial.append(s)
    for i in range(2, len(ds)-1):
        nxt = ds[i+1]
        si = partial[i]
        c1 = nxt <= si-2 and nxt != si-4
        c2 = nxt == si-4 and i+2 < len(ds) and ds[i+2] == si-2
        if not (c1 or c2):
            return False
    return True

def subset_missing(ds):
    bits = 1
    for d in ds:
        bits |= bits << d
    total = sum(ds)
    return [m for m in range(1,total+1) if ((bits >> m) & 1) == 0]

def predicted(a,b,c):
    return a >= 2 and a+b+c >= 5

bases = [(3,1,1),(2,2,1),(2,1,2)]
for t in bases:
    ds = divisors(*t)
    assert stewart(ds)
    total = sum(ds)
    assert subset_missing(ds) == [2,total-2]

assert not stewart(divisors(2,1,1))
for b in range(1,7):
    for c in range(1,7):
        assert not stewart(divisors(1,b,c))

count = 0
for a,b,c in product(range(1,7), repeat=3):
    assert stewart(divisors(a,b,c)) == predicted(a,b,c)
    count += 1

print(f"VERIFY_OK base_cases={len(bases)} grid={count}")
