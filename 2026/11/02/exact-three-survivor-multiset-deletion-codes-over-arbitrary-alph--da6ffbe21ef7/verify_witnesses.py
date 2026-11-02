"""Constructive checks of the all-alphabet three-survivor theorem."""


def overlap(a, b):
    return sum(min(i, j) for i, j in zip(a, b))


def constants(q, n):
    return [tuple(n if i == j else 0 for i in range(q)) for j in range(q)]


def light(q, n):
    assert q <= n <= 2 * q
    return tuple(2 if i < n - q else 1 for i in range(q))


def two_boundary_lights(q):
    # q+1 symbols in each, maximum multiplicity 2, common size exactly 2.
    if q % 2:
        a = b = (q - 1) // 2
        x = (2,) + (2,) * a + (0,) * b
        y = (2,) + (0,) * a + (2,) * b
    else:
        a = (q - 2) // 2
        x = (2, 1) + (2,) * a + (0,) * a
        y = (1, 2) + (0,) * a + (2,) * a
    return x, y


def valid(code, n):
    assert len(code) == len(set(code))
    assert all(sum(x) == n for x in code)
    assert all(overlap(x, y) <= 2 for i, x in enumerate(code) for y in code[:i])


if __name__ == '__main__':
    profiles = 0
    for q in range(2, 41):
        for n in range(q + 2, 2 * q + 3):
            if n <= 2 * q:
                code = constants(q, n) + [light(q, n)]
                assert len(code) == q + 1
            else:
                code = constants(q, n)
                assert len(code) == q
            valid(code, n)
            profiles += 1
        n = q + 1
        code = constants(q, n) + list(two_boundary_lights(q))
        assert len(code) == q + 2
        valid(code, n)
        profiles += 1
    print('VERIFY_WITNESSES_OK', profiles, 'different (q,n) profiles for q=2..40')
    print('q=4, n=5 boundary two-light certificate:', two_boundary_lights(4))
    print('q=5, n=6 boundary two-light certificate:', two_boundary_lights(5))
