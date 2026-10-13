"""Reproduce finite exact tests of the sharp paired-block sampling bound.

Requires only Python 3 standard library. The universal inequality is proved
in the accompanying mathematical argument, not inferred from these tests.
"""
from fractions import Fraction as Q
from math import sqrt
from random import Random


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Q(0))


def pair_data(A, r):
    n = len(A[0])
    g = [sum((A[i][j] * r[i] for i in range(len(A))), Q(0)) for j in range(n)]
    blocks = []
    for j in range((n + 1) // 2):
        pair = sorted(set((j, n - 1 - j)))
        if len(pair) == 1:
            u = pair[0]
            h = sum((A[i][u] ** 2 for i in range(len(A))), Q(0))
            w = g[u] ** 2
            blocks.append((w, w / h, float(h), float(h), pair))
            continue
        u, v = pair
        h11 = sum((A[i][u] ** 2 for i in range(len(A))), Q(0))
        h22 = sum((A[i][v] ** 2 for i in range(len(A))), Q(0))
        h12 = sum((A[i][u] * A[i][v] for i in range(len(A))), Q(0))
        det = h11 * h22 - h12 * h12
        assert det > 0
        w = g[u] ** 2 + g[v] ** 2
        d = (h22 * g[u] ** 2 - 2 * h12 * g[u] * g[v] + h11 * g[v] ** 2) / det
        center = float(h11 + h22) / 2
        rad = sqrt(float((h11 - h22) ** 2 + 4 * h12 * h12)) / 2
        blocks.append((w, d, center - rad, center + rad, pair))
    return blocks


def check(A, r):
    blocks = pair_data(A, r)
    S = sum((row[0] for row in blocks), Q(0))
    D = sum((row[1] for row in blocks), Q(0))
    if not S:
        return
    raw = sum((w * d for w, d, _, _, _ in blocks), Q(0)) / S
    uniform = D / len(blocks)
    assert uniform > 0 and raw > 0
    # Every exact block projection agrees with its explicit residual update.
    n = len(A[0])
    for w, d, _, _, pair in blocks:
        g = [sum((A[i][j] * r[i] for i in range(len(A))), Q(0)) for j in pair]
        h = [[sum((A[i][u] * A[i][v] for i in range(len(A))), Q(0)) for v in pair] for u in pair]
        if len(pair) == 1:
            alpha = [g[0] / h[0][0]]
        else:
            det = h[0][0] * h[1][1] - h[0][1] ** 2
            alpha = [(g[0] * h[1][1] - g[1] * h[0][1]) / det,
                     (g[1] * h[0][0] - g[0] * h[1][0]) / det]
        projected = [r[i] - sum((A[i][j] * alpha[k] for k, j in enumerate(pair)), Q(0)) for i in range(len(A))]
        assert dot(r, r) - dot(projected, projected) == d
    lo = min(block[2] for block in blocks)
    hi = max(block[3] for block in blocks)
    assert lo > 0
    kappa = hi / lo
    threshold = 4 * sqrt(kappa) / (1 + sqrt(kappa)) ** 2
    assert float(raw / uniform) >= threshold - 1e-11
    # Progress-normalized sampling is no worse than uniform (an established rule).
    norm = sum((d*d for _,d,_,_,_ in blocks), Q(0)) / D
    assert norm >= uniform


def main():
    cases = 0
    A = [[Q(4),Q(0),Q(0),Q(0)],
         [Q(0),Q(1),Q(0),Q(0)],
         [Q(0),Q(0),Q(1),Q(0)],
         [Q(0),Q(0),Q(0),Q(4)]]
    r = [Q(-1),Q(-2),Q(0),Q(0)]
    check(A,r); cases+=1
    blocks = pair_data(A,r)
    raw=sum((w*d for w,d,*_ in blocks),Q(0))/sum((w for w,*_ in blocks),Q(0))
    uni=sum((d for _,d,*_ in blocks),Q(0))/len(blocks)
    assert (raw,uni,raw/uni)==(Q(8,5),Q(5,2),Q(16,25))
    for t in range(2,70):
        # Pair curvatures k*k and 1 with progress energies 1 and k.
        k = t*t
        a = [[Q(k if i==j and i in (0,3) else (1 if i==j else 0))
               for j in range(4)] for i in range(4)]
        r = [Q(-1),Q(-t),Q(0),Q(0)]
        bb = pair_data(a,r)
        rr=sum((w*d for w,d,*_ in bb),Q(0))/sum((w for w,*_ in bb),Q(0))
        uu=sum((d for _,d,*_ in bb),Q(0))/len(bb)
        assert rr / uu == Q(4*k,(k+1)*(k+1))
        check(a,r);cases+=1
    rng = Random(20240523)
    for n in range(2,10):
        for _ in range(150):
            # Full-rank upper triangular, including nonorthogonal mirror pairs.
            A = [[Q(rng.randint(-2,2)) if i<j else (Q(rng.randint(1,5)) if i==j else Q(0))
                  for j in range(n)] for i in range(n)]
            r = [Q(rng.randint(-4,4)) for _ in range(n)]
            check(A,r)
            cases+=1
    print('PASS: %d exact-projection, sampling, and sharp-frontier cases' % cases)

if __name__ == '__main__':
    main()
