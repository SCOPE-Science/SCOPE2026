from itertools import permutations
from math import factorial

def partitions(n, top=None):
    if n == 0:
        yield ()
        return
    if top is None or top > n:
        top = n
    for a in range(top, 0, -1):
        for rest in partitions(n-a, a):
            yield (a,) + rest

def conjugate(lam):
    return tuple(sum(row >= j for row in lam) for j in range(1, lam[0]+1))

def hook_degree(lam):
    n = sum(lam)
    hprod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            below = sum(1 for k in range(i+1, len(lam)) if lam[k] > j)
            hprod *= (row-j) + below
    return factorial(n) // hprod

def alternating_degrees(n):
    seen = set()
    out = []
    for lam in partitions(n):
        if lam in seen:
            continue
        mu = conjugate(lam)
        d = hook_degree(lam)
        if mu == lam:
            assert d % 2 == 0
            out.append((d//2, lam, "split-a"))
            out.append((d//2, lam, "split-b"))
            seen.add(lam)
        else:
            out.append((d, lam, "paired"))
            seen.add(lam)
            seen.add(mu)
    return out

def parity(p):
    inv = 0
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            inv += p[i] > p[j]
    return inv & 1

def compose(p, q):
    # p after q
    return tuple(p[q[i]] for i in range(len(p)))

def inverse(p):
    r = [0]*len(p)
    for i, a in enumerate(p):
        r[a] = i
    return tuple(r)

def perm_from_cycles(n, cycles):
    p = list(range(n))
    for cyc in cycles:
        for i, a in enumerate(cyc):
            p[a] = cyc[(i+1) % len(cyc)]
    return tuple(p)

def components(group, S):
    unseen = set(group)
    sizes = []
    while unseen:
        root = next(iter(unseen))
        stack = [root]
        unseen.remove(root)
        count = 0
        while stack:
            g = stack.pop()
            count += 1
            for s in S:
                h = compose(g, s)
                if h in unseen:
                    unseen.remove(h)
                    stack.append(h)
        sizes.append(count)
    return sorted(sizes)

def fixed_points(p):
    return sum(i == a for i, a in enumerate(p))

for n in (7, 8):
    adeg = alternating_degrees(n)
    matches = [row for row in adeg if row[0] == n-1]
    assert len(matches) == 1, (n, matches)

    G = [p for p in permutations(range(n)) if parity(p) == 0]
    assert len(G) == factorial(n)//2

    x = perm_from_cycles(n, [(0,1,2)])
    y = perm_from_cycles(n, [(0,1,2),(3,4,5)])
    assert x in G and y in G
    ix, iy = inverse(x), inverse(y)
    assert compose(compose(x,x),x) == tuple(range(n))
    assert compose(compose(y,y),y) == tuple(range(n))

    cs = components(G, [x, ix])
    ct = components(G, [y, iy])
    assert set(cs) == {3} and set(ct) == {3}
    assert len(cs) == len(ct) == len(G)//3

    chi_x = fixed_points(x)-1
    chi_ix = fixed_points(ix)-1
    chi_y = fixed_points(y)-1
    chi_iy = fixed_points(iy)-1
    sum_s = chi_x + chi_ix
    sum_t = chi_y + chi_iy
    assert sum_s == 2*(n-4)
    assert sum_t == 2*(n-7)
    assert sum_s - sum_t == 6

    print({
        "n": n,
        "|A_n|": len(G),
        "components": len(G)//3,
        "degree_n_minus_1_irreducibles": len(matches),
        "sum_S": sum_s,
        "sum_T": sum_t,
    })

print("VERIFY_OK")
