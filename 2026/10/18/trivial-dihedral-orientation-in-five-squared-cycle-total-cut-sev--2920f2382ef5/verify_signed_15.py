"""Independent signed fixed-simplex Lefschetz check for the n=15, k=4 case.
Run: python3 verify_signed_15.py
"""
from itertools import combinations

n, k = 15, 4
facets = []
for subset in combinations(range(n), k):
    if all(min((u-v) % n, (v-u) % n) > 2 for u, v in combinations(subset, 2)):
        facets.append(set(range(n)) - set(subset))
assert len(facets) == 75
faces = [s for bits in range(1 << n)
         if any(all(not (bits >> v & 1) for v in range(n) if v not in f)
                for f in facets)
         for s in [tuple(i for i in range(n) if (bits >> i) & 1)]]
assert len(faces) == 22547


def reduced_lefschetz(slope, shift):
    total = -1   # augmented empty-simplex term; independent of group element
    for face in faces:
        if not face:
            continue
        mapped = [(slope * i + shift) % n for i in face]
        if sorted(mapped) != list(face):
            continue
        inv = sum(mapped[i] > mapped[j]
                  for i in range(len(mapped)) for j in range(i+1, len(mapped)))
        total += (-1)**(len(face)-1+inv)
    return total


for sign in (1, -1):
    for shift in range(n):
        assert reduced_lefschetz(sign, shift) == -1, (sign, shift)
print("INDEPENDENT_SIGNED_CHECK_OK 30 dihedral elements, reduced Lefschetz -1")
