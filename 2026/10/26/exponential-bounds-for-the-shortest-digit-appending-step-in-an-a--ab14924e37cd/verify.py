"""Exact finite witnesses for digit-appending recurrence steps.

This verifies finite instances only; asymptotic estimates require the paper proof.
"""


def smallest_step(seq, base, m, bound):
    start = seq(m)
    assert start != 0
    sign = 1 if start > 0 else -1
    for k in range(1, bound + 1):
        target = seq(m + k)
        if target * sign <= 0:
            continue
        # A nonnegative appended block corresponds to the unique base power
        # satisfying b^t <= abs(target)/abs(start) < b^(t+1), for abs(start)>=1.
        ratio = abs(target) // abs(start)
        if ratio < base:
            continue
        power = 1
        length = 0
        while power * base <= ratio:
            power *= base
            length += 1
        digit = abs(target) - power * abs(start)
        if 0 <= digit < power:
            assert target == power * start + digit * sign
            return (k, length, digit)
    return None


def run():
    expected_powers = {
        1: (7, 2), 2: (10, 3), 3: (10, 3), 4: (10, 3),
        5: (10, 3), 6: (103, 31), 7: (196, 59),
        8: (681, 205), 9: (1651, 497), 10: (2136, 643),
    }
    for m, (k, t) in expected_powers.items():
        hit = smallest_step(lambda j: 2**j, 10, m, k)
        assert hit is not None and hit[:2] == (k, t), (m, hit)
    expected_shift = {1: (6, 9), 2: (2, 3), 3: (7, 11),
                      4: (12, 19), 5: (106, 168), 6: (53, 84)}
    for m, (k, t) in expected_shift.items():
        hit = smallest_step(lambda j: 3**j + 1, 2, m, k)
        assert hit is not None and hit[:2] == (k, t), (m, hit)
    neg_cases = []
    for m in range(1, 7):
        hit = smallest_step(lambda j: (-2)**j, 10, m, 1000)
        assert hit is not None
        assert hit[0] % 2 == 0
        neg_cases.append((m, hit[0], hit[1]))
    print('VERIFY_OK: 10 power, 6 shifted-power, 6 negative-root cases')
    print('NEGATIVE_ROOT_CASES', neg_cases)


if __name__ == '__main__':
    run()
