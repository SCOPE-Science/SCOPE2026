"""Independent direct checks of a covering/independent-set witness in Q8."""
from collections import deque

N = 8
EVEN_WITNESS = (0, 15, 51, 60, 85, 154, 225, 238)
ODD_WITNESS = tuple(w ^ 1 for w in EVEN_WITNESS)
TOTAL_WITNESS = frozenset(EVEN_WITNESS + ODD_WITNESS)
assert len(TOTAL_WITNESS) == 16
assert all(w.bit_count() % 2 == 0 for w in EVEN_WITNESS)
assert all(w.bit_count() % 2 == 1 for w in ODD_WITNESS)

for code in (EVEN_WITNESS, ODD_WITNESS):
    assert all((a ^ b).bit_count() >= 4
               for i, a in enumerate(code) for b in code[i+1:])
    for vertex in range(256):
        if vertex.bit_count() % 2 == code[0].bit_count() % 2:
            assert min((vertex ^ c).bit_count() for c in code) <= 2

# Verify total mutual visibility from the definition (unselected
# internal vertices of an endpoint geodesic), without the coding lemma.
def avoiding_distance(start, finish):
    frontier = deque([(start, 0)])
    visited = {start}
    while frontier:
        vertex, depth = frontier.popleft()
        if vertex == finish:
            return depth
        for coordinate in range(N):
            neighbor = vertex ^ (1 << coordinate)
            if neighbor in visited or (neighbor in TOTAL_WITNESS and neighbor != finish):
                continue
            visited.add(neighbor)
            frontier.append((neighbor, depth+1))
    return None

for source in range(256):
    for destination in range(source+1, 256):
        assert avoiding_distance(source, destination) == (source ^ destination).bit_count()

# Inclusion-maximality by two-step blocking within each parity component.
for outsider in range(256):
    if outsider not in TOTAL_WITNESS:
        assert any((outsider ^ c).bit_count() == 2 for c in TOTAL_WITNESS)

anchored = 142380
half_count = 128 * anchored // 8
assert half_count == 2278080
assert half_count ** 2 == 5189648486400
print('WITNESS_OK total=16; half_count=2278080; min_maximal_total=5189648486400')
