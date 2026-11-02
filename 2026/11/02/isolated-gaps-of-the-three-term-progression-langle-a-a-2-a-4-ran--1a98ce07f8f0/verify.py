"""Exhaustive small-parameter check for isolated gaps in <a,a+2,a+4>.

The analytic theorem is proved separately; this file tests its formula
against dynamic-programming semigroup membership and an independent genus count.
Run: python verify.py
"""


def predicted(a):
    assert a >= 3 and a % 2 == 1
    s = (a - 1) // 2
    return {
        a * u + 2 * j
        for j in range(s + 1, 2 * s + 1)
        for u in range((j - s + 1) // 2 - 1, (j + 1) // 2)
    }


def direct(a):
    limit = (a * a + a - 4) // 2
    present = [False] * (limit + 2)
    present[0] = True
    gens = (a, a + 2, a + 4)
    for x in range(1, limit + 2):
        present[x] = any(x >= b and present[x - b] for b in gens)
    gaps = {x for x in range(1, limit + 1) if not present[x]}
    isolated = {x for x in gaps if present[x - 1] and present[x + 1]}
    return gaps, isolated


def verify():
    total_gaps = total_isolated = 0
    cases = 0
    for a in range(3, 302, 2):
        s = (a - 1) // 2
        gaps, isolated = direct(a)
        predicted_set = predicted(a)
        expected_genus = s * (s + 2)
        expected_count = (s * (s + 2)) // 2
        expected_F = (a * a + a - 4) // 2
        assert gaps and max(gaps) == expected_F, ('F', a)
        assert len(gaps) == expected_genus, ('genus', a)
        assert isolated == predicted_set, ('set', a, isolated ^ predicted_set)
        assert len(isolated) == expected_count, ('count', a)
        assert min(isolated) == a + 1 and max(isolated) == expected_F, ('ends', a)
        total_gaps += len(gaps)
        total_isolated += len(isolated)
        cases += 1
    print(f'PASS: {cases} odd multiplicities 3..301')
    print(f'PASS: {total_gaps} directly enumerated gaps, {total_isolated} isolated gaps')
    print('PASS: exact sets, genus, isolated counts, Frobenius bounds, and endpoints')


if __name__ == '__main__':
    verify()
