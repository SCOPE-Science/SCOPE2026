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
The universal theorem is analytic. The standalone checker replays exact rational instances.

For
\[
P=\operatorname{diag}(4,1),
\]
the predicted isotropy noise is
\[
r_*=\frac43.
\]
Measuring the first coordinate gives posterior first variance
\[
\frac{4r_*}{4+r_*}=1,
\]
so the complete posterior covariance is exactly \(I\).

For the stronger measurement
\[
r=\frac14,
\]
the first posterior variance is
\[
\frac{4r}{4+r}=\frac4{17},
\]
and the other variance remains \(1\). Hence
\[
\kappa_2(P^+)=\frac{17}{4}>4=\kappa_2(P).
\]
The exact prior-worsening threshold is
\[
\frac{L\mu^2}{L^2-\mu^2}=\frac4{15},
\]
and indeed
\[
\frac14<\frac4{15}.
\]

The checker also tests the determinant identity for several rational priors and unit-direction squared weights, confirming that the determinant of the information update is maximized by the largest-variance eigendirection in those replay cases.

Finite replay is corroborative only. The direction optimum and all-parameter thresholds are proved symbolically in `RESULT.md`.
