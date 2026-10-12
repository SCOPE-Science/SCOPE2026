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

# Verification details

The companion `verify.py` is standalone Python using only the standard library. Invoke `python3 verify.py` from the directory containing this document and the source file. A successful run prints `TORIC_SURFACE_BASKET_CHECK_OK` and reports 1967 exact integral test cases. It verifies all cone determinant and basis-weight formulas for coprime \(1\le B\le80\) and \(B\le A\le2B\), including the smooth case and the triangular endpoint.

The proof in `RESULT.md` establishes the classification for arbitrary positive coprime integers in range by explicit vertex analysis, determinants, and unimodular-coordinate changes. The program is not a certificate of mathematical novelty, a test of complex analytic equivalence beyond the toric quotient theorem, or a proof by exhaustive enumeration over unbounded integers. No independent audit has occurred.
