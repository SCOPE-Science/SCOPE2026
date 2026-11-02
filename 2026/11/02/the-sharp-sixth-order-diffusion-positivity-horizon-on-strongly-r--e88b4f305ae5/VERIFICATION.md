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

# Reproducibility and scientific limits

Run `python verify.py` with Python 3.9 or later; only the standard library is used. This is a deterministic exact-rational test, not a floating-point-only experiment. Successful execution prints `VERIFY_OK` and the following group totals:

- 4 exact polynomial identities (the rational function relation, two derivatives, and the fourth-order four-cycle contrast);
- 2,945 direct rational-matrix entries compared exactly with the spectral formulas;
- 2,670 strict positive off-diagonal checks;
- 275 exact row-sum checks;
- 6 exact rational brackets for the first and only diagonal crossing, plus the exact Petersen fourth-order edge value \(-36/4123\) at \(z=4\).

The cases are `C4`, `K3,3`, `Petersen`, `Rook3`, `Rook4`, and `Triangular5`; each uses dimensionless timesteps \(z\in\{1/5,1,2,5,11\}\). Both the strongly regular parameters and spectral integer roots are checked independently of their reported names. The six root intervals arise from 40 exact-rational bisections; decimal endpoints are displayed only for convenience.

The all-graph quantifiers, strict scalar monotonicity and uniqueness do **not** follow from these finite checks. They follow from the exact spectral-projector and derivative proof in `RESULT.md`. The matrix test is limited to integral-spectrum examples, but the analytic argument permits irrational eigenvalues. No claims are made about arbitrary graphs, intermediate Gauss–Legendre stage positivity, finite-precision implementations, or external independent verification.
