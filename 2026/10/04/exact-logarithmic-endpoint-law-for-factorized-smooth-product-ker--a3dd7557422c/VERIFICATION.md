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

The verification is analytic and has three layers.

For one factor, the homogeneous kernel satisfies a uniform far-field expansion
\[
T_\Omega f(x)
=
\left(\int f\right)\frac{\Omega(x/|x|)}{|x|^d}
+
O(|x|^{-d-1})
\]
for compactly supported input. Scaling \(x=t^{-1/d}y\) converts the low-level distribution into a bounded-domain indicator limit. The limiting boundary has measure zero, so dominated convergence applies and polar coordinates give
\[
\lim_{t\downarrow0}t|\{|T_\Omega f|>t\}|
=
\frac{|\int f|}{d}\int_{S^{d-1}}|\Omega|\,d\sigma.
\]

For two factors, a separate product-tail lemma shows that two tails \(A/t\) and \(B/t\) produce
\[
\frac{AB}{\lambda}\log\frac1\lambda
\]
to leading order. The regions above a fixed amplitude are only \(O(\lambda^{-1})\), using \(L^p\) integrability for some \(p>1\).

For the coordinate-Riesz specialization,
\[
\int_{S^{d-1}}|\theta_1|\,d\sigma=2V_{d-1},
\]
which yields the displayed coefficient
\[
\frac{4V_nV_{n-1}V_mV_{m-1}}{nm}.
\]

No numerical sampling, finite truncation, or unproved extrapolation is used. The result does not verify the nonfactorized-kernel or zero-mass regimes.
