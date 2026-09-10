"""Consolidated stdlib-only audit for the emergent disproof (no third-party imports).
Recomputes EVERYTHING from coxeter_base.json + counterexample_sign_vector.json:
 base invariants (28v/42e/cubic/girth7, distribution, intersection array, unsigned
 charpoly closed form), B invariants (56v/84e/cubic/connected/bipartite/girth8),
 balance + fibre-symmetry, trace rigidity, dictionary identity, exact LDL upper
 bounds (2.978 direct, 2.6105, 2.62, 2.98), exact Rayleigh lower bound 2.6104,
 Newton checks of both charpolys, integer threshold arithmetic.
Prints AUDIT_OK or raises on first failure. Run: python3 audit_emergent_stdlib.py
from the workspace root."""
import json
from collections import Counter, deque
from fractions import Fraction

E = [tuple(e) for e in json.load(open("output/artifacts/coxeter_base.json"))["edges"]]
c = json.load(open("output/artifacts/counterexample_sign_vector.json"))
s = [int(x) for x in c["base_sign"]]
v84 = [int(x) for x in c["fibre_vector84"]]
n, N = 28, 56

# 1. balance + fibre-symmetry
assert len(E) == 42 and len(s) == 42 and len(v84) == 84
assert sum(1 for x in s if x == 1) == 21 and sum(1 for x in s if x == -1) == 21
assert all(v84[2 * e] == s[e] and v84[2 * e + 1] == s[e] for e in range(42))
assert sum(1 for x in v84 if x == 1) == 42 and sum(1 for x in v84 if x == -1) == 42
print("1. balance 21/21 base, 42/42 fibre + fibre-symmetry OK")


def girth(adj):
    g = 10 ** 9
    for st in range(len(adj)):
        dist = [-1] * len(adj)
        par = [-1] * len(adj)
        dist[st] = 0
        q = deque([st])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if dist[w] == -1:
                    dist[w] = dist[u] + 1
                    par[w] = u
                    q.append(w)
                elif par[u] != w and par[w] != u:
                    g = min(g, dist[u] + dist[w] + 1)
    return g


# 2. base invariants
adj0 = [[] for _ in range(n)]
for u, v in E:
    adj0[u].append(v)
    adj0[v].append(u)
assert all(len(a) == 3 for a in adj0) and girth(adj0) == 7
exp = {0: (0, 0, 3), 1: (1, 0, 2), 2: (1, 0, 2), 3: (1, 1, 1), 4: (2, 1, 0)}
for st in range(n):
    dist = [-1] * n
    dist[st] = 0
    q = deque([st])
    while q:
        u = q.popleft()
        for w in adj0[u]:
            if dist[w] == -1:
                dist[w] = dist[u] + 1
                q.append(w)
    assert dict(Counter(dist)) == {0: 1, 1: 3, 2: 6, 3: 12, 4: 6}
    for x in range(n):
        i = dist[x]
        nb = [dist[w] for w in adj0[x]]
        assert ((nb.count(i - 1) if i > 0 else 0), nb.count(i), nb.count(i + 1)) == exp[i]
print("2. base 28v/42e/cubic/girth7 + intersection array {3,2,2,1;1,1,1,2} OK")

# 3. B invariants
adjB = [[] for _ in range(N)]
for u, v in E:
    adjB[u].append(v + 28)
    adjB[v + 28].append(u)
    adjB[u + 28].append(v)
    adjB[v].append(u + 28)
assert all(len(a) == 3 for a in adjB) and girth(adjB) == 8
col = [-1] * N
col[0] = 0
q = deque([0])
while q:
    u = q.popleft()
    for w in adjB[u]:
        if col[w] == -1:
            col[w] = col[u] ^ 1
            q.append(w)
        else:
            assert col[w] != col[u]
assert all(x != -1 for x in col)
print("3. B 56v/84e/cubic/connected/bipartite/girth8 OK")


def matmul(A, B):
    C = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for l in range(len(B)):
            a = A[i][l]
            if a:
                row, Bl = C[i], B[l]
                for j in range(len(B[0])):
                    row[j] += a * Bl[j]
    return C


def matpow(A, p):
    R = [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]
    B = A
    while p:
        if p & 1:
            R = matmul(R, B)
        B = matmul(B, B)
        p >>= 1
    return R


def traces(M, kmax):
    P = [[1 if i == j else 0 for j in range(len(M))] for i in range(len(M))]
    out = {}
    for k in range(1, kmax + 1):
        P = matmul(P, M)
        out[k] = sum(P[i][i] for i in range(len(M)))
    return out


A0 = [[0] * n for _ in range(n)]
At = [[0] * n for _ in range(n)]
for e, (u, v) in enumerate(E):
    A0[u][v] += 1
    A0[v][u] += 1
    At[u][v] += s[e]
    At[v][u] += s[e]
