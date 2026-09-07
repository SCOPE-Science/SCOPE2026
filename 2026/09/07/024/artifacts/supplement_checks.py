import math, random, time
from audit_ehrhart import ehrhart_via_gauge, hstar_from_ehrhart, age_hist


def age_hist_frac(u, v, m):
    Q = 42 * m
    h = [0] * 5
    for k in range(Q):
        a = ((k * u) % Q) / Q + ((k * v) % Q) / Q + \
            (k % 7) / 7 + (k % 3) / 3 + (k % 2) / 2
        ai = int(round(a))
        assert abs(a - ai) < 1e-9, (u, v, k, a)
        h[ai] += 1
    return tuple(h)


def divs(n):
    return [d for d in range(1, n + 1) if n % d == 0]


D = divs(42)
pairs = [(u, v) for u in D for v in D if u <= v and math.gcd(u, v) == 1]
ok = True
for (u, v) in pairs:
    m = u + v
    q = tuple(sorted((u, v, 6 * m, 14 * m, 21 * m)))
    if age_hist(q) != age_hist_frac(u, v, m):
        ok = False
        print("MISMATCH", u, v)
print("frac-decomposition agreement on all 14:", ok)

# widen gauge loop bounds and confirm L unchanged for big violator
import audit_ehrhart as A


def ehrhart_wide(q, t, pad=50):
    Q = sum(q)
    q4 = q[4]
    total = 0
    for S in range(t - (t * Q) // q4 - Q - 2 - pad, t + Q + 1 + pad):
        B = 0
        for i in range(4):
            B += math.ceil((S - t) * q[i] / Q)
        b4 = math.ceil((S - t) * q4 / Q)
        for x4 in range(q4):
            T = S - x4
            if T < B or x4 < b4:
                continue
            total += math.comb(T - B + 3, 3)
    return total


q = (2, 7, 54, 126, 189)
L1 = [A.ehrhart_via_gauge(q, t) for t in range(5)]
L2 = [ehrhart_wide(q, t) for t in range(5)]
print("bounds test:", L1, L2, L1 == L2)

# random-sample gauge recount over Q<=377 table
import json
tab = json.load(open("output/artifacts/table_Q5_430.json"))
small = [r for r in tab if r["Q"] <= 377]
random.seed(80)
samp = random.sample(small, 10)
allok = True
for r in samp:
    qq = tuple(r["q"])
    L = [A.ehrhart_via_gauge(qq, t) for t in range(5)]
    hg = A.hstar_from_ehrhart(L)
    ha = tuple(r["h"])
    m = "OK" if hg == ha else "MISMATCH"
    if hg != ha:
        allok = False
    print(qq, "Q=", r["Q"], hg, ha, m)
print("random-sample gauge agreement:", allok)
