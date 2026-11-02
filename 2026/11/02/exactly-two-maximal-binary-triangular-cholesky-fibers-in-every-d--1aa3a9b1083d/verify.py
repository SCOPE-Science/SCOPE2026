"""Exact finite-field checks for an extremal binary triangular Gram-fiber theorem.

Run with Python 3 and no third-party packages: python verify.py
A finite check corroborates, but does not replace, the all-dimension proof.
"""
from collections import Counter


def symmetric_positions(n):
    return [(i, j) for i in range(n) for j in range(i, n)]


def row_outer_masks(n, positions):
    masks = []
    for i in range(n):
        row = []
        for x in range(1 << (n-i)):
            mask = 0
            for k, (a,b) in enumerate(positions):
                if a >= i and (x >> (a-i) & 1) and (x >> (b-i) & 1):
                    mask |= 1 << k
            row.append(mask)
        masks.append(row)
    return masks


def direct_counts(n, positions):
    # Every triangular matrix is encoded by its independent upper entries.
    N = len(positions)
    fibers = [0] * (1 << N)
    for u in range(1 << N):
        rows = [[0] * n for _ in range(n)]
        for k, (i,j) in enumerate(positions):
            rows[i][j] = u >> k & 1
        target = 0
        for k, (i,j) in enumerate(positions):
            bit = 0
            for t in range(i + 1):
                bit ^= rows[t][i] & rows[t][j]
            target |= bit << k
        fibers[target] += 1
    return fibers


def hadamard_transform(vector):
    out = vector[:]
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2*step):
            for j in range(base, base+step):
                a, b = out[j], out[j+step]
                out[j], out[j+step] = a+b, a-b
        step *= 2
    return out


def gf2_rank(vectors):
    pivots = {}
    for v in vectors:
        while v:
            p = v.bit_length() - 1
            if p not in pivots:
                pivots[p] = v
                break
            v ^= pivots[p]
    return len(pivots)


def main():
    expected_zero = [1, 2, 6, 28, 192]
    for n in range(1, 6):
        pos = symmetric_positions(n)
        N = len(pos)
        fiber = direct_counts(n, pos)
        assert sum(fiber) == 1 << N
        nn = 1 << (N-1)
        assert fiber[0] == expected_zero[n-1]
        maxima = [a for a,c in enumerate(fiber) if c == max(fiber)]
        assert maxima == [0, nn], (n, maxima)
        assert all(fiber[a] == fiber[a ^ nn] for a in range(1 << N))
        fourier = hadamard_transform(fiber)
        assert min(fourier) >= 0
        positive = [i for i, c in enumerate(fourier) if c > 0]
        assert all((i & nn) == 0 for i in positive)
        assert gf2_rank(positive) == N-1
        # Independently compute Fourier transform as product of quadratic
        # Gauss sums from the nested supports of the triangular rows.
        rows = row_outer_masks(n, pos)
        for mask in range(1 << N):
            product = 1
            for row in rows:
                factor = sum(1 if ((mask & t).bit_count() & 1)==0 else -1 for t in row)
                product *= factor
                if not product:
                    break
            assert fourier[mask] == product, (n, mask, product, fourier[mask])
        print('n=%d N=%d zero=%d maximizers=%s fourier_support=%d span_rank=%d' %
              (n, N, fiber[0], maxima, len(positive), N-1))
    # Check the flat Walsh-magnitude lemma for every Boolean quadratic form
    # through four variables, including all linear terms and perturbations.
    for m in range(1, 5):
        pos = symmetric_positions(m)
        vectors = row_outer_masks(m, pos)[0]
        N = len(pos)
        checked = 0
        for q in range(1 << N):
            values = [1 if (q & v).bit_count() % 2 == 0 else -1 for v in vectors]
            spectrum = hadamard_transform(values)
            if spectrum[0] > 0:
                assert set(abs(z) for z in spectrum) <= {0, spectrum[0]}
            checked += 1
        print('quadratic_gauss_m=%d forms=%d flat_spectra_checked' % (m, checked))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
