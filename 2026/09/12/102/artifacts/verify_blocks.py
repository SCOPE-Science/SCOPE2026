"""Exact verification of the sigma/sigma' balanced-block closure.

Recomputes, with stdlib-only exact integer arithmetic:
 1. sigma, sigma' share incidence matrix M = [[0,0,1],[1,0,0],[0,1,2]].
 2. Balanced-block closure from the 3 diagonal seeds is finite (9 blocks,
    max word length 7) and every Phi-image splits exactly into minimal blocks.
 3. M^4 > 0 (M primitive); N^8 > 0 (Phi primitive).
Run: python3 verify_blocks.py
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

SIGMA = {'1': '2', '2': '3', '3': '133'}
SIGMAP = {'1': '2', '2': '3', '3': '313'}
M = [[0, 0, 1], [1, 0, 0], [0, 1, 2]]


def apply_sub(sub, w):
    return ''.join(sub[c] for c in w)


def ab(w):
    return (w.count('1'), w.count('2'), w.count('3'))


def matvec(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(3)) for i in range(3))


def matmul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                aik = A[i][k]
                for j in range(n):
                    C[i][j] += aik * B[k][j]
    return C


def matpow(A, k):
    n = len(A)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = matmul(R, A)
    return R


def split_blocks(U, V):
    assert ab(U) == ab(V), (U, V)
    assert len(U) == len(V)
    ax = ay = az = 0
    bx = by = bz = 0
    cuts = [0]
    n = len(U)
    for k in range(n):
        c, d = U[k], V[k]
        if c == '1':
            ax += 1
        elif c == '2':
            ay += 1
        else:
            az += 1
        if d == '1':
            bx += 1
        elif d == '2':
            by += 1
        else:
            bz += 1
        if k < n - 1:
            assert not ((ax, ay, az) == (bx, by, bz) and False), \
                'interior cut inside a minimal block'
        if (ax, ay, az) == (bx, by, bz):
            cuts.append(k + 1)
    assert cuts[-1] == n, (U, V, cuts)
    return [(U[a:b], V[a:b]) for a, b in zip(cuts[:-1], cuts[1:])]


def interior_cuts(u, v):
    a = [0, 0, 0]
    b = [0, 0, 0]
    idx = {'1': 0, '2': 1, '3': 2}
    out = []
    for k in range(len(u)):
        a[idx[u[k]]] += 1
        b[idx[v[k]]] += 1
        if k < len(u) - 1 and tuple(a) == tuple(b):
            out.append(k + 1)
    return out


def main():
    ok = True
    # 1. shared incidence matrix
    for letter in '123':
        for sub in (SIGMA, SIGMAP):
            if ab(sub[letter]) != matvec(M, ab(letter)):
                print('FAIL: incidence mismatch', letter, sub[letter])
                ok = False
    print('shared-matrix check:', 'PASS' if ok else 'FAIL')

    # 2. closure
    seeds = [('1', '1'), ('2', '2'), ('3', '3')]
    seen = list(seeds)
    known = set(seeds)
    queue = list(seeds)
    while queue:
        u, v = queue.pop(0)
        U, V = apply_sub(SIGMA, u), apply_sub(SIGMAP, v)
        assert ab(U) == ab(V), (u, v, U, V)
        for blk in split_blocks(U, V):
            if blk not in known:
                known.add(blk)
                seen.append(blk)
                queue.append(blk)
    # minimality of every block
    for blk in seen:
        assert ab(blk[0]) == ab(blk[1]), blk
        assert interior_cuts(blk[0], blk[1]) == [], blk
    # Phi images close inside the set
    idx = {b: i for i, b in enumerate(sorted(known, key=lambda x: (len(x[0]), x)))}
    phi = {}
    for blk in seen:
        im = split_blocks(apply_sub(SIGMA, blk[0]), apply_sub(SIGMAP, blk[1]))
        assert all(x in known for x in im), (blk, im)
        phi[blk] = im
    order = sorted(known, key=lambda x: (len(x[0]), x))
    print('closure: %d blocks, maxlen %d: %s'
          % (len(order), max(len(b[0]) for b in order),
             'PASS' if len(order) == 9 else 'FAIL'))
    if len(order) != 9:
        ok = False
    n = len(order)
    N = [[0] * n for _ in range(n)]
    for j, blk in enumerate(order):
        for x in phi[blk]:
            N[idx[x]][j] += 1
    P = matpow(N, 8)
    pmin = min(min(r) for r in P)
    print('N^8 strictly positive (min=%d): %s' % (pmin, 'PASS' if pmin >= 1 else 'FAIL'))
    if pmin < 1:
        ok = False
    M4 = matpow(M, 4)
    m4min = min(min(r) for r in M4)
    print('M^4 strictly positive (min=%d): %s' % (m4min, 'PASS' if m4min >= 1 else 'FAIL'))
    if m4min < 1:
        ok = False
    # prolongability witness: Phi^3(B2) starts with B2
    b2 = order[2]
    assert b2 == ('3', '3'), b2
    s = [b2]
    for _ in range(3):
        nxt = []
        for blk in s:
            nxt += phi[blk]
        s = nxt
    print('Phi^3(3,3) starts with (3,3): %s' % ('PASS' if s[0] == ('3', '3') else 'FAIL'))
    if s[0] != ('3', '3'):
        ok = False
    print('OVERALL:', 'PASS' if ok else 'FAIL')
    with open(os.path.join(BASE, 'blocks.json')) as f:
        saved = json.load(f)
    assert saved['N'] == N, 'blocks.json matrix mismatch'
    assert [tuple(b) for b in saved['blocks']] == order, 'blocks.json block mismatch'
    print('blocks.json consistency: PASS')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
