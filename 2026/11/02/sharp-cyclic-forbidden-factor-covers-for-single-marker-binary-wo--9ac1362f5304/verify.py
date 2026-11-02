"""Independent checks for sparse single-forbidden-factor circular covering."""
from collections import deque, Counter
from itertools import product


def shortest_bridge(n, forbidden):
    """Breadth-first search in the actual surviving de Bruijn edge graph."""
    m = n - 1
    mask = (1 << m) - 1
    source, target = forbidden >> 1, forbidden & mask
    q = deque([(source, 0)])
    seen = {source}
    while q:
        node, depth = q.popleft()
        if depth > 0 and node == target:
            return depth
        for bit in (0, 1):
            edge = (node << 1) | bit
            if edge == forbidden:
                continue
            head = edge & mask
            if head not in seen:
                seen.add(head)
                q.append((head, depth + 1))
    return None


def sparse_bridge(n, i):
    """Mathematically proposed unique shortest repair string, not BFS-derived."""
    j = n - 1 - i
    source = '0' * i + '1' + '0' * (j - 1)
    if i == j:
        return source, '1' + '0' * i
    return source, '1' + '0' * (i - 1) + '1' + '0' * j


def eulerian_circular_cover(n, forbidden, bridge_first, append):
    """Construct an Euler tour after adding the certified repair edges."""
    mask = (1 << (n - 1)) - 1
    adj = [[] for _ in range(1 << (n - 1))]
    for edge in range(1 << n):
        if edge != forbidden:
            adj[edge >> 1].append(edge)
    repair = bridge_first + append
    expected = []
    for k in range(len(append)):
        edge = int(repair[k:k + n], 2)
        assert edge != forbidden
        adj[edge >> 1].append(edge)
        expected.append(edge)
    start = forbidden >> 1
    stack = [(start, None)]
    tour = []
    while stack:
        node = stack[-1][0]
        if adj[node]:
            edge = adj[node].pop()
            stack.append((edge & mask, edge))
        else:
            _v, edge = stack.pop()
            if edge is not None:
                tour.append(edge)
    tour.reverse()
    assert len(tour) == (1 << n) - 1 + len(append)
    assert tour and (tour[0] >> 1) == start
    for a, b in zip(tour, tour[1:] + tour[:1]):
        assert (a & mask) == (b >> 1)
    word = ''.join(str(e & 1) for e in tour)
    observed = Counter(int(''.join(word[(q + r) % len(word)] for r in range(n)), 2)
                       for q in range(len(word)))
    truth = Counter({x: 1 for x in range(1 << n) if x != forbidden})
    truth.update(expected)
    assert observed == truth
    return word


def brute_cycles(n, forbidden, length):
    """Literal circular-window search, restricted to small cases."""
    count = 0
    required = set(range(1 << n)) - {forbidden}
    for bits in product((0, 1), repeat=length):
        if bits[0] != 0:
            continue
        factors = set()
        for start in range(length):
            a = 0
            for offset in range(n):
                a = (a << 1) | bits[(start + offset) % length]
            factors.add(a)
        if forbidden not in factors and required <= factors:
            count += 1
    return count


def verify():
    cases = 0
    reconstructed_words = 0
    for n in range(3, 13):
        for i in range(n):
            forbidden = 1 << (n - 1 - i)
            delta = shortest_bridge(n, forbidden)
            if i in (0, n - 1):
                assert delta is None, (n, i, delta)
                continue
            predicted = (n + 1) // 2 if n % 2 == 1 and i == (n - 1) // 2 else n
            assert delta == predicted, (n, i, delta, predicted)
            source, suffix = sparse_bridge(n, i)
            assert len(suffix) == predicted
            tail = source + suffix
            assert tail[-(n - 1):] == '0' * (i - 1) + '1' + '0' * (n - 1 - i)
            assert all(int(tail[k:k+n], 2) != forbidden for k in range(len(suffix)))
            word = eulerian_circular_cover(n, forbidden, source, suffix)
            assert len(word) == (1 << n) - 1 + predicted
            cases += 1
            reconstructed_words += len(word)
    # This brute force does not assume any Euler/postman model; it compares
    # actual length-three circular windows at the boundary length.
    assert brute_cycles(3, 0b010, 8) == 0
    assert brute_cycles(3, 0b010, 9) > 0
    # An independent brute-force check one order higher, for both orientations.
    for f in (0b0100, 0b0010):
        assert brute_cycles(4, f, 18) == 0
        assert brute_cycles(4, f, 19) > 0
    for n in range(3, 8):
        for i in (0, n - 1):
            forbidden = 1 << (n - 1 - i)
            assert shortest_bridge(n, forbidden) is None
    print('VERIFY_OK', 'orders=3..12', 'interior_cases=', cases,
          'total_constructed_symbols=', reconstructed_words,
          'literal_exhaustion_n3=8,9_n4=18,19')


if __name__ == '__main__':
    verify()
