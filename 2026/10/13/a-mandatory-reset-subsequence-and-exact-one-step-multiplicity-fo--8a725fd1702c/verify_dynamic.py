"""Exact power-subset counting for cyclic synchronizing automata."""
from collections import defaultdict, deque


def next_mask(mask, n, symbol):
    full = (1 << n) - 1
    if symbol == 'a':
        return ((mask << 1) & full) | (mask >> (n - 1))
    return (mask & ~(1 << (n - 1))) | int(bool(mask & (1 << (n - 1))))


def main():
    for n in range(2, 13):
        full = (1 << n) - 1
        target = (n - 1) ** 2 + 1
        counts = {full: 1}
        for length in range(target):
            nxt = defaultdict(int)
            for subset, count in counts.items():
                for symbol in 'ab':
                    nxt[next_mask(subset, n, symbol)] += count
            counts = nxt
            if length == target - 2:
                assert sum(v for s, v in counts.items() if s.bit_count() == 1) == 1, n
        observed = sum(v for s, v in counts.items() if s.bit_count() == 1)
        expected = n * n - 4 * n + 7
        assert observed == expected, (n, observed, expected)
        print(f'n={n}: shortest=1, excess-one={observed}')
    print('VERIFY_DYNAMIC_OK')


if __name__ == '__main__':
    main()
