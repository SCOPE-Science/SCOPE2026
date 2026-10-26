"""Direct brute-force finite-field checks for the graph-algebra multiplication-rank theorem.

Run: python verify.py
No third-party libraries required.
"""
from itertools import product
from math import comb


def matrix_rank_mod(rows, p, ncols):
    m = [list(v) for v in rows]
    rank = 0
    for j in range(ncols):
        pivot = next((i for i in range(rank, len(m)) if m[i][j] % p), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        inv = pow(m[rank][j], -1, p)
        m[rank] = [(v * inv) % p for v in m[rank]]
        for i in range(rank + 1, len(m)):
            factor = m[i][j]
            if factor:
                m[i] = [(a - factor * b) % p for a, b in zip(m[i], m[rank])]
        rank += 1
    return rank


def rank_by_linear_algebra(edges, coeff, p):
    n = len(coeff)
    mat = []
    for u, v in edges:
        row = [0] * n
        row[u] = coeff[v]
        row[v] = coeff[u]
        mat.append(row)
    return matrix_rank_mod(mat, p, n)


def rank_by_support(edges, coeff, p):
    n = len(coeff)
    supp = {i for i, v in enumerate(coeff) if v}
    closed = set(supp)
    for u, v in edges:
        if u in supp or v in supp:
            closed.add(u)
            closed.add(v)
    adj = [set() for _ in range(n)]
    for u, v in edges:
        if u in supp and v in supp:
            adj[u].add(v)
            adj[v].add(u)
    seen = set()
    beta = 0
    for root in supp:
        if root in seen:
            continue
        stack = [(root, 0)]
        colors = {}
        bip = True
        while stack:
            x, color = stack.pop()
            if x in colors:
                if colors[x] != color:
                    bip = False
                continue
            colors[x] = color
            seen.add(x)
            for y in adj[x]:
                stack.append((y, color ^ 1))
        if p == 2 or bip:
            beta += 1
    return len(closed) - beta


def transfer_trace(n, w, z):
    t = [[w*z, 1, 0], [w*z, 0, 1], [w*z*z, 0, 1]]
    p = [[int(i == j) for j in range(3)] for i in range(3)]
    for _ in range(n):
        p = [[sum(p[i][k] * t[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    return sum(p[i][i] for i in range(3))


def transfer_coeffs(n, q, p):
    w = q - 1
    # Evaluation and interpolation avoided: directly polynomial-multiply matrices.
    # Polynomials represented by lists [coefficient of z^j].
    def add(a, b):
        r = [0] * max(len(a), len(b))
        for i, v in enumerate(a): r[i] += v
        for i, v in enumerate(b): r[i] += v
        return r
    def mul(a, b):
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b): r[i+j] += x*y
        return r
    Z0, Z1, Z2 = [0], [0, w], [0, 0, w]
    T = [[Z1, [1], Z0], [Z1, Z0, [1]], [Z2, Z0, [1]]]
    P = [[[int(i == j)] for j in range(3)] for i in range(3)]
    for _ in range(n):
        P = [[add(add(mul(P[i][0],T[0][j]),mul(P[i][1],T[1][j])),mul(P[i][2],T[2][j])) for j in range(3)] for i in range(3)]
    zpoly = add(add(P[0][0],P[1][1]),P[2][2]); zpoly.extend([0] * max(0, n + 1-len(zpoly)))
    if p == 2 or n%2==0:
        zpoly[n] -= w**n
        zpoly[n-1] += w**n
    return zpoly


def cycle_rank_from_ones(ones, n, p):
    if not ones: return 0
    if len(ones) == n: return n-int(p==2 or n%2==0)
    zero = [i not in ones for i in range(n)]
    long_runs = sum(zero[i] and zero[(i-1)%n] and not zero[(i-2)%n] for i in range(n))
    # This counts the second zero in each run of length >= 2.
    return len(ones) + long_runs



def gf4_mul(a, b):
    # Binary polynomials modulo u^2 + u + 1.
    out = 0
    while b:
        if b & 1: out ^= a
        b >>= 1
        a <<= 1
        if a & 4: a ^= 7
    return out

def rank_over_gf4(edges, coeff):
    n = len(coeff)
    mat = []
    for u, v in edges:
        row = [0] * n
        row[u], row[v] = coeff[v], coeff[u]
        mat.append(row)
    rk = 0
    for j in range(n):
        pivot = next((i for i in range(rk, len(mat)) if mat[i][j]), None)
        if pivot is None: continue
        mat[rk], mat[pivot] = mat[pivot], mat[rk]
        inv = next(t for t in (1, 2, 3) if gf4_mul(t, mat[rk][j]) == 1)
        mat[rk] = [gf4_mul(t, inv) for t in mat[rk]]
        for i in range(rk + 1, len(mat)):
            factor = mat[i][j]
            if factor:
                mat[i] = [t ^ gf4_mul(factor, r) for t, r in zip(mat[i], mat[rk])]
        rk += 1
    return rk


def run():
    trials = 0
    for p, n in [(2,4),(2,5),(2,6),(2,7),(2,8),(3,4),(3,5),(3,6),(3,7),(5,4),(5,5),(7,4)]:
        edges = [(i,(i+1)%n) for i in range(n)]
        obs = [0]*(n+1)
        for a in product(range(p),repeat=n):
            direct = rank_by_linear_algebra(edges,a,p)
            formula = rank_by_support(edges,a,p)
            zero_pos = {i for i,v in enumerate(a) if v}
            cycle = cycle_rank_from_ones(zero_pos,n,p)
            assert direct == formula == cycle, (p,n,a,direct,formula,cycle)
            obs[direct] += 1
        pred = transfer_coeffs(n,p,p)
        assert obs == pred[:n+1], (p,n,obs,pred)
        assert sum(obs) == p**n
        trials += 1
    # Composite prime-power field: two-bit polynomial representation of F_4.
    for n in (4, 5, 6):
        edges = [(i, (i + 1) % n) for i in range(n)]
        obs = [0] * (n + 1)
        for a in product(range(4), repeat=n):
            direct = rank_over_gf4(edges, a)
            support = rank_by_support(edges, a, 2)
            cycle = cycle_rank_from_ones({i for i, x in enumerate(a) if x}, n, 2)
            assert direct == support == cycle, (n, a, direct, support, cycle)
            obs[direct] += 1
        assert obs == transfer_coeffs(n, 4, 2)[:n+1]
        assert sum(obs) == 4**n
        trials += 1
    # Arbitrary graphs (not necessarily triangle-free) support formula.
    for p in (2,3):
        n=4
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<len(pairs)):
            edges=[pair for k,pair in enumerate(pairs) if mask & (1<<k)]
            for a in product(range(p),repeat=n):
                assert rank_by_linear_algebra(edges,a,p)==rank_by_support(edges,a,p)
        trials+=1
    print('GRAPH_LEFSCHETZ_RANK_ENUMERATOR_OK',trials,'families')

if __name__=='__main__': run()
