"""Exact finite checks for augmentation-fibre n-sum lifting.

Finite tests complement, but do not replace, the general proof.
Use: python3 verify.py
"""
from itertools import permutations, product


def rank_mod(mat, p):
    a = [row[:] for row in mat]
    rows, cols = len(a), len(a[0])
    rank = 0
    for j in range(cols):
        i = next((k for k in range(rank, rows) if a[k][j] % p), None)
        if i is None:
            continue
        a[rank], a[i] = a[i], a[rank]
        inv = pow(a[rank][j] % p, -1, p)
        a[rank] = [(z * inv) % p for z in a[rank]]
        for k in range(rows):
            if k != rank and a[k][j]:
                c = a[k][j]
                a[k] = [(u - c*v) % p for u, v in zip(a[k], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def check_s3_group_ring():
    p = 3
    group = list(permutations(range(3)))
    gi = {g: i for i, g in enumerate(group)}
    mul = [[gi[tuple(x[y[i]] for i in range(3))] for y in group] for x in group]
    els = list(product(range(p), repeat=6))
    unit = []
    for x in els:
        mat = [[0]*6 for _ in range(6)]
        for g, a in enumerate(x):
            if a:
                for h in range(6):
                    mat[mul[g][h]][h] = (mat[mul[g][h]][h] + a) % p
        if rank_mod(mat, p) == 6:
            unit.append(x)
    # Compare the n-fold unit sumset with exactly the field-sum fibre.
    for U in [{1}, {1, 2}]:
        V = [x for x in unit if sum(x) % p in U]
        actual = {tuple((a+b) % p for a, b in zip(x, y)) for x in V for y in V}
        field_sum = {(a+b) % p for a in U for b in U}
        expected = {x for x in els if sum(x) % p in field_sum}
        assert actual == expected
        assert len(actual) == len(expected)
    print('F3[S3]: 729 elements; exact 2-fold sumsets for U={1} and U={1,2} verified; units:', len(unit))


def check_triangular_13():
    p = 13
    U = {pow(x, 2, p) for x in range(1,p)}
    assert len(U) == 6 and (p-1) in U
    assert {(x+y)%p for x in U for y in U} == set(range(p))
    for subset in (U, {1}):
        V = [(a,b,c) for a in subset for b in range(p) for c in range(1,p)]
        actual = {((a+d)%p,(b+e)%p,(c+f)%p)
                  for a,b,c in V for d,e,f in V}
        possible = {(a+d)%p for a in subset for d in subset}
        expected = {(a,b,c) for a in possible for b in range(p) for c in range(p)}
        assert actual == expected
    print('T_2(F13): all 2197 elements covered by two U-normalized units for U=squares; singleton fibre also verified')


def check_binary_sharpness():
    # R=F2 x F2, epsilon is first projection, U={1}.
    V = {(1,1)}
    sums = {((a+c)%2, (b+d)%2) for a,b in V for c,d in V}
    preimage = {(0,0),(0,1)}
    assert sums == {(0,0)} and sums != preimage
    print('F2 x F2: exact counterexample to the q>2 hypothesis')


if __name__ == '__main__':
    check_s3_group_ring()
    check_triangular_13()
    check_binary_sharpness()
    print('VERIFY_OK')
