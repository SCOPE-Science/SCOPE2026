from itertools import product

def is_tr2df(n, lab):
    A = lab[:n]
    B = lab[n:]
    X = sum(A)
    Y = sum(B)

    # Every zero vertex receives total neighboring weight at least 2.
    for i, x in enumerate(A):
        if x == 0 and Y - B[i] < 2:
            return False
    for i, y in enumerate(B):
        if y == 0 and X - A[i] < 2:
            return False

    # Positive support induces no isolated vertex.
    for i, x in enumerate(A):
        if x > 0 and not any(B[j] > 0 for j in range(n) if j != i):
            return False
    for i, y in enumerate(B):
        if y > 0 and not any(A[j] > 0 for j in range(n) if j != i):
            return False

    return True

def expected_minima(n):
    out = set()
    for i in range(n):
        for j in range(i + 1, n):
            lab = [0] * (2 * n)
            lab[i] = lab[j] = 1
            lab[n + i] = lab[n + j] = 1
            out.add(tuple(lab))
    return out

total = 0
print("VERIFY_OK")
for n in range(2, 7):
    best = 10**9
    mins = []
    for lab in product(range(3), repeat=2*n):
        total += 1
        w = sum(lab)
        if w > best:
            continue
        if is_tr2df(n, lab):
            if w < best:
                best = w
                mins = []
            mins.append(tuple(lab))
    expected = expected_minima(n)
    assert best == 4, (n, best)
    assert set(mins) == expected, (n, len(mins), len(expected), set(mins) ^ expected)
    assert len(mins) == n * (n - 1) // 2
    print(f"n={n}: gamma_tR2=4, minimum_functions={len(mins)}")

print("ternary_labelings_checked =", total)
print("all minima were identical two-index label-1 supports on the two sides")
