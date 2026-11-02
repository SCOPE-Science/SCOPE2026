"""Exact modular checks for central-shell actuation of binary hypercubes.

Run: python verify.py
The theorem for all dimensions is proved separately; these computations test finite cases.
"""
from math import comb
import numpy as np

PRIMES = (1000003, 1000033)


def leaders(d):
    m = d // 2
    if d % 2:
        return [v for v in range(1 << d) if v.bit_count() == m]
    return [v for v in range(1 << (d-1)) if v.bit_count() in (m-1, m)]


def rank_mod(matrix, p):
    a = np.asarray(matrix, dtype=np.int64).copy() % p
    rows, cols = a.shape
    r = 0
    for c in range(cols):
        if r == rows:
            break
        candidates = np.flatnonzero(a[r:, c])
        if not candidates.size:
            continue
        s = r + int(candidates[0])
        if s != r:
            a[[r, s], :] = a[[s, r], :]
        a[r, c:] = (a[r, c:] * pow(int(a[r, c]), -1, p)) % p
        if r + 1 < rows:
            f = a[r+1:, c].copy()
            a[r+1:, c:] = (a[r+1:, c:] - f[:, None]*a[r:r+1, c:]) % p
        r += 1
    return r


def test_spectral():
    count = 0
    for d in range(1, 11):
        v = leaders(d)
        q = comb(d, d//2)
        assert len(v) == q
        assert len(set(v)) == q
        assert max(v) < (1 << d)
        for w in range(d+1):
            s = [i for i in range(1 << d) if i.bit_count() == w]
            mat = np.array([[1 if ((x & y).bit_count() & 1)==0 else -1 for x in v] for y in s], dtype=np.int64)
            for p in PRIMES:
                assert rank_mod(mat, p) == len(s), (d, w, p)
                count += 1
    return count


def test_kalman():
    count = 0
    for d in range(1, 6):
        n = 1 << d
        v = leaders(d)
        A = np.zeros((n,n),dtype=np.int64)
        for x in range(n):
            for j in range(d):
                A[x,x^(1<<j)] = 1
        B = np.zeros((n,len(v)),dtype=np.int64)
        for i,x in enumerate(v):
            B[x,i]=1
        for p in PRIMES:
            blocks=[]
            current=B
            for j in range(d+1):
                blocks.append(current)
                current = (A @ current) % p
            assert rank_mod(np.concatenate(blocks,axis=1),p)==n, (d,p)
            count+=1
    return count

if __name__=='__main__':
    a=test_spectral()
    b=test_kalman()
    print(f'PASS: {a} spectral restriction ranks, {b} direct modular Kalman ranks; dimensions 1 through 10 (spectral), 1 through 5 (Kalman); two exact prime fields.')
