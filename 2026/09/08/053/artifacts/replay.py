"""Lane 201: whole-period Goldbach band certification over [210000,252000).
Generates certified_summary.json, G_table.json, rho_table.json in its own dir.
Stdlib only. Scope is half-open [LO,HI): 21000 evens, 200 periods mod 210,
1400 per mod-30 band. Also serves as the independent replay script.
Normalization (auditor repair, option A): H is the UNORDERED-count prediction
H(n) = C2*n/(log n)^2 * S(n), compared to unordered G(n) = #{p <= n/2}.
(The pre-repair version used 2*C2, the ordered-count normalization, against
unordered G, which depressed rho by a factor ~2.)
"""
import bisect, hashlib, json, math, os, random
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 60
HERE = os.path.dirname(os.path.abspath(__file__))
LO, HI = 210000, 252000
C2F = 0.6601618158468695
C2D = Decimal("0.6601618158468695739278122243")
BANDS = list(range(0, 30, 2))

# ---- Lemma L1: prime table to HI + segmented cross-check ----
bs = bytearray(b'\x01') * (HI + 1)
bs[0] = bs[1] = 0
for i in range(2, int(HI ** 0.5) + 1):
    if bs[i]:
        bs[i * i:HI + 1:i] = b'\x00' * (((HI - i * i) // i) + 1)
primes = [i for i in range(HI + 1) if bs[i]]
# segmented sieve on [LO,HI] with independent base-prime generation
base = [i for i in range(2, int(HI ** 0.5) + 1)
        if all(i % p for p in range(2, int(i ** 0.5) + 1))]
seg = bytearray(b'\x01') * (HI - LO + 1)
for p in base:
    start = max(p * p, ((LO + p - 1) // p) * p)
    for j in range(start, HI + 1, p):
        seg[j - LO] = 0
seg_primes = [LO + i for i, v in enumerate(seg) if v and LO + i >= 2]
plain_in = [p for p in primes if LO <= p <= HI]
assert seg_primes == plain_in, "segmented-sieve mismatch"

def mr(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 7, 61):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

random.seed(201)
samp = random.sample(range(LO, HI + 1), 2000)
mr_bad = sum(1 for n in samp if bool(bs[n]) != mr(n))
assert mr_bad == 0

# ---- unordered Goldbach counts G(n), n even in [LO,HI) ----
Gser = {}
for n in range(LO, HI, 2):
    idx = bisect.bisect_right(primes, n // 2)
    c = 0
    for k in range(idx):
        if bs[n - primes[k]]:
            c += 1
    Gser[n] = c

def sexact(n):
    m = n
    while m % 2 == 0:
        m //= 2
    s = Fraction(1, 1)
    d = 3
    while d * d <= m:
        if m % d == 0:
            s *= Fraction(d - 1, d - 2)
            while m % d == 0:
                m //= d
        d += 2
    if m > 1:
        s *= Fraction(m - 1, m - 2)
    return s

def sfloat(n):
    m = n
    while m % 2 == 0:
        m //= 2
    s = 1.0
    d = 3
    while d * d <= m:
        if m % d == 0:
            s *= (d - 1) / (d - 2)
            while m % d == 0:
                m //= d
        d += 2
    if m > 1:
        s *= (m - 1) / (m - 2)
    return s

assert max(abs(float(sexact(n)) - sfloat(n)) for n in range(LO, HI, 2)) < 2e-15

N = 1400
Gsum = {c: 0 for c in BANDS}
for n, g in Gser.items():
    Gsum[n % 30] += g
Gmean = {c: Fraction(Gsum[c], N) for c in BANDS}
oG = sorted(Gmean, key=lambda c: Gmean[c])
gG = [Gmean[oG[i + 1]] - Gmean[oG[i]] for i in range(14)]

Rsum = {c: 0.0 for c in BANDS}
rhoF = {}
for n, g in Gser.items():
    h = C2F * n / (math.log(n) ** 2) * sfloat(n)
    r = g / h
    rhoF[n] = r
    Rsum[n % 30] += r
muF = {c: Rsum[c] / N for c in BANDS}
oR = sorted(muF, key=lambda c: muF[c])
dR = min(muF[oR[i + 1]] - muF[oR[i]] for i in range(14))

RsumD = {c: Decimal(0) for c in BANDS}
for n, g in Gser.items():
    se = sexact(n)
    ln = Decimal(n).ln()
    hD = C2D * Decimal(n) / (ln * ln) * Decimal(se.numerator) / Decimal(se.denominator)
    RsumD[n % 30] += Decimal(g) / hD
muD = {c: RsumD[c] / Decimal(N) for c in BANDS}
oD = sorted(muD, key=lambda c: muD[c])
assert oD == oR, (oD, oR)
assert max(abs(muF[c] - float(muD[c])) for c in BANDS) < 1e-12
dD = min(muD[oD[i + 1]] - muD[oD[i]] for i in range(14))

E = max(abs(v - 1) for v in rhoF.values())
nE = max(Gser, key=lambda n: abs(rhoF[n] - 1))
meanrho = sum(rhoF.values()) / len(rhoF)
varF = {c: sum((rhoF[n] - muF[c]) ** 2 for n in Gser if n % 30 == c) / N for c in BANDS}
sha = hashlib.sha256(",".join(str(Gser[n]) for n in sorted(Gser)).encode()).hexdigest()

art = {
    "scope": {"lo": LO, "hi_exclusive": HI, "nevens": len(Gser),
              "periods_mod210": 200, "per_band": N},
    "C2": C2F,
    "H_def": "H(n)=C2*n/(log n)^2 * S(n), S(n)=prod_{odd p|n}(p-1)/(p-2), natural log; unordered-count prediction compared to unordered G(n)",
    "G_sums": {str(c): Gsum[c] for c in sorted(Gsum)},
    "G_means_exact": {str(c): str(Gmean[c]) for c in sorted(Gmean)},
    "G_order": oG,
    "G_gaps_exact": [str(g) for g in gG],
    "G_mingap_exact": str(min(gG)),
    "rho_means_float": {str(c): muF[c] for c in sorted(muF)},
    "rho_means_dec50": {str(c): str(muD[c]) for c in sorted(muD)},
    "rho_order": oR,
    "rho_delta_float": dR,
    "rho_delta_dec": str(dD),
    "E": E, "nE": nE, "G_at_nE": Gser[nE], "rho_at_nE": rhoF[nE],
    "mean_rho": meanrho,
    "rho_spread": max(muF.values()) - min(muF.values()),
    "variances": {str(c): varF[c] for c in sorted(varF)},
    "minG": min(Gser.values()), "maxG": max(Gser.values()),
    "sha_G_series": sha, "pi_HI": len(primes),
    "seg_primes_in_scope": len(plain_in), "mr_mismatches": mr_bad,
}
with open(os.path.join(HERE, "certified_summary.json"), "w") as f:
    json.dump(art, f, indent=1)
with open(os.path.join(HERE, "G_table.json"), "w") as f:
    json.dump({str(n): Gser[n] for n in sorted(Gser)}, f)
with open(os.path.join(HERE, "rho_table.json"), "w") as f:
    json.dump({str(n): rhoF[n] for n in sorted(rhoF)}, f)
print("pi_HI:", len(primes), "seg_in_scope:", len(plain_in), "mr_bad:", mr_bad)
print("G_order:", oG, "G_mingap:", min(gG), float(min(gG)))
print("rho_order:", oR, "rho_delta:", dR)
print("E:", E, "at:", nE, "G:", Gser[nE], "mean_rho:", meanrho)
print("sha:", sha, "minG,maxG:", min(Gser.values()), max(Gser.values()))
