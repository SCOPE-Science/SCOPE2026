"""Check finite S5 knowing-whether announcement confluence and its partition criterion.

Uses the standard library. Finite checks illustrate, rather than prove, the
unrestricted set-theoretic theorem.
"""
from math import comb


def partitions(items):
    """Yield all set partitions of a tuple of distinct vertices."""
    if not items:
        yield ()
        return
    head, *tail = items
    for rest in partitions(tuple(tail)):
        yield ((head,),) + rest
        for i, block in enumerate(rest):
            yield rest[:i] + ((head,) + block,) + rest[i + 1 :]


def uniform_after(current, blocks, true_worlds):
    """One public announcement of 'knowing whether p' on the induced model."""
    remaining = set()
    for block in blocks:
        active = current.intersection(block)
        if active and (active.isdisjoint(true_worlds) or active <= true_worlds):
            remaining.update(active)
    return frozenset(remaining)


def sequence(n, first, second, true_worlds):
    current = frozenset(range(n))
    current = uniform_after(current, first, true_worlds)
    return uniform_after(current, second, true_worlds)


def criterion(first, second):
    for left in first:
        if len(left) <= 1:
            continue
        a = frozenset(left)
        for right in second:
            if len(right) > 1 and a.intersection(right) and a != frozenset(right):
                return False
    return True


def finite_exhaustion():
    expected = (1, 1, 4, 13, 61, 304)
    total_pairs = 0
    tested_masks = 0
    for n in range(1, 6):
        all_partitions = list(partitions(tuple(range(n))))
        count = 0
        for first in all_partitions:
            for second in all_partitions:
                total_pairs += 1
                structural = criterion(first, second)
                semantic = True
                for truth_mask in range(1 << n):
                    tested_masks += 1
                    true_worlds = frozenset(
                        w for w in range(n) if truth_mask & (1 << w)
                    )
                    if sequence(n, first, second, true_worlds) != sequence(
                        n, second, first, true_worlds
                    ):
                        semantic = False
                        break
                assert semantic == structural, (n, first, second)
                count += structural
        assert count == expected[n], (n, count, expected[n])
        print(f"n={n}: partitions={len(all_partitions)}, compatible_pairs={count}")
    a = [1]
    for n in range(8):
        a.append(a[n] + 3 * sum(comb(n, j) * a[n - j] for j in range(1, n + 1)))
    assert a == [1, 1, 4, 13, 61, 304, 1747, 10945, 74830]
    example_a = ((0, 1), (2,))
    example_b = ((0,), (1, 2))
    truth = frozenset((1,))
    assert sequence(3, example_a, example_b, truth) == frozenset((2,))
    assert sequence(3, example_b, example_a, truth) == frozenset((0,))
    print(f"frame_pairs_checked={total_pairs}, valuations_evaluated={tested_masks}")
    print("VERIFY_OK")


if __name__ == "__main__":
    finite_exhaustion()
