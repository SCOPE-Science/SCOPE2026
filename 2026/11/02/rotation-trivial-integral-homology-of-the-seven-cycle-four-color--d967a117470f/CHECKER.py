"""Exact finite-cell verifier for a cycle-complete-graph independence complex.

Requires Python 3 and sympy. Computes all faces, an explicit acyclic
matching on the reduced face poset, the integral Morse differential, and
rotation-fixed oriented simplices. All data are reconstructed from the graph.
"""
from collections import Counter, deque
from functools import lru_cache
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N, COLORS = 7, 4
V = N * COLORS
adj = [0] * V
for i in range(N):
    for color in range(COLORS):
        v = i * COLORS + color
        for j in ((i - 1) % N, (i + 1) % N):
            for other in range(COLORS):
                if color != other:
                    adj[v] |= 1 << (j * COLORS + other)

def bits(mask):
    while mask:
        b = mask & -mask
        mask -= b
        yield b.bit_length() - 1

all_faces = set()
def enumerate_faces(choices, mask):
    all_faces.add(mask)
    while choices:
        b = choices & -choices
        choices -= b
        v = b.bit_length() - 1
        enumerate_faces(choices & ~adj[v], mask | b)
enumerate_faces((1 << V) - 1, 0)
assert len(all_faces) == 36069
face_counts = Counter(x.bit_count() for x in all_faces)
assert tuple(face_counts[i] for i in range(13)) == (
    1, 28, 294, 1512, 4291, 7420, 8680, 7228,
    4270, 1764, 490, 84, 7)

remaining = set(all_faces)
lower_to_upper, upper_to_lower = {}, {}
for v in range(V):
    bit = 1 << v
    lows = [m for m in remaining if not m & bit and m | bit in remaining]
    for low in lows:
        high = low | bit
        remaining.remove(low)
        remaining.remove(high)
        lower_to_upper[low] = high
        upper_to_lower[high] = low
assert len(lower_to_upper) == 18024
critical_three = sorted(m for m in remaining if m.bit_count() == 4)
critical_four = sorted(m for m in remaining if m.bit_count() == 5)
assert len(remaining) == 21 and len(critical_three) == 9 and len(critical_four) == 12

# The complete matched Hasse graph must be acyclic, not merely plausible.
arcs = {m: [] for m in all_faces}
indegree = {m: 0 for m in all_faces}
for low in all_faces:
    for v in bits(((1 << V) - 1) ^ low):
        high = low | (1 << v)
        if high not in all_faces:
            continue
        src, dst = (low, high) if lower_to_upper.get(low) == high else (high, low)
        arcs[src].append(dst)
        indegree[dst] += 1
queue = deque(m for m in all_faces if indegree[m] == 0)
visited = 0
while queue:
    m = queue.popleft()
    visited += 1
    for other in arcs[m]:
        indegree[other] -= 1
        if indegree[other] == 0:
            queue.append(other)
assert visited == len(all_faces)

index = {m: i for i, m in enumerate(critical_three)}
@lru_cache(None)
def reduced_face(face):
    """Integral algebraic-Morse reduction of a three-face to critical cells."""
    if face in index:
        return {index[face]: 1}
    if face in upper_to_lower:
        return {}
    assert face in lower_to_upper
    upper = lower_to_upper[face]
    pivot = (upper ^ face).bit_length() - 1
    pivot_sign = (-1) ** (face & ((1 << pivot) - 1)).bit_count()
    answer = Counter()
    for j, w in enumerate(bits(upper)):
        if w == pivot:
            continue
        for idx, val in reduced_face(upper ^ (1 << w)).items():
            answer[idx] -= pivot_sign * ((-1) ** j) * val
    return {idx: val for idx, val in answer.items() if val}

morse_boundary = []
for upper in critical_four:
    row = Counter()
    for j, w in enumerate(bits(upper)):
        for idx, val in reduced_face(upper ^ (1 << w)).items():
            row[idx] += ((-1) ** j) * val
    morse_boundary.append([row.get(i, 0) for i in range(len(critical_three))])
A = Matrix(morse_boundary)
assert A.rank() == 6
D = smith_normal_form(A, domain=ZZ)
assert [abs(int(D[i, i])) for i in range(min(D.shape))] == [1]*6 + [0]*3

# Every nonidentity cyclic rotation has exactly four invariant simplices,
# one seven-vertex simplex per color. A seven-cycle has even orientation.
for step in range(1, N):
    def rotate(mask):
        ans = 0
        for v in bits(mask):
            i, color = divmod(v, COLORS)
            ans |= 1 << (((i + step) % N) * COLORS + color)
        return ans
    fixed = [mask for mask in all_faces if rotate(mask) == mask]
    assert len(fixed) == 5 and {m.bit_count() for m in fixed} == {0, 7}
    for mask in fixed:
        if not mask:
            continue
        positions = list(bits(mask))
        induced = [positions.index(((v // COLORS + step) % N)*COLORS + v % COLORS)
                   for v in positions]
        inversions = sum(induced[i] > induced[j]
                         for i in range(len(induced)) for j in range(i + 1, len(induced)))
        assert inversions % 2 == 0

print('C7_K4_ROTATION_INTEGRAL_MORSE_OK')
print('faces=36069 matched_pairs=18024 critical_dim3=9 critical_dim4=12')
print('morse_smith=1,1,1,1,1,1,0,0,0')
print('homology_dim3=3 dim4=6 fixed_rotated_simplices=4 reduced_lefschetz=3')
