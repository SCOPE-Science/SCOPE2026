"""Exhaustive low-field Grassmannian check for the strictly upper-triangular 4x4 Lie algebra."""
from itertools import combinations, product


def planes(n, q):
    """Every two-plane exactly once, via reduced row-echelon generators."""
    for i, j in combinations(range(n), 2):
        positions0 = [k for k in range(i + 1, n) if k != j]
        positions1 = list(range(j + 1, n))
        for values in product(range(q), repeat=len(positions0) + len(positions1)):
            x, y = [0] * n, [0] * n
            x[i], y[j] = 1, 1
            for k, val in zip(positions0, values):
                x[k] = val
            for k, val in zip(positions1, values[len(positions0):]):
                y[k] = val
            yield x, y


def count(q):
    rank_totals = [0, 0, 0]
    elementary_rank_totals = [0, 0, 0]
    components = [0, 0, 0]  # X_H, Y, intersection
    enumerated = 0
    for x, y in planes(6, q):
        enumerated += 1
        p_ab = x[0] * y[1] - x[1] * y[0]
        p_bc = x[1] * y[2] - x[2] * y[1]
        p_ae_minus_cd = x[0] * y[4] - x[4] * y[0] + x[3] * y[2] - x[2] * y[3]
        if any(z % q for z in (p_ab, p_bc, p_ae_minus_cd)):
            continue
        proj_minors = [p_ab, x[0] * y[2] - x[2] * y[0], p_bc]
        rank = 2 if any(z % q for z in proj_minors) else 1 if any(z % q for z in x[:3] + y[:3]) else 0
        rank_totals[rank] += 1
        in_H = x[1] % q == 0 and y[1] % q == 0
        in_Y = rank <= 1
        components[0] += int(in_H)
        components[1] += int(in_Y)
        components[2] += int(in_H and in_Y)
        if q == 3:
            cube_x = x[0] * x[1] * x[2]
            cube_y = y[0] * y[1] * y[2]
            # For a commuting pair of nilpotent 4x4 matrices in characteristic 3,
            # (lambda*x+mu*y)^3=lambda^3*x^3+mu^3*y^3.
            if cube_x % 3 == 0 and cube_y % 3 == 0:
                elementary_rank_totals[rank] += 1
    expected = [q * q + q + 1, q * q * (q**3 + 3*q*q + 2*q + 1), q**5]
    component_expected = [q**5 + q**4 + 2*q**3 + 2*q*q + q + 1,
                          q**5 + 3*q**4 + 2*q**3 + 2*q*q + q + 1,
                          q**4 + 2*q**3 + 2*q*q + q + 1]
    assert rank_totals == expected, (q, rank_totals, expected)
    assert components == component_expected, (q, components, component_expected)
    if q == 3:
        assert elementary_rank_totals == [13, 405, 243], elementary_rank_totals
    expected_count = 2*q**5 + 3*q**4 + 2*q**3 + 2*q*q + q + 1
    assert sum(rank_totals) == expected_count
    return enumerated, rank_totals, components, elementary_rank_totals if q == 3 else None


if __name__ == '__main__':
    for Q in (2, 3, 5):
        enumerated, ranks, components, elementary = count(Q)
        print(f'GF({Q}) two-planes={enumerated}, commuting strata={ranks}, components/intersection={components}, elementary={elementary}')
    print('VERIFY_OK')
