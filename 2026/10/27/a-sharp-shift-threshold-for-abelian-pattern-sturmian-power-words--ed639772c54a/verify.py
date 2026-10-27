#!/usr/bin/env python3
"""Finite checks for affine-geometric additive incidence graphs.
Only confirms finite cases; the infinite claim uses the accompanying proof.
"""

def contains_cycle(sums):
    """Independent union-find for all graph edges with prescribed finite sums."""
    if not sums: return False
    m = max(sums)
    parent = list(range(2 * (m + 1)))
    size = [1] * len(parent)
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for s in sorted(sums):
        for x in range(s + 1):
            a, b = find(x), find(m + 1 + s - x)
            if a == b:
                return True
            if size[a] < size[b]: a, b = b, a
            parent[b] = a
            size[a] += size[b]
    return False

def proposed_cycle(base, offset):
    threshold = base * (base - 2)
    assert offset >= threshold
    t = offset - threshold
    step = base - 1
    vertices = [('L', t + base * step)]
    for j in range(base + 1):
        vertices.append(('R', j * step))
        if j < base:
            vertices.append(('L', t + (base - j - 1) * step))
    # The last vertex is R_b. The closing edge to the first is sum b^2+offset.
    assert len(vertices) == 2 * base + 2
    assert len(set(vertices)) == len(vertices)
    allowable = {1 + offset, base + offset, base * base + offset}
    for i, v in enumerate(vertices):
        w = vertices[(i + 1) % len(vertices)]
        assert v[0] != w[0]
        assert v[1] + w[1] in allowable, (base,offset,i,v,w,allowable)
    return vertices


def run():
    count = 0
    for base in range(2, 10):
        threshold = base * (base - 2)
        for offset in range(0, 3 * base * base + 1):
            observed = contains_cycle([1 + offset, base + offset, base * base + offset])
            predicted = offset >= threshold
            assert observed == predicted, (base, offset, observed, predicted)
            count += 1
        for offset in range(max(0, threshold)):
            assert not contains_cycle([base**i + offset for i in range(5)]), (base,offset)
            count += 1
    print('FINITE_FOREST_CASES_OK',count)
    for base in range(2, 40):
        for offset in (base * (base - 2), base * (base - 2) + 1, base * (base - 2) + 123):
            c = proposed_cycle(base, offset)
            assert len(c) == 2 * base + 2
    print('CYCLE_FORMULAS_OK',38 * 3)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
