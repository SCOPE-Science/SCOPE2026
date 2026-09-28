"""Reproducible headline verifier for SCOPE-20260910-006.

Uses only files committed in this record:
  gen.py, gogam.py, lgv_cert.py, lgv2.py
and the Python standard library.

Checks the finite (n,k)=(6,3) equinumeration headline, nearby left
projection counts, a small Schutzenberger involution check, and the
Fischer/LGV determinant totals used as the independent third leg.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from gen import gen_gog, gen_magog, is_gog, is_magog
from gogam import schutzenberger, is_gogam, left_trap
from lgv_cert import lgv_total

ASM = {4: 42, 5: 429, 6: 7436}
LEFT_EXPECTED = {
    4: {1: 14, 2: 35, 3: 42},
    5: {1: 42, 2: 219, 3: 387},
    6: {1: 132, 2: 1594, 3: 4862},
}

def check(name, condition, detail=""):
    if not condition:
        raise AssertionError(f"{name}: {detail}")
    print(f"PASS {name}" + (f" | {detail}" if detail else ""), flush=True)

cache = {}
for n in (4, 5, 6):
    gog = gen_gog(n)
    magog = gen_magog(n)
    check(f"gog-count-{n}", len(gog) == ASM[n], str(len(gog)))
    check(f"magog-count-{n}", len(magog) == ASM[n], str(len(magog)))
    check(f"gog-valid-{n}", all(is_gog(x) for x in gog))
    check(f"magog-valid-{n}", all(is_magog(x) for x in magog))
    gogam = [schutzenberger(x) for x in magog]
    check(f"gogam-ineq-{n}", all(is_gogam(x) for x in gogam))
    for k in (1, 2, 3):
        cg = len({left_trap(x, k) for x in gog})
        cm = len({left_trap(x, k) for x in gogam})
        expected = LEFT_EXPECTED[n][k]
        check(f"left-{n}-{k}", cg == cm == expected, f"{cg}={cm}, expected {expected}")
    cache[n] = (gog, magog)

g4, m4 = cache[4]
check("S-involution-gog-4", all(schutzenberger(schutzenberger(x)) == x for x in g4))
check("S-involution-magog-4", all(schutzenberger(schutzenberger(x)) == x for x in m4))

for n, k, expected in ((3, 2, 7), (4, 2, 35), (4, 3, 42), (5, 2, 219), (5, 3, 387), (6, 3, 4862)):
    total, nrows, _ = lgv_total(0, n, k)
    check(f"LGV-{n}-{k}", total == expected, f"{total}, bottom rows {nrows}")

print("VERIFY_OK")
