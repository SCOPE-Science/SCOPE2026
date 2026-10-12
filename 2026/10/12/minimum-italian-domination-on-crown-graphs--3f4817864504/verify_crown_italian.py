from itertools import product

def italian_ok(n, lab):
    A = lab[:n]
    B = lab[n:]
    for i in range(n):
        if A[i] == 0 and sum(B[j] for j in range(n) if j != i) < 2:
            return False
        if B[i] == 0 and sum(A[j] for j in range(n) if j != i) < 2:
            return False
    return True

def expected(n):
    gamma = 3 if n == 3 else 4
    count = {2: 9, 3: 2, 4: 12}.get(n, n * (n + 1) // 2)
    return gamma, count

total = 0
summaries = []
for n in range(2, 7):
    best = 10**9
    count = 0
    tested = 0
    for lab in product(range(3), repeat=2*n):
        tested += 1
        w = sum(lab)
        if w > best:
            continue
        if italian_ok(n, lab):
            if w < best:
                best, count = w, 1
            elif w == best:
                count += 1
    total += tested
    eg, ec = expected(n)
    assert (best, count) == (eg, ec), (n, best, count, eg, ec)
    summaries.append(f"{n}:{best}/{count}")

print("ALL CHECKS PASSED; n_range=2..6; exhaustive_labelings="
      + str(total) + "; minima=(" + ",".join(summaries) + ")")
