"""Exact independent finite checks for the Mersenne 2-rank formula.

This checker corroborates the all-parameter proof; it is not a replacement
for the algebraic-geometry and combinatorial arguments.
"""

def lucas(n):
    a, b = 2, 1
    if n == 0:
        return a
    for _ in range(1, n):
        a, b = b, a+b
    return b


def basis(k):
    """Indices of the explicit holomorphic differential basis."""
    return {j for j in range(1, k)
            if (3*j > k and 2*j < k) or (3*j > 2*k)}


def v_of(j, k):
    if 3*j > k and 2*j < k:
        return 0
    if 3*j > 2*k:
        return 1
    raise ValueError('index outside basis')


def cartier_target(j, k, ids):
    """The Cartier formula on omega_j; None indicates zero."""
    v = v_of(j, k)
    if j % 2 == 0:
        if v == 0:
            return None
        m = j//2
        assert m in ids and v_of(m, k) == 0
        return m
    m = (j+k)//2
    assert m in ids and v_of(m, k) == 1
    return m


def circular_no_00(j, r):
    return all(((j >> a) & 1) or ((j >> ((a+1)%r)) & 1)
               for a in range(r))


def main():
    for r in range(3, 16, 2):
        k = 2**r-1
        ids = basis(k)
        assert len(ids) == (k-1)//2
        # All three branch-point valuations of each differential are nonnegative.
        for j in ids:
            v = v_of(j, k)
            assert min(k-1-j, k-1+k*v-2*j, -k-1-k*v+3*j) >= 0
            tgt = cartier_target(j, k, ids)
            if tgt is not None:
                assert (2*tgt-j) % k == 0
        # Stabilize the Cartier directed graph. Every edge carries unit coefficient.
        persistent = set()
        for j in ids:
            t = j
            for _ in range(r):
                if t is None:
                    break
                t = cartier_target(t, k, ids)
            if t is not None:
                persistent.add(j)
        good_orbits = {j for j in range(1, k)
                       if all((j*(2**a)) % k in ids for a in range(r))}
        no_adjacent_zeros = {j for j in range(1, k)
                             if circular_no_00(j, r)}
        assert persistent == good_orbits == no_adjacent_zeros
        assert len(persistent) == lucas(r)-1
        assert 2*len(persistent) <= 3*(k-1)//2
        print(f'r={r} k={k} quotient_genus={(k-1)//2} '
              f'quotient_2rank={len(persistent)} '
              f'cover_2rank={2*len(persistent)}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
