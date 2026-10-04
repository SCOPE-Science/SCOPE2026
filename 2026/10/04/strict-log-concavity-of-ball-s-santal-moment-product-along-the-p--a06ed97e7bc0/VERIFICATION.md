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

The analytic proof has three independent components.

1. The slice beta integral gives
\[
I_n(p)=\frac{2^n}{3}\frac{\Gamma(1+3/p)\Gamma(1+1/p)^{n-1}}{\Gamma(1+(n+2)/p)}.
\]
2. Twice-differentiated Gauss multiplication gives
\[
\Phi_a''(t)=\sum_{r=1}^a G_t(r/a),
\]
with \(G_t\) strictly decreasing because trigamma has the positive series \(\sum_{k\ge0}(z+k)^{-2}\).
3. For \(N=n+2\ge4\), the sorted grid \(r/N\) is coordinatewise no larger than \(1/3,2/3,1,\ldots,1\), with a strict comparison. This proves \((\log F_n)''<0\) for the whole continuum.

The standalone `verify.py` was replayed from the packaged artifact path and printed `VERIFY_OK`. It compares the moment formula with direct slice quadrature at separated sample parameters, evaluates the analytic second derivative at separated points, checks strict inequality away from the center for representative dimensions, and checks the endpoint limit. These computations are consistency checks only; no finite sampling is used as a proof of strict concavity.

Unproved limits: no claim is made for arbitrary convex-body deformations, for complex \(\ell_p\) balls, or for concavity as a function of \(p\) itself.
