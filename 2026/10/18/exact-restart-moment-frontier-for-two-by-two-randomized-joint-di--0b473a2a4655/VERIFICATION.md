---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For A=diag(1,-1) and B=eps[[0,1],[1,0]], explicit orthogonal rotation yields loss 2 sin²(2alpha)+2 eps² cos²(2alpha), minimized at 2eps². The eigenbasis of the Gaussian pencil has loss 2eps²/(cos²theta+eps² sin²theta), theta uniform unsigned Gaussian angle. Monotonicity maps best of L trials to the minimum order statistic with density 2L/pi (1-2theta/pi)^(L-1). The exact expectation follows. T=tan(theta) gives E[L1]=2eps; the endpoint u=pi/2-theta has a uniform O(1) comparison for L2 to integral u/(u²+eps²), yielding 16/pi² eps² log(1/eps). The L>=3 rescaled integrand is dominated by u^(L-3), integrable; L=3 integrates to 48 log2/pi². Thus precisely three trials are necessary and sufficient for bounded expected squared-loss/optimum ratio on THIS matrix family, not across all algorithms or families. Independently evaluated quadrature at eps 0.1, 0.02 and 0.005 corroborates divergent L1/L2 ratios and finite L3 ratio; source rational and eigenbasis code was inspected without relying on its success marker.

## originality

PASS

The exact mathematical conclusions compared to prior results were not identified as an implication of an inspected stronger result; best-of-knowledge, not exhaustive priority certification. Relevant full-text access limitations and aliases recorded.

## value

PASS

The trial count required to control mean-square residual of a published randomized eigendecomposition method is a naturally motivated robustness boundary. Exact 2x2 witness distinguishes one-trial inverse-linear, two-trial logarithmic degradation and three-trial constant-factor risk with matching sharp constants, providing a rigorous benchmark that general tail upper bounds alone do not furnish. It is not an arbitrary parameter substitution or a purported solver-independent lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
