"""Exact (Fractions) piecewise verification for the Wilf-gap-2 target.

For each (atom-pattern pat, witness-combo, argmax j) subpiece, the feasible
integer Kunz tuples satisfy a fixed linear system over integers:
  Kunz weak (8) + ki>=1 (4) + integer-strengthened atom ineqs of the two
  atom residues (4) + dominance wj>=wi (3) + 2 witness equalities.
Objective W(j) = 7kj - 3*sum_{i!=j} ki + 2j - 8 (exact on the piece).

Method (exact rational arithmetic throughout):
  * enumerate all basic solutions (2 equalities + 2 active inequalities);
  * INFEASIBLE if no feasible vertex (polyhedron is pointed -> complete);
  * recession check (2 equalities + F.v=-1 + 1 active) proves boundedness;
  * otherwise min over feasible vertices is the exact real minimum.
Subpieces whose exact real minimum is < 2 are the EXCEPTIONAL set, handled
by exact integer hand-proofs (see DRAFT.md); every other subpiece must have
exact minimum >= 2. Any violation aborts with nonzero exit.
"""
import itertools
from fractions import Fraction as Q

# ---------- constraint data (variable order k1..k4) ----------
def ineq_rows():
    A, b = [], []
    # Kunz facets as A<=b: 2k1-k2>=0 -> [-2,1,0,0]<=0; ...; 2k4+1>=k3 -> [0,0,1,-2]<=1.
    K = [([-2, 1, 0, 0], 0), ([-1, -1, 1, 0], 0), ([-1, 0, -1, 1], 0),
         ([0, -2, 0, 1], 0), ([1, -1, 0, -1], 1), ([1, 0, -2, 0], 1),
         ([0, 1, -1, -1], 1), ([0, 0, 1, -2], 1)]
    for r, rhs in K:
        A.append([Q(v) for v in r]); b.append(Q(rhs))
    for j in range(4):
        r = [Q(0)] * 4; r[j] = Q(-1)
        A.append(r); b.append(Q(-1))
    return A, b

ATOM = {
    # integer strict forms r.k >= rhs, i.e. rows appended as -r <= -rhs:
    # A1: -k1+2k3>=0 ; -k1+k2+k4>=0
    # A2: 2k1-k2>=1 ; -k2+k3+k4>=0
    # A3: k1+k2-k3>=1 ; -k3+2k4>=0
    # A4: k1+k3-k4>=1 ; 2k2-k4>=1
    1: [([-1, 0, 2, 0], 0), ([-1, 1, 0, 1], 0)],
    2: [([2, -1, 0, 0], 1), ([0, -1, 1, 1], 0)],
    3: [([1, 1, -1, 0], 1), ([0, 0, -1, 2], 0)],
    4: [([1, 0, 1, -1], 1), ([0, 2, 0, -1], 1)],
}
EQS = {
    '1a': ([-1, 1, 0, 1], -1), '1b': ([-1, 0, 2, 0], -1),
    '2a': ([2, -1, 0, 0], 0), '2b': ([0, -1, 1, 1], -1),
    '3a': ([1, 1, -1, 0], 0), '3b': ([0, 0, -1, 2], -1),
    '4a': ([1, 0, 1, -1], 0), '4b': ([0, 2, 0, -1], 0),
}
WIT = {1: ['1a', '1b'], 2: ['2a', '2b'], 3: ['3a', '3b'], 4: ['4a', '4b']}

# (pat, combo, j) subpieces whose exact real minimum is < 2 (integer proofs apply)
EXCEPTIONAL = {
    ((1, 2), ('3a', '4b'), 3), ((1, 2), ('3a', '4b'), 4),
    ((1, 3), ('2a', '4a'), 2), ((1, 3), ('2a', '4a'), 4),
    ((1, 4), ('2a', '3a'), 3), ((1, 4), ('2a', '3a'), 4),
    ((1, 4), ('2a', '3b'), 2), ((1, 4), ('2a', '3b'), 3),
    ((2, 3), ('1b', '4b'), 1), ((2, 3), ('1b', '4b'), 4),
    ((2, 4), ('1a', '3b'), 1), ((2, 4), ('1a', '3b'), 3),
    ((3, 4), ('1b', '2b'), 1), ((3, 4), ('1b', '2b'), 2),
}

