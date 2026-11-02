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
# Verification and independent-validation boundary

The analytical proof is in `RESULT.md` and establishes the theorem for all continuous convex \(L\)-Lipschitz functions and every positive-width partition. Its key local identity is \(E_s=h^2[(\rho-Z)_+-\rho^2]/2\), with \(Z\sim\operatorname{Unif}[0,1/2]\). The exact moments and covariance follow by integrating a piecewise-linear function, and convex curvature-measure decomposition plus the sharp \(L^2\) triangle inequality prove the global law.

Run `python verify.py` from the extracted package using Python 3 and its standard library. The observed result on the prepared package is `VERIFY_OK 3562 exact rational assertions`. Assertions compare the covariance formula to direct exact integral evaluation, check the sharp extremal constant and the added independent measurement-noise variance for rational test cases. No outside modules, input data, or network access are required.

These finite tests verify algebraic identities on a large finite sample of rational inputs, not universal validity by enumeration. The universal claim is supported by the written proof. Publication-priority assessment is provisional and based on the specifically inspected prior sources; independent scientific audit has not been performed.
