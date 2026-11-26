"""Enumerate and check an acyclic matching for Ind_4(GP(8,3))."""
import json
from collections import Counter, defaultdict, deque


def main():
    n = 16
    full = (1 << n) - 1
    adjacency = [set() for _ in range(n)]
    for i in range(8):
        for u, v in ((i, (i+1) % 8), (i, 8+i), (8+i, 8+(i+3) % 8)):
            adjacency[u].add(v)
            adjacency[v].add(u)
    assert all(len(v) == 3 for v in adjacency)
    connected = {1 << i for i in range(n)}
    for _ in range(4):
        connected = {a | (1 << j) for a in connected for i in range(n)
                     if (a >> i) & 1 for j in adjacency[i] if not ((a >> j) & 1)}
    faces = set(range(full + 1))
    for a in connected:
        free = full ^ a
        b = free
        while True:
            faces.discard(a | b)
            if not b:
                break
            b = (b - 1) & free

    unmatched = set(faces)
    paired = {}
    for j in (*range(15, 7, -1), *range(8)):
        bit = 1 << j
        for a in sorted(unmatched):
            if not (a & bit) and (a | bit) in unmatched:
                paired[a] = a | bit
                unmatched.remove(a)
                unmatched.remove(a | bit)
    assert len(faces) == len(unmatched) + 2*len(paired)
    assert paired[0] == (1 << 15)

    indegree = dict.fromkeys(faces, 0)
    outgoing = defaultdict(list)
    for upper in faces:
        b = upper
        while b:
            bit = b & -b
            lower = upper ^ bit
            assert lower in faces
            tail, head = (lower, upper) if paired.get(lower) == upper else (upper, lower)
            outgoing[tail].append(head)
            indegree[head] += 1
            b ^= bit
    ready = deque(a for a in faces if indegree[a] == 0)
    visited = 0
    while ready:
        a = ready.popleft()
        visited += 1
        for b in outgoing[a]:
            indegree[b] -= 1
            if not indegree[b]:
                ready.append(b)
    assert visited == len(faces) == 21973
    critical = Counter(a.bit_count()-1 for a in unmatched)
    assert critical == {7: 21}
    print(json.dumps({
        'faces_including_empty': len(faces),
        'face_incidences': sum(map(len, outgoing.values())),
        'matched_pairs_including_empty': len(paired),
        'topologically_sorted_faces': visited,
        'critical_faces_in_augmented_matching': critical,
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
