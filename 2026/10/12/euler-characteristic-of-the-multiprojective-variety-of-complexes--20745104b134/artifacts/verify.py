from itertools import product

def brute_count(dims):
    n = len(dims) - 1
    arrows = []
    for i in range(1, n + 1):
        arrows.append([(s, t) for s in range(dims[i-1]) for t in range(dims[i])])
    total = 0
    for tup in product(*arrows):
        ok = True
        for i in range(n - 1):
            s_next = tup[i+1][0]
            t_prev = tup[i][1]
            if s_next == t_prev:
                ok = False
                break
        if ok:
            total += 1
    return total

def formula(dims):
    n = len(dims) - 1
    ans = dims[0] * dims[-1]
    for i in range(1, n):
        ans *= dims[i] * (dims[i] - 1)
    return ans

def ambient_euler(dims):
    ans = 1
    for i in range(1, len(dims)):
        ans *= dims[i-1] * dims[i]
    return ans

checked = 0
tuples_checked = 0
for n in range(1, 6):
    for dims in product(range(1, 5), repeat=n+1):
        ambient_fixed = ambient_euler(dims)
        if ambient_fixed > 250000:
            continue
        b = brute_count(dims)
        f = formula(dims)
        assert b == f
        if any(d == 1 for d in dims[1:-1]):
            assert b == 0
        if f:
            left_num = f
            left_den = ambient_fixed
            right_num = 1
            right_den = 1
            for d in dims[1:-1]:
                right_num *= d - 1
                right_den *= d
            assert left_num * right_den == left_den * right_num
        checked += 1
        tuples_checked += ambient_fixed

assert checked > 1000
assert tuples_checked > 100000

print("VERIFY_OK", checked, tuples_checked)
