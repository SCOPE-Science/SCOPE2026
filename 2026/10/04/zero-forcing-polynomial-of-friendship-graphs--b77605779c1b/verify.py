from itertools import combinations

def friendship(k):
    n = 2*k + 1
    adj = [set() for _ in range(n)]
    for i in range(k):
        a, b = 2*i + 1, 2*i + 2
        for u, v in [(0, a), (0, b), (a, b)]:
            adj[u].add(v)
            adj[v].add(u)
    return adj

def is_zero_forcing(adj, mask):
    n = len(adj)
    blue = mask
    full = (1 << n) - 1
    while True:
        changed = False
        for u in range(n):
            if not ((blue >> u) & 1):
                continue
            white_neighbors = [v for v in adj[u] if not ((blue >> v) & 1)]
            if len(white_neighbors) == 1:
                blue |= 1 << white_neighbors[0]
                changed = True
                break
        if not changed:
            break
    return blue == full

def structural_condition(k, mask):
    center = (mask & 1) != 0
    counts = []
    for i in range(k):
        a, b = 2*i + 1, 2*i + 2
        counts.append(((mask >> a) & 1) + ((mask >> b) & 1))
    if center:
        return all(t >= 1 for t in counts)
    return all(t >= 1 for t in counts) and any(t == 2 for t in counts)

def predicted_coeffs(k):
    # Z(F_k;x) = x^k((1+x)(2+x)^k - 2^k)
    n = 2*k + 1
    c = [0]*(n+1)
    from math import comb
    for j in range(1, k+2):
        s = k + j
        term1 = comb(k, j) * (2**(k-j)) if 0 <= j <= k else 0
        term2 = comb(k, j-1) * (2**(k-j+1)) if 0 <= j-1 <= k else 0
        c[s] = term1 + term2
    return c

graphs = subsets = forcing_sets = 0
for k in range(1, 9):
    adj = friendship(k)
    n = len(adj)
    coeff = [0]*(n+1)
    for mask in range(1 << n):
        subsets += 1
        actual = is_zero_forcing(adj, mask)
        pred = structural_condition(k, mask)
        assert actual == pred, (k, mask, actual, pred)
        if actual:
            forcing_sets += 1
            coeff[mask.bit_count()] += 1
    p = predicted_coeffs(k)
    assert coeff == p, (k, coeff, p)
    z = next(i for i,a in enumerate(coeff) if a)
    assert z == k+1, (k,z)
    assert coeff[k+1] == (2**k + k*(2**(k-1))), (k, coeff[k+1])
    assert sum(coeff) == 2*(3**k) - 2**k, (k, sum(coeff))
    graphs += 1

print("VERIFY_OK")
print("friendship_graphs_checked =", graphs)
print("vertex_subsets_checked =", subsets)
print("zero_forcing_sets_checked =", forcing_sets)
print("k = 1..8")
print("all direct forcing tests matched the structural classification")
print("all polynomial coefficients matched")
print("all minimum values and minimum-set counts matched")
print("all total zero-forcing-set counts matched")
