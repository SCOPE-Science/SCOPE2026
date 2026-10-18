"""Standalone finite checks of multiplicative-character Hamming-variety sampling.

The field enters only through its cyclic nonzero multiplicative group, order M.
No external input or packages except numpy for the optional direct Gram check.
"""
import itertools
import math
from collections import Counter, defaultdict


def weight(alpha):
    return sum(v != 0 for v in alpha)


def spectrum_by_orbits(M, d, k):
    classes = defaultdict(int)
    for alpha in itertools.product(range(M), repeat=d):
        if weight(alpha) <= k:
            key = min(tuple((v + shift) % M for v in alpha)
                      for shift in range(M))
            classes[key] += 1
    return Counter(classes.values()), sum(classes.values()), len(classes)


def compositions(n, length):
    if length == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for sub in compositions(n-a, length-1):
                yield (a,)+sub


def spectrum_by_occupancies(M, d, k):
    out = Counter()
    for counts in compositions(d, M):
        t = sum(n >= d-k for n in counts)
        if t:
            # Exact multinomial calculation, without integer truncation.
            v = math.factorial(d) // math.prod(math.factorial(n) for n in counts)
            out[t] += v
    assert all(n % M == 0 for n in out.values()), (M, d, k, out)
    return Counter({t: n // M for t, n in out.items()})


def direct_gram(M, d, k, residue_sum):
    import numpy as np
    basis = [a for a in itertools.product(range(M), repeat=d) if weight(a) <= k]
    points = [u for u in itertools.product(range(M), repeat=d)
              if sum(u) % M == residue_sum]
    omega = np.exp(2j*np.pi/M)
    V = np.asarray([[omega ** (sum(a_i*u_i for a_i, u_i in zip(a, u))%M)
                      for a in basis] for u in points], dtype=np.complex128)
    G = V.conj().T @ V / len(points)
    ev = np.linalg.eigvalsh(G)
    expected_counts, B, _ = spectrum_by_orbits(M, d, k)
    expected = [0.] * (B - sum(expected_counts.values()))
    for val, mult in expected_counts.items():
        expected.extend([float(val)]*mult)
    expected.sort()
    err = max(abs(a-b) for a,b in zip(sorted(ev), expected))
    assert err < 1e-8, (M,d,k,residue_sum,err)
    return err


def run():
    cases = 0
    for M in range(2, 6):
        for d in range(2, 8):
            if M**d > 40000:
                continue
            for k in range(d+1):
                orbit_counts, B, rank = spectrum_by_orbits(M, d, k)
                occ_counts = spectrum_by_occupancies(M, d, k)
                assert orbit_counts == occ_counts, (M,d,k,orbit_counts,occ_counts)
                assert B == sum(math.comb(d,w)*(M-1)**w for w in range(k+1))
                assert sum(v for v in orbit_counts.values()) == rank
                assert sum(t*v for t,v in orbit_counts.items()) == B
                assert rank == M**(d-1) if k >= d-math.ceil(d/M) else rank < M**(d-1)
                if 2*k < d:
                    assert orbit_counts == Counter({1:B}), (M,d,k)
                if 2*k >= d and k<d:
                    assert B>rank, (M,d,k)
                    assert max(orbit_counts) == min(M, d//(d-k))
                    assert set(orbit_counts)==set(range(1,max(orbit_counts)+1))
                if M == 2 and d % 2 == 1 and k == (d-1)//2:
                    assert B == rank == 2**(d-1)
                cases += 1
    numerical = []
    for M,d in [(2,3),(2,5),(3,3),(3,4),(4,3),(4,4)]:
        for k in range(d+1):
            for residue in [0, 1]:
                err=direct_gram(M,d,k,residue)
                numerical.append((M,d,k,residue,err))
    print(f'PASS {cases} full orbit/occupancy/band-threshold cases')
    print(f'PASS {len(numerical)} direct complex character Gram spectra')
    print('maximum direct eigenvalue discrepancy:',max(x[4] for x in numerical))
    for M,d,k in [(2,5,2),(3,4,2),(4,4,2),(4,5,3),(3,5,3)]:
        spec,B,R=spectrum_by_orbits(M,d,k)
        print(f'M={M},d={d},k={k}: columns={B},rank={R}, positive_eigenvalue_multiplicities={dict(sorted(spec.items()))}')

if __name__ == '__main__':
    run()
