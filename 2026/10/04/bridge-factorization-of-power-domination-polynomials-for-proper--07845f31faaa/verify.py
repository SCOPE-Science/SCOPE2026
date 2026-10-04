from math import comb


def double_star(a, b):
    # centers 0=u, 1=v; u-leaves 2..a+1; v-leaves a+2..a+b+1
    n = a + b + 2
    adj = [set() for _ in range(n)]
    adj[0].add(1); adj[1].add(0)
    for x in range(2, a + 2):
        adj[0].add(x); adj[x].add(0)
    for y in range(a + 2, n):
        adj[1].add(y); adj[y].add(1)
    return adj


def power_dominates(adj, mask):
    n = len(adj)
    observed = mask
    # domination step: selected vertices and all their neighbors
    for v in range(n):
        if (mask >> v) & 1:
            observed |= 1 << v
            for w in adj[v]:
                observed |= 1 << w
    full = (1 << n) - 1
    while observed != full:
        changed = False
        for v in range(n):
            if not ((observed >> v) & 1):
                continue
            unseen = [w for w in adj[v] if not ((observed >> w) & 1)]
            if len(unseen) == 1:
                observed |= 1 << unseen[0]
                changed = True
                break
        if not changed:
            return False
    return True


def structural(a, b, mask):
    u = (mask & 1) != 0
    v = (mask & 2) != 0
    left = sum((mask >> x) & 1 for x in range(2, a + 2))
    right = sum((mask >> y) & 1 for y in range(a + 2, a + b + 2))
    return (u or left >= a - 1) and (v or right >= b - 1)


def poly_mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out


def star_factor(t):
    # Q_t(x) = x(1+x)^t + t x^(t-1) + x^t
    out = [0] * (t + 2)
    for j in range(t + 1):
        out[j+1] += comb(t, j)
    out[t-1] += t
    out[t] += 1
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out

pairs = subsets = pds_count = 0
for a in range(2, 8):
    for b in range(2, 8):
        adj = double_star(a, b)
        n = a + b + 2
        coeff = [0] * (n + 1)
        for mask in range(1 << n):
            subsets += 1
            actual = power_dominates(adj, mask)
            pred = structural(a, b, mask)
            assert actual == pred, (a, b, mask, actual, pred)
            if actual:
                pds_count += 1
                coeff[mask.bit_count()] += 1
        while len(coeff) > 1 and coeff[-1] == 0:
            coeff.pop()
        expected = poly_mul(star_factor(a), star_factor(b))
        assert coeff == expected, (a, b, coeff, expected)
        assert sum(coeff) == (2**a + a + 1) * (2**b + b + 1)
        minimum = next(i for i, c in enumerate(coeff) if c)
        assert minimum == 2, (a, b, minimum)
        min_count = (3 if a == 2 else 1) * (3 if b == 2 else 1)
        assert coeff[2] == min_count, (a, b, coeff[2], min_count)
        pairs += 1

print('VERIFY_OK')
print('double_star_parameter_pairs_checked =', pairs)
print('vertex_subsets_checked =', subsets)
print('power_dominating_sets_checked =', pds_count)
print('parameters a,b = 2..7')
print('all direct power-domination tests matched the structural classification')
print('all polynomial coefficients matched Q_a(x)Q_b(x)')
print('all total counts and minimum-set counts matched')
