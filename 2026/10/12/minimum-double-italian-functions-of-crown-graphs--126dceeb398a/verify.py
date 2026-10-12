from itertools import product

def is_didf(n, lab):
    A = lab[:n]
    B = lab[n:]
    X, Y = sum(A), sum(B)
    for i in range(n):
        x, y = A[i], B[i]
        if x <= 1 and x + Y - y < 3:
            return False
        if y <= 1 and y + X - x < 3:
            return False
    return True

def predicted_minima(n):
    out = set()
    for A in product(range(4), repeat=n):
        if sum(A) == 3:
            out.add(tuple(A + A))
    return out

total = 0
print("VERIFY_OK")
for n in range(2, 6):
    best = 10**9
    mins = []
    for lab in product(range(4), repeat=2*n):
        total += 1
        w = sum(lab)
        if w > best:
            continue
        if is_didf(n, lab):
            if w < best:
                best = w
                mins = []
            mins.append(tuple(lab))
    if n >= 4:
        exp = predicted_minima(n)
        assert best == 6, (n, best)
        assert set(mins) == exp, (n, len(mins), len(exp), set(mins)^exp)
        assert len(mins) == (n+2)*(n+1)*n//6
    print(f"n={n}: gamma_dI={best}, minimum_functions={len(mins)}")
print("quaternary_labelings_checked =", total)
print("for n=4,5 all minima matched identical-side compositions of total side weight 3")
