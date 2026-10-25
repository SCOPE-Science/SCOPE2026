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

The actual RESULT.md fixes d≥2, strictly positive categorical p, and m=n−1 trials. Direct enumeration for rational p and n=3..6 confirms E T_n=mq and Var T_n=mq(1−q)+2(n−2)(s3−s2²). The proof correctly uses a bounded stationary 1-dependent CLT with variance σ²=τ²+2δ and exact binomial(m,q) upper comparison. For the minimax lower bound it treats near-optimal independent Bernoulli arrays of length ≤m, uses Var Z≤μ(1−μ/m), subsequential mean shifts and variance ratios, and tests centered normal CDFs at ±u. Diverging shifts force distance→1 and zero variance gives a point-mass distance ≥1/2. Cauchy–Schwarz gives δ≥0 with equality precisely for uniform positive p; uniform transition indicators are independent. The finite support/variance obstruction for nonuniform n≥3 also follows.

## originality

PASS

Previously studied runs and approximations concern normal, Poisson, pseudo-binomial/negative-binomial or fixed-composition sequences, not a proof of the exact positive asymptotic infimum in Kolmogorov distance over all ≤n−1 independent Bernoulli variables; novelty is confined to that quantified constrained minimax barrier, not the easy finite non-Poisson-binomial obstruction.

## value

PASS

A random categorical transition count is a natural runs statistic. The exact and positive best possible Kolmogorov error for a natural one-proxy-per-transition independent approximation class is a motivated sharp approximation-theory obstruction, distinguishes uniform versus nonuniform sources, and is not merely the known finite support/variance test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
