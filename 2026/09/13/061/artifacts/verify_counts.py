"""Brute-force verification (exact rationals) of R_k line-arrangement counts for k=1..4."""
from fractions import Fraction

def S_set(k):
    M = [a for a in range(-k + 1, k + 1)]
    halves = [Fraction(a, 2) for a in range(-k + 1, k + 1)]
    S = sorted(set([Fraction(a) for a in M]) | set(halves))
    return M, S

def brute(k):
    M, S = S_set(k)
    Ms = set(Fraction(a) for a in M)
    # lines as (family, const): A: u=a; B: v=b; C: u-v=c; D: u+v=d
    lines = ([('A', Fraction(a)) for a in M] + [('B', b) for b in S]
             + [('C', Fraction(c)) for c in M] + [('D', Fraction(d)) for d in M])
    N = len(lines)
    # pairwise cross-family meetings
    P2 = 0
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if lines[i][0] != lines[j][0]:
                P2 += 1
    # points: map point -> list of line indices
    def meet_pt(f1, c1, f2, c2):
        # returns (u,v) as Fractions or None if parallel
        if f1 == f2:
            return None
        # solve
        # A: u=c1; B: v=c2; C: u-v=c1... general linear solve
        def eq(f, c):
            if f == 'A':
                return (Fraction(1), Fraction(0), c)
            if f == 'B':
                return (Fraction(0), Fraction(1), c)
            if f == 'C':
                return (Fraction(1), Fraction(-1), c)
            if f == 'D':
                return (Fraction(1), Fraction(1), c)
        a1, b1, r1 = eq(f1, c1)
        a2, b2, r2 = eq(f2, c2)
        det = a1 * b2 - a2 * b1
        if det == 0:
            return None
        u = (r1 * b2 - r2 * b1) / det
        v = (a1 * r2 - a2 * r1) / det
        return (u, v)
    pts = {}
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            p = meet_pt(lines[i][0], lines[i][1], lines[j][0], lines[j][1])
            if p is not None:
                pts.setdefault(p, []).append((i, j))
    # multiplicity per point = # distinct lines through it
    mult = {}
    for p, pairs in pts.items():
        ls = set()
        for (i, j) in pairs:
            ls.add(i)
            ls.add(j)
        mult[p] = len(ls)
    from collections import Counter
    mc = Counter(mult.values())
    Cnum = len(pts)
    Sig = sum(m - 1 for m in mult.values())
    # triple / quadruple concurrency counts by definition
    ABC = sum(1 for a in M for b in S if (Fraction(a) - b) in Ms)
    ABD = sum(1 for a in M for b in S if (Fraction(a) + b) in Ms)
    ACD = sum(1 for a in M for c in M for d in M if c + d == 2 * a)
    BCD = sum(1 for c in M for d in M if (Fraction(d - c, 2)) in set(S))
    T3 = ABC + ABD + ACD + BCD
    Q = sum(1 for a in M for b in S
            if (Fraction(a) - b) in Ms and (Fraction(a) + b) in Ms)
    # identity checks
    assert P2 == sum(m * (m - 1) // 2 for m in mult.values()), (k, P2)
    assert T3 == sum(m * (m - 1) * (m - 2) // 6 for m in mult.values()), (k, T3)
    assert Q == sum(m * (m - 1) * (m - 2) * (m - 3) // 24 for m in mult.values()), (k, Q)
    assert max(mult.values()) <= 4
    assert Sig == P2 - T3 + Q, (k, Sig, P2, T3, Q)
    B = N
    Delta = B * B - 4 * Sig
    # closed forms
    expB2 = (41 * k * k) // 2 if k % 2 == 0 else (41 * k * k + 1) // 2
    expD = -(k * k) if k % 2 == 0 else -(k * k + 2)
    assert Sig == expB2, (k, Sig, expB2)
    assert Delta == expD, (k, Delta, expD)
    # finite-field check mod p (large prime): complement count = p^2 - N p + Sig
    p = 1009
    Fp_lines = []
    inv2 = (p + 1) // 2
    Smod = sorted(set([a % p for a in M]) | set([(a * inv2) % p for a in M]))
    # count union over grid
    covered = 0
    Amod = [a % p for a in M]
    Cmod = [c % p for c in M]
    Dmod = [d % p for d in M]
    for u in range(p):
        for v in range(p):
            hit = (u in set(Amod)) or (v in set(Smod)) or ((u - v) % p in set(Cmod)) or ((u + v) % p in set(Dmod))
            if hit:
                covered += 1
    comp = p * p - covered
    assert comp == p * p - N * p + Sig, (k, comp, p * p - N * p + Sig)
    print(f"k={k}: N={N} P2={P2} T3={T3} Q={Q} Sig={Sig} Delta={Delta} "
          f"multdist={dict(sorted(mc.items()))} mod{p}-check OK")

for k in (1, 2, 3, 4):
    brute(k)
print("ALL COUNT CHECKS PASSED")
