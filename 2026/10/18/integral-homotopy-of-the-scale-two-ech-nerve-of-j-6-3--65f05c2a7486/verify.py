#!/usr/bin/env python3
"""Exact finite verification of the radius-one closed-ball nerve of J(6,3)."""
from collections import Counter, deque
from itertools import combinations


def vertices():
    return list(combinations(range(6), 3))


def face_data():
    verts = vertices()
    closed = []
    for a in verts:
        closed.append(sum(1 << j for j, b in enumerate(verts)
                          if len(set(a).intersection(b)) >= 2))
    faces = set()
    for neighborhood in closed:
        face = neighborhood
        while face:
            faces.add(face)
            face = (face - 1) & neighborhood
    # An independently phrased membership test from common centers.
    center_mask = [sum(1 << j for j, c in enumerate(closed)
                       if c & (1 << i)) for i in range(20)]
    common = [0] * (1 << 20)
    common[0] = (1 << 20) - 1
    count = 0
    for face in range(1, 1 << 20):
        low = face & -face
        common[face] = common[face ^ low] & center_mask[low.bit_length() - 1]
        present = common[face] != 0
        assert present == (face in faces), 'inconsistent face enumeration'
        count += present
    assert count == len(faces)
    return faces, closed


def boundary(face):
    """Exact signed simplicial boundary of an oriented increasing face."""
    ix = 0
    remaining = face
    while remaining:
        low = remaining & -remaining
        yield face ^ low, (-1 if ix & 1 else 1)
        ix += 1
        remaining ^= low


def matching_data(faces):
    remaining = set(faces)
    lower_to_upper, upper_to_lower = {}, {}
    stage_counts = []
    for j in range(20):
        bit = 1 << j
        remove = set()
        for lo in remaining:
            hi = lo | bit
            if not (lo & bit) and hi in remaining:
                assert lo not in lower_to_upper and hi not in upper_to_lower
                lower_to_upper[lo] = hi
                upper_to_lower[hi] = lo
                remove.add(lo)
                remove.add(hi)
        remaining.difference_update(remove)
        stage_counts.append(len(remove) // 2)
    assert 2 * len(lower_to_upper) + len(remaining) == len(faces)
    return lower_to_upper, upper_to_lower, remaining, stage_counts


def acyclic(faces, lower_to_upper):
    """Explicitly topologically sort every oriented face-poset cover relation."""
    indegree = {f: 0 for f in faces}
    covers = 0
    for upper in faces:
        for lower, _ in boundary(upper):
            if lower not in faces:
                continue
            covers += 1
            if lower_to_upper.get(lower) == upper:
                indegree[upper] += 1  # matched cover points upward
            else:
                indegree[lower] += 1  # ordinary cover points downward
    q = deque(f for f, degree in indegree.items() if degree == 0)
    processed = 0
    while q:
        face = q.popleft()
        processed += 1
        if face in lower_to_upper:
            neighbor = lower_to_upper[face]
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
        for lo, _ in boundary(face):
            if lo in faces and lower_to_upper.get(lo) != face:
                indegree[lo] -= 1
                if indegree[lo] == 0:
                    q.append(lo)
    assert processed == len(faces), (processed, len(faces))
    return covers


def morse_boundary(crit, lower_to_upper, upper_to_lower):
    c3 = sorted(f for f in crit if f.bit_count() == 4)
    c4 = sorted(f for f in crit if f.bit_count() == 5)
    basis = {f: j for j, f in enumerate(c3)}
    cache, visiting = {}, set()

    def normal(form):
        if form in cache:
            return cache[form]
        if form in basis:
            return {basis[form]: 1}
        if form in upper_to_lower:
            return {}
        assert form in lower_to_upper, 'unclassified Morse face'
        assert form not in visiting, 'cyclic gradient expansion'
        visiting.add(form)
        upper = lower_to_upper[form]
        coefficient = dict(boundary(upper))[form]
        result = Counter()
        for other, sign in boundary(upper):
            if other == form:
                continue
            for j, amount in normal(other).items():
                result[j] -= coefficient * sign * amount
        visiting.remove(form)
        out = {j: amount for j, amount in result.items() if amount}
        cache[form] = out
        return out

    columns = []
    for cell in c4:
        image = Counter()
        for facet, sign in boundary(cell):
            for j, amount in normal(facet).items():
                image[j] += sign * amount
        columns.append({j: amount for j, amount in image.items() if amount})
    assert not any(columns), 'a nonzero integral Morse attaching degree'
    return len(c3), len(c4), len(cache)


def main():
    faces, closed = face_data()
    face_counts = Counter(f.bit_count() - 1 for f in faces)
    assert len(closed) == 20
    assert all(x.bit_count() == 10 for x in closed)
    assert len(faces) == 16140
    assert [face_counts.get(i, 0) for i in range(10)] == [20,180,960,2850,4500,4110,2400,900,200,20]
    low_up, up_low, crit, stages = matching_data(faces)
    assert len(low_up) == 8049
    critical_counts = Counter(x.bit_count() - 1 for x in crit)
    assert critical_counts == {0: 1, 3: 11, 4: 30}
    covers = acyclic(faces, low_up)
    a, b, cache_size = morse_boundary(crit, low_up, up_low)
    euler = sum((-1) ** i * face_counts[i] for i in range(10))
    assert euler == 20 and euler - 1 == b - a == 19
    print('VERIFY_OK faces=%d covers=%d matched_pairs=%d critical=(1,11,30) '
          'integer_Morse_d4=zero EULER_reduced=19 memoized_three_faces=%d' %
          (len(faces), covers, len(low_up), cache_size))
    print('stage_match_counts=' + ','.join(map(str, stages)))


if __name__ == '__main__':
    main()
