#!/usr/bin/env python3
"""Independent integer check of the conic-arrangement obstruction.

Pure standard-library code. This enumerates weak singularity-count vectors
satisfying Bezout, the nearly-free Tjurina identity, and the published
orbifold BMY inequality in the only degrees still to be excluded.
The published freeness and Jacobian-syzygy bounds are applied in the proof.
"""

def qualifying_counts(k):
    K = k * (k - 1)
    vectors = []
    for t5 in range(K // 2 + 1):
        for t7 in range(K // 3 + 1):
            for t3 in range(K + 1):
                n3 = K - t3 - 2*t5 - 3*t7
                n2 = t5 + 2*t7 - n3
                if n2 < 0 or n3 < 0:
                    continue
                assert n2 + 2*t3 + 3*n3 + 3*t5 + 4*t7 == 2*K
                assert n2 + 3*t3 + 4*n3 + 5*t5 + 7*t7 == 3*K
                if 560*k + 100*n2 + 75*n3 >= 608*t7 + 404*t5 + 184*t3:
                    vectors.append((n2,t3,n3,t5,t7))
    return vectors


def analytic_certificate(k):
    K = k * (k - 1)
    R = 2800*k - 458*K
    if k == 8:
        assert R == -3248
        return R, []
    if k == 7:
        assert R == 364
        possibilities = [(u,n) for u in range(R // 271 + 1)
                         for n in range(R // 333 + 1)
                         if 271*u + 333*n <= R]
        assert possibilities == [(0,0),(0,1),(1,0)]
        assert all((3*u - (K+n)) % 5 != 0 for u,n in possibilities)
        return R, possibilities
    raise ValueError('only k=7,8')


if __name__ == '__main__':
    for k in (7,8):
        rhs, possibilities = analytic_certificate(k)
        candidates = qualifying_counts(k)
        assert not candidates, (k,candidates)
        print(f'k={k}: certificate_rhs={rhs}, preliminary_pairs={possibilities}, admissible_count={len(candidates)}')
    print('CONIC_CEILING_EXACT_OK')
