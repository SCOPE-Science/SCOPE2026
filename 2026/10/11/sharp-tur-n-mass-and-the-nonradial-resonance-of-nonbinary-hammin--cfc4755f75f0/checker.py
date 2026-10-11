"""Reproducibility checks for the q-ary weight-two positive-definite mass theorem.

All sharp-constant and slice-rank checks use exact integer/rational arithmetic.
Finite checks support, but do not replace, the all-parameter proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb
import cmath


def K2(q, d, t):
    y = d * (q - 1) - q * t
    n = y * y - (q - 2) * y - d * (q - 1)
    assert n % 2 == 0
    return n // 2


def rank_mod(rows, prime=1_000_003):
    """Exact rank modulo prime; used only as a finite check."""
    if not rows:
        return 0
    b = [list(map(lambda x: x % prime, row)) for row in rows]
    n, m = len(b), len(b[0])
    k = 0
    for j in range(m):
        pivot = next((r for r in range(k, n) if b[r][j]), None)
        if pivot is None:
            continue
        b[k], b[pivot] = b[pivot], b[k]
        inv = pow(b[k][j], -1, prime)
        for z in range(j, m):
            b[k][z] = b[k][z] * inv % prime
        for r in range(k+1, n):
            if b[r][j]:
                mult = b[r][j]
                for z in range(j, m):
                    b[r][z] = (b[r][z] - mult * b[k][z]) % prime
        k += 1
        if k == n:
            break
    return k


def check_radial(q, d):
    vals = [K2(q, d, t) for t in range(d+1)]
    mu = min(vals)
    ks = [t for t, v in enumerate(vals) if v == mu]
    assert mu < 0
    # The q-ary second Krawtchouk eigenvalue has the standard shell valency.
    assert vals[0] == comb(d, 2) * (q-1) ** 2
    assert 2 <= ks[0] and ks[-1] <= d-2
    assert len(ks) == (2 if d % q == 1 else 1)
    T = Fraction(mu - vals[0], mu)
    assert T >= 1
    if d % q == 2:
        k = ks[0]
        assert len(ks) == 1
        assert k == 1 + (d-2) * (q-1) // q
        assert mu == -d * (q-1) // 2
        assert T == 1 + (d-1) * (q-1)
        eps = Fraction(q, d*(q-1))
        a = [eps, -eps] + [Fraction(0)]*(d-2)
        # Every subset A of nonzero frequency positions must be nonnegative.
        for bits in product((0, 1), repeat=d):
            t = sum(bits)
            spectral = 1 - Fraction(vals[t], mu) + (t-k)*sum(a[i]*bits[i] for i in range(d))
            assert spectral >= 0, (q, d, bits, spectral)
            if t == k:
                assert spectral == 0
        assert sum(a) == 0
    return mu, ks, T


def check_slice_rank(q, d):
    p = 1_000_003
    assert q % p
    minval = min(K2(q, d, t) for t in range(d+1))
    ks = [t for t in range(d+1) if K2(q, d, t) == minval]
    edges = list(combinations(range(d), 2))
    invq = pow(q, -1, p)
    # h_i = u_i - (q-1)/q. With c=0 (fixed mean), evaluate h_i*h_j
    # on each minimizing Hamming slice. Its nullity is d-1 at resonance.
    rows = []
    for k in ks:
        for ones in combinations(range(d), k):
            one = set(ones)
            h = [(int(i in one) - (q-1)*invq) % p for i in range(d)]
            rows.append([(h[i]*h[j]) % p for i,j in edges])
    rank = rank_mod(rows, p)
    expect = d-1 if d % q == 2 else 0
    assert len(edges) - rank == expect, (q, d, ks, len(edges)-rank, expect)
    return rank


def check_edge_identity(q, d):
    """Check the resonant edge-additive Fourier polynomial identity exactly."""
    assert d % q == 2
    p = Fraction(q-1, q)
    k = 1 + (d-2)*(q-1)//q
    a = [Fraction(1, 7), Fraction(-1, 7)] + [Fraction(0)]*(d-2)
    for bits in product((0, 1), repeat=d):
        h = [Fraction(b)-p for b in bits]
        left = sum((a[i]+a[j])*h[i]*h[j] for i,j in combinations(range(d),2))
        t = sum(bits)
        right = (t-k)*sum(a[i]*bits[i] for i in range(d))
        assert left == right


def direct_fourier_check_ternary(d):
    q = 3
    mu = min(K2(q, d, t) for t in range(d+1))
    root = cmath.exp(2j * cmath.pi/3)
    for z in [(0,)*d, (1,)+(0,)*(d-1), (1,1)+(0,)*(d-2),
              (1,1,1)+(0,)*(d-3), (1,2)+(0,)*(d-2)]:
        total = 0j
        for xi in product(range(3), repeat=d):
            spec = 1 - Fraction(K2(q, d, sum(v != 0 for v in xi)), mu)
            total += float(spec)*root**(sum(x*y for x,y in zip(xi,z))%3)
        total /= 3**d
        wt = sum(x != 0 for x in z)
        wanted = (1 if wt == 0 else (Fraction(-1, mu) if wt == 2 else 0))
        assert abs(total-complex(float(wanted),0)) < 2e-11, (d,z,total,wanted)


def main():
    radial_cases = 0
    rank_cases = 0
    for q, lo, hi in [(3,6,11),(4,8,12),(5,10,13),(7,14,15)]:
        for d in range(lo, hi+1):
            mu,ks,T = check_radial(q,d)
            radial_cases += 1
            if d <= 12:
                check_slice_rank(q,d)
                rank_cases += 1
    check_edge_identity(3, 8)
    check_edge_identity(4, 10)
    direct_fourier_check_ternary(6)
    direct_fourier_check_ternary(8)
    print(f'VERIFY_OK radial_exact={radial_cases} slice_ranks_mod_1000003={rank_cases} ternary_fourier=10 edge_identities=2')
    print('examples:', 'q=3,d=8', check_radial(3,8), 'q=4,d=10', check_radial(4,10))


if __name__ == '__main__':
    main()
