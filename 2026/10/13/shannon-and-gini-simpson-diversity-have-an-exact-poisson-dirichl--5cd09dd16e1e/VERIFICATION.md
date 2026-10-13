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

The proof is analytic. The standalone checker evaluates the mixed moment by two separate deterministic routes.

The first route uses
\[
\mathbb E[S_uS_v]
=
\frac{
(1-\alpha)_{u+v-1}
+
(\theta+\alpha)
(1-\alpha)_{u-1}
(1-\alpha)_{v-1}
}{
(\theta+1)_{u+v-1}
}
\]
and differentiates numerically at
\[
(u,v)=(2,1).
\]

The second route works directly with
\[
V_1\sim\operatorname{Beta}(1-\alpha,\theta+\alpha)
\]
and
\[
V_2\sim\operatorname{Beta}(1-\alpha,\theta+2\alpha),
\]
using beta-function derivatives for the logarithmic moments. This independently reconstructs
\[
\mathbb E[S_2H].
\]

Across the tested parameter grid, both routes agree with
\[
\operatorname{Cov}(D,H)
=
\frac{\theta+\alpha}{(\theta+1)^2(\theta+2)}
\]
to high precision. The checker also verifies the quadratic variance formula, positivity and valid magnitude of the exact correlation, and convergence toward the large-concentration limit.

The finite grid does not establish the theorem. The all-parameter proof is the beta-integral derivation and analytic differentiation in `RESULT.md`.

Independent audit has not been performed.

Exact deterministic replay: `VERIFY_OK mixed_checks=30 covariance_checks=60 variance_checks=90 correlation_checks=30 asymptotic_checks=5 dirichlet_limit=0.8804959104761448`.
