"""Exact integer checks for signed four-atom periodic phase retrieval."""
from collections import defaultdict
from itertools import combinations, product
from math import comb


def autocorrelation(points, modulus):
    """Periodic autocorrelation indexed by the signed difference."""
    c = [0] * modulus
    for x, a in points:
        for y, b in points:
            c[(x-y) % modulus] += a*b
    return tuple(c)


def orbit_representative(points, modulus):
    """Canonical representative under translations, reflections, global sign."""
    return min(
        tuple(sorted(((direction*(x-origin)) % modulus, phase*a)
                     for x, a in points))
        for origin, _ in points
        for direction in (1, -1)
        for phase in (1, -1)
    )


def enumerate_fibers(modulus):
    fibers = defaultdict(set)
    count = 0
    # Every four-atom signed signal translates, then changes global sign,
    # to one of these configurations, with the coefficient at zero equal +1.
    for other_sites in combinations(range(1, modulus), 3):
        for other_signs in product((1, -1), repeat=3):
            points = ((0, 1),) + tuple(zip(other_sites, other_signs))
            fibers[autocorrelation(points, modulus)].add(
                orbit_representative(points, modulus))
            count += 1
    assert count == comb(modulus-1, 3)*8
    return fibers, count


def autocorrelation_integer(points):
    c = defaultdict(int)
    for x, a in points:
        for y, b in points:
            c[x-y] += a*b
    return {k: v for k, v in c.items() if v}


def polynomial_product(first, second):
    out = [0] * (len(first)+len(second)-1)
    for i, a in enumerate(first):
        for j, b in enumerate(second):
            out[i+j] += a*b
    return tuple(out)


def integer_polynomial_factor_checks():
    common = polynomial_product((1, 0, 1), (1, 0, -1, 1))
    first = polynomial_product(common, (-1, -1, 0, 1))
    second = polynomial_product(common, (-1, 0, 1, 1))
    assert first == (-1, -1, 0, 0, 0, 0, 0, -1, 1)
    assert second == (-1, 0, 1, 0, 1, 0, 0, 0, 1)
    # Opposite reversed cubic: B(z)=-z^3 A(1/z).
    assert (-1, 0, 1, 1) == tuple(-x for x in (-1, -1, 0, 1)[::-1])


def universal_witness():
    integer_polynomial_factor_checks()
    f = ((0,-1), (1,-1), (7,-1), (8,1))
    h = ((0,-1), (2,1), (4,1), (8,1))
    assert autocorrelation_integer(f) == autocorrelation_integer(h)
    # They are inequivalent on every Z_p, prime p >= 11:
    # opposite global sign is necessary; after alignment of the unique
    # negative atom at 0, the positive positions are either
    # {-8,-7,-1} or {8,7,1}, not {2,4,8} modulo p.
    for p in (11, 13, 17, 19, 23, 29, 101):
        assert autocorrelation(f, p) == autocorrelation(h, p)
        assert orbit_representative(f,p) != orbit_representative(h,p)


def run():
    checks = 0
    for p, expected_fibers, expected_orbits, expected_ambiguous in (
        (5,6,6,0), (7,26,26,0), (11,135,140,5)):
        fibers, count = enumerate_fibers(p)
        assert len(fibers) == expected_fibers
        assert sum(map(len, fibers.values())) == expected_orbits
        ambiguous = {key: value for key, value in fibers.items()
                     if len(value)>1}
        assert len(ambiguous) == expected_ambiguous
        assert all(len(value) == 2 for value in ambiguous.values())
        if p == 11:
            known = set()
            for d in range(1,6):
                c = [0]*11
                c[0] = 4
                for j, v in ((d,-1),(-d,-1),(2*d,1),(-2*d,1)):
                    c[j % 11] = v
                known.add(tuple(c))
            assert len(known) == 5
            assert set(ambiguous) == known
            # Count all 4-site +/-1 signals to rule out a missed sign orbit.
            full_reps = set()
            for support in combinations(range(p),4):
                for signs in product((1,-1),repeat=4):
                    pts = tuple(zip(support,signs))
                    full_reps.add(orbit_representative(pts,p))
            assert len(full_reps) == expected_orbits
            assert full_reps == set().union(*fibers.values())
        print('p=%d normalized=%d spectra=%d orbits=%d ambiguous_spectra=%d'
              % (p,count,len(fibers),expected_orbits,len(ambiguous)))
        checks += count
    universal_witness()
    checks += 7
    print('CHECK_PASS exact enumerated base configurations = %d'
          % (checks-7))


if __name__ == '__main__':
    run()
