"""Auditable verifier for the crank-sliced spt micro-cell (target audit plan).

Recomputes from definitions (exact integer arithmetic, stdlib only):
 1. HAND-PROOF certificate (no enumeration): S(6;6)=6 and S(7;6)=1 exactly,
    by part-count bounding (see WORKLOG §hand-proof). Hence 6 != 1 mod 11,
    refuting r-independence at the first progression index N=6.
 2. Brute-force census of all 11-colored partitions of 6 (29,183) confirming
    the full exact slice row [1894,5873,2728,949,253,49,6,1,11,78,426].
 3. Collapsed mod-11 DP pipeline to N=150 confirming every residue row
    N=11n+6 (14 rows) is non-constant mod 11.
Prints OBSTRUCTION_FOUND + VERIFY_OK on success.
"""
import itertools, json, time

MOD = 11
K = 11

def partitions(n):
    if n == 0:
        yield []
        return
    def rec(rem, mx, cur):
        if rem == 0:
            yield list(cur)
            return
        for p in range(min(mx, rem), 0, -1):
            cur.append(p)
            yield from rec(rem-p, p, cur)
            cur.pop()
    yield from rec(n, n, [])

def s_first(lam):
    return lam.count(lam[-1]) if lam else 0

# ---- 1. hand-proof bounding check (machine-checked logic) ----
# Pure-arithmetic proof (no partition facts beyond: each part >= 1, so
# #(parts of lambda) <= |lambda|; and the all-ones forcing: c parts summing
# to c must be [1^c], whose smallest-part multiplicity is c).
# Setup: N=6, j=|pi1|, m=|pi2|, rest>=0, j+m+rest=6; c1<=j, c2<=m.
# Class 6 mod 11 needs diff=c1-c2 in {-5,6} (range [-6,6]).
#   diff 6: c1=6,c2=0 -> j=6,m=0,rest=0 -> pi1=[1^6], weight 6.
#   diff -5: (c1,c2)=(0,5) [c1=0 -> weight 0] or (1,6) [needs m>=6,j>=1,
#     j+m>=7>6, impossible]. So S(6;6)=6.
# Class 7 mod 11 needs diff=-4 (diff 7 unattainable): cells (0,4) [weight 0],
#   (2,6) [needs j+m>=8>6, impossible], (1,5) [needs j>=1,m>=5,j+m<=6, so
#   (j,m)=(1,5), rest=0 -> pi1=[1], pi2=[1^5], weight 1]. So S(7;6)=1.
# Integer-cell audit: the ONLY cells with c1>=1 compatible with the bounds:
for ax, expect in ((6, [(6,0,6,0,0)]), (7, [(1,5,1,5,0)])):
    compat = [(c1,c2,j,m,6-j-m) for j in range(7) for m in range(7-j)
              for c1 in range(1,j+1) for c2 in range(m+1) if (c1-c2) % MOD == ax]
    assert compat == expect, (ax, compat)
print("arithmetic cell audit: unique forced cells (6,0,6,0,0) and (1,5,1,5,0)")
def hand_S66():
    # verify uniqueness claims computationally (tiny searches)
    assert [l for l in partitions(6) if len(l) == 6] == [[1]*6]
    # diff -5 cell: c1=0 -> s-weight 0
    return 6

def hand_S76():
    # diff must be -4 (diff 7 impossible as c1<=6). c1-c2=-4, c1+c2-parts<=6 -> c1<=1.
    # c1=0: weight 0. c1=1,c2=5: forces |pi1|=1,|pi2|=5,rest=0.
    assert [l for l in partitions(1) if len(l) == 1] == [[1]]
    assert [l for l in partitions(5) if len(l) == 5] == [[1]*5]
    return 1

a, b = hand_S66(), hand_S76()
print(f"hand-proof: S(6;6)={a}, S(7;6)={b}, equal mod 11? {a % 11 == b % 11}")
assert (a - b) % 11 != 0

# ---- 2. brute-force census N=6 ----
plist = [list(partitions(s)) for s in range(7)]
S = [0]*MOD
cnt = 0
def comp(rem, kk, cur):
    if kk == 1:
        yield cur + [rem]
        return
    for v in range(rem+1):
        yield from comp(rem-v, kk-1, cur+[v])
for sizes in comp(6, K, []):
    for tup in itertools.product(*[plist[s] for s in sizes]):
        cnt += 1
        S[(len(tup[0])-len(tup[1])) % MOD] += s_first(tup[0])
print(f"census: {cnt} colored partitions; exact row = {S}")
assert cnt == 29183, cnt
assert S == [1894, 5873, 2728, 949, 253, 49, 6, 1, 11, 78, 426], S
assert S[6] == 6 and S[7] == 1  # matches hand-proof
assert len(set(x % MOD for x in S)) > 1

# ---- 3. collapsed pipeline to 150 ----
t0 = time.time()
NMAX = 150
dp = [[0]*(NMAX+1) for _ in range(NMAX+1)]
dp[0][0] = 1
for part in range(1, NMAX+1):
    for n in range(part, NMAX+1):
        rn, rp = dp[n], dp[n-part]
        for c in range(1, NMAX+1):
            rn[c] += rp[c-1]
def Af(n, c):
    if n == 0 or c == 0:
        return 0
    tot, s0 = 0, 1
    while c*s0 <= n:
        m = n - c*s0
        for t in range(c):
            tot += (c-t)*dp[m][t]
        s0 += 1
    return tot
A1 = [[0]*MOD for _ in range(NMAX+1)]
D2 = [[0]*MOD for _ in range(NMAX+1)]
for j in range(NMAX+1):
    for c in range(NMAX+1):
        if j == 0:
            if c == 0:
                D2[j][0] = (D2[j][0]+dp[j][c]) % MOD
        else:
            if c >= 1:
                A1[j][c % MOD] = (A1[j][c % MOD]+Af(j, c)) % MOD
            D2[j][c % MOD] = (D2[j][c % MOD]+dp[j][c]) % MOD
p = [sum(dp[n]) % MOD for n in range(NMAX+1)]
tc = [0]*(NMAX+1); tc[0] = 1
for _ in range(K-2):
    new = [0]*(NMAX+1)
    for x in range(NMAX+1):
        if tc[x]:
            for y in range(NMAX+1-x):
                new[x+y] = (new[x+y]+tc[x]*p[y]) % MOD
    tc = new
rows = {}
for n in range(14):
    NN = 11*n+6
    acc = [0]*MOD
    for j in range(NN+1):
        Aj = A1[j]
        if all(v == 0 for v in Aj):
            continue
        for m in range(NN+1-j):
            w = tc[NN-j-m]
            if w == 0:
                continue
            Dm = D2[m]
            for u in range(MOD):
                if Aj[u] == 0:
                    continue
                for v in range(MOD):
                    if Dm[v] == 0:
                        continue
                    acc[(u-v) % MOD] = (acc[(u-v) % MOD]+Aj[u]*Dm[v]*w) % MOD
    rows[NN] = acc
    assert len(set(acc)) > 1, (NN, acc)
print("collapsed table to 150: all 14 rows non-constant")
for NN, r in rows.items():
    print(NN, r)
print("OBSTRUCTION_FOUND least-N=6; VERIFY_OK")
