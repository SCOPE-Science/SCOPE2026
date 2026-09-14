"""Independent certificate checker for the 8x8 window bound.

Reads run_lo.log / run_hi.log, re-verifies:
  (1) total == 200^144 (conservation checksum),
  (2) 4*crossed_lo - 200^144 > 0  (P_0.495 >= 1/4),
  (3) 3*200^144 - 4*crossed_hi > 0 (P_0.505 <= 3/4),
using only exact integer arithmetic. Prints PASS/FAIL.
"""
import re, sys
from fractions import Fraction

def get(path, key):
    txt = open(path).read()
    m = re.search(key + r"=(\d+)", txt)
    assert m, (path, key)
    return int(m.group(1))

ok = True
T = 200**144
for path, name, check in [("output/artifacts/run_lo.log","lo",None),
                          ("output/artifacts/run_hi.log","hi",None)]:
    c = get(path, "crossed")
    u = get(path, "uncrossed")
    t = get(path, "total")
    cons = (c + u == t and t == T)
    print(f"{name}: conservation crossed+uncrossed==total==200^144: {cons}")
    ok &= cons
clo = get("output/artifacts/run_lo.log","crossed")
chi = get("output/artifacts/run_hi.log","crossed")
g1 = 4*clo - T
g2 = 3*T - 4*chi
print("4*C(0.495)-200^144 =", str(g1)[:60], "... digits:", len(str(g1)), ">0:", g1>0)
print("3*200^144-4*C(0.505) =", str(g2)[:60], "... digits:", len(str(g2)), ">0:", g2>0)
print("P_0.495 =", float(Fraction(clo,T)), " P_0.505 =", float(Fraction(chi,T)))
ok &= (g1>0 and g2>0)
print("CERTIFICATE:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
