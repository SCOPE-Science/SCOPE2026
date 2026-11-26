---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Equal flux gives y_0=0, y_{n+1}=1, and y_{k+1}=J/(1-y_k^r) before the hit. At J<=J_* the lower fixed point bounds the iterates. At J=J_*+delta the increment is at least delta until the hit, so first hitting is finite; monotone shooting therefore gives J_n decreasing to J_*. Expansion at s gives drift a delta+b u^2+O(delta |u|+|u|^3), with a=(r+1)/r and b=(r+1)/(2s). For fixed small epsilon, monotonicity of the map bounds entry overshoot and exit undershoot at the window endpoints by O(epsilon^2+delta), leaving the crossing locations a distance comparable to epsilon from s. Exterior steps and endpoint integral errors are bounded for fixed epsilon. The derivative of the drift is O(epsilon+delta) inside the window; each complete discrete step contributes 1+O(epsilon+delta) to the reciprocal-drift integral. Taking n to infinity and then epsilon to zero gives total passage (n+1)sqrt(ab delta) -> pi; the integral stopped at k=floor(t(n+1)) similarly gives sqrt(ab delta) k = pi/2+arctan((y_k-s)sqrt(b/(a delta)))+o(1). This proves both the stated coefficient and the correctly oriented cotangent limit. This is a fixed-r, strict-interior result. The frozen verification is illustrative; the independent command `python /tmp/opencode/frozen_review_checks_3_4.py transport` checked r=2,3,5,8 at n=128,512,2048 and t=.2,.5,.8; at n=2048 current relative errors were below .0029 and profile absolute errors below .0055 at those points. The numerical check does not certify either limit.

## originality

PASS

The model and steady-flux recurrence are prior, as is the generic bottleneck mechanism. The model-specific pair of exact coefficients and discrete stopped profile was not found or shown to follow directly from an inspected result. The key distinction is that a continuous-time full delay is not a discrete stopped passage theorem.

## value

PASS

The exact constant quantifies finite-length bias in a natural stationary observable; the stopped profile distinguishes a genuinely inhomogeneous bulk at first order from a spatially flat approximation. Both arise from a controlled discrete mechanism, not merely fitting the predicted exponent. The relevance is mathematical, not a claim of empirical calibration or applicability to heterogeneous chains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