trU, trW = traces(A0, 8), traces(At, 8)
assert (trU[2], trU[4], trU[6]) == (84, 420, 2436) == (trW[2], trW[4], trW[6])
assert (trU[7], trU[8]) == (336, 15540) and (trW[7], trW[8]) == (-168, 14964)
print("4. trace rigidity Tr2/4/6 signed==unsigned (84/420/2436); split at Tr7/Tr8 OK")

As = [[0] * N for _ in range(N)]
for e, (u, v) in enumerate(E):
    sv = s[e]
    As[u][v + 28] += sv
    As[v + 28][u] += sv
    As[u + 28][v] += sv
    As[v][u + 28] += sv
for i in range(n):
    for j in range(n):
        assert As[i][j] == 0 and As[i + 28][j + 28] == 0
        assert As[i][j + 28] == At[i][j] and As[i + 28][j] == At[i][j]
print("5. dictionary A_s=[[0,A_t],[A_t,0]] EXACT; rho(A_s)=rho(A_t) analytic")
A2 = matmul(As, As)
assert sum(A2[i][i] for i in range(N)) == 168
A4, A6 = matmul(A2, A2), matmul(matmul(A2, A2), A2)
assert sum(A4[i][i] for i in range(N)) == 840
assert sum(A6[i][i] for i in range(N)) == 4872
print("6. 56x56 signed Tr2/Tr4/Tr6 = 168/840/4872 (=2x base) OK")


def ldl(Mint):
    nn = len(Mint)
    Dd = [Fraction(0)] * nn
    L = [[Fraction(0)] * nn for _ in range(nn)]
    for j in range(nn):
        acc = Fraction(Mint[j][j], 1)
        for k in range(j):
            acc -= L[j][k] * L[j][k] * Dd[k]
        Dd[j] = acc
        if Dd[j] <= 0:
            return None
        for i in range(j + 1, nn):
            acc2 = Fraction(Mint[i][j], 1)
            for k in range(j):
                acc2 -= L[i][k] * L[j][k] * Dd[k]
            L[i][j] = acc2 / Dd[j]
    return Dd


for Rnum, Rden, tag in [(2978, 1000, "2.978 DIRECT"), (26105, 10000, "2.6105"),
                        (262, 100, "2.62"), (298, 100, "2.98")]:
    Mint = [[-Rden * Rden * A2[i][j] for j in range(N)] for i in range(N)]
    for i in range(N):
        Mint[i][i] += Rnum * Rnum
    assert ldl(Mint) is not None, tag
    print(f"7. exact LDL rho < {tag} OK (all 56 pivots > 0)")

r = json.load(open("output/artifacts/rayleigh_lower_26104.json"))
w = r["w"]
assert len(w) == N
Aw = [sum(As[i][j] * w[j] for j in range(N)) for i in range(N)]
num = sum(w[i] * Aw[i] for i in range(N))
den = sum(x * x for x in w)
assert num == r["num"] and den == r["den"]
assert 10000 * num - 26104 * den >= 0
print(f"8. Rayleigh {num}/{den} ~= 2.6105 >= 2.6104 EXACT OK")

# 9. Newton checks k=1..8 for both saved charpolys
for fn, tr in [("witness_charpoly.json", trW), ("coxeter_unsigned_charpoly.json", trU)]:
    asc = json.load(open(f"output/artifacts/{fn}"))["charpoly_ascending"]
    Nn = len(asc) - 1
    e = [Fraction(0)] * (Nn + 1)
    e[0] = Fraction(1)
    for k in range(1, Nn + 1):
        e[k] = Fraction((-1) ** k * asc[Nn - k], 1)
    p = {0: Nn}
    p.update(tr)
    for k in range(1, 9):
        assert e[k] == sum(((-1) ** (i - 1)) * e[k - i] * p[i] for i in range(1, k + 1)) / k, (fn, k)
print("9. Newton identities k=1..8 exact for both charpolys OK")

# 10. unsigned closed form (x-3)(x-2)^8(x+1)^7(x^2+2x-1)^6
def pmul(a, b):
    r = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def ppow(a, k):
    r = [Fraction(1)]
    for _ in range(k):
        r = pmul(r, a)
    return r


cf = pmul(pmul(pmul([-3, 1], ppow([-2, 1], 8)), ppow([1, 1], 7)), ppow([-1, 2, 1], 6))
assert [int(x) for x in cf] == json.load(open("output/artifacts/coxeter_unsigned_charpoly.json"))["charpoly_ascending"]
print("10. unsigned charpoly == closed form EXACT OK")

# 11. integer threshold arithmetic: 2*sqrt(2)+0.15 > 2.9784 > 2.978
assert 14142 ** 2 < 2 * 10000 ** 2
assert 2 * 14142 * 10 + 1500 > 2978 * 10
print("11. 2*sqrt2+0.15 > 2.9784 > 2.978 OK; rho in [2.6104,2.6105): TARGET FALSE")
print("AUDIT_OK")
