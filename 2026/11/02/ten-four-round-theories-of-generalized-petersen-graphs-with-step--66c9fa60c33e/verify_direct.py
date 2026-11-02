"""Independent, orbit-free exact four-round recursion on GP(n,2), 5<=n<=16.

The recursion stores full ordered vertex tuples, and uses graph edge sets
rather than cyclic tuple normalization. Executable with the standard library.
"""

from functools import lru_cache

TYPE_KEYS = [dict() for _ in range(5)]


def root_type(n: int) -> int:
    assert n >= 5
    vertices = tuple(range(2 * n))
    edges = set()
    for index in range(n):
        edges.add(frozenset((index, (index + 1) % n)))
        edges.add(frozenset((n + index, n + (index + 2) % n)))
        edges.add(frozenset((index, n + index)))

    def atomic(vertices_selected: tuple[int, ...]) -> tuple[tuple[bool, bool], ...]:
        facts = []
        for j in range(len(vertices_selected)):
            for i in range(j):
                x, y = vertices_selected[i], vertices_selected[j]
                facts.append((x == y, x != y and frozenset((x, y)) in edges))
        return tuple(facts)

    @lru_cache(maxsize=None)
    def get_type(selected: tuple[int, ...]) -> int:
        rounds = 4 - len(selected)
        if rounds == 0:
            key = (atomic(selected),)
        else:
            key = (atomic(selected), frozenset(get_type(selected + (z,)) for z in vertices))
        interner = TYPE_KEYS[rounds]
        if key not in interner:
            interner[key] = len(interner)
        return interner[key]

    return get_type(())


def main() -> None:
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 6, 8, 9, 9]
    obtained = [root_type(n) for n in range(5, 17)]
    assert obtained == expected, (obtained, expected)
    for n, label in zip(range(5, 17), obtained):
        print(f'n={n:2d} rank4_type={label:2d}')
    print('INDEPENDENT_DIRECT_ENUMERATION_OK: orbit-free agreement n=5..16')


if __name__ == '__main__':
    main()
