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

For a positive-definite covariance matrix \(\Sigma\), define
\[
\tau=\mathbf 1^\top\Sigma\mathbf 1,
\qquad
\beta=\frac{\Sigma\mathbf 1}{\tau},
\qquad
C=
\Sigma-
\frac{\Sigma\mathbf 1\mathbf 1^\top\Sigma}{\tau}.
\]
The deterministic identities checked by the bundled script are
\[
\mathbf 1^\top\beta=1
\]
and
\[
C\mathbf 1=0.
\]
These are the algebraic content needed for the common-residual conditional representation.

The script also checks a positive-row-sum example and a positive-definite covariance matrix having one negative row sum. In the latter case the corresponding conditional mean slope is negative, which directly contradicts monotonicity of that coordinate.

For the unit-variance \(d=3\) equicorrelated example with
\[
\rho=-\frac25,
\]
the covariance eigenvalues are
\[
\frac15,\frac75,\frac75,
\]
and
\[
\Sigma\mathbf 1=\frac15\mathbf 1,
\qquad
\beta=\frac13\mathbf 1.
\]
The sum of off-diagonal covariances in each row is
\[
-\frac45,
\]
so the earlier sufficient condition fails while the exact criterion holds.

Expected successful terminal line:
`VERIFY_OK equicorr_beta=0.333333333333 negative_row_beta=-0.250000000000`.

The script verifies algebra and examples only. The stochastic-order theorem itself is proved by the analytic coupling and necessity arguments.
