#!/usr/bin/env python3
"""Definition-based exhaustive checks of constrained Roman labelings."""
from itertools import product

def run():
    profiles = 0
    labelings = 0
    for n in range(3, 7):
        neigh = [set(range(n, 2*n)) - {n+i} for i in range(n)]
        neigh += [set(range(n)) - {j} for j in range(n)]
        optimum = 2*n if n == 3 else n+3
        expected = 25 if n == 3 else 2*n*(n-1)
        seen = 0
        min_weight = 10**5
        for f in product(range(3), repeat=2*n):
            labelings += 1
            z = {v for v in range(2*n) if f[v] == 0}
            if any(u in z for v in z for u in neigh[v]):
                continue
            if any(not any(f[u] == 2 for u in neigh[v]) for v in z):
                continue
            if any(not any(f[u] > 0 for u in neigh[v]) for v in range(2*n) if f[v] > 0):
                continue
            weight = sum(f)
            assert weight >= optimum, (n, f, weight)
            if weight < min_weight:
                min_weight = weight
                seen = 0
            if weight == min_weight:
                seen += 1
                if n >= 4:
                    az = [i for i in range(n) if f[i] == 0]
                    bz = [i for i in range(n) if f[n+i] == 0]
                    if az:
                        assert len(az) == n-2 and not bz
                        assert all(f[n+i] >= 1 for i in range(n))
                        defenders = [i for i in range(n) if f[n+i] == 2]
                        assert len(defenders) == 1 and defenders[0] not in az
                    else:
                        assert len(bz) == n-2
                        defenders = [i for i in range(n) if f[i] == 2]
                        assert len(defenders) == 1 and defenders[0] not in bz
        assert min_weight == optimum and seen == expected, (n,min_weight,seen,expected)
        profiles += 1
    print(f'VERIFICATION_OK profiles={profiles} labelings={labelings} optimum_counts=25,24,40,60')

if __name__ == '__main__':
    run()
