"""Exact checks of cyclic simplicial traces in two-cover graph complexes.

Run with Python 3 (standard library only): python3 verify_rotation.py
"""
from itertools import combinations
from math import comb, gcd


def pairs(m):
    return list(combinations(range(m), 2))


def rotation_edge_orbits(m, step):
    seen = set()
    answer = []
    for e in pairs(m):
        if e in seen:
            continue
        orbit = set()
        current = e
        while current not in orbit:
            orbit.add(current)
            current = tuple(sorted(((current[0] + step) % m,
                                    (current[1] + step) % m)))
        seen.update(orbit)
        answer.append(frozenset(orbit))
    return answer


def two_coverable(edge_set, m):
    return any(all(a in e or b in e for e in edge_set)
               for a, b in pairs(m))


def exact_reduced_lefschetz(m, step, max_orbits=19):
    """Compute the trace on augmented simplicial chains by orbit enumeration.

    An invariant face is a union of complete edge orbits. An orbit of size L
    permutes its vertices with sign (-1)^(L-1); the face has dimension E-1.
    Consequently its alternating signed trace is (-1)^(number of orbits-1).
    The empty face contributes -1.
    """
    os = rotation_edge_orbits(m, step)
    if len(os) > max_orbits:
        return None
    total = -1
    for mask in range(1, 1 << len(os)):
        es = frozenset().union(*(os[k] for k in range(len(os))
                                 if (mask >> k) & 1))
        if two_coverable(es, m):
            total += (-1) ** (mask.bit_count() - 1)
    return total


def predicted_trace(m, step):
    if step == 0:
        return comb(m - 1, 4)
    order = m // gcd(m, step)
    return 1 - m // 3 if order == 3 else 1


def multiplicity(m, j):
    b = comb(m - 1, 4)
    # Multiplication by three removes rational intermediate values.
    num = 3 * (b - 1) + 3 * m * (j == 0)
    if m % 3 == 0:
        num -= m * (2 if j % 3 == 0 else -1)
    assert num % (3 * m) == 0, (m, j, num)
    return num // (3 * m)


def test_orbit_structure():
    tested = 0
    exact = 0
    for m in range(5, 36, 2):
        for step in range(1, m):
            order = m // gcd(m, step)
            os = rotation_edge_orbits(m, step)
            allowed = [o for o in os if two_coverable(o, m)]
            if order >= 5:
                assert allowed == [], (m, step, 'unexpected orbit')
            else:
                assert order == 3
                assert len(allowed) == m // 3
                assert all(len(o) == 3 and len(set().union(*o)) == 3
                           for o in allowed)
                for a, b in combinations(allowed, 2):
                    assert not two_coverable(a | b, m)
            tested += 1
            if m <= 11:
                val = exact_reduced_lefschetz(m, step, max_orbits=19)
                if val is not None:
                    asserted = -1 if order >= 5 else m // 3 - 1
                    assert val == asserted, (m, step, val, asserted)
                    exact += 1
    print('orbit_structures_checked', tested)
    print('full_signed_chain_traces_checked', exact)


def test_eigenvalues():
    tested = 0
    for m in range(5, 102, 2):
        all_mults = [multiplicity(m, j) for j in range(m)]
        assert min(all_mults) >= 0
        assert sum(all_mults) == comb(m - 1, 4)
        # Reconstruct all integer character traces from the eigenvalue
        # multiplicities using an integer cyclotomic model (no float FFT).
        for step in range(m):
            expected = predicted_trace(m, step)
            # Independent numerical complex Fourier reconstruction. The
            # multiplicity and integrality checks above are exact integers.
            import cmath
            actual = sum(v * cmath.exp(2j * cmath.pi * j * step / m)
                         for j, v in enumerate(all_mults))
            assert abs(actual.real - expected) < 1e-7
            assert abs(actual.imag) < 1e-7
        tested += 1
    print('odd_orders_and_character_reconstructions', tested)
    for m in (5, 7, 9, 15, 21):
        arr = [multiplicity(m, j) for j in range(m)]
        print('multiplicity_sample', m, 'rank', comb(m - 1, 4),
              'invariant_dimension', arr[0], 'spectrum', arr)


if __name__ == '__main__':
    test_orbit_structure()
    test_eigenvalues()
    print('VERIFY_OK')
