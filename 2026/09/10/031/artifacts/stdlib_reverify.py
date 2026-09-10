"""Independent stdlib-only re-verification (no numpy): recompute A_s, A^2, LDL pivots,
Rayleigh quotient, graph6 round-trip. Guards against numpy-int artefacts."""
import json
from fractions import Fraction

d = json.load(open("output/artifacts/coxeter_base.json"))
E = [tuple(e) for e in d["edges"]]
c = json.load(open("output/artifacts/counterexample_sign_vector.json"))
s = [int(x) for x in c["base_sign"]]
n = 28; N = 56
assert len(E) == 42 and len(s) == 42

# Build signed 56x56 as dict/list of lists (pure python ints)
As = [[0]*N for _ in range(N)]
for e, (u, v) in enumerate(E):
    sv = s[e]
    As[u][v+28] += sv; As[v+28][u] += sv
    As[u+28][v] += sv; As[v][u+28] += sv

# A^2 pure python
A2 = [[0]*N for _ in range(N)]
for i in range(N):
    Ai = As[i]
    nz = [(k, aik) for k, aik in enumerate(Ai) if aik]
    for k, aik in nz:
        Ak = As[k]
        row = A2[i]
        if aik == 1:
            for j in range(N):
                row[j] += Ak[j]
        else:
            for j in range(N):
                row[j] -= Ak[j]
# spot-check trace = 168
tr2 = sum(A2[i][i] for i in range(N))
print("Tr(A_s^2) =", tr2)
assert tr2 == 168

def ldl_frac(Mint):
    nn = len(Mint)
    D = [Fraction(0)]*nn
    L = [[Fraction(0)]*nn for _ in range(nn)]
    for j in range(nn):
        acc = Fraction(Mint[j][j], 1)
        for k in range(j):
            acc -= L[j][k]*L[j][k]*D[k]
        D[j] = acc
        if D[j] <= 0:
            return None
        for i in range(j+1, nn):
            acc2 = Fraction(Mint[i][j], 1)
            for k in range(j):
                acc2 -= L[i][k]*L[j][k]*D[k]
            L[i][j] = acc2/D[j]
    return D

for Rnum, Rden, tag in [(26105, 10000, "2.6105"), (298, 100, "2.98"), (2978, 1000, "2.978 direct"), (262, 100, "2.62")]:
    Mint = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            Mint[i][j] = -Rden*Rden*A2[i][j]
        Mint[i][i] += Rnum*Rnum
    D = ldl_frac(Mint)
    print(f"R={tag}: {'PD all pivots>0, min='+str(min(D))[:50] if D else 'FAIL'}")
    assert D is not None

# Rayleigh lower bound pure python
r = json.load(open("output/artifacts/rayleigh_lower_26104.json"))
w = r["w"]
assert len(w) == N
Aw = [0]*N
for i in range(N):
    tot = 0
    row = As[i]
    for j in range(N):
        if row[j]:
            tot += row[j]*w[j]
    Aw[i] = tot
num = sum(w[i]*Aw[i] for i in range(N))
den = sum(x*x for x in w)
print("num =", num, "den =", den, "match:", num == r["num"] and den == r["den"])
assert num == r["num"] and den == r["den"]
assert 10000*num - 26104*den >= 0
print("Rayleigh rho>=2.6104 EXACT (stdlib) OK")

# graph6 round-trip for base
g6 = json.load(open("output/artifacts/coxeter_graph6.json"))["graph6"]
def graph6_decode(g):
    nn = ord(g[0]) - 63
    bits = []
    for ch in g[1:]:
        v = ord(ch) - 63
        for b in range(5, -1, -1):
            bits.append((v >> b) & 1)
    A = [[0]*nn for _ in range(nn)]
    p = 0
    for j in range(1, nn):
        for i in range(j):
            A[i][j] = A[j][i] = bits[p]; p += 1
    return A
Ab = graph6_decode(g6)
deg = sorted(sum(row) for row in Ab)
assert deg[0] == 3 and sum(deg)//2 == 42
print("graph6 round-trip base 28v/42e/cubic OK")
print("STDLIB_VERIFY_OK")
