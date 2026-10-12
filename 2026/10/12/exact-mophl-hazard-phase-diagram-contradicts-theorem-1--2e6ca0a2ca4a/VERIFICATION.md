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
Put
\[
c=2\alpha-1,
\qquad
u=\gamma x^\theta.
\]
For the published hazard,
\[
r'(x)
=
\frac{\theta\gamma x^{\theta-2}e^u}{(e^u+c)^2}
\Phi_{\theta,c}(u),
\]
where
\[
\Phi_{\theta,c}(u)
=
(\theta-1)(e^u+c)+\theta c u.
\]

For \(\theta>1\) and \(c<0\), \(\Phi\) is strictly convex. Its minimum is nonnegative exactly when
\[
-c
\le
\frac{\theta-1}{\theta}e^{1/\theta}.
\]
For \(0<\theta<1\) and \(c>0\), \(\Phi\) is strictly concave. Its maximum is nonpositive exactly when
\[
c
\le
\frac{1-\theta}{\theta}e^{1/\theta}.
\]
These conditions give the complete monotonicity phase diagram.

The bundled checker verifies both threshold formulas, reproduces the two turning points for the paper's \((\alpha,\theta,\gamma)=(0.03,2.52,0.03)\) simulation, and checks two simple pointwise counterexamples to the published theta-only theorem.
