"""verify.py — audit the dual-route mesh census (stdlib only).
Run: python3 verify.py   (resolves logs relative to this script's directory)
"""
import sys, itertools, os

HERE = os.path.dirname(os.path.abspath(__file__))

def parse(path, mesh_tag, class_tag):
    mesh, cla = {}, {}
    with open(path) as f:
        for line in f:
            p = line.split()
            if not p:
                continue
            if p[0] == mesh_tag:
                mesh[p[1]] = list(map(int, p[2:]))
            elif p[0] == class_tag:
                cla[p[1]] = list(map(int, p[2:]))
    return mesh, cla

def main():
    A, CA = parse(os.path.join(HERE, "routeA.log"), "MESH_A", "CLASS_A")
    B, CB = parse(os.path.join(HERE, "routeB.log"), "MESH_B", "CLASS_B")
    ok = True
    agree = 0
    for m in ["M%d" % i for i in range(8)]:
        assert len(A[m]) == 10 and len(B[m]) == 10, (m, A.get(m), B.get(m))
        for n in range(10):
            if A[m][n] == B[m][n]:
                agree += 1
            else:
                ok = False
                print("DISAGREE %s n=%d A=%d B=%d" % (m, n + 1, A[m][n], B[m][n]))
    print("AGREEMENT %d/80" % agree)
    pairs = []
    for x, y in itertools.combinations(["M%d" % i for i in range(8)], 2):
        if A[x] == A[y] and B[x] == B[y]:
            pairs.append((x, y))
    print("COLLAPSE_PAIRS %s" % (pairs if pairs else "none"))
    av10 = {m: A[m][9] for m in A}
    mx = max(av10.values()); mn = min(av10.values())
    print("AV10 %s" % av10)
    print("AV10_MAXMIN %.6f (max=%d min=%d) threshold=1.5 -> %s"
          % (mx / mn, mx, mn, "PASS" if mx / mn >= 1.5 else "FAIL"))
    for m in range(8):
        base = CA["B0"] if m < 4 else CA["B1"]
        for n in range(10):
            if not (A["M%d" % m][n] >= base[n] and B["M%d" % m][n] >= base[n]):
                print("SANITY_FAIL M%d n=%d mesh < classical" % (m, n + 1))
                ok = False
    oeis1324 = [1, 2, 6, 23, 103, 513, 2762, 15793, 94776, 591950]  # A061552
    oeis1234 = [1, 2, 6, 23, 103, 513, 2761, 15767, 94359, 586590]  # A005802
    print("CLASS_A_B0 %s" % CA["B0"])
    print("CLASS_A_B1 %s" % CA["B1"])
    print("CLASS_B_B0 %s" % CB["B0"])
    print("CLASS_B_B1 %s" % CB["B1"])
    print("OEIS_1324_MATCH_A=%s B=%s" % (CA["B0"] == oeis1324, CB["B0"] == oeis1324))
    print("CLASS_B1_EQ_1234_A=%s B=%s" % (CA["B1"] == oeis1234, CB["B1"] == oeis1234))
    if CA["B0"] != CB["B0"] or CA["B1"] != CB["B1"]:
        print("CLASSICAL_ROUTE_MISMATCH")
        ok = False
    print("VERIFY_%s" % ("OK" if ok and agree == 80 else "FAIL"))
    return 0 if (ok and agree == 80) else 1

sys.exit(main())
