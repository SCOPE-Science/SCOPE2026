---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed the unrestricted optimization and fixed-width limit in RESULT.md lines 46–103. On the connected-support simplex, X=L+11ᵀ/(mn) is positive definite, and the trace-inverse second variation is the trace of a positive congruence of the square of X^(−1/2)HX^(−1/2), times two. It is strictly positive because distinct simple-graph edge coordinates appear in distinct off-diagonal entries. Boundary sequences tending to disconnected support have diverging inverse-gap cost. Existence, strict convexity and translation invariance thus give one optimizer with constant weights by direction, both positive by connectivity. Differentiating the exact Fourier trace at x=h/(1+τ) gives the stated Φ; strict convexity in y/h (not necessarily in τ) and the derivative signs at the two ends give uniqueness. Exchange symmetry at equal lengths gives τ=1. The cycle resolvent follows from periodizing the exponential line kernel. As an independent replay of the singular constants, for p=1,2 use g_p(t)=(4sin²(πt)+c)^(−p): its total variation is ≤2c^(−p), so the Fourier sum differs from m∫g_p by O(c^(−p)). The p=1 integral is 1/√(c(c+4)) by a tangent substitution; negative differentiation gives the p=2 integral (c+2)/(c(c+4))^(3/2). When c=τb_l and τ=z m^(−2/3), the relative errors are O(1/(m√c)), uniformly for z in compact positive intervals and fixed n. The exact zero-mode sum is (m²−1)/12 (also the constant term of the small-c cycle resolvent after the pole 1/c). The resulting scaled derivative tends to 1/12−S_n/(4z^(3/2)), bracketing the unique root, and the scaled trace correction is z_n/12+S_n/(2√z_n)=z_n/4. Equal design has hT=m²/6+O_n(m). Independent direct Fourier sums and bisection in y/h at n=3, m=98,304 gave scaled ratio 2.28840 and scaled correction 0.57261, near the analytic 2.28943 and 0.57236; this is illustrative, not the limit proof. Inspected VERIFICATION.md and verify.py without executing the supplied script; its recorded 1,296 finite checks are supplementary (the Green-loop checks values, not an independent derivative certificate). The two-term law is for hT with fixed n≥3, not jointly diverging widths. The variance interpretation uses mean-zero diffusion with identity noise covariance on the mean-zero subspace.

## originality

PASS

The generic convex optimization framework and the two-thirds mechanism for the width-two prism have prior coverage. The distinct content supported here is the sharp fixed-n≥3 cycle-product allocation and trace correction in terms of the entire transverse spectrum. The methods are closely related; this is a bounded comparison, not a priority determination.

## value

PASS

For every fixed transverse cycle this determines how much conductance buys connectivity versus the dominant long-direction resistance, with an explicit transverse-spectrum prefactor and quantified leading departure from the zero-band cost. The leading factor-of-two saving over equal spending is interpretable, but the main value beyond the earlier prism is the shared conductance balance across all transverse modes and its sharp width-dependent correction, not the exponent in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
