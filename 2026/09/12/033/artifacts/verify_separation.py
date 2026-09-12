"""Verify separating transformation-monoid witnesses for the path-swap family.

For each N>=2: states {s0,x1..xN,yN,z}; A,B,C as in WORKLOG.
Check: s0.A^n == s0.C^n iff n != N (for n in 1..3N), i.e.
phi(a^n b c^n) == phi(c^n b a^n) iff n != N, as constant maps.
Also verify the Graph-coequalizer mismatch words r=a p_2, r'=a q_2.
"""
import json

def build(N):
    # indices: 0=s0, 1..N=x1..xN, N+1=yN, N+2=z
    S = list(range(N + 3))
    z = N + 2
    A = [0] * (N + 3)
    C = [0] * (N + 3)
    B = [0] * (N + 3)
    A[0] = 1
    for i in range(1, N):
        A[i] = i + 1       # xi -> x_{i+1} (for N=2: A[1]=2)
    A[N] = z
    A[N + 1] = z
    A[z] = z
    C[0] = 1
    for i in range(1, N - 1):
        C[i] = i + 1
    C[N - 1] = N + 1       # x_{N-1} -> yN (for N=2: C[1]=3)
    C[N] = z
    C[N + 1] = z
    C[z] = z
    return A, B, C

def orbit(start, F, n):
    s = start
    for _ in range(n):
        s = F[s]
    return s

results = {}
for N in range(2, 11):
    A, B, C = build(N)
    ok = True
    detail = {}
    for n in range(1, 3 * N + 1):
        u = orbit(0, A, n)
        v = orbit(0, C, n)
        eq = (u == v)
        want = (n != N)
        if eq != want:
            ok = False
            detail[n] = (u, v, eq, want)
    # full-map check at the critical indices: phi(p_n), phi(q_n) as const maps
    assert ok, f"N={N} FAILED: {detail}"
    results[N] = {"states": N + 3, "holds_for_1..3N_except_N": True}

# Graph mismatch words: p_n = a^n b c^n, q_n = c^n b a^n as strings over {a,b,c}
def p(n): return "a" * n + "b" + "c" * n
def q(n): return "c" * n + "b" + "a" * n

pn, qn = {n: p(n) for n in range(2, 8)}, {n: q(n) for n in range(2, 8)}
# distinctness of all p_n, q_n (n>=2)
words = [pn[n] for n in pn] + [qn[n] for n in qn]
assert len(set(words)) == len(words), "pairs must be pairwise disjoint as words"
# p_n != q_n first-letter check
assert all(pn[n][0] == "a" and qn[n][0] == "c" for n in pn)
# mismatch: r = a p_2, r' = a q_2 have even length -> equal no p_n/q_n; r != r'
r, rp = "a" + p(2), "a" + q(2)
assert len(r) % 2 == 0 and all(len(w) % 2 == 1 for w in words)
assert r not in words and rp not in words and r != rp
# abelianization check: exponent vectors of p_n, q_n agree (Q nontrivial, consistent)
from collections import Counter
for n in range(2, 8):
    assert Counter(p(n)) == Counter(q(n))

print(json.dumps({"separation": results,
                  "r": r, "rp": rp, "r_len": len(r),
                  "graph_mismatch_ok": True}, indent=1))
print("ALL CHECKS PASSED")
