#!/usr/bin/env python3
"""Independent finite checks of exact finite-depth valuation-kernel rank claims.
This is corroboration, not a proof of the infinite result."""

def rank_mod(rows, modulus=1000003):
    pivots = {}
    for row in rows:
        a = [x % modulus for x in row]
        while True:
            j = next((k for k, x in enumerate(a) if x), None)
            if j is None:
                break
            if j not in pivots:
                inverse = pow(a[j], -1, modulus)
                pivots[j] = [(x * inverse) % modulus for x in a]
                break
            factor = a[j]
            pivot = pivots[j]
            for k in range(j, len(a)):
                a[k] = (a[k] - factor * pivot[k]) % modulus
    return len(pivots)

def valuations(poly, p, limit):
    ans = []
    for n in range(limit):
        x = poly(n)
        assert x != 0
        v = 0
        while x % p == 0:
            x //= p
            v += 1
        ans.append(v)
    return ans

def roots(poly, p, depth):
    lift = [0]
    for e in range(1,depth+1):
        power = p**(e-1)
        lift = [r + j * power for r in lift for j in range(p) if poly(r + j * power) % (power*p) == 0]
    return lift

def check(poly, p, max_depth, N):
    # Build one entire p-kernel row at each residue; include every prior depth.
    arr = valuations(poly, p, p**max_depth * N)
    rows = [[arr[n] for n in range(N)]]
    assert len(roots(poly,p,1)) >= 2
    d = len(roots(poly,p,1))
    for e in range(1,max_depth+1):
        power = p**e
        for r in range(power):
            rows.append([arr[n*power+r] for n in range(N)])
        rank = rank_mod(rows)
        expected = d+1 if e==1 else d*e+2
        assert rank == expected,(p,e,rank,expected)
        assert len(roots(poly,p,e)) == d
        print(f"LEVEL_OK p={p} depth={e} rank_mod_1000003={rank} predicted={expected} rows={len(rows)}")

if __name__ == '__main__':
    check(lambda n: n*n+1, 5, 4, 200)
    check(lambda n: n*n+1, 13, 2, 200)
    check(lambda n: n*n*n-2, 31, 2, 200)
    print('VERIFY_OK all tested finite-depth sample ranks agree')
