"""Self-contained exact checks for an irrevocable one-spike allocation theorem.

Run: python verify_one_spike.py
No external Python packages are required. All comparisons are exact rationals.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product


def allocate(m, high_positions):
    assert len(high_positions) == 3
    count = [0, 0, 0]
    frozen = set()
    shared_seen = False
    recipients = []
    for t in range(m):
        high = [i for i in range(3) if high_positions[i] == t]
        empty = [i for i in range(3) if count[i] == 0]
        remaining = m - t
        assert remaining >= len(empty)
        if remaining == len(empty):
            recipient = empty[0]
        elif not shared_seen:
            if len(high) >= 2:
                free_high = [i for i in high if count[i] == 0]
                assert free_high, (m, high_positions, t, count)
                recipient = free_high[0]
                frozen.add(recipient)
                shared_seen = True
            elif len(high) == 1:
                recipient = high[0]
            else:
                recipient = next((i for i in range(3) if count[i]), 0)
        else:
            assert len(high) <= 1
            if high:
                recipient = high[0]
            else:
                recipient = next(
                    (i for i in range(3) if i not in frozen and count[i]),
                    next(i for i in range(3) if i not in frozen),
                )
        assert recipient not in frozen or count[recipient] == 0
        count[recipient] += 1
        recipients.append(recipient)
    assert min(count) >= 1
    for agent in range(3):
        high_owner = recipients[high_positions[agent]]
        assert high_owner == agent or count[high_owner] == 1
    return tuple(recipients)


def efx_factor(m, high_positions, recipients, H):
    count = [recipients.count(i) for i in range(3)]
    receiver = [recipients[pos] for pos in high_positions]
    factor = Fraction(1)
    for i in range(3):
        own = count[i] + (H - 1) * (receiver[i] == i)
        for j in range(3):
            if i != j and count[j]:
                # The most expensive deletion for the envied recipient
                # removes a unit-value good when one exists.
                after_deletion = count[j] - 1
                if receiver[i] == j and count[j] >= 2:
                    after_deletion += H - 1
                if after_deletion > 0:
                    factor = min(factor, Fraction(own, after_deletion))
    return factor


def minimax(m, H):
    """Exhaustive adaptive-adversary game, independent of the proposed policy."""
    @lru_cache(maxsize=None)
    def value(counts, receiver):
        t = sum(counts)
        if t == m:
            if -1 in receiver:
                return Fraction(0)
            result = Fraction(1)
            for i in range(3):
                own = counts[i] + (H - 1) * (receiver[i] == i)
                for j in range(3):
                    if i != j and counts[j] >= 2:
                        rem = counts[j] - 1 + (H - 1) * (receiver[i] == j)
                        result = min(result, Fraction(own, rem))
                    elif i != j and counts[j] == 1:
                        pass
            return result
        pending = [i for i in range(3) if receiver[i] == -1]
        lowest = Fraction(1)
        for mask in range(1 << len(pending)):
            if t == m - 1 and mask != (1 << len(pending)) - 1:
                continue
            newly_high = [pending[r] for r in range(len(pending)) if mask >> r & 1]
            best = Fraction(0)
            for recipient in range(3):
                next_counts = list(counts)
                next_counts[recipient] += 1
                next_receiver = list(receiver)
                for i in newly_high:
                    next_receiver[i] = recipient
                best = max(best, value(tuple(next_counts), tuple(next_receiver)))
            lowest = min(lowest, best)
        return lowest
    return value((0, 0, 0), (-1, -1, -1))


def test():
    total = 0
    for m in range(6, 16):
        for positions in product(range(m), repeat=3):
            rec = allocate(m, positions)
            for H in (2, 7, (m - 2) * (m - 3) + 1, 100000):
                assert efx_factor(m, positions, rec, H) >= Fraction(1, m - 3)
            total += 1
    print('Policy: verified', total, 'high-position triples for m=6..15 at four heights each')
    for m in range(6, 11):
        H = (m - 2) * (m - 3) + 1
        best = minimax(m, H)
        assert best == Fraction(1, m - 3), (m, H, best)
        print('Independent minimax: m=', m, 'H=', H, 'optimal=', best)
    print('ALL EXACT CHECKS PASSED')


if __name__ == '__main__':
    test()
