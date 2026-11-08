---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For a,c>0 on the unit critical lattice, the weighted cosecant partial fraction yields exact Zak intensity π²[H²(1−s)(y−c/y)²+J²s(y+c/y)²]/(H²+s)², H=sinh(πa), J=cosh(πa), s=sin²(πx), y∈[e^{−πa},e^{πa}]. Its derivative as function of s has a strictly decreasing linear numerator, hence interior stationary points are maxima and the infimum lies at s∈{0,1}. Monotonicity of both endpoint squares in y for c outside the cancellation interval yields the five analytic branches with transitions c=e^{±4πa} and frame zeros for e^{−2πa}≤c≤e^{2πa}. Energy ∥g∥²=π(1+c²)/a and c↔1/c symmetry yield unique optimizers c=e^{±4πa}, max normalized 2πa/cosh(4πa). Independently evaluated complex Zak and real-intensity algebra on a∈{.13,.55}, several c,x,ω points, and checked the claimed lower bound and optimum. The proof, not those samples, covers all parameters.

## originality

PASS

The announced qualitative two-kernel frame set and established single-pole constants are credited; the exact five-branch lower bound and energy-normalized optimizer were not implied by inspected primary texts.

## value

PASS

Determines exact stability and best normalized conditioning within a natural two-pole critical Gabor design family, including location switches distinct from existence thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
