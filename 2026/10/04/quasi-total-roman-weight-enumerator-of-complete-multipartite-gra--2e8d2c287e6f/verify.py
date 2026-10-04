import itertools, math


def partitions(n, r, lo=1):
    if r == 0:
        if n == 0:
            yield ()
        return
    for x in range(lo, n + 1):
        if n - x < x * (r - 1):
            break
        for tail in partitions(n - x, r - 1, x):
            yield (x,) + tail


def part_labels(parts):
    out = []
    for i, a in enumerate(parts):
        out.extend([i] * a)
    return out


def direct_qtr(vals, labels):
    n = len(vals)
    for v, value in enumerate(vals):
        if value == 0:
            if not any(vals[u] == 2 and labels[u] != labels[v] for u in range(n)):
                return False
        elif value == 2:
            if not any(vals[u] > 0 and labels[u] != labels[v] for u in range(n)):
                return False
    return True


def add(a, b):
    m = max(len(a), len(b))
    out = [0] * m
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return out


def sub(a, b):
    m = max(len(a), len(b))
    out = [0] * m
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] -= x
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def power(base, n):
    out = [1]
    for _ in range(n): out = mul(out, base)
    return out


def closed_formula(parts):
    N = sum(parts)
    # all ones
    ans = [0] * (2*N + 1)
    ans[N] = 1

    # exactly one part contains label 2
    for ni in parts:
        inside = sub(power([0,1,1], ni), power([0,1], ni))
        outside = sub(power([1,1], N-ni), [1])
        ans = add(ans, mul(inside, outside))

    # label 2 occurs in at least two parts
    at_least_two = sub(power([1,1,1], N), power([1,1], N))
    for ni in parts:
        exactly_here = mul(
            sub(power([1,1,1], ni), power([1,1], ni)),
            power([1,1], N-ni),
        )
        at_least_two = sub(at_least_two, exactly_here)
    ans = add(ans, at_least_two)
    ans += [0] * (2*N + 1 - len(ans))
    return ans[:2*N+1]


def total_count_formula(parts):
    N = sum(parts)
    return (
        1
        + sum((2**ni - 1) * (2**(N-ni) - 1) for ni in parts)
        + 3**N - 2**N
        - sum((3**ni - 2**ni) * 2**(N-ni) for ni in parts)
    )


types = 0
labelings = 0
for N in range(2, 10):
    for r in range(2, N + 1):
        for parts in partitions(N, r):
            labels = part_labels(parts)
            actual = [0] * (2*N + 1)
            for vals in itertools.product(range(3), repeat=N):
                labelings += 1
                if direct_qtr(vals, labels):
                    actual[sum(vals)] += 1
            predicted = closed_formula(parts)
            assert actual == predicted, (parts, actual, predicted)
            assert sum(actual) == total_count_formula(parts), parts
            gamma = min(i for i, c in enumerate(actual) if c)
            assert gamma == min(N, min(parts) + 2, 4), (parts, gamma)
            types += 1

print('VERIFY_OK')
print('multipartite_types_checked =', types)
print('ternary_labelings_checked =', labelings)
print('orders = 2..9')
print('definition-level QTR condition matched every polynomial coefficient')
print('total-function count matched')
print('minimum-weight corollary matched')
