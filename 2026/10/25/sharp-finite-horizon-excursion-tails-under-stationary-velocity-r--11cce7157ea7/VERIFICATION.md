---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The Poisson exponential backward age A at stationarity and V0|A∼N(0,2DA) give Laplace density κ exp(-κ|v|)/2 with κ=√(r/D). Conditional on future reset interval lengths ℓ_j summing to T, the increment X_T=L V0+G, L=ℓ_1 and G independent centered normal with variance (2D/3)∑ℓ_j³. For c=κ/T all partitions satisfy e^{cx}P(X_T>x|partition)≤exp(Dc²∑ℓ³/3)≤exp(rT/3); if any future reset L<T, the c-weighted tail tends to zero, while on no reset L=T its limit is exp(rT/3)/2. Dominated convergence and P(no reset)=exp(-rT) give constant exp(-2rT/3)/2 and conditional no-reset posterior→1. The MGF denominator κ²-θ²L² and positive-probability L=T event prove its exact finite domain |θ|<κ/T and boundary coefficient exp(-2rT/3). Stationary covariance (2D/r)exp(-r|t|) yields Var X_T=(4D/r³)(rT-1+exp(-rT)). Independent convolution numerics matched the tail constant for three parameter sets; universal asymptotic follows analytically.

## originality

PASS

Olsen–Löwen 2024 analyze the same velocity-only resetting model and derive Fourier–Laplace transforms, moment recursions, and long-time effective diffusion, all explicitly credited. The assessed fixed-T stationary-initial-state tail residue and conditional no-future-reset law are not stated in accessible abstract. The full primary text could not be materially inspected; Oxford access reported vpn_disconnected, so this is a significant residual risk. Singh 2020 resets different coordinates; Smith–Majumdar 2022 concern large-time/other initialized ensembles. No located Resultary equivalent.

## value

PASS

The fixed-horizon extremes provide a sharp, physically interpretable diagnostic: sufficiently far spatial excursions from stationary velocity were overwhelmingly free of velocity resets during the observation window. The exact exponential moment threshold and its residue distinguish fixed-time rare displacement from large-T diffusive variance; this is meaningful boundary behavior of a precisely specified stochastic model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
