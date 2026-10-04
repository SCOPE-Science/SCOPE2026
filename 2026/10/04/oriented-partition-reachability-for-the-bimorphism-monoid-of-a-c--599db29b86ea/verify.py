from functools import lru_cache


def partitions(n):
    if n == 0:
        return [()]
    out = []
    for p in partitions(n - 1):
        out.append(p + ((n - 1,),))
        for i in range(len(p)):
            q = list(p)
            q[i] = q[i] + (n - 1,)
            out.append(tuple(q))
    return out

@lru_cache(None)
def bell(n):
    return len(partitions(n))


def weight(p):
    return 1 << sum(len(b) * (len(b) - 1) // 2 for b in p)


def refines(pi, sigma):
    block_of = {}
    for j, b in enumerate(sigma):
        for x in b:
            block_of[x] = j
    return all(len({block_of[x] for x in b}) == 1 for b in pi)


def orbit_count_direct(n):
    return sum(weight(p) for p in partitions(n))


def comparable_count_product(n):
    ans = 0
    for sigma in partitions(n):
        w = weight(sigma)
        r = 1
        for b in sigma:
            r *= bell(len(b))
        ans += w * r
    return ans


def comparable_count_refinement(n):
    ps = partitions(n)
    ans = 0
    for sigma in ps:
        target_orientations = weight(sigma)
        refinements = sum(1 for pi in ps if refines(pi, sigma))
        ans += target_orientations * refinements
    return ans


def rank_counts(n):
    d = {}
    for p in partitions(n):
        r = n - len(p)
        d[r] = d.get(r, 0) + weight(p)
    return tuple(d.get(r, 0) for r in range(n))

expected_A = [1, 1, 3, 15, 121, 1665, 43883, 2437423]
expected_C = [1, 1, 5, 53, 1193, 60329, 7071533, 1893360157]
A = [orbit_count_direct(n) for n in range(8)]
C = [comparable_count_product(n) for n in range(8)]
assert A == expected_A, (A, expected_A)
assert C == expected_C, (C, expected_C)
for n in range(7):
    assert comparable_count_refinement(n) == C[n]
for n in range(1, 8):
    rc = rank_counts(n)
    assert sum(rc) == A[n]
    assert rc[0] == 1  # all coordinates in distinct components
    assert rc[-1] == 2 ** (n * (n - 1) // 2)  # one tournament block
print('A_0..A_7 =', A)
print('C_0..C_7 =', C)
print('rank rows n=1..7 =', [rank_counts(n) for n in range(1,8)])
print('VERIFY_OK')
