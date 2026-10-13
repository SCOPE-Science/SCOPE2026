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

# Reproducibility

For an exact-fraction spot check, run `python3 CHECK.py` with a standard Python 3 interpreter. It was run on the authored `CHECK.py` source and printed `VERIFY_OK`.

The mathematical proof in `RESULT.md` independently establishes the universal statement for every real penalty ratio at least one. The script tests only selected rational parameter ratios and domain points, not an exhaustive set and not a computer proof of the universal statement. To check the sharpness analytically, verify that the affine penalty model has slope \(2r-1\) on the certificate ball and that the original feasibility bound is attained at the candidate. To verify quadratic growth, use the exact identity \(\phi_1(x)=1+|x+1|\) on the full domain.

No numerical tolerance, solver, or external computation package is required. Independent audit has not been performed.
