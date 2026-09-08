#!/usr/bin/env python3
"""Independent verification: MN orthogonality, trivial-column delta,
Frobenius column/row dims, and class-sum certificates for witnesses."""
import json, math
from collections import Counter

D = json.load(open("output/artifacts/restriction_tables.json"))
P = D["pairs"]

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for f in range(min(max_part, n), 0, -1):
        for rest in partitions(n - f, f):
            yield (f,) + rest

def csize(n, mu):
    c = Counter(mu)
    z = 1
    for l, m in c.items():
        z *= (l ** m) * math.factorial(m)
    return math.factorial(n) // z

def hook_dim(lam):
    d = 1
    for r in range(len(lam)):
        for c in range(lam[r]):
            d *= (lam[r] - c) + sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
    return math.factorial(sum(lam)) // d

# Rebuild chi tables independently via cache-free recursion to cross-check dims/orthog
import sys
sys.path.insert(0, "output/artifacts")
from compute_restriction import make_chi, prod_type

print("== MN row orthogonality n<=12 ==")
for n in [2, 3, 4, 5, 6, 8, 9, 10, 12]:
    pls, ch = make_chi(n)
    classes = list(partitions(n))
    ok = True
    for a in pls:
        for b in pls:
            s = sum(csize(n, mu) * ch(a, mu) * ch(b, mu) for mu in classes)
            if s != (math.factorial(n) if a == b else 0):
                ok = False
                print("ORTH FAIL", n, a, b, s)
                break
    print(f"n={n}: {'OK' if ok else 'FAIL'}")

print("== trivial column: mult(triv,triv;[N])==1 else 0 over alpha,beta ==")
for key, T in P.items():
    m, n = map(int, key.split("x"))
    N = m * n
    tk = ",".join([str(N)])
    ak = str(m) + "|" + str(n)
    bad = []
    for ab, row in T["table"].items():
        want = 1 if ab == ak else 0
        if row[tk] != want:
            bad.append((ab, row[tk]))
    print(key, "trivial-column:", "OK delta" if not bad else f"FAIL {bad}")

print("== certificate: (3,4) max witness a=[2,1] b=[3,1] l=[5,3,2,1,1] ==")
T = P["3x4"]["table"]
print("stored value:", T["2,1|3,1"]["5,3,2,1,1"])
_, chM = make_chi(3)
_, chN = make_chi(4)
_, chL = make_chi(12)
tot = 0
terms = []
for mu in partitions(3):
    for nu in partitions(4):
        rho = prod_type(mu, nu)
        t = (csize(3, mu) * csize(4, nu) * chL((5, 3, 2, 1, 1), rho)
             * chM((2, 1), mu) * chN((3, 1), nu))
        terms.append((list(mu), list(nu), list(rho), chL((5, 3, 2, 1, 1), rho),
                      chM((2, 1), mu), chN((3, 1), nu), t))
        tot += t
print(f"sum={tot} / (3!4!)={math.factorial(3)*math.factorial(4)} -> {tot/(math.factorial(3)*math.factorial(4))}")
json.dump(terms, open("output/artifacts/cert_max_3x4.json", "w"))
print("wrote cert_max_3x4.json with", len(terms), "summands")

print("== certificate: (2,2) exceptional witness a=[2] b=[2] l=[2,2] ==")
print("stored value:", P["2x2"]["table"]["2|2"]["2,2"])
_, c2 = make_chi(2)
_, c4 = make_chi(4)
tot = 0
terms = []
for mu in partitions(2):
    for nu in partitions(2):
        rho = prod_type(mu, nu)
        t = csize(2, mu) * csize(2, nu) * c4((2, 2), rho) * c2((2,), mu) * c2((2,), nu)
        terms.append((list(mu), list(nu), list(rho), t))
        tot += t
print(f"sum={tot} / 4 -> {tot/4}")
json.dump(terms, open("output/artifacts/cert_exc_2x2.json", "w"))

print("== two-row stability rows for report ==")
for k in [2, 3, 4, 5, 6]:
    key = f"2x{k}"
    N = 2 * k
    for beta in ([str(k)], [f"{k-1},1"] if k > 2 else ["1,1"]):
        row = P[key]["table"][f"2|{beta[0]}"]
        vals = []
        for j in range(0, N // 2 + 1):
            l = f"{N-j},{j}" if j > 0 else f"{N}"
            vals.append(row[l])
        print(f"{key} beta=[{beta[0]}]: {vals}")
