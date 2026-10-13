"""Finite-field checks for minimal coordinate dependencies of cubic first-jet codes.
Pure Python 3; no third-party packages required.
"""
from itertools import combinations
from math import comb

POLYS = {2: 0b111, 3: 0b1011, 4: 0b10011}


def mul(a, b, m):
    poly = POLYS[m]
    res = 0
    for _ in range(m):
        if b & 1: res ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m): a ^= poly
    return res


def power(a, n, m):
    ans = 1
    while n:
        if n & 1: ans = mul(ans, a, m)
        a = mul(a, a, m)
        n >>= 1
    return ans


def rank(cols, m):
    if not cols: return 0
    mat = [[cols[j][i] for j in range(len(cols))] for i in range(4)]
    row = 0
    for col in range(len(cols)):
        pivot = next((r for r in range(row, 4) if mat[r][col]), None)
        if pivot is None: continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        inv = power(mat[row][col], (1 << m)-2, m)
        mat[row] = [mul(inv, v, m) for v in mat[row]]
        for r in range(4):
            if r != row and mat[r][col]:
                f = mat[r][col]
                mat[r] = [v ^ mul(f, w, m) for v, w in zip(mat[r], mat[row])]
        row += 1
        if row == 4: break
    return row


def run(m):
    q = 1 << m
    E = [(1, a, mul(a,a,m), mul(mul(a,a,m),a,m)) for a in range(q)]
    T = [(0, 1, 0, mul(a,a,m)) for a in range(q)]
    cols = E+T
    assert rank(cols, m) == 4
    observed = {2: set(), 3: set(), 4: set()}
    for size in (2,3,4):
        for inds in combinations(range(2*q), size):
            if rank([cols[j] for j in inds],m) < size:
                if all(rank([cols[j] for j in inds if j != i],m) == size-1 for i in inds):
                    observed[size].add(inds)
    expected3 = {tuple(q+a for a in abc) for abc in combinations(range(q),3)}
    expected4 = set()
    inv_squares = {mul(a,a,m):a for a in range(q)}
    for a,b,c in combinations(range(q),3):
        pairwise = mul(a,b,m) ^ mul(a,c,m) ^ mul(b,c,m)
        d = inv_squares[pairwise]
        assert d not in (a,b,c)
        expected4.add((a,b,c,q+d))
    assert not observed[2]
    assert observed[3] == expected3, (q,len(observed[3]),len(expected3))
    assert observed[4] == expected4, (q,len(observed[4]),len(expected4))
    for d in range(q):
        triples = {tuple(sorted((a,b,c))) for a,b,c,D in expected4 if D == q+d}
        assert len(triples) == (q-1)*(q-2)//6
        for a,b in combinations([x for x in range(q) if x != d],2):
            ua = power(a ^ d,q-2,m)
            ub = power(b ^ d,q-2,m)
            uc = ua ^ ub
            c = d ^ power(uc,q-2,m)
            assert c not in (a,b,d) and tuple(sorted((a,b,c))) in triples
    # Every evaluation point has exactly binom(q-1,2) three-helper circuits.
    for a in range(q):
        assert sum(a in S for S in expected4) == comb(q-1,2)
    # Sharp disjoint construction uses powers of a primitive generator.
    g = next(g for g in range(2,q) if len({power(g,i,m) for i in range(q-1)}) == q-1)
    for a in range(q):
        used = set()
        for i in range((q-2)//2):
            x, y = power(g,2*i,m), power(g,2*i+1,m)
            b, c = a^x, a^y
            d = a^inv_squares[mul(x,y,m)]
            helpers = {b,c,q+d}
            assert a not in (b,c) and not used.intersection(helpers)
            assert tuple(sorted((a,b,c)))+(q+d,) in expected4
            used.update(helpers)
        assert len(used) == 3*((q-2)//2)
    print(f'GF({q}) VERIFY_OK: rank=4, circuits_3={len(observed[3])}, circuits_4={len(observed[4])}, derivative_STS_blocks={(q-1)*(q-2)//6}, value_disjoint={(q-2)//2}')

if __name__ == '__main__':
    for m in (2,3,4): run(m)
    print('VERIFY_OK')
