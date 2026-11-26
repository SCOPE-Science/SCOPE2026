---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and mathematical checks

The inputs are a simple horn in dimension \(n\ge2\), of order \(a>n+1\), and an outer-slice threshold \(R\) as in Definition 2.1 of arXiv:2610.17527v1. All curves or paths used in the ray-tail proof are restricted to radii \(t>R\); this inclusion follows from (2.3) and Reinhardt invariance and does not require anything about intermediate radii. The integrable monomials are those of degree below \(a-n\) by Theorem 3.1; their constants \(c_p\) are defined by their squared norms, not numerical approximations.

1. Use the projective pullback formula for the diagonal kernel and the Gram speed formula. The two squared speeds are \(t^{-2}\operatorname{Var}_{w(t)}(|p|)\) and \(\operatorname{Var}_{w(t)}(p\cdot v)\), with \(w_p(t)=s_pt^{2|p|}/\sum_{|q|\le m}s_qt^{2|q|}\).
2. The squared radial speed for \(m=1\) is exactly \(A_0A_1/(A_0+A_1t^2)^2\). For any \(m\ge1\), expanding the probability of degree \(m-1\) gives the general leading term \((A_{m-1}/A_m)t^{-4}\) for the squared speed, with remainder \(O(t^{-6})\).
3. Diagonal rotation at fixed radius costs \(O(t^{-1})\) for a bounded angle, while unequal phase classes are separated by ratios of the top-degree projective coordinates at exponents \(me_i\) and \((m-1)e_i+e_j\). The projective distance is only a lower bound on the intrinsic distance. The same exponent differences identify the kernel of the limiting covariance.

No full completion classification, ray minimality, or intrinsic boundary metric is asserted. The degree-one calculation checks the normalization; the proof in RESULT.md addresses all allowed degrees.
