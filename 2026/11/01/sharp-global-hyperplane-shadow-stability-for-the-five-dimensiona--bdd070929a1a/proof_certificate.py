#!/usr/bin/env python3
"""Exact integer certificate for the five-dimensional cross-polytope brightness deficit."""
from itertools import product

D = 10**10
Q = 2921101299          # c0 = Q/D, with c0 < (25-7 sqrt(5))/32 < (Q+1)/D
EQUALITY_MASKS = {65535, 65256}
S = [(1, *x) for x in product((-1, 1), repeat=4)]
SCALE = D // 16


def projected_norm2_times60(g):
    """Euclidean cone projection of g onto t1>=...>=t5>=0; return 60*norm^2."""
    blocks = []
    for i, x in enumerate(g):
        blocks.append([x, 1])
        while len(blocks) > 1 and blocks[-2][0] * blocks[-1][1] < blocks[-1][0] * blocks[-2][1]:
            s, k = blocks.pop()
            blocks[-1][0] += s
            blocks[-1][1] += k
    return sum(60 // k * s*s for s, k in blocks if s > 0)


def certificate():
    g = [-sum(row[j] for row in S) for j in range(5)]
    max_nonspecial = (-1, -1)
    for mask in range(1 << 16):
        # Recompute the integer signed-gradient vector from the current mask.
        g = [-sum(row[k] for row in S) for k in range(5)]
        for i in range(16):
            if mask & (1 << i):
                for k in range(5):
                    g[k] += 2*S[i][k]
        w = [g[0]*SCALE-Q] + [z*SCALE for z in g[1:]]
        val = projected_norm2_times60(w)
        if mask not in EQUALITY_MASKS:
            assert val <= 60*(7*D//10)**2, (mask,val)
            if val > max_nonspecial[0]:
                max_nonspecial = (val, mask)
    assert max_nonspecial[1] == 65520, max_nonspecial
    # Confirm that the exceptional masks correspond exactly to the two
    # analytically treated gradients e1 and (3/8,...,3/8).
    expected = {65535: (16, 0, 0, 0, 0), 65256: (6, 6, 6, 6, 6)}
    for mask, target in expected.items():
        g = [-sum(row[k] for row in S) for k in range(5)]
        for i in range(16):
            if mask & (1 << i):
                for k in range(5):
                    g[k] += 2*S[i][k]
        assert tuple(g) == target, (mask, g)
    # Exact rational certificate that c is in (Q/D,(Q+1)/D).
    # c=(25-7 sqrt(5))/32.  c>z iff sqrt(5)<(25-32z)/7.
    for val, direction in ((Q, 'lower'), (Q+1, 'upper')):
        A = 25*D-32*val
        assert A > 0
        diff = A*A-245*D*D
        if direction == 'lower': assert diff>0
        else: assert diff<0
    print('Verified 65536 sign assignments with exact integers.')
    print('Only the two equality candidates were exempted from the strict 0.70 bound.')
    print('largest nonexceptional 60*projection^2 =', max_nonspecial)
    print('c0 bounds verified by exact squares.')

if __name__=='__main__': certificate()
