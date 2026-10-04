from fractions import Fraction

def condat(y, a):
    y = [Fraction(v) for v in y]
    a = Fraction(a)
    v = [y[0]]
    buf = []
    rho = y[0] - a
    for yn in y[1:]:
        if yn > rho:
            rho = rho + (yn - rho) / Fraction(len(v) + 1)
            if rho > yn - a:
                v.append(yn)
            else:
                buf.extend(v)
                v = [yn]
                rho = yn - a
    if buf:
        for yy in buf:
            if yy > rho:
                v.append(yy)
                rho = rho + (yy - rho) / Fraction(len(v))
    start_size = len(v)
    tests = 0
    pass_sizes = []
    while True:
        before = len(v)
        pass_sizes.append(before)
        snapshot = list(v)
        for yy in snapshot:
            if yy not in v:
                continue
            tests += 1
            if yy <= rho:
                v.remove(yy)
                rho = rho + (rho - yy) / Fraction(len(v))
        if len(v) == before:
            break
    return start_size, len(v), tests, pass_sizes, rho

def family(N, K):
    H = Fraction(4 * N * N)
    d = N - K
    if d == 0:
        y = [H] * N
        return y, sum(y)
    r = [Fraction(0), Fraction(1, N - 1)]
    z = [Fraction(-1)]
    for q in range(1, d):
        zq = (r[q - 1] + r[q]) / 2
        z.append(zq)
        r.append(r[q] + (r[q] - zq) / Fraction(N - q - 1))
    y = [None] * N
    for q, zq in enumerate(z):
        y[d - 1 - q] = zq
    for i in range(d, N):
        y[i] = H
    return y, sum(y)

for N in range(2, 31):
    for K in range(2, N + 1):
        y, a = family(N, K)
        start, final_k, tests, sizes, rho = condat(y, a)
        target = (N * (N + 1) - (K - 1) * K) // 2
        assert start == N, (N, K, "start", start)
        assert final_k == K, (N, K, "support", final_k)
        assert tests == target, (N, K, "tests", tests, target)
        assert sizes == list(range(N, K - 1, -1)), (N, K, sizes)

singleton_examples = [
    ([Fraction(5), Fraction(0), Fraction(-2)], Fraction(1)),
    ([Fraction(-3), Fraction(10), Fraction(1), Fraction(2)], Fraction(2)),
    ([Fraction(0), Fraction(0), Fraction(9), Fraction(-1), Fraction(1)], Fraction(3)),
]
for y, a in singleton_examples:
    start, final_k, tests, sizes, rho = condat(y, a)
    assert final_k == 1
    assert start == 1
    assert tests == 1
    assert sizes == [1]

print("VERIFY_OK")
