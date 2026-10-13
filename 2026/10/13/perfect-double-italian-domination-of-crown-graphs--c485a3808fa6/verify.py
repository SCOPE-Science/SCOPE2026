from math import comb

def bounded_vectors(length, max_value=3, max_sum=6):
    vec = [0] * length
    def rec(i, remaining):
        if i == length:
            yield tuple(vec)
            return
        for x in range(min(max_value, remaining) + 1):
            vec[i] = x
            yield from rec(i + 1, remaining - x)
    for total in range(max_sum + 1):
        yield from rec_exact(vec, 0, total, max_value)

def rec_exact(vec, i, remaining, max_value):
    if i == len(vec):
        if remaining == 0:
            yield tuple(vec)
        return
    for x in range(min(max_value, remaining) + 1):
        vec[i] = x
        yield from rec_exact(vec, i + 1, remaining - x, max_value)

def is_pdidf(n, lab):
    A = lab[:n]
    B = lab[n:]
    X = sum(A)
    Y = sum(B)
    for i in range(n):
        x, y = A[i], B[i]
        if x <= 1:
            s = x + Y - y
            if not (3 <= s <= 4):
                return False
        if y <= 1:
            s = y + X - x
            if not (3 <= s <= 4):
                return False
    return True

def predicted(n, lab):
    if sum(lab) != 6:
        return False
    A = lab[:n]
    B = lab[n:]
    return A == B and sum(A) == 3

print("VERIFY_OK")
checked = 0
minimum_functions = 0
for n in range(4, 11):
    feasible_le6 = []
    for lab in rec_exact([0]*(2*n), 0, 6, 3):
        checked += 1
        if is_pdidf(n, lab):
            feasible_le6.append(lab)
    # Check all smaller weights separately.
    for weight in range(6):
        for lab in rec_exact([0]*(2*n), 0, weight, 3):
            checked += 1
            assert not is_pdidf(n, lab), (n, weight, lab)

    expected = {lab for lab in feasible_le6 if predicted(n, lab)}
    assert len(feasible_le6) == comb(n+2, 3), (n, len(feasible_le6), comb(n+2,3))
    assert set(feasible_le6) == expected, (n, len(feasible_le6), len(expected))
    minimum_functions += len(feasible_le6)
    print(f"n={n}: gamma_p_dI=6, minimum_functions={len(feasible_le6)}")

print("bounded_labelings_checked =", checked)
print("minimum_functions_checked =", minimum_functions)
print("all minima matched identical side-vectors of side weight 3")
