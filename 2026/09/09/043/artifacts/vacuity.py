"""vacuity.py — machine-check the shading-removal lemmas (stdlib only).
For each of the 6 vacuous cases, exhaustively enumerate all relative orders of
(a,b,c,d,v) (permutations of 0..4 — covers every total order) satisfying:
  (i)  (a,b,c,d) is the claimed base pattern (1324 or 2143), and
  (ii) v lies in the shaded region's value-interval;
then assert the replacement 4-tuple is again the base pattern (with the
improved index measure noted). The minimal-counterexample framing
(minimal i1 / minimal i2-then-maximal i1 / minimal i3) then forces every
permutation containing the classical pattern to contain an UNSHADED occurrence.
Also asserts the M4/M7 replacements FAIL (produce 0132/1023), i.e. those
shadings are genuinely restrictive — consistent with the census.
"""
import itertools

def pat(t):
    s = sorted(t)
    return tuple(s.index(x) for x in t)

P1324 = (0, 2, 1, 3)
P2143 = (1, 0, 3, 2)

# (name, base, region-value-constraint, replacement-tuple-of-roles, replacement-pattern-must-equal-base?)
# roles: a,b,c,d,v
cases = [
    # M0: corner (0,0) over 1324; region v<min; repl (v,b,c,d), improves i1
    ("M0", P1324, lambda a, b, c, d, v: v < min(a, b, c, d),
     lambda a, b, c, d, v: (v, b, c, d), True),
    # M1: edge (0,1) over 1324; region a<v<c; repl (v,b,c,d), improves i1
    ("M1", P1324, lambda a, b, c, d, v: a < v < c,
     lambda a, b, c, d, v: (v, b, c, d), True),
    # M2: near-corner (1,1) over 1324; region a<v<c; repl (v,b,c,d), same i2 bigger i1
    ("M2", P1324, lambda a, b, c, d, v: a < v < c,
     lambda a, b, c, d, v: (v, b, c, d), True),
    # M3: central (2,2) over 1324; region c<v<b; repl (a,b,v,d), improves i3
    ("M3", P1324, lambda a, b, c, d, v: c < v < b,
     lambda a, b, c, d, v: (a, b, v, d), True),
    # M5: edge (0,1) over 2143; region b<v<a; repl (v,b,c,d), improves i1
    ("M5", P2143, lambda a, b, c, d, v: b < v < a,
     lambda a, b, c, d, v: (v, b, c, d), True),
    # M6: near-corner (1,1) over 2143; region b<v<a; repl (v,b,c,d), same i2 bigger i1
    ("M6", P2143, lambda a, b, c, d, v: b < v < a,
     lambda a, b, c, d, v: (v, b, c, d), True),
    # M4: corner (0,0) over 2143; region v<b; repl (v,b,c,d) expected NOT base
    ("M4", P2143, lambda a, b, c, d, v: v < b,
     lambda a, b, c, d, v: (v, b, c, d), False),
    # M7: central (2,2) over 2143; region a<v<d; repl (a,b,v,d) expected NOT base
    ("M7", P2143, lambda a, b, c, d, v: a < v < d,
     lambda a, b, c, d, v: (a, b, v, d), False),
]

ok = True
for name, base, inreg, repl, expect_base in cases:
    ncon = 0
    bad = 0
    replpats = set()
    for perm in itertools.permutations(range(5)):
        a, b, c, d, v = perm
        if pat((a, b, c, d)) != base:
            continue
        if not inreg(a, b, c, d, v):
            continue
        ncon += 1
        rp = pat(repl(a, b, c, d, v))
        replpats.add(rp)
        if expect_base and rp != base:
            bad += 1
        if not expect_base and rp == base:
            bad += 1
    status = "VACUOUS" if expect_base else "GENUINE"
    flag = "OK" if bad == 0 and ncon > 0 else "FAIL"
    if flag == "FAIL":
        ok = False
    print("%s %s: constrained-orders=%d repl-patterns=%s -> %s"
          % (name, status, ncon, sorted(replpats), flag))
print("VACUITY_%s" % ("OK" if ok else "FAIL"))
