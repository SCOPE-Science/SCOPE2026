"""Exact finite checks for periodically forbidden summand indices.

Run: python3 verify.py
Only standard-library integer arithmetic is used.  These are sanity checks,
not a proof of the central limit theorem for all periodic functions.
"""
from itertools import product


def f_sequence(period, length):
    values = [1]
    for i in range(length):
        previous = i - period[i % len(period)]
        values.append(values[-1] + (values[previous] if previous >= 0 else 1))
    return values


def automaton_histogram(period, length):
    bound = max(period)
    states = [{} for _ in range(bound + 1)]
    states[bound] = {0: 1}
    for i in range(length):
        next_states = [{} for _ in states]
        for state, counts in enumerate(states):
            for selected, count in counts.items():
                successor = min(bound, state + 1)
                target = next_states[successor]
                target[selected] = target.get(selected, 0) + count
                if state >= period[i % len(period)]:
                    target = next_states[0]
                    target[selected + 1] = target.get(selected + 1, 0) + count
        states = next_states
    return [sum(d.get(k, 0) for d in states) for k in range(length + 1)]


def brute_histogram(period, length):
    ans = [0] * (length + 1)
    for word in range(1 << length):
        legal = True
        for i in range(length):
            if not (word & (1 << i)):
                continue
            lower = max(0, i - period[i % len(period)])
            if (word >> lower) & ((1 << (i - lower)) - 1):
                legal = False
                break
        if legal:
            ans[word.bit_count()] += 1
    return ans


def primitive_witness(period):
    m, bound = len(period), max(period)
    steps = m * (2 * bound + 4)
    for start in range(bound + 1):
        reachable = {start}
        for i in range(steps):
            successor = {min(bound, s + 1) for s in reachable}
            successor.update(0 for s in reachable if s >= period[i % m])
            reachable = successor
        if reachable != set(range(bound + 1)):
            return False
    return True


def main():
    tested = 0
    for m in (1, 2, 3):
        for period in product(range(3), repeat=m):
            assert primitive_witness(period), period
            for length in range(12):
                expected = brute_histogram(period, length)
                actual = automaton_histogram(period, length)
                assert actual == expected, (period, length, actual, expected)
                assert sum(actual) == f_sequence(period, length)[-1]
                tested += 1
    for period in ((0, 3, 1), (2, 1, 3), (1, 1, 2)):
        assert primitive_witness(period)
        for length in range(13):
            expected = brute_histogram(period, length)
            assert automaton_histogram(period, length) == expected
            assert sum(expected) == f_sequence(period, length)[-1]
            tested += 1
    print('checked', tested, 'histograms; VERIFY_OK')


if __name__ == '__main__':
    main()