def solve4(M, r):
    """Exact solve of 4x4 rational system; None if singular."""
    n = 4
    M = [[Q(x) for x in row] for row in M]
    r = [Q(x) for x in r]
    for col in range(n):
        piv = next((i for i in range(col, n) if M[i][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        r[col], r[piv] = r[piv], r[col]
        for i in range(n):
            if i != col and M[i][col] != 0:
                f = M[i][col] / M[col][col]
                for j in range(col, n):
                    M[i][j] -= f * M[col][j]
                r[i] -= f * r[col]
    return [r[i] / M[i][i] for i in range(n)]

def dot(u, v):
    return sum(a * c for a, c in zip(u, v))

def check_piece(pat, combo, j):
    A0, b0 = ineq_rows()
    A = [row[:] for row in A0]; b = list(b0)
    for i in pat:
        for r, rhs in ATOM[i]:
            # strict form r.k >= rhs  <=>  (-r).k <= -rhs
            A.append([Q(-v) for v in r]); b.append(Q(-rhs))
    for i in (1, 2, 3, 4):
        if i == j:
            continue
        r = [Q(0)] * 4
        r[j - 1] = Q(-5); r[i - 1] = Q(5)
        A.append(r); b.append(Q(j - i))
    m = len(A)
    E = [[Q(v) for v in EQS[c][0]] for c in combo]
    d = [Q(EQS[c][1]) for c in combo]
    F = [Q(-3)] * 4; F[j - 1] += Q(10)
    c0 = Q(2 * (j - 4))
    feas = []
    for r, s in itertools.combinations(range(m), 2):
        x = solve4([E[0], E[1], A[r], A[s]], [d[0], d[1], b[r], b[s]])
        if x is None:
            continue
        if all(dot(A[t], x) <= b[t] for t in range(m)):
            feas.append(dot(F, x) + c0)
    if not feas:
        return ("INFEASIBLE", None)
    for r in range(m):
        v = solve4([E[0], E[1], F, A[r]], [Q(0), Q(0), Q(-1), Q(0)])
        if v is None:
            continue
        if all(dot(A[t], v) <= 0 for t in range(m)):
            return ("UNBOUNDED", min(feas))
    return ("OPTIMAL", min(feas))

def main():
    n_ok = n_inf = n_exc = 0
    worst = None
    for pat in [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]:
        non = [i for i in (1, 2, 3, 4) if i not in pat]
        for combo in itertools.product(*[WIT[i] for i in non]):
            for j in (1, 2, 3, 4):
                status, val = check_piece(pat, combo, j)
                tag = (tuple(pat), combo, j)
                if tag in EXCEPTIONAL:
                    assert status == "OPTIMAL" and val is not None and val < 2, \
                        ("exceptional piece changed status", tag, status, val)
                    n_exc += 1
                    print("EXC  pat%s combo%s j=%d exactmin=%s" % (pat, combo, j, val))
                    continue
                if status == "INFEASIBLE":
                    n_inf += 1
                    continue
                assert status == "OPTIMAL", ("unexpected", tag, status)
                assert val is not None and val >= 2, ("BOUND FAIL", tag, val)
                n_ok += 1
                if worst is None or val < worst[0]:
                    worst = (val, tag)
    print("verified>=2: %d  infeasible: %d  exceptional(hand-proof): %d" % (n_ok, n_inf, n_exc))
    print("worst non-exceptional exact minimum:", worst)
    assert n_exc == 14
    print("ALL EXACT CHECKS PASSED")

if __name__ == "__main__":
    main()
