from itertools import combinations


def subsets(n):
    for r in range(n + 1):
        for s in combinations(range(n), r):
            yield s


def all_words(n):
    return [format(x, f"0{n}b") for x in range(2**n)]


def construct(n, M):
    if n == 1:
        if M == 1:
            base = ["0"]
        else:
            base = ["0", "1"]
    elif n == 2:
        if M == 1:
            base = ["00"]
        elif M == 2:
            base = ["00", "11"]
        elif M == 3:
            base = ["00", "01", "10"]
        else:
            base = all_words(2)
    elif n == 3:
        if M == 1:
            base = ["000"]
        elif M == 2:
            base = ["000", "111"]
        elif M == 3:
            base = ["000", "011", "101"]
        elif M >= 4:
            parity = ["000", "011", "101", "110"]
            if M <= 8:
                rest = [w for w in all_words(3) if w not in parity]
                base = parity + rest[: M - 4]
            else:
                base = all_words(3)
        else:
            raise AssertionError
    else:
        raise ValueError("n must be 1, 2, or 3")

    if len(base) < M:
        base = base + [base[i % len(base)] for i in range(M - len(base))]
    return base[:M]


def projection_count(code, S):
    return len({tuple(word[i] for i in S) for word in code})


for n in (1, 2, 3):
    for M in range(1, 65):
        code = construct(n, M)
        assert len(code) == M
        for S in subsets(n):
            got = projection_count(code, S)
            want = min(M, 2 ** len(S))
            assert got == want, (n, M, S, got, want, code)

print("VERIFY_OK")
