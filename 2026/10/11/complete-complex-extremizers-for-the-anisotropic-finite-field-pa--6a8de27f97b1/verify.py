"""Finite checks for anisotropic paraboloid extremizer rigidity (standard library only).

The proof is independent of finite checks. Run: python verify.py
"""
from collections import defaultdict
from cmath import exp
from math import pi


def rank_mod_p(rows, p, width):
    pivots = {}
    for row in rows:
        a = [int(v) % p for v in row]
        while True:
            k = next((j for j, v in enumerate(a) if v), None)
            if k is None:
                break
            if k in pivots:
                b = pivots[k]
                fac = a[k]
                a = [(u - fac * v) % p for u, v in zip(a, b)]
            else:
                inv = pow(a[k], -1, p)
                pivots[k] = [(inv * v) % p for v in a]
                break
    return len(pivots)


def test_prime(p):
    assert p % 4 == 3 and p >= 3
    vecs = [(x, y) for x in range(p) for y in range(p)]
    idx = {v: i for i, v in enumerate(vecs)}
    radii = defaultdict(list)
    for d in vecs:
        if d != (0, 0):
            radii[(d[0] * d[0] + d[1] * d[1]) % p].append(d)
    assert 0 not in radii  # anisotropy
    rows = []
    for c in vecs:
        for rad, ds in radii.items():
            # Each unordered antipodal pair is represented once.
            pairs = {}
            for d in ds:
                e = ((-d[0]) % p, (-d[1]) % p)
                pairs[min(d, e)] = True
            ds = sorted(pairs)
            anchor = ds[0]
            for d in ds[1:]:
                r = [0] * (p * p)
                for vec, sign in [(anchor, 1), (d, -1)]:
                    for ep in (1, -1):
                        z = ((c[0] + ep * vec[0]) % p,
                             (c[1] + ep * vec[1]) % p)
                        r[idx[z]] += sign
                rows.append(r)
    rank = rank_mod_p(rows, p, p * p)
    assert rank == p * p - 4, (p, rank)
    for alpha, beta, gamma in ((0, 0, 0), (1, 0, 0),
                               (0, 1, 0), (0, 0, 1), (2, 3, 4)):
        coeff = [(alpha * x + beta * y + gamma * (x*x+y*y)) % p
                 for x, y in vecs]
        for r in rows:
            assert sum(a*b for a, b in zip(r, coeff)) % p == 0
    # Direct fourth-extension moments for two distinct quadratic chirps.
    for alpha, beta, gamma in ((0, 0, 0), (1, 2, 3)):
        phase = [(alpha*x+beta*y+gamma*(x*x+y*y)) % p
                 for x,y in vecs]
        total = 0.0
        for X, Y in vecs:
            for t in range(p):
                z = sum(exp(2j*pi*((phase[i]+X*x+Y*y+t*(x*x+y*y))%p)/p)
                        for i,(x,y) in enumerate(vecs))/(p*p)
                total += abs(z)**4
        predicted = 1 + 1/p - 1/(p*p)
        assert abs(total-predicted) < 3e-9, (p,total,predicted)
    return p, len(rows), rank


if __name__ == '__main__':
    for prime in (3, 7, 11):
        print('p, constraint_rows, Fp_rank:', *test_prime(prime))
    print('All finite checks passed; not a substitute for the general proof.')
