from itertools import combinations

def pfaffian(A, idx):
    idx = tuple(idx)
    if not idx:
        return 1
    if len(idx) % 2:
        return 0
    i = idx[0]
    total = 0
    for pos in range(1, len(idx)):
        j = idx[pos]
        rest = idx[1:pos] + idx[pos+1:]
        sign = 1 if pos % 2 == 1 else -1
        total += sign * A[i][j] * pfaffian(A, rest)
    return total

def block_edges(a, b):
    return {(i, j) for i in range(a, b+1) for j in range(i+1, b+1)}

def coordinate_matrix(n, edge):
    A = [[0 for _ in range(n)] for _ in range(n)]
    i, j = edge
    A[i][j] = 1
    A[j][i] = -1
    return A

def survives_bruteforce(n, edge, blocks):
    A = coordinate_matrix(n, edge)
    for a, b, t in blocks:
        size = 2 * t
        verts = list(range(a, b+1))
        if size > len(verts):
            continue
        for U in combinations(verts, size):
            if pfaffian(A, U) != 0:
                return False
    return True

cases = coordinate_checks = pfaffian_checks = 0

for n in range(4, 11):
    # Deterministic family of monotone interval collections.
    candidates = []
    for a1 in range(0, n-1):
        for b1 in range(a1+1, n):
            candidates.append([(a1, b1)])
            if b1 + 1 < n:
                candidates.append([(a1, b1), (a1+1, min(n-1, b1+1))])
            if a1 + 2 < n:
                candidates.append([(a1, b1), (a1+2, n-1)])

    for intervals in candidates[:80]:
        # Two threshold patterns for each ladder: one with possible linear blocks,
        # one with all genuinely higher Pfaffians whenever the block size permits.
        patterns = []
        mixed = []
        nonlinear = []
        for q, (a, b) in enumerate(intervals):
            max_t = max(1, (b-a+1)//2)
            mixed.append(1 if q % 2 == 0 else min(2, max_t))
            nonlinear.append(min(2, max_t))
        patterns.append(mixed)
        patterns.append(nonlinear)

        for ts in patterns:
            blocks = [(a, b, t) for (a, b), t in zip(intervals, ts)]
            Y = set()
            killed = set()
            for a, b, t in blocks:
                E = block_edges(a, b)
                Y |= E
                if t == 1:
                    killed |= E

            expected_survivors = Y - killed
            actual_survivors = set()
            for edge in Y:
                ok = survives_bruteforce(n, edge, blocks)
                if ok:
                    actual_survivors.add(edge)
                coordinate_checks += 1

                # Independently verify every higher Pfaffian vanishes at the coordinate point.
                A = coordinate_matrix(n, edge)
                for a, b, t in blocks:
                    if t >= 2 and 2*t <= b-a+1:
                        for U in combinations(range(a, b+1), 2*t):
                            assert pfaffian(A, U) == 0
                            pfaffian_checks += 1

            assert actual_survivors == expected_survivors
            cases += 1

print("VERIFY_OK", cases, coordinate_checks, pfaffian_checks)
