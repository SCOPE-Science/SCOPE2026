"""Independent exact re-verification of certificates.json (stdlib only).

For each certificate: rebuild piece (A,b,E,d,F,c0), check
  y >= 0,  sum y_r A[r] + z1 E[0] + z2 E[1] == -F,  c0 - b.y - d.z == min >= 2.
Also re-runs the full exact piecewise check. Exits nonzero on any failure.
"""
import json
from fractions import Fraction as Q
import verify_piecewise_exact as V


def build_piece(pat, combo, j):
    """Rebuild the exact piece system (A,b,E,d,F,c0) with row labels."""
    A0, b0 = V.ineq_rows()
    A = [row[:] for row in A0]; b = list(b0)
    labels = (["K%d" % (t + 1) for t in range(8)] + ["LB%d" % (t + 1) for t in range(4)])
    for i in pat:
        for s, (r, rhs) in enumerate(V.ATOM[i]):
            A.append([Q(-v) for v in r]); b.append(Q(-rhs))
            labels.append("A%d%s" % (i, "ab"[s]))
    for i in (1, 2, 3, 4):
        if i == j:
            continue
        r = [Q(0)] * 4
        r[j - 1] = Q(-5); r[i - 1] = Q(5)
        A.append(r); b.append(Q(j - i))
        labels.append("DOM%d" % i)
    E = [[Q(v) for v in V.EQS[c][0]] for c in combo]
    d = [Q(V.EQS[c][1]) for c in combo]
    elabels = ["EQ:" + c for c in combo]
    F = [Q(-3)] * 4; F[j - 1] += Q(10)
    c0 = Q(2 * (j - 4))
    return A, b, labels, E, d, elabels, F, c0

def main():
    certs = json.load(open("output/artifacts/certificates.json"))
    assert len(certs) == 6, len(certs)
    for key, C in certs.items():
        pat = tuple(C["piece"]["pat"]); combo = tuple(C["piece"]["combo"]); j = C["piece"]["j"]
        A, b, labels, E, d, elabels, F, c0 = build_piece(pat, combo, j)
        ysup = [(int(r), Q(v)) for r, v in C["cert"]["y"]]
        z = [Q(v) for v in C["cert"]["z"]]
        assert all(v >= 0 for _, v in ysup), key
        for c in range(4):
            lhs = sum(v * A[r][c] for r, v in ysup) + z[0] * E[0][c] + z[1] * E[1][c]
            assert lhs == -F[c], (key, c, lhs, -F[c])
        val = c0 - sum(v * b[r] for r, v in ysup) - (d[0] * z[0] + d[1] * z[1])
        assert val == Q(C["cert"]["value"]) == Q(C["min"]), (key, val)
        assert val >= 2, (key, val)
        print(key, "dual value", val, "OK")
    # full rerun of the vertex-enumeration proof
    V.main()
    print("CERTIFICATE RE-VERIFICATION PASSED")

if __name__ == "__main__":
    main()
