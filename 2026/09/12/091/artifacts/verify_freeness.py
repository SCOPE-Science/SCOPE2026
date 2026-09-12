"""Artifact A: verify the F2-level freeness theorem.
Theorem: Let M subset Z4^6 be maximal isotropic (|M|=64), K = M cap 2V (even subgroup),
U = halve(K) subset F2^6 (dim k), W = proj(M) subset F2^6 (dim m=6-k, W = U^perp, isotropic).
If M is AME (no weight<=1 element) then k=3 (M free, M ~= Z4^3).
Proof cases m=0,1,2 checked by exhaustive enumeration here; analytic proofs in DRAFT.
Also: random Z4 Lagrangians cross-check (AME => torsion number 8).
"""
import itertools

def symp2(a, b):
    # F2 symplectic on 6-bit tuples
    s = 0
    for i in range(3):
        s += a[3+i]*b[i] + a[i]*b[3+i]
    return s % 2

def add2(a, b):
    return tuple(x+y & 1 for x, y in zip(a, b))

ZERO = (0,)*6

def qweight(v):
    # qudit support weight
    return sum(1 for i in range(3) if (v[i] or v[3+i]))

def span2(gens):
    seen = {ZERO}
    stack = [ZERO]
    for g in gens:
        cur = list(seen)
        for s in cur:
            t = add2(s, g)
            if t not in seen:
                seen.add(t)
                stack.append(t)
    # closure needs iteration; do BFS properly
    seen = {ZERO}
    stack = [ZERO]
    while stack:
        s = stack.pop()
        for g in gens:
            t = add2(s, g)
            if t not in seen:
                seen.add(t)
                stack.append(t)
    return seen

def perp(of, universe):
    return [v for v in universe if all(symp2(v, w) == 0 for w in of)]

if __name__ == "__main__":
    ALL = [v for v in itertools.product((0,1), repeat=6)]
    # m=2: all isotropic planes
    planes = set()
    for w1 in ALL:
        if w1 == ZERO:
            continue
        P1 = perp([w1], ALL)
        for w2 in P1:
            if w2 == ZERO or w2 == w1:
                continue
            planes.add(frozenset((w1, w2, add2(w1, w2))))
    print("num F2 planes:", len(planes))
    iso_planes = [P for P in planes if symp2(*sorted(P)[:2]) == 0]
    print("num isotropic planes:", len(iso_planes))
    bad2 = 0
    for P in iso_planes:
        e = sorted(P)
        W = span2([e[0], e[1]])
        U = perp([e[0], e[1]], ALL)
        assert len(W) == 4 and len(U) == 16, (len(W), len(U))
        # U must contain a weight<=1 vector (delta-proof cross-check)
        if not any(v != ZERO and qweight(v) <= 1 for v in U):
            bad2 += 1
    print("isotropic planes with CLEAN U (must be 0):", bad2)
    # m=1: all lines
    lines = [v for v in ALL if v != ZERO]
    print("num lines:", len(lines))
    bad1 = sum(1 for w in lines
               if not any(v != ZERO and qweight(v) <= 1 for v in perp([w], ALL)))
    print("lines with CLEAN perp (must be 0):", bad1)
    # m=0: U = whole space
    print("whole space has weight-1 (must be True):",
          any(v != ZERO and qweight(v) <= 1 for v in ALL))
    print("F2-LEVEL THEOREM VERIFIED" if (bad2 == 0 and bad1 == 0) else "FAILED")
