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

The proof has two independent components. First, the closed score formula depends on the original five trainable parameters only through \((\omega_d,\omega_s,\alpha,\beta)\), giving the analytic upper bound \(d_Q\le4\). Second, one explicit four-input Jacobian has a strictly positive exact determinant, giving \(d_Q\ge4\).

The embedded `artifacts/verify.py` differentiates the closed formula symbolically and checks the displayed Jacobian entry by entry. It then verifies
\[
\det J=
\frac{111}{512}
+\frac{87\sqrt2}{512}
+\frac{45\sqrt3}{256}
+\frac{129\sqrt6}{1024}>0.
\]
A successful replay prints `VERIFY_OK`.

The script uses exact symbolic arithmetic. It is a finite certificate for the stated Jacobian identity, while the conclusion about the complete function family follows from the analytic factorization and inverse-function rank argument. No numerical sampling, tolerance-based rank test, or extrapolation is part of the proof.

Limit: the calculation follows the gate ordering in Eq. (7) of arXiv:2605.25365v1 and does not assess alternative circuit orderings or different notions of effective dimension.
