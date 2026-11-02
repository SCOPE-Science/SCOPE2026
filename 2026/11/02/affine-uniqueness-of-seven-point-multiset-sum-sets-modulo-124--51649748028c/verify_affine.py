#!/usr/bin/env python3
"""Check the affine orbit and the normalized exhaustive census for Z/124Z."""
from math import gcd
from pathlib import Path

N = 124
canonical = (0, 1, 3, 7, 15, 31, 63)
path = Path(__file__).with_name('normalized_valid.txt')
lines = [line.strip() for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
normalized = {tuple(int(x) for x in line.split()) for line in lines}
assert len(lines) == len(normalized) == 10
assert all(len(a) == 7 and a[:2] == (0, 1) and tuple(sorted(a)) == a and a[-1] < N for a in normalized)

def valid(a):
    target = sum(a) % N
    # Complete enumeration of all 1716 multiplicity vectors summing to seven.
    def dfs(j, remaining, residue, nontrivial):
        if j == 6:
            return (nontrivial or remaining != 1) and (residue + remaining * a[j]) % N == target
        return any(dfs(j+1, remaining-k, (residue+k*a[j]) % N, nontrivial or k != 1)
                   for k in range(remaining+1))
    return not dfs(0, 7, 0, False)

assert all(valid(a) for a in normalized)
units = [u for u in range(N) if gcd(u, N) == 1]
assert len(units) == 60
orbit = {tuple(sorted((u*x+b) % N for x in canonical)) for u in units for b in range(N)}
assert len(orbit) == N * len(units) == 7440
normalized_orbit = {a for a in orbit if a[:2] == (0, 1)}
assert normalized_orbit == normalized
assert sum(tuple(sorted((u*x+b) % N for x in canonical)) == canonical
           for u in units for b in range(N)) == 1
print(f'ORBIT_OK orbit={len(orbit)} normalized={len(normalized_orbit)} canonical_stabilizer=1')
