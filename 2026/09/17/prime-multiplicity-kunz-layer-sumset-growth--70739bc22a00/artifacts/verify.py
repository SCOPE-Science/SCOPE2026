from heapq import heappush, heappop

GENS = [29, 41, 42, 54, 56, 57]

def apery(gens):
    m = min(gens)
    inf = 10**30
    dist = [inf] * m
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        d, r = heappop(heap)
        if d != dist[r]:
            continue
        for g in gens:
            nd = d + g
            nr = nd % m
            if nd < dist[nr]:
                dist[nr] = nd
                heappush(heap, (nd, nr))
    return dist

def reachable_below(gens, limit):
    seen = [False] * limit
    seen[0] = True
    for n in range(limit):
        if seen[n]:
            for g in gens:
                if n + g < limit:
                    seen[n + g] = True
    return seen

ap = apery(GENS)
m = min(GENS)
F = max(ap) - m
c = F + 1
q = (c + m - 1) // m
rho = q * m - c
x = [(ap[i] - i) // m for i in range(m)]
eta = sum(xi == 1 for xi in x[1:])
theta = {t: sum(xi <= t for xi in x[1:]) for t in range(1, q)}
seen = reachable_below(GENS, c)
L = sum(seen)
e = len(GENS)
W = e * L - c

H = (q - 1) // 2
B = {h: min(m - 1, h * eta) for h in range(1, H + 1)}
layer_lower = q + 2 * sum(B[h] for h in range(1, H)) + (q - 2 * H) * B[H]

assert m == 29
assert c == 218 and q == 8 and rho == 14
assert e == 6 and eta == 5
assert [theta[t] for t in range(1, 7)] == [5, 7, 13, 16, 21, 24]
assert L == 107 and W == 424
assert B == {1: 5, 2: 10, 3: 15}
assert layer_lower == 68
assert L >= layer_lower
assert e * layer_lower + rho >= q * m
assert e * (eta + 2) < 2 * m
assert (eta + 1) * (eta + 2) < 2 * m
assert c > 3 * m
assert e < m / 3

print("m,e,c,q,rho,eta,L,W =", m, e, c, q, rho, eta, L, W)
print("Theta_1..Theta_6 =", [theta[t] for t in range(1, 7)])
print("B_1..B_H =", [B[h] for h in range(1, H + 1)])
print("layer lower bound for |L| =", layer_lower)
print("new sufficient inequality:", e * layer_lower + rho, ">=", q * m)
print("Yang-Zhang mixed first-layer test:", e * (eta + 2), "<", 2 * m)
print("Yang-Zhang eta-only test:", (eta + 1) * (eta + 2), "<", 2 * m)
