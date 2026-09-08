"""Two-method verification for stretched LR ray (from-scratch, stdlib only).
Method A: Steinberg formula with from-scratch A3 Kostant partition function.
Method B: GL(4) hive integer-point enumeration (3 interior variables).
Checks: base decomposition totals, stretched values t=0..8 on rays
nu*=(5,4,2,2) [P(t)=t+1] and nu2=(6,4,2,1) [P(t)=(t+1)^2],
hive forcing equalities, and explicit hive witness at t=1.
Run: python3 verify_ray.py
"""
import itertools, json

def P_simple(b):
    b1, b2, b3 = b
    if b1 < 0 or b2 < 0 or b3 < 0:
        return 0
    count = 0
    for k4 in range(0, min(b1, b2) + 1):
        for k5 in range(0, min(b2 - k4, b3) + 1):
            m6 = min(b1 - k4, b2 - k4 - k5, b3 - k5)
            for _ in range(0, m6 + 1):
                count += 1
    return count

def P_e(g):
    if sum(g) != 0:
        return 0
    return P_simple((g[0], g[0] + g[1], g[0] + g[1] + g[2]))

perms = list(itertools.permutations([0, 1, 2, 3]))
def sgn(p):
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
    return -1 if inv % 2 else 1

def steinberg(lam, mu, nu):
    assert sum(lam) + sum(mu) == sum(nu)
    rho = (3, 2, 1, 0)
    Lp = tuple(lam[i] + rho[i] for i in range(4))
    Mp = tuple(mu[i] + rho[i] for i in range(4))
    Np = tuple(nu[i] + 2 * rho[i] for i in range(4))
    total = 0
    for w in perms:
        Lw = tuple(Lp[w[i]] for i in range(4))
        for v in perms:
            s = sgn(w) * sgn(v)
            Mv = tuple(Mp[v[i]] for i in range(4))
            g = (Lw[0] + Mv[0] - Np[0], Lw[1] + Mv[1] - Np[1],
                 Lw[2] + Mv[2] - Np[2], Lw[3] + Mv[3] - Np[3])
            if sum(g) != 0:
                continue
            total += s * P_e(g)
    return total

def hive_count(lam, mu, nu, sign=+1):
    n = 4
    assert sum(lam) + sum(mu) == sum(nu)
    a = {}
    for i in range(n + 1):
        a[(i, 0)] = sum(lam[:i])
    for j in range(n + 1):
        a[(n - j, j)] = sum(lam) + sum(mu[:j])
    for j in range(n + 1):
        a[(0, j)] = sum(nu[:j])
    tot = sum(nu)
    count = 0
    pts = []
    for v11 in range(-2, tot + 3):
        for v21 in range(-2, tot + 3):
            for v12 in range(-2, tot + 3):
                a[(1, 1)] = v11
                a[(2, 1)] = v21
                a[(1, 2)] = v12
                def g(p, q, r, s):
                    return (a[p] + a[q] - a[r] - a[s]) * sign
                ok = True
                for j in range(1, n):
                    for i in range(0, n - j):
                        if g((i, j), (i + 1, j), (i, j + 1), (i + 1, j - 1)) < 0:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                for i in range(1, n + 1):
                    for j in range(0, n - i):
                        if (i - 1, j + 1) not in a:
                            continue
                        if g((i, j), (i, j + 1), (i + 1, j), (i - 1, j + 1)) < 0:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                for j in range(1, n + 1):
                    for i in range(0, n - j):
                        if g((i, j), (i + 1, j - 1), (i, j - 1), (i + 1, j)) < 0:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    count += 1
                    pts.append((v11, v21, v12))
    return count, pts

lam = (4, 2, 0, 0)
mu = (4, 2, 1, 0)
nu_star = (5, 4, 2, 2)
nu_max = (6, 4, 2, 1)

# 1. base decomposition cross-check (Steinberg vs hive) for all constituents found
base_nus = [(6,4,2,1),(5,4,3,1),(7,3,2,1),(5,4,2,2),(5,5,2,1),(6,3,2,2),
            (6,3,3,1),(6,4,3,0),(6,5,1,1),(6,5,2,0),(7,4,1,1),(7,4,2,0),
            (4,4,3,2),(4,4,4,1),(5,3,3,2),(5,4,4,0),(5,5,3,0),(6,6,1,0),
            (7,2,2,2),(7,3,3,0),(7,5,1,0),(8,2,2,1),(8,3,1,1),(8,3,2,0),(8,4,1,0)]
base_mult = [4,3,3,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1]
for nu, m in zip(base_nus, base_mult):
    s = steinberg(lam, mu, nu)
    h, _ = hive_count(lam, mu, nu)
    assert s == m == h, (nu, s, m, h)
print("base decomposition: 25 constituents, Steinberg==hive==GT-table, OK")

# 2. stretched values t=0..8, two-method agreement, formula check
for nu, formula, name in [(nu_star, lambda t: t + 1, "nu*"),
                          (nu_max, lambda t: (t + 1) ** 2, "nu_max")]:
    for t in range(9):
        L = tuple(t * x for x in lam)
        M = tuple(t * x for x in mu)
        N = tuple(t * x for x in nu)
        s = steinberg(L, M, N)
        h, _ = hive_count(L, M, N)
        assert s == h == formula(t), (name, t, s, h, formula(t))
    print(f"ray {name}={nu}: t=0..8 Steinberg==hive==formula, OK")

# 3. forcing equalities on nu* ray (symbolic, checked numerically at t=1..8)
# y: E3#15 y-10t>=0 and E2#12 -y+10t>=0 -> y=10t
# z: E3#20 z-11t>=0 and E1#6 -z+11t>=0 -> z=11t
for t in range(1, 9):
    L = tuple(t * x for x in lam)
    M = tuple(t * x for x in mu)
    N = tuple(t * x for x in nu_star)
    _, pts = hive_count(L, M, N)
    assert len(pts) == t + 1
    assert all(y == 10 * t and z == 11 * t for _, y, z in pts)
    assert sorted(x for x, _, _ in pts) == list(range(8 * t, 9 * t + 1))
print("forcing equalities y=10t, z=11t, x in [8t,9t]: verified t=1..8, OK")

# 4. hive witness at t=1, nu*: the two hives (x,y,z)=(8,10,11),(9,10,11)
_, pts1 = hive_count(lam, mu, nu_star)
assert sorted(pts1) == [(8, 10, 11), (9, 10, 11)], pts1
print("t=1 hive witness:", sorted(pts1), "OK")
print("ALL CHECKS PASSED")
