#!/usr/bin/env python3
"""Independently check the stated recurrent-state census for small cycle complements."""
from math import comb

def transition(x, n):
    # Deliberately use graph adjacency, not the global-weight derivation.
    output = 0
    for i in range(n):
        neighbors = [j for j in range(n) if j != i and j != (i-1)%n and j != (i+1)%n]
        ones = sum((x >> j) & 1 for j in neighbors)
        if 2*ones > len(neighbors) or (2*ones == len(neighbors) and (x >> i) & 1):
            output |= (1 << i)
    return output

def local_pattern(x, n):
    b = [(x >> i) & 1 for i in range(n)]
    alternating = all(b[i] != b[(i+1)%n] for i in range(n))
    no_singletons = all(not(b[i-1] == b[(i+1)%n] != b[i]) for i in range(n))
    one_run = sum(b[i] != b[(i+1)%n] for i in range(n)) == 2
    return alternating, no_singletons, one_run

def formula(n):
    if n % 2: return 2*n + 2
    m=n//2
    H=sum((n*comb(m-r-1,r-1)**2)//r for r in range(1,m//2+1))
    return H+2*n+4

def predicted(x,n):
    s=x.bit_count()
    if s==0 or s==n:return True
    alt,none,run=local_pattern(x,n)
    if n%2:
        m=n//2
        if s==m:
            return all(not(((x>>i)&1) and ((x>>((i+1)%n))&1)) for i in range(n))
        if s==m+1:
            return all(not((not ((x>>i)&1)) and (not ((x>>((i+1)%n))&1))) for i in range(n))
        return False
    m=n//2
    return ((s==m and (alt or none)) or (s in (m-1,m+1) and run))

for n in range(5,19):
    f = [transition(x,n) for x in range(1<<n)]
    recurrent = {x for x in range(1<<n) if f[f[x]]==x}
    expected = {x for x in range(1<<n) if predicted(x,n)}
    assert recurrent==expected, (n, sorted(recurrent^expected)[:4])
    fixed = sum(f[x]==x for x in recurrent)
    expected_fixed = 2*n+2 if n%2 else 4
    assert fixed==expected_fixed, (n,fixed,expected_fixed)
    assert len(recurrent)==formula(n), (n,len(recurrent),formula(n))
    print(f'n={n:2d} fixed={fixed:5d} recurrent={len(recurrent):7d} 2cycles={(len(recurrent)-fixed)//2:7d} PASS')
print('VERIFY_OK')
