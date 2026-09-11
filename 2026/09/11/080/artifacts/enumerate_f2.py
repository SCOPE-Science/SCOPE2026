"""Relative floor-diagram ledger for F2, class beta = E+4F (a=1 in B-basis: beta = B+2F).

Conventions (documented in DRAFT.md):
- CJMR (Cavalieri-Johnson-Markwig-Ranganathan) floor diagrams for F_k, k=2,
  genus 0, primary (psi-power 0 everywhere).
- B-side (left): transverse fixed profile (1^4): 4 distinct fixed ends weight 1.
- E-side (right): total weight beta.E = 2. Five profiles:
    A: fixed (2) ......... 1 fixed end w2
    B: fixed (1,1) ....... 2 fixed ends w1,w1 (distinct)
    C: moving (2) ........ 1 moving end w2
    D: moving (1,1) ...... 2 moving ends w1,w1 (distinct)
    E: mixed (1f+1m) ..... 1 fixed w1 + 1 moving w1 (distinct)
- Vertices: n = n2 + 2a + g - 1 with a=1,g=0 => n = n2+1.
  One white (size 1), rest black (size 0). All g=0, k=0 (primary).
- Divergence: white: signed(right-left)+edges = -k*s = -2.
  black: = 0. Sign: right/outgoing +, left/incoming -.
  Edge i->j (i<j) weight w: contributes +w at i, -w at j.
  Left end w at v: contributes -w. Right end w at v: contributes +w.
- Thickening (primary): white needs 0 thick flags; black needs exactly 2;
  each compact edge has exactly one thick flag.
  Fixed ends are normal; moving ends are thick.
  => white gets no moving ends; edge incident to white is normal on white side
     (thick on other side). Black-black edges: 2 possible thick sides.
- Multiplicity: complex = prod_e w(e) (vertex factors = 1 for rational
  primary size<=1 floors: unique fiber line; documented assumption, matched
  with CJMR Def 4.3 one-point values = 1 in these degrees).
  Refined: prod_e [w(e)]_q, [m]_q = (q^{m/2}-q^{-m/2})/(q^{1/2}-q^{-1/2}).
  Signed (tropical Welschinger, q->-1): 0 if any w even else
  prod_e (-1)^{(w-1)/2}.
- Graphs: all trees on ordered vertex set (edges i<j), weights 1..WMAX=8.
  Ends labeled (distinct); every assignment enumerated once.

Output: per-profile ledgers + refined polynomials + signed sums.
"""
import itertools
import json
from collections import defaultdict

K = 2
WMAX = 8

def trees(n):
    """All trees on vertices 0..n-1 (as edge sets), edges oriented i<j."""
    if n == 1:
        yield []
        return
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    # choose n-1 pairs forming a tree (connected)
    for combo in itertools.combinations(pairs, n-1):
        # connectivity check via union-find
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        ok = True
        for (a, b) in combo:
            ra, rb = find(a), find(b)
            if ra == rb:
                ok = False
                break
            parent[ra] = rb
        if not ok:
            continue
        roots = {find(i) for i in range(n)}
        if len(roots) == 1:
            yield list(combo)

def qnum(m):
    """Return refined [m]_q as dict exponent->coeff in q^{1/2} powers.
    [m] = q^{(m-1)/2}+q^{(m-3)/2}+...+q^{-(m-1)/2}. Exponents in half-integers."""
    return {(m-1-2*j)/2: 1 for j in range(m)}

def mul_qpolys(p, q):
    r = defaultdict(int)
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1+e2] += c1*c2
    return dict(r)

def add_qpolys(p, q):
    r = defaultdict(int, p)
    for e, c in q.items():
        r[e] += c
    return dict(r)

def eval_qm1(poly):
    """Evaluate q-polynomial (exponents possibly half-integer) at q=-1.
    q^{1/2} -> i. Returns complex (should be real integer)."""
    import cmath
    s = 0j
    for e, c in poly.items():
        s += c * (1j ** (2*e))
    return s

PROFILES = {
    "A_fix2": {"fixed": [2], "moving": []},
    "B_fix11": {"fixed": [1, 1], "moving": []},
    "C_mov2": {"fixed": [], "moving": [2]},
    "D_mov11": {"fixed": [], "moving": [1, 1]},
    "E_mix11": {"fixed": [1], "moving": [1]},
}
BLEFT = [1, 1, 1, 1]  # 4 distinct fixed left ends

