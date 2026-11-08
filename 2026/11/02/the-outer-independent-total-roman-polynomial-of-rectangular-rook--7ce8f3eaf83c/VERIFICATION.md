---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The outer-independent zero set is exactly a nonattacking rook placement: matching of k row/column pairs, in A_mn(k)=C(m,k)C(n,k)k! ways. Once zeros fixed, the number of nonzero cells in the union of the defense neighborhoods of s selected zeros is s(m+n−s−1); including/excluding their failure to have any 2-labeled neighbor yields the stated alternating polynomial with factor z^{mn−k}(1+z)^{mn−k−s(m+n−s−1)}. Every positive cell has ≥m+n−4 positive neighbors for m+n≥5; for 2x2 a full two-zero matching leaves isolated positive vertices, and the exact correction is −4z³−2z⁴. For k zeros, t labels 2 cover at most 2 zeros each: t≥ceil(k/2), yielding min bound mn−floor(k/2) and exact constructed attainment. Equality cases split into pairs of zero squares served at one cross-intersection, an odd path triple plus pairs, and an odd single-cover extension to unused row/column; the resulting optimizer counts match formulas. Independently brute-force original three label constraints for 2x2,2x3,2x4,3x3 and compared entire weight-polynomial coefficient arrays and optimal labels, including 2x2 min4 / count9; infinite formula justified combinatorially not by these tests.

## originality

PASS

Best-of-knowledge PASS for the two-parameter full weight polynomial and complete minimum-function counts/shapes. The scalar minimum in nonexceptional cases is already Theorem 3.4 of Cabrera Martínez–Kuziak–Yero 2022, and is acknowledged; the exact 2x2 totality exception corrects a boundary overlooked by the published all-(r,s≥2) scalar formula.

## value

PASS

Determining all coefficients of a natural domination weight polynomial and all optimizing labeled functions strengthens a known scalar invariant across an infinite two-parameter family. The 2x2 totality anomaly matters substantively, and complete matching/defender classification is useful for exact combinatorial enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
