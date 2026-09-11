"""Exact star-sum evaluation for lane-996 (stdlib only).

Standard reading (Graber-Pandharipande Sec.4 + quintic twist):
  per ordered star (k; q1..q4), weights w_a = lam_k - lam_qa:
    J      = int_{Mbar_0,4} prod_a 1/(w_a - psi_a)
           = (sum_a 1/w_a) / (prod_a w_a)      [dim 1, int psi_a = 1]
    P4     = 1/(e(T_pk) prod_a e(T_qa)) * prod_a 1/(-w_a) * J
    QUINT  = prod_a Q(k,qa) / (5 lam_k)^3,
             Q(k,q) = prod_{m=0..5} ((5-m) lam_k + m lam_q)
    k = 0 sector -> 0 (numerator ~lam0^4 vs denom ~lam0^3).
  Sstar = (1/24) * sum over ordered stars (orbit-stabilizer for 1/|Aut|).

Run: python3 output/artifacts/star_sum.py  (cwd = lane dir or anywhere)
Prints exact fractions + float cross-checks and variant sweep.
"""
from fractions import Fraction
from itertools import product as iprod

LAM = [Fraction(0), Fraction(1), Fraction(3), Fraction(7), Fraction(11)]
TARGET = Fraction(589731482057, 6)


def eT(lam, k):
    p = Fraction(1)
    for j in range(5):
        if j == k:
            continue
        p *= lam[k] - lam[j]
    return p


def Qedge(lam, k, q):
    p = Fraction(1)
    for m in range(6):
        p *= (5 - m) * lam[k] + m * lam[q]
    return p


def star(lam, k, qs):
    ws = [lam[k] - lam[q] for q in qs]
    if any(w == 0 for w in ws):
        return None  # pole at test point (never happens: weights distinct)
    prodw = Fraction(1)
    s = Fraction(0)
    for w in ws:
        prodw *= w
        s += Fraction(1, 1) / w
    J = s / prodw
    outer = Fraction(1)
    for w in ws:
        outer *= Fraction(1, 1) / (-w)
    ek = eT(lam, k)
    peq = Fraction(1)
    for q in qs:
        peq *= eT(lam, q)
    invN = Fraction(1, 1) / (ek * peq) * outer * J
    num = Fraction(1)
    for q in qs:
        num *= Qedge(lam, k, q)
    den = (5 * lam[k]) ** 3
    if den == 0:
        return Fraction(0)
    return num / den * invN


def total(lam, div=Fraction(24)):
    S = Fraction(0)
    n = 0
    for k in range(5):
        others = [j for j in range(5) if j != k]
        for qs in iprod(others, repeat=4):
            v = star(lam, k, qs)
            assert v is not None
            S += v
            if v != 0:
                n += 1
    return S / div, n


def main():
    S, n = total(LAM)
    print("nonzero ordered terms:", n, "(of 4*4^4 + ... = 1020; k=0 block vanishes)")
    print("Sstar standard /24 =", S)
    print("  float:", float(S))
    print("target              =", TARGET)
    print("  float:", float(TARGET))
    print("match:", S == TARGET)
    for k in range(5):
        others = [j for j in range(5) if j != k]
        Sk = sum(star(LAM, k, qs) for qs in iprod(others, repeat=4)) / Fraction(24)
        print(f"  central k={k} lam={LAM[k]}: {Sk}  float {float(Sk)}")
    # J cross-check on a sample star
    k, qs = 1, (0, 2, 3, 4)
    ws = [LAM[k] - LAM[q] for q in qs]
    J = sum(Fraction(1, 1) / w for w in ws)
    from functools import reduce
    import operator
    J /= reduce(operator.mul, ws, Fraction(1))
    print("sample J(k=1,qs=(0,2,3,4)) =", J, float(J))
    print("sample star value =", star(LAM, k, qs), float(star(LAM, k, qs)))
    # Variant sweep: alternate Mbar integral / normalizations
    print("--- variants (all /24 unless noted) ---")
    terms = []
    for k in range(1, 5):
        others = [j for j in range(5) if j != k]
        for qs in iprod(others, repeat=4):
            ws = [LAM[k] - LAM[q] for q in qs]
            prodw = Fraction(1)
            s = Fraction(0)
            for w in ws:
                prodw *= w
                s += Fraction(1, 1) / w
            Jv = s / prodw
            sw = sum(ws)
            Ja = Fraction(1, 1) / sw if sw != 0 else None
            outer = Fraction(1)
            for w in ws:
                outer *= Fraction(1, 1) / (-w)
            base = Fraction(1, 1) / (eT(LAM, k) *
                    __import__('functools').reduce(lambda a, b: a * b,
                    [eT(LAM, q) for q in qs], Fraction(1))) * outer
            num = Fraction(1)
            for q in qs:
                num *= Qedge(LAM, k, q)
            den3 = (5 * LAM[k]) ** 3
            terms.append((base, Jv, Ja, num, den3))
    def show(name, f):
        Sv = Fraction(0)
        skip = 0
        for t in terms:
            try:
                Sv += f(*t)
            except ZeroDivisionError:
                skip += 1
        Sv /= Fraction(24)
        print(f"{name}: {Sv} float {float(Sv)} match={Sv == TARGET} skip={skip}")
    show("Jalt=1/sum(w)", lambda b, J, Ja, n, d: b * Ja * n / d if Ja is not None else Fraction(0))
    show("no-node-subtraction", lambda b, J, Ja, n, d: b * J * n)
    # pure P4
    P = Fraction(0)
    for k in range(5):
        others = [j for j in range(5) if j != k]
        for qs in iprod(others, repeat=4):
            ws = [LAM[k] - LAM[q] for q in qs]
            prodw = Fraction(1)
            s = Fraction(0)
            for w in ws:
                prodw *= w
                s += Fraction(1, 1) / w
            Jv = s / prodw
            outer = Fraction(1)
            for w in ws:
                outer *= Fraction(1, 1) / (-w)
            peq = Fraction(1)
            for q in qs:
                peq *= eT(LAM, q)
            P += Fraction(1, 1) / (eT(LAM, k) * peq) * outer * Jv
    P /= Fraction(24)
    print("pure-P4 /24:", P, float(P))
    print("VERIFY:", "OK" if S != TARGET and P != TARGET else "UNEXPECTED-MATCH")


if __name__ == "__main__":
    main()