def enumerate_profile(name):
    prof = PROFILES[name]
    RF, RM = prof["fixed"], prof["moving"]
    nF, nM = len(RF), len(RM)
    n2 = nM
    n = n2 + 1
    results = []  # (white_pos, edges, weights, left_assign, rightF_assign, rightM_assign, thickchoice, cplx, signed)
    refined_total = defaultdict(int)  # half-int exponent -> coeff (times cplx structure? refined = sum_D prod[w]_q)
    cplx_total = 0
    signed_total = 0
    ndiag = 0
    # assignments: left ends distinct -> vertex per end: n^4 possibilities
    # right fixed distinct -> n^nF; right moving distinct -> restricted to black vertices
    for white_pos in range(n):
        blacks = [v for v in range(n) if v != white_pos]
        for edge_list in trees(n):
            nedges = len(edge_list)
            # weight loops
            for weights in itertools.product(range(1, WMAX+1), repeat=nedges) if nedges else [()]:
                wdict = dict(zip(edge_list, weights))
                # black-black edges need thick-side choices
                bb = [(a, b) for (a, b) in edge_list if a != white_pos and b != white_pos]
                nbb = len(bb)
                for lassign in itertools.product(range(n), repeat=4):
                    L = [0]*n
                    for k, v in enumerate(lassign):
                        L[v] += BLEFT[k]
                    for fassign in itertools.product(range(n), repeat=nF) if nF else [()]:
                        RFv = [0]*n
                        for k, v in enumerate(fassign):
                            RFv[v] += RF[k]
                        # moving ends: each to a black vertex only (white gets none)
                        if nM and not blacks:
                            continue
                        for massign in itertools.product(blacks, repeat=nM) if nM else [()]:
                            RMv = [0]*n
                            RMcount = [0]*n
                            for k, v in enumerate(massign):
                                RMv[v] += RM[k]
                                RMcount[v] += 1
                            # thick choices for bb edges
                            for tmask in range(1 << nbb):
                                # thick count per vertex from edges
                                thick = [0]*n
                                # edges incident to white: thick on other side (forced)
                                # bb edges: thick on chosen side
                                valid = True
                                for ii, (a, b) in enumerate(edge_list):
                                    if a == white_pos or b == white_pos:
                                        other = b if a == white_pos else a
                                        thick[other] += 1
                                    else:
                                        j = bb.index((a, b))
                                        side = (tmask >> j) & 1
                                        thick[a if side == 0 else b] += 1
                                for v in range(n):
                                    thick[v] += RMcount[v]
                                # check thick requirements
                                if thick[white_pos] != 0:
                                    continue
                                if any(thick[v] != 2 for v in blacks):
                                    continue
                                # divergence check
                                bal = [0]*n
                                for v in range(n):
                                    bal[v] = RFv[v] + RMv[v] - L[v]
                                for (a, b) in edge_list:
                                    w = wdict[(a, b)]
                                    bal[a] += w
                                    bal[b] -= w
                                if bal[white_pos] != -2:
                                    continue
                                if any(bal[v] != 0 for v in blacks):
                                    continue
                                # valid diagram
                                c = 1
                                for w in weights:
                                    c *= w
                                # refined factor prod [w]_q
                                ref = {0: 1}
                                for w in weights:
                                    ref = mul_qpolys(ref, qnum(w))
                                # signed: 0 if any even else prod (-1)^((w-1)/2)
                                if any(w % 2 == 0 for w in weights):
                                    s = 0
                                else:
                                    s = 1
                                    for w in weights:
                                        s *= (-1) ** ((w-1)//2)
                                cplx_total += c
                                signed_total += s
                                refined_total = add_qpolys(refined_total, ref)
                                ndiag += 1
                                results.append((white_pos, tuple(edge_list), tuple(weights),
                                                tuple(lassign), tuple(fassign), tuple(massign), tmask, c, s))
    return {"n": n, "ndiag": ndiag, "complex": cplx_total, "signed": signed_total,
            "refined": dict(sorted(refined_total.items())), "diagrams": results}

def main():
    out = {}
    for name in PROFILES:
        r = enumerate_profile(name)
        ref = r.pop("diagrams")
        print(f"{name}: n={r['n']} ndiag={r['ndiag']} complex={r['complex']} signed={r['signed']} refined={r['refined']}")
        # verify refined at q=1 equals complex, at q=-1 equals signed
        rq1 = sum(c * 1 for e, c in r["refined"].items())
        ev = eval_qm1(r["refined"])
        print(f"   check q=1: {rq1} (cplx {r['complex']}), q=-1: {ev} (signed {r['signed']})")
        assert rq1 == r["complex"], "q=1 mismatch"
        assert abs(ev - r["signed"]) < 1e-6, "q=-1 mismatch"
        out[name] = r
    with open("ledger.json", "w") as f:
        json.dump({k: {kk: vv for kk, vv in v.items()} for k, v in out.items()}, f, indent=1)
    print("wrote ledger.json")

if __name__ == "__main__":
    main()
