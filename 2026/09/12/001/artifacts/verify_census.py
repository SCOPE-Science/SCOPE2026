"""Certified refutation of the S1={2,3,5,7,50021} census claim.

Claim under test: x+y=1 in Z_S1^times has exactly 212 solutions up to
symmetry (1269 ordered) AND every solution satisfies Weil height h <= 14.

Strategy: the height cap makes the search space finite. We
 (1) rigorously certify e^14 < 1202605 with exact integer arithmetic, so
     every rational with h <= 14 has numerator,denominator <= 1202604 =: B;
 (2) exhaustively list every S1-smooth integer <= B by trial division;
 (3) exhaustively list every primitive triple 0<a<=b<c<=B, a+b=c, all terms
     S1-smooth (these biject with S3-orbits of solutions);
 (4) show the count is 66, not 212 (ordered: 393, not 1269).

Stdlib only. Run:  python3 verify_census.py   (prints VERIFY_OK on success)
"""
import math
import os

S1 = [2, 3, 5, 7, 50021]
B = 1202604
BPLUS = 1202605

# ---- (1) rigorous upper bound e^14 < 1202605 ----
# e = sum_{k=0..N} 1/k! + R, 0 < R < 1/(N*N!). With D = N!:
# e < (N*s + 1)/(N*D) where s = sum_{k<=N} D/k! (exact integer).
N = 22
D = math.factorial(N)
s = sum(D // math.factorial(k) for k in range(N + 1))
e_num = N * s + 1
e_den = N * D
assert pow(e_num, 14) < BPLUS * pow(e_den, 14), "height-cap certificate FAILED"
print("height-cap certificate: e^14 < 1202605  (exact big-int check PASSED)")

# ---- (2) exhaustive S1-smooth list <= B by sieve trial division ----

def is_smooth(n):
    for p in S1:
        while n % p == 0:
            n //= p
    return n == 1

smooth = [n for n in range(1, B + 1) if is_smooth(n)]
S = set(smooth)
print("S1-smooth integers <= %d: %d" % (B, len(smooth)))
assert len(smooth) == 1349
# cross-check: all prime factors of every entry lie in S1 (re-factor check)
for n in smooth:
    m = n
    for p in S1:
        while m % p == 0:
            m //= p
    assert m == 1

# ---- (3) exhaustive primitive triple enumeration ----
prim = []
for a in smooth:
    if 2 * a > B:
        break
    for c in smooth:
        if c <= a:
            continue
        if c > B:
            break
        b = c - a
        if b < a:
            continue
        if b in S and math.gcd(a, b) == 1:
            prim.append((a, b, c))
print("primitive triples 0<a<=b<c<=B, a+b=c: %d" % len(prim))
assert len(prim) == 66

# exactly one symmetric triple -> ordered count is 6*T - 3
sym = [t for t in prim if t[0] == t[1]]
assert sym == [(1, 1, 2)], sym
ordered = 6 * len(prim) - 3
print("ordered solutions via 6T-3: %d" % ordered)
assert ordered == 393

# ---- independent ordered-pair recount: x=u/v coprime S-smooth, 1-x S-unit ----
cnt = 0
for u in smooth:
    for v in smooth:
        if max(u, v) > B:
            continue
        if math.gcd(u, v) != 1:
            continue
        for sgn in (1, -1):
            d = v - sgn * u
            if d != 0 and abs(d) in S:
                cnt += 1
print("ordered pairs by direct unit loop: %d" % cnt)
assert cnt == 393 == ordered

# ---- named witnesses from the claim are present ----
T = set(prim)
for w in [(1, 1, 2), (1, 2, 3), (1, 8, 9), (1, 24, 25), (1, 48, 49)]:
    assert w in T, w
print("named witnesses (1,1,2),(1,2,3),(1,8,9),(1,24,25),(1,48,49): present")

# ---- the three 50021-divisible triples ----
big = [t for t in prim if any(v % 50021 == 0 for v in t)]
print("triples with a term divisible by 50021: %s" % (big,))
assert big == [(1, 300125, 300126), (21, 50000, 50021), (400, 50021, 50421)]

# ---- verdict on the target claim ----
print("claimed: 212 triples / 1269 ordered, all with h<=14")
print("certified under the claimed cap: 66 triples / 393 ordered")
assert (len(prim), ordered) != (212, 1269)

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "ledger_66.txt"), "w") as f:
    for t in prim:
        f.write("%d %d %d\n" % t)
print("ledger written to ledger_66.txt")
print("VERIFY_OK")
