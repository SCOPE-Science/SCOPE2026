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

The full argument is the explicit two-vector Cauchy--Schwarz correlation inequality, the root-mean-square strictness criterion, and the nonnegative Fourier moment expansion. For each integer \(s\ge2\), a strict change at a nonzero lag contributes to \((h,-h,0,\ldots,0)\) in the moment sum. The statement applies to finitely supported coefficients; no numerical cutoff is needed for the algebraic proof.

Run the standalone file `artifacts/verify.py` with Python 3. It tests integer-valued reflection pairs on cyclic groups with 2 through 14 points, compares exact cyclic autocorrelations, exact fourth/sixth/eighth moments, and Gaussian-integer phase majorization. The checked output is `VERIFY_OK exact_cyclic_cases=624 strict_asymmetric=412 exact_moments_2_3_4=PASS aperiodic_checks=10`.

The finite checks do not establish claims for all discrete abelian groups, all exponents, or all coefficient values. They only independently exercise normalizations and finite identities. The source and comparisons are in RESULT.md and REVIEW.md. Independent audit has not been performed.
