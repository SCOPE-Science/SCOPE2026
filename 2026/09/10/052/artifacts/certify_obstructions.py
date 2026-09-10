"""Certify momentum-preserving exact-resonance obstructions for lane-646 target.

Zero-amplitude (linear) divisor with (2pi)^3 factored out:
  D0(l,j) = l1 + 8*l2 + sum_k j_k^3   (tangential weights 1^3, 2^3 = 1, 8)
  M(l,j)  = l1 + 2*l2 + sum_k j_k      (momentum; must vanish)
S+ = {1,2}; S^perp excludes {-2,-1,0,1,2}.
K-M third-Melnikov exclusion: jk + jm != 0 for all pairs (k,m).

Certificates:
 (C1) two minimal nontrivial cubic exact resonances (D0=0, M=0, no pair sums 0).
 (C2) infinite P(l)=0 family: P(l)=l1+8l2-(l1+2l2)^3 = 6*l2 - L^3 + L, L=l1+2l2;
      parametrize L=4: l2 = (64-4)/6 = 10, l1 = 4-20 = -16, etc.
 (C3) one non-integrable quartic exact resonance (l!=0) blocking the 2nd BNF step.
 (C4) exhaustive counts in bounded windows.
Stdlib only. Writes certificate JSON next to this script.
"""
import json
import os

SPLUS = (1, 2)
EXCLUDED = {-2, -1, 0, 1, 2}


def D0(l1, l2, js):
    return l1 + 8 * l2 + sum(j ** 3 for j in js)


def M(l1, l2, js):
    return l1 + 2 * l2 + sum(js)


def P(l1, l2):
    L = l1 + 2 * l2
    return l1 + 8 * l2 - L ** 3


def normal(j):
    return j not in EXCLUDED


def pairs_ok(js):
    for a in range(len(js)):
        for b in range(a, len(js)):
            if js[a] + js[b] == 0:
                return False
    return True


cert = {"Splus": list(SPLUS)}

# C1: minimal cubic witnesses
cub_wits = [(-3, 0, (-5, 4, 4)), (3, 0, (-4, -4, 5))]
c1 = []
for (l1, l2, js) in cub_wits:
    assert all(normal(j) for j in js), (l1, l2, js)
    assert D0(l1, l2, js) == 0, (l1, l2, js)
    assert M(l1, l2, js) == 0, (l1, l2, js)
    assert pairs_ok(js), (l1, l2, js)
    c1.append({"l": [l1, l2], "j": list(js), "D0": 0, "M": 0,
               "pair_sums": [js[0] + js[1], js[0] + js[2], js[1] + js[2]]})
cert["C1_cubic_witnesses"] = c1

# C2: infinite family: L=4 line -> l1 = 4-2*l2 with P=0 iff 6*l2 = 60 iff l2=10;
# general: P(l) = 6*l2 - L^3 + L; show parametric infinite solutions of P=0:
# take l2 = t, L = t' ... simplest: exhibit closed form subfamily L = 1 - 6k?
# Direct: L fixed => l2 = (L^3 - L)/6; integer iff L^3-L = L(L-1)(L+1) divisible by 6 (always).
fam = []
for L in [3, 4, 5, 6, -3, -4]:
    assert (L ** 3 - L) % 6 == 0
    l2 = (L ** 3 - L) // 6
    l1 = L - 2 * l2
    assert P(l1, l2) == 0, (l1, l2, L)
    N = L + 7  # any normal N with -N, -L normal and N != +-L
    js = (N, -N, -L)
    assert all(normal(j) for j in js)
    assert D0(l1, l2, js) == 0 and M(l1, l2, js) == 0
    fam.append({"L": L, "l": [l1, l2], "j": list(js)})
cert["C2_infinite_P_family_sample"] = fam
cert["C2_lemma"] = ("P(l1,l2) = l1+8*l2-(l1+2*l2)^3 = 6*l2-L^3+L with L=l1+2*l2; "
                    "for every integer L, L^3-L is divisible by 6, giving integer "
                    "(l1,l2)=(L-2*l2,(L^3-L)/6) with P(l)=0; infinitely many. "
                    "Each yields exact D0=0 via the pair-cancel family (N,-N,-L). "
                    "NOTE: pair-cancel triples have jk+jm=0 so are EXCLUDED from the "
                    "K-M/Target third-Melnikov divisor class; C2 alone does NOT block "
                    "the loss-free bound. It documents why the exclusion exists, while "
                    "C1 shows the exclusion is INSUFFICIENT (nontrivial exact zeros remain).")

# C3: quartic witness (MINIMAL |l|_2 = 1 in |l1|<=14, |l2|<=10, j in [-10,10]^4 window;
# cubes -729-125+343+512 = 1, l-part -1, D0 = 0; M = -1+(-9-5+7+8) = 0)
ql, qj = (-1, 0), (-9, -5, 7, 8)
assert all(normal(j) for j in qj)
assert D0(ql[0], ql[1], qj) == 0
assert M(ql[0], ql[1], qj) == 0
assert (ql[0], ql[1]) != (0, 0)
cert["C3_quartic_witness"] = {"l": list(ql), "j": list(qj), "D0": 0, "M": 0,
                              "note": "l!=0 (|l|_2=1, minimal in window): non-integrable; quartic homological divisor vanishes"}

# C4: exhaustive counts
Sperp = [j for j in range(-12, 13) if j not in EXCLUDED]
seen = set()
for l1 in range(-60, 61):
    for l2 in range(-30, 31):
        J = -(l1 + 2 * l2)
        if abs(J) > 36:
            continue
        for j1 in Sperp:
            for j2 in Sperp:
                j3 = J - j1 - j2
                if j3 not in Sperp:
                    continue
                if D0(l1, l2, (j1, j2, j3)) != 0:
                    continue
                key = (l1, l2, tuple(sorted((j1, j2, j3))))
                seen.add(key)
nontrivial = [k for k in seen if pairs_ok(k[2])]
cert["C4_cubic_window"] = {"l1_range": [-60, 60], "l2_range": [-30, 30],
                           "j_window": [-12, 12],
                           "canonical_exact": len(seen),
                           "nontrivial_pair_exclusion": len(nontrivial)}
Sperp10 = set(j for j in range(-10, 11) if j not in EXCLUDED)
qseen = set()
for l1 in range(-12, 13):
    for l2 in range(-8, 9):
        J = -(l1 + 2 * l2)
        if abs(J) > 30:
            continue
        for j1 in Sperp10:
            for j2 in Sperp10:
                for j3 in Sperp10:
                    j4 = J - j1 - j2 - j3
                    if j4 not in Sperp10:
                        continue
                    if D0(l1, l2, (j1, j2, j3, j4)) != 0:
                        continue
                    qseen.add((l1, l2, tuple(sorted((j1, j2, j3, j4)))))


def paired(js):
    s = sorted(js)
    return s[0] + s[3] == 0 and s[1] + s[2] == 0


nonint = [t for t in qseen if not (t[0] == 0 and t[1] == 0 and paired(t[2]))]
cert["C4_quartic_window"] = {"l1_range": [-12, 12], "l2_range": [-8, 8],
                             "j_window": [-10, 10],
                             "canonical_exact": len(qseen),
                             "nonintegrable": len(nonint)}
cert["status"] = "VERIFY_OK"

out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "obstruction_certificate.json")
with open(out, "w") as f:
    json.dump(cert, f, indent=2)
print("VERIFY_OK")
print(json.dumps({"C1": len(c1), "C2_samples": len(fam),
                  "C4_cubic": cert["C4_cubic_window"],
                  "C4_quartic": cert["C4_quartic_window"]}, indent=2))
