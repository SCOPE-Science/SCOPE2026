---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

For g=√f, direct differentiation gives |g′(1−u)|² ∼ (2Z_κ u log(1/u)^κ)⁻¹, with the same left-end coefficient. To make the shift argument uniform for κ≤1, use a fixed M>2 and small c, treating end strips within Mh of the endpoints (including nonoverlap) at cost O_M(h² log(1/h)^(-κ)) and the fixed interior at cost O_c(h²). On each band Mh≤u≤c the derivative sampled by a length-h mean-value increment differs from the endpoint leading expression by a relative O(1/M)+o_c(1), uniformly, since the endpoint distance varies by at most h. The truncated energy integral on this band is asymptotically the integral from h to c for fixed M,c, by divergence; letting M increase and c decrease fixes the leading coefficient. Both ends and the factor 1/2 yield h²/(2Z_κ) times that integral, with the stated log power or log-log. For κ>1 the zero extension is continuous and has an L² weak derivative (no boundary jump); the L² derivative of translations gives I_κ h²/8, and logarithmic differentiation gives exactly the integral displayed. Divergence of H²/h² in the other regimes precludes quadratic-mean differentiability. The log-density Hessian check follows from q′²/q″=2x²/(1+x²)≤1 and L=1+q≥1. For inversion, shifts bounded away from zero have H² bounded away from zero by continuity, unequal supports and disjointness for h≥2. Near zero, the regularly varying leading functions are eventually increasing and sandwich the true distance, which justifies inversion of the supremum. For κ<1, log(1/(2r))∼½ log(1/t) at the inverse scale, giving the factor 2^(−κ) inside the squared inverse constant; the iterated logarithm is unchanged to first order and κ>1 gives √(2t/I_κ). Substituting the three local shifts and using the product affinity (1−H²)^n gives respectively the exponents a²/[2^(2−κ)Z_κ(1−κ)], a²/(2Z_1), and I_κ a²/8; evenness handles negative shifts. Wang–Gao transfer the inverse-modulus orders at fixed confidence, not sharp estimator constants.

## originality

PASS

The supported distinct claim is the explicit critical-line endpoint calculation for κ>0, in particular the nonregular log-log threshold and first-order constants. The Epanechnikov endpoint κ=0, the general Fisher/Sobolev connection, the adaptive modulus theorem, and product-affinity and inversion methods are prior tools or cases, not independent novelty. The closest same-family follow-up cites these asymptotics as input. No inspected source establishes this critical-line calculation earlier or as a stated stronger result covering the logarithmic endpoint regime.

## value

PASS

This is the natural omitted boundary of the prior power-log example. The logarithm changes both the order of statistical localization and whether the location family is regular in quadratic mean, with a genuine log-log regime at the dividing parameter. The exact constants distinguish two-point experiments at the critical scales, while the all-shape estimator implication is properly limited to rate orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
