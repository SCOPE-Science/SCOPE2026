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
# Verification

Replay with `python3 artifacts/verify.py` using only the Python standard library. The verifier independently builds canon words from \(k\)-row lattice-word constraints and all relabelings, directly excludes the nesting patterns using occurrence positions, cross-checks a literal quadruple-pattern test in small cases, and compares direct bivariate \((\operatorname{des},\operatorname{maj})\) coefficients against both the structural boundary-swap family and an independently assembled Euler–Mahonian product.

Exhaustively tested parameter cases: \(1\le n\le4\) and \(k\in\{3,4\}\), plus \((5,3)\), \((2,5)\), and \((3,5)\). Exactly 1,347,568 canon words were checked in total; 2,390 were accepted, across eleven cases.

Exact replay terminal line:

`ALL CHECKS PASSED; cases=11; canons_tested=1347568; literal_four_index_checks=263; admissible_words=2390; all cases exhaustive`

The calculation proves the finite cases only. The unrestricted theorem is supported by the complete occurrence-position and boundary-swap proof in `RESULT.md`.
