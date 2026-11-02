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

# Verification record

Analytic verification: coordinate sign-change isometries reduce the general hyperplane to nonnegative weights. The center feasibility interval criterion gives an exact radius for any bounded set. Its two weighted-extrema terms are bounded by the complement of the maximum coefficient times diameter; the explicit simplex-like configuration attains that complement, together with the universal half-diameter lower bound. The optional rank-one coordinate elimination proves isometry in the dominant coefficient regime. All quantifiers and equality boundaries are covered in RESULT.md.

To reproduce finite exact checks using only Python's standard library, run `python verification/check_exact.py`. This test passed 52,800 exact rational assertions involving up to nine coordinates, including zero coefficients and random bounded sets. To run an independent optimization formulation using SciPy's `linprog` and its HiGHS solver, use `python verification/check_lp.py`; 1,200 signed-coefficient cases passed with maximum discrepancy below `1e-7`.

A finite computation cannot certify the theorem for all dimensions and coefficients; the proof is the source of the universal statement. Literature review is limited where full texts were inaccessible, especially Franchetti (1977) and Bayod–Masa (1990). No external scientific audit was performed.
