"""Numerical verification for cubic-residue discrepancy proof (target-only lane).
Checks: (i) E_p*sqrt(p) bounded range; (ii) Koksma single-mode lower bound;
(iii) dichotomy: bound holds via k=2 when 2 is cubic non-residue;
(iv) ~2/3 of p=7 mod 12 have 2 as cubic non-residue (Chebotarev fiber prediction).
"""
import cmath, math, sympy as sp

def Ep(p):
    C = sorted(h for h in range(1, p) if pow(h, (p - 1) // 3, p) == 1)
    N = len(C)
    m = 0.0
    for i, h in enumerate(C):
        m = max(m, abs((i + 1) / N - h / p), abs(i / N - h / p))
    return m, N

def NS(p, k):
    C = [h for h in range(1, p) if pow(h, (p - 1) // 3, p) == 1]
    N = len(C)
    s = sum(cmath.exp(2j * math.pi * k * h / p) for h in C)
    return s, N  # s = N*S_k

ps = [p for p in sp.primerange(7, 3000) if p % 12 == 7]
print(f"n primes = {len(ps)}")
nonres = [p for p in ps if pow(2, (p - 1) // 3, p) != 1]
print(f"2 non-residue count = {len(nonres)}/{len(ps)} = {len(nonres)/len(ps):.3f} (expect ~0.667)")
lo = []
ok_koksma = True
ok_dich = True
for p in ps:
    m, N = Ep(p)
    lo.append(m * math.sqrt(p))
    s1, _ = NS(p, 1)
    s2, _ = NS(p, 2)
    # Koksma lower bound: E >= max(|S1|/8, |S2|/16)
    lb = max(abs(s1) / (8 * N), abs(s2) / (16 * N))
    if lb > m + 1e-9:
        ok_koksma = False
        print("KOKSMA VIOLATION", p)
    if p in nonres:
        if max(abs(s1), abs(s2)) < (math.sqrt(p) - 1) / 3 - 1e-6:
            ok_dich = False
            print("DICHOTOMY VIOLATION", p)
print(f"E_p*sqrt(p): min={min(lo):.3f} max={max(lo):.3f}")
print("Koksma lower-bound check passed:", ok_koksma)
print("Dichotomy (2 non-residue => max|NS| >= (sqrt(p)-1)/3) passed:", ok_dich)
# show k=1 alone can be tiny (necessity of k=2/dichotomy)
tiny = []
for p in ps:
    s1, N = NS(p, 1)
    if abs(s1) / N < 0.5 / math.sqrt(p):
        tiny.append(p)
print("primes where |S_1| < 0.5/sqrt(p) (k=1 alone fails):", tiny[:10])
# upper-bound shape: E_p*sqrt(p)/log(p) bounded
ush = [Ep(p)[0] * math.sqrt(p) / math.log(p) for p in ps]
print(f"E_p*sqrt(p)/log(p): min={min(ush):.3f} max={max(ush):.3f}")
