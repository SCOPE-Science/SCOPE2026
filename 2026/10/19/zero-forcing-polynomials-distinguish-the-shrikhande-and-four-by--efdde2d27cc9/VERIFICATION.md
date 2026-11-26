---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Both given graphs have six neighbors per vertex and two common neighbors per distinct pair, verified for all labels. This gives A²=4I+2J, with constant eigenvalue 6 and trace-determined multiplicities 6 and 9 for 2 and −2. Their root neighborhoods are respectively C6 and two disjoint triangles. A nonempty fort contained in the whites cannot lose its first vertex and a nonempty white closure is itself a fort. The independent 65,536-mask scan per graph computes simultaneous forcing by dynamic recursion to strictly smaller white masks. It reproduces the exact labeled coefficients and both minimum/total counts, comparing all 131,072 decisions against the two binary blocks by explicit bit order. Superset marking of newly found minimal forts in increasing order gives least obstruction sizes without a zeta transform; it agrees with the closure decision for every mask and gives minimal fort counts (60,48,336) and (60,144,112) at sizes 4,5,6 only, as well as both full five- and six-white classifications. A successful set is inclusion-minimal iff no one-vertex removal succeeds, by monotonicity; these scans give only size-ten minimal sets. The round counts at size ten are 1312/2304 for Shrikhande and 864/2592 for rook. For the symmetry check, the root has six neighbors forming a six-cycle; the other nine vertices have distinct two-neighbor signatures in it. Enumerating all images of the root and cycle permutations and checking the unique extensions gives exactly 192 automorphisms. The resulting 23 orbits match every CSV field, with sizes 192×15, 96×7 and 64 once. The two polynomials differ only at degrees ten and eleven by 160 and 96; the higher-degree equality has independently checked nonzero coefficients, not just a shared zero-forcing number.

## originality

PASS

The rook-side forcing polynomial and minimum sets are already covered by a stronger all-rook formula and are an expressly identified benchmark, not an originality credit. A later general classification also covers rook minimal forts. Abiad et al. give ordinary Z separation for a different cospectral pair, and for these exact two graphs give a PSD, not ordinary, separation. The supported distinct finding is that the standard full polynomials separate this canonical pair despite the equal standard minimum, with the Shrikhande counts, orbit/time data and exact comparative obstruction geometry. No checked statement or implication supplies that finding in full.

## value

PASS

A canonical pair of nonisomorphic strongly regular graphs with the same spectrum and the same ordinary forcing number is a natural controlled test of the extra information in the ordinary polynomial. The precise difference and fort-size thresholds make the distinction interpretable, and the Shrikhande orbit/time data make the exceptional minimum configurations usable as a benchmark. Independent value lies in the distinction and the Shrikhande side, not in rediscovering the rook polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
