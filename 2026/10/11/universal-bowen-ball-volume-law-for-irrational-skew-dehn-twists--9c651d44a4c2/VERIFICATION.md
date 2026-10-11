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

# Analytic verification

The exact fiber discrepancy is
\[
v_j=\eta+jk\delta+\delta\int_0^1\sum_{\ell=0}^{j-1}\psi'(x+s\delta+\ell\alpha)\,ds.
\]
The one-step difference satisfies \(|v_{j+1}-v_j|\le(|k|+\|\psi'\|_\infty)|\delta|<1/8\). Since \(\varepsilon<1/8\), the gap between distinct admissible integer-lift neighborhoods is \(1-2\varepsilon>3/4\), so no shift to another lift is possible. Every Bowen point therefore satisfies the real constraints \(|v_j|<\varepsilon\).

A trigonometric zero-mean approximation to \(\psi'\), together with irrationality of \(\alpha\), proves
\[
\frac1n\sup_u\max_{0\le j<n}\left|\sum_{\ell=0}^{j-1}\psi'(u+\ell\alpha)\right|\to0.
\]
The final displacement forces \(|n\delta|\le4\varepsilon/|k|\) for sufficiently large \(n\). Write \(a=n\delta\). The rescaled orbit difference approximates the affine path \(\eta+kat\) uniformly in \(t\in[0,1]\) and all centers. Its strict maximum constraint is equivalent, except for a zero-area boundary, to \(|\eta|<\varepsilon\) and \(|\eta+ka|<\varepsilon\). Integrating the interval of allowed \(a\) for each \(\eta\) gives \((2\varepsilon)(2\varepsilon/|k|)=4\varepsilon^2/|k|\). The coordinate change \(a=n\delta\) supplies exactly the factor \(n\) in the measured Bowen-ball limit.

The independent polynomial-entropy check uses covering measure for a lower bound proportional to \(n\), and an explicit base-by-fiber grid of sizes \(O(n)\) and \(O(1)\) for an upper bound. This establishes the exponent \(1\) but no metric-independent coefficient. No computer-assisted enumeration, numerical fit, independent external review or unavailable external certificate was relied upon.
