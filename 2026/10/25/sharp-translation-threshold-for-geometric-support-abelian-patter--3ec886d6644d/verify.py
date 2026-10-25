"""Finite exact diagnostics for the translated geometric-support forest theorem.
The proof is mathematical; this program checks finite prefixes only.
"""


def forest(prefix):
    parent = {}
    size = {}

    def root(vertex):
        if vertex not in parent:
            parent[vertex] = vertex
            size[vertex] = 1
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    for total in prefix:
        for left in range(total + 1):
            a = root((0, left))
            b = root((1, total - left))
            if a == b:
                return False
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
    return True


def explicit_cycle(base, offset):
    # Distinct alternating left/right vertices of a 2(base+1)-cycle.
    gap = base - 1
    initial = base**0 + offset
    first = base + offset
    second = base * base + offset
    left = [i * gap for i in range(base + 1)]
    right = [initial - i * gap for i in range(base)] + [first]
    assert min(left) >= 0 and min(right) >= 0
    assert len(set(left)) == base + 1
    assert len(set(right)) == base + 1
    for i in range(base):
        assert left[i] + right[i] == initial
        assert left[i + 1] + right[i] == first
    assert left[-1] + right[-1] == second
    assert left[0] + right[-1] == first
    return True


def main():
    checks = 0
    for base in range(2, 9):
        boundary = base * (base - 2)
        for offset in range(-1, boundary + 9):
            expected = offset < boundary
            # Exhaust all edges in the first four diagonal matchings.
            totals = [base**j + offset for j in range(4)]
            observed = forest(totals)
            assert observed == expected, (base, offset, observed, expected)
            checks += 1
            if not expected:
                assert explicit_cycle(base, offset)
                checks += 1
        for j in range(1, 10):
            offset = boundary - 1
            assert base**(j + 1) + offset > 2 * (base**j + offset)
            checks += 1
        assert forest([1 + (-1), base + (-1)])
        checks += 1
    print(f"PASS: {checks} exact tests of finite forest status, explicit cycles and growth bounds")
    print("NOTE: finite tests do not establish the infinite theorem; see RESULT.md proof.")


if __name__ == "__main__":
    main()
