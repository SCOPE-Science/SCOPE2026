---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For f(x)=Lx²/2 the exact Bregman curvature difference is (L/2)(x_k−x_{k−1})², reducing Algorithm 2 test to λ_{k−1}>τ=2η0/L and its reset output to r=2η1/L; otherwise λ grows by 1+ε_{k−1}. After consecutive resets disjoint expansion-factor blocks each exceed τ/r=η0/η1, so total finite P yields N−1<log P/log(η0/η1) and N≤ceil(log P/log ratio), including N=1 when P=1. Since all later positive factors would trigger a new reset above τ, the post-last-reset stepsizes increase to λ∞∈(r,τ]. An explicit positive summable dyadic product realizes each λ∞, and scalar gradient recurrence gives asymptotic |1−Lλ∞|. For η0≤1/2 this gives [1−2η0,1−2η1); small λ0 with no reset yields factor near one. Finite-termination and never-reset branches are scoped separately; numerical verifier is supporting only.

## originality

PASS

The primary Hoai–Hoang–Lara MPG-NGD manuscript provides Algorithm 2 and general eventual monotonicity and convergence lemmas but no exact scalar reset count, total-multiplicative budget inequality, realizable continuum terminal-step interval, or quantitative rate dichotomy. An indexed earlier NIPG scalar spike/reset law is for the original gradient-difference rule rather than this function-value MPG-NGD normalization, and is not a dominating statement. The scalar analysis here imposes specialized hypotheses and obtains a structurally useful, substantially sharper classification, not just a restatement of eventual monotonicity.

## value

PASS

A canonical strongly convex scalar test isolates an adaptive nonlinear controller and yields an exact finite reset budget and sharp rate window for parameters repeatedly used in the method. The post-reset near-optimal tuning versus arbitrarily slow no-reset branch exposes initialization-dependent behavior absent from the general convergence guarantee; a meaningful interpretable boundary case, though not a multidimensional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
