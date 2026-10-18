"""Exhaustive Kripke-semantics verification of a prelinearity joint spectrum.

Run with Python 3 standard library only:
  python verify_prelinearity.py
"""


def compositions(n):
    for cuts in range(1 << (n - 1)):
        parts = []
        previous = 0
        for i in range(1, n):
            if cuts & (1 << (i - 1)):
                parts.append(i - previous)
                previous = i
        parts.append(n - previous)
        yield tuple(parts)


def direct_spectrum(level_sizes):
    levels = tuple(i for i, size in enumerate(level_sizes)
                   for _ in range(size))
    n = len(levels)
    cones = tuple(sum(1 << j for j, rank in enumerate(levels)
                      if i == j or rank > levels[i])
                  for i in range(n))
    upsets = tuple(u for u in range(1 << n)
                   if all(not (u & (1 << i)) or (u & cone) == cone
                          for i, cone in enumerate(cones)))
    comparable = only_local = failure = 0
    for u in upsets:
        for v in upsets:
            differences_uv, differences_vu = u & ~v, v & ~u
            global_comparable = not differences_uv or not differences_vu
            # Both implications fail at a common world precisely if both
            # directional differences occur above that world.
            prelinearity_fails = any((cone & differences_uv) and
                                     (cone & differences_vu)
                                     for cone in cones)
            if global_comparable:
                assert not prelinearity_fails
                comparable += 1
            elif prelinearity_fails:
                failure += 1
            else:
                only_local += 1
    return len(upsets), comparable, only_local, failure


def predicted(level_sizes):
    upsets = 1 + sum(2**size - 1 for size in level_sizes)
    q = [4**size - 2*3**size + 2**size for size in level_sizes]
    return upsets, upsets*upsets - sum(q), q[0], sum(q[1:])


def main():
    tested = 0
    for n in range(1, 10):
        for levels in compositions(n):
            actual = direct_spectrum(levels)
            expected = predicted(levels)
            if actual != expected:
                raise AssertionError((levels, actual, expected))
            assert (actual[3] == 0) == all(m == 1 for m in levels[1:])
            tested += 1
    assert tested == 511
    for m in range(1, 15):
        N, globally_comparable, only_local, failure = predicted((m, m))
        assert N == 2 ** (m + 1) - 1
        assert globally_comparable + only_local + failure == N * N
        assert min(globally_comparable, only_local, failure) >= 0
    print('VERIFY_OK exact joint spectrum on all 511 compositions of 1..9 worlds; '
          '14 large-parameter algebraic consistency tests')


if __name__ == '__main__':
    main()
