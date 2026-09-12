"""Exact rational simplicial homology (REDUCED: C_0 -> Q via augmentation). H_0 here is reduced."""
from fractions import Fraction
from itertools import combinations

def betti_unreduced(faces, maxd=7):
    """faces: set of tuples (sorted). Returns dict d -> dim H_d (reduced H_0; ordinary H_{>0})."""
    F = set(faces)
    def bmat(d):
        Cd1 = sorted([f for f in F if len(f) - 1 == d - 1])
        Cd = sorted([f for f in F if len(f) - 1 == d])
        if not Cd:
            return None, 0
        rix = {f: i for i, f in enumerate(Cd1)}
        M = [[Fraction(0)] * len(Cd) for _ in Cd1]
        for j, f in enumerate(Cd):
            for k in range(len(f)):
                g = tuple(x for t, x in enumerate(f) if t != k)
                if g in rix:
                    M[rix[g]][j] += Fraction((-1) ** k)
        return M, len(Cd)
    def rank(M):
        if M is None or not M or not M[0]:
            return 0
        A = [row[:] for row in M]
        r = 0
        for c in range(len(A[0])):
            piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
            if piv is None:
                continue
            A[r], A[piv] = A[piv], A[r]
            iv = A[r][c]
            for j in range(c, len(A[0])):
                A[r][j] /= iv
            for i in range(len(A)):
                if i != r and A[i][c] != 0:
                    f = A[i][c]
                    for j in range(c, len(A[0])):
                        A[i][j] -= f * A[r][j]
            r += 1
        return r
    out = {}
    for d in range(maxd + 1):
        Md, nc = bmat(d)
        Mdp, _ = bmat(d + 1)
        out[d] = nc - rank(Md) - rank(Mdp)
    return out

def check(name, faces, expect):
    got = betti_unreduced(set(faces))
    got = {d: v for d, v in got.items() if v}
    ok = all(got.get(d, 0) == v for d, v in expect.items()) and all(got.get(d, 0) == expect.get(d, 0) for d in got)
    print(("PASS" if ok else "FAIL"), name, "got", got, "expect", expect)
    return ok

if __name__ == "__main__":
    # S^1 hollow triangle
    F = {(), (0,), (1,), (2,), (0,1), (0,2), (1,2)}
    check("S^1", F, {0:1, 1:1})
    # S^2 octahedron boundary
    def oct_face(S):
        for P in [{0,1},{2,3},{4,5}]:
            if P.issubset(set(S)):
                return False
        return True
    FO = {()}
    for r in range(1,7):
        for S in combinations(range(6), r):
            if oct_face(S):
                FO.add(S)
    check("octahedron S^2", FO, {0:1, 2:1})
    # tetrahedron boundary S^2
    FT = {(), (0,), (1,), (2,), (3,), (0,1),(0,2),(0,3),(1,2),(1,3),(2,3), (0,1,2),(0,1,3),(0,2,3),(1,2,3)}
    check("tetra S^2", FT, {0:1, 2:1})
    # solid tetra (ball)
    FB = set(FT) | {(0,1,2,3)}
    check("ball B^3", FB, {0:1})
