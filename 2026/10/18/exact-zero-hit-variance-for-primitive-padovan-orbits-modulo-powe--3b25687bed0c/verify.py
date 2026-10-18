"""Independent finite checks of the Padovan primitive-orbit zero-hit moments."""
from collections import Counter

def multiply(A, B, modulus=None):
    n = len(A)
    entries = [[sum(A[i][r] * B[r][j] for r in range(n)) for j in range(n)] for i in range(n)]
    if modulus is not None:
        return [[v % modulus for v in row] for row in entries]
    return entries

def power(A, e, modulus=None):
    R = [[int(i == j) for j in range(len(A))] for i in range(len(A))]
    while e:
        if e & 1:
            R = multiply(R, A, modulus)
        A = multiply(A, A, modulus)
        e //= 2
    return R

Q = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
I = [[int(i == j) for j in range(3)] for i in range(3)]
B = [[0, 1, 1], [1, 1, 1], [1, 2, 1]]
C = [[2, 4, 3], [3, 5, 4], [4, 7, 5]]
assert power(Q, 7) == [[I[i][j] + 2 * B[i][j] for j in range(3)] for i in range(3)]
assert power(Q, 14) == [[I[i][j] + 4 * C[i][j] for j in range(3)] for i in range(3)]
def det(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
assert det(B) == det(C) == 1

for k in range(1, 10):
    mod = 2**k
    T = 7 * 2**(k-1)
    assert power(Q, T, mod) == I
    if k > 1:
        assert power(Q, T // 2, mod) != I
    counts = []
    for d in range(T):
        row = power(Q, d, mod)[0]
        if d == 0:
            counts.append(3 * 4**(k-1))
            continue
        h = k
        for coord in row[1:]:
            if coord:
                h = min(h, (coord & -coord).bit_length() - 1)
        expected = 0 if d % 7 else 1 + ((d // 7 & -(d // 7)).bit_length() - 1)
        assert h == expected, (k, d, h, expected)
        counts.append(2**(k + h - 1))
    N = 4**(k-1)
    assert counts[0] == 3*N
    assert sum(counts) == (k+8)*N

for k in range(1, 6):
    m = 2**k
    T = 7 * 2**(k-1)
    unseen = {(a, b, c) for a in range(m) for b in range(m) for c in range(m)
              if (a | b | c) & 1}
    hist = Counter()
    while unseen:
        seed = next(iter(unseen))
        v = seed
        visited = set()
        hits = 0
        for _ in range(T):
            assert v not in visited
            visited.add(v)
            hits += (v[0] == 0)
            v = (v[1], v[2], (v[0]+v[1])%m)
        assert v == seed
        assert visited <= unseen
        unseen.difference_update(visited)
        hist[hits] += 1
    N = 4**(k-1)
    assert sum(hist.values()) == N
    assert sum(z * multiplicity for z,multiplicity in hist.items()) == 3*N
    assert sum(z*z * multiplicity for z,multiplicity in hist.items()) == (k+8)*N
print('VERIFY_OK: two exact matrix powers; primitive orbit periods and lag ranks k<=9; brute orbit moments k<=5')
