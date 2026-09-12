"""Full 81-field census: rho-cycle narrow class numbers + CF unit norms + Legendre/Redei logs.
Pure stdlib. Writes output/artifacts/census.json and prints summary.
"""
import math, json, os

HERE = os.path.dirname(os.path.abspath(__file__))

def primes_upto(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = [False] * len(s[i * i::i])
    return [i for i, v in enumerate(s) if v]

def reduced_forms(D):
    r = math.sqrt(D)
    forms = []
    A = int(r) + 3
    for a in range(-A, A + 1):
        if a == 0:
            continue
        for b in range(-int(r) - 4, int(r) + 4):
            t = b * b - D
            if t % (4 * a) != 0:
                continue
            c = t // (4 * a)
            if abs(r - 2 * abs(a)) < b < r:
                assert math.gcd(math.gcd(a, b), c) == 1, (D, (a, b, c))
                forms.append((a, b, c))
    return forms

def rho_form(a, b, c, D):
    r = math.sqrt(D)
    lo = r - 2 * abs(c)
    for k in range(-100000, 100000):
        b1 = -b + 2 * c * k
        if lo < b1 < r:
            assert (b1 * b1 - D) % (4 * c) == 0
            return (c, b1, (b1 * b1 - D) // (4 * c))
    raise ValueError((a, b, c, D))

def narrow_census(D):
    S = set(reduced_forms(D))
    assert len(S) > 0
    img = {}
    for f in S:
        g = rho_form(*f, D)
        assert g in S, (D, f, g)  # closure
        img[f] = g
    assert len(set(img.values())) == len(S), (D, "rho not bijective")  # permutation
    seen = set()
    ncyc = 0
    cyclens = []
    for f in S:
        if f in seen:
            continue
        cur = f
        path = []
        local = {}
        while cur not in seen and cur not in local:
            local[cur] = len(path)
            path.append(cur)
            cur = img[cur]
        if cur in local:
            cyc = path[local[cur]:]
            cyclens.append(len(cyc))
            ncyc += 1
        for x in path:
            seen.add(x)
    assert len(seen) == len(S)
    return len(S), ncyc, sorted(cyclens)

def cf_period(D):
    a0 = int(math.isqrt(D))
    assert a0 * a0 != D
    m = 0
    den = 1
    a = a0
    per = []
    while True:
        m = den * a - m
        den = (D - m * m) // den
        a = (a0 + m) // den
        per.append(a)
        if a == 2 * a0:
            break
        assert len(per) < 100000
    return per

def main():
    PR = primes_upto(2500)
    P1 = [p for p in PR if p % 4 == 1]
    pairs = [(p, q) for i, p in enumerate(P1) for q in P1[i + 1:] if p * q < 2500]
    rows = []
    for (p, q) in pairs:
        D = p * q
        nred, hplus, cyclens = narrow_census(D)
        per = cf_period(D)
        N = 1 if len(per) % 2 == 0 else -1
        h = hplus if N == -1 else hplus // 2
        assert hplus % 2 == 0 if N == 1 else True
        leg = 1 if pow(p, (q - 1) // 2, q) == 1 else -1
        leg2 = 1 if pow(q, (p - 1) // 2, p) == 1 else -1
        assert leg == leg2, (p, q)  # reciprocity, both 1 mod 4
        redei_rank = 0 if leg == 1 else 1
        pred_narrow = 1 - redei_rank
        r4 = 1 if h % 4 == 0 else 0
        assert h % 2 == 0, (D, h)  # genus 2-rank 1 forces h even
        rows.append(dict(p=p, q=q, D=D, leg=leg, redei_rank=redei_rank,
                         pred_narrow_r4=pred_narrow, period=len(per), N=N,
                         nred=nred, hplus=hplus, h=h, r4=r4,
                         cyclens=cyclens))
    out = os.path.join(HERE, "census.json")
    with open(out, "w") as f:
        json.dump(rows, f)
    # summary
    from collections import Counter
    print("nfields", len(rows))
    print("(leg,N,r4) counts:", Counter((r["leg"], r["N"], r["r4"]) for r in rows))
    print("(pred_narrow,r4,N) counts:", Counter((r["pred_narrow_r4"], r["r4"], r["N"]) for r in rows))
    bad = [r for r in rows if not (
        (r["N"] == -1 and r["r4"] == r["pred_narrow_r4"]) or (r["N"] == 1))]
    print("N=-1 mismatches vs narrow prediction:", len(bad))
    for r in bad:
        print(r)
    print("--- N=+1 fields (correction cases):", sum(1 for r in rows if r["N"] == 1))
    for r in rows:
        if r["N"] == 1:
            print({k: r[k] for k in ("p", "q", "D", "leg", "redei_rank", "pred_narrow_r4", "hplus", "h", "r4")})
    print("--- r4=1 fields:", sum(r["r4"] for r in rows))

if __name__ == "__main__":
    main()
