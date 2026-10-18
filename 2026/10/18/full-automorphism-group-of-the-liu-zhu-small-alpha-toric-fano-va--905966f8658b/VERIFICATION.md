---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the full automorphism-group theorem

The direct argument proves that the sum of all primitive rays is zero. A Demazure root must then have exactly one pairing \(-1\), exactly one pairing \(+1\), and all remaining pairings zero. For \(n\ge3\), two intact rows of ray pairings force the character to be constant modulo the diagonal, hence zero; in dimension two, any four distinct polygon rays span the plane.

The two facet types are classified by the ray incidence counts \(n\) and \(n(n-1)\), except in dimension two, where their lattice determinants are \(3\) and \(8\). All lower facets must therefore be preserved setwise, forcing a permutation of the \(n+1\) coordinate functionals. Standard complete-toric automorphism theory then produces the asserted semidirect product.

Run `python3 artifacts/verify.py` to check the exact arithmetic for all dimensions from \(2\) to \(8\). The script verifies \(n(n+1)\) primitive rays, zero total ray sum, the complete facet incidence counts, rank after removing any two rays (using exact finite-field arithmetic), and the two dimension-two cone determinants; the last line is `VERIFY_OK`. Exact modular full rank is a valid finite certificate of rational full rank. The proof extends beyond the computed range.

This is verification of the stated mathematics, not an independent audit. Unresolved priority risk remains because the full primary Liu–Zhu manuscript could not be materially inspected; the accessible full published account of the same fan was inspected, and literature comparisons are documented in the separate review.
