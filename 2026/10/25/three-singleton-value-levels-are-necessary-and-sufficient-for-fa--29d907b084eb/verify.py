#!/usr/bin/env python3
"""Self-contained exact check for a three-level fair-division counterexample."""
from itertools import product

VALUES = ((4, 3, 3, 1), (4, 3, 3, 3), (4, 4, 4, 3))
ITEMS = 'abcd'
ALL = tuple(product(range(3), repeat=4))


def bundles(a):
    return tuple(tuple(g for g in range(4) if a[g] == i) for i in range(3))


def utilities(a):
    b = bundles(a)
    return tuple(sum(VALUES[i][g] for g in b[i]) for i in range(3))


def is_efx(a):
    b = bundles(a)
    for i in range(3):
        own = sum(VALUES[i][g] for g in b[i])
        for j in range(3):
            if i == j:
                continue
            for g in b[j]:
                if own < sum(VALUES[i][h] for h in b[j] if h != g):
                    return False
    return True


U = {a: utilities(a) for a in ALL}


def is_po(a):
    ua = U[a]
    return all(not (all(U[c][i] >= ua[i] for i in range(3))
                    and any(U[c][i] > ua[i] for i in range(3))) for c in ALL)


def fmt(a):
    b = bundles(a)
    return '(' + ','.join(''.join(ITEMS[g] for g in x) or '-' for x in b) + ')'


EFX = tuple(a for a in ALL if is_efx(a))
GOOD = tuple(a for a in EFX if is_po(a))
EXPECTED_GOOD = (
    (0, 1, 2, 1), (0, 2, 1, 1), (0, 2, 2, 1),
    (1, 0, 2, 2), (1, 2, 0, 2)
)
assert len(ALL) == 81
assert len(EFX) == 14, len(EFX)
assert len(GOOD) == 5, GOOD
assert GOOD == EXPECTED_GOOD
assert set(v for row in VALUES for v in row) == {1, 3, 4}
assert tuple(len(set(row)) for row in VALUES) == (3, 2, 2)

print('Allocation count: 81; EFX count: 14; EFX and PO count: 5')
for a in EFX:
    if is_po(a):
        print('EFX+PO ', fmt(a), U[a])
    else:
        witness = next(c for c in ALL if all(U[c][i] >= U[a][i] for i in range(3))
                       and any(U[c][i] > U[a][i] for i in range(3)))
        print('EFX only', fmt(a), U[a], 'dominated by', fmt(witness), U[witness])

# For any lottery on GOOD let x=p_0+p_1, y=p_2, z=p_3+p_4.
# The following are the exact no-envy surpluses per extreme allocation.

def envy(a, i, j):
    b = bundles(a)
    return sum(VALUES[i][g] for g in b[i]) - sum(VALUES[i][g] for g in b[j])

T = {pair: tuple(envy(a, *pair) for a in GOOD)
     for pair in ((0, 1), (0, 2), (2, 1))}
assert T[(0, 1)] == (0, 0, 3, -1, -1)
assert T[(0, 2)] == (1, 1, -2, -1, -1)
assert T[(2, 1)] == (-3, -3, 5, 3, 3)
print('Surpluses for comparisons (1,2),(1,3),(3,2):')
for pair, v in T.items():
    print((pair[0] + 1, pair[1] + 1), v)
assert tuple(3*T[(0, 2)][h] + T[(2, 1)][h] for h in range(5)) == (0, 0, -1, 0, 0)
print('Exact certificate: 3*d_13 + d_32 = -y <= 0; both required >=0 => y=0.')
print('Then d_12=-z forces z=0; d_32=-3x forces x=0; contradicts x+y+z=1.')
print('PASS')
