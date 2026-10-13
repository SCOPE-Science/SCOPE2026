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
The universal statements are analytic.

For a positive diagonal matrix and zero start, the first BiCGSTAB half-step has
\[
\alpha_1^{-1}=m,
\]
where \(m\) is the initial squared-residual spectral mean. The stabilization step has
\[
\omega_1^{-1}=n,
\]
where \(n\) is a second spectral mean weighted by the squared intermediate residual. Therefore
\[
x_{1,i}=\frac{m+n-\lambda_i}{mn}b_i.
\]

The lower envelope follows from concavity in \(\lambda_i\) and endpoint optimization. The upper envelope follows from
\[
\frac{\lambda(m+n-\lambda)}{mn}
=
\frac{(m+n)^2}{4mn}
-
\frac{(\lambda-(m+n)/2)^2}{mn}
\]
and the sharp endpoint ratio bound on \(m/n\).

The embedded `verify.py` uses exact `Fraction` arithmetic to replay the rational three-mode sign-loss witness, check the coordinate formula against the algorithm, and verify the two-mode identity on several rational cases. A deterministic rational grid also checks the stated envelope numerically in exact arithmetic. These finite checks are corroboration only and do not replace the analytic proof.

Later BiCGSTAB cycles, alternative shadow residuals, preconditioning, nondiagonal systems, nonsymmetric M-matrices, breakdown handling, and floating-point behavior are not verified by this package.
