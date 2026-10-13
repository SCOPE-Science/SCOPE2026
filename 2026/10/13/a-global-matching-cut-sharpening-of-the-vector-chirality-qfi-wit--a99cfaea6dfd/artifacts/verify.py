def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None:
        cap = n
    for x in range(min(cap, n), 0, -1):
        for rest in partitions(n - x, x):
            yield (x,) + rest

def relaxed_value(N, block_sizes):
    m = max(block_sizes)
    cross_incidence_bound = N if 2 * m <= N else 2 * (N - m)
    return sum(x * x for x in block_sizes) + cross_incidence_bound

def claimed(N, k):
    q, s = divmod(N, k)
    return q * k * k + s * s + N - max(0, 2 * k - N)

for N in range(4, 32, 2):
    all_parts = list(partitions(N))
    for k in range(1, N + 1):
        feasible = [p for p in all_parts if max(p) <= k]
        exact_relaxation = max(relaxed_value(N, p) for p in feasible)
        want = claimed(N, k)
        assert exact_relaxation == want, (N, k, exact_relaxation, want)

        q, s = divmod(N, k)
        source = q * k * k + s * s + N
        if k > N // 2:
            assert want < source
        else:
            assert want == source

    assert claimed(N, N) == N * N

print("VERIFY_OK")
