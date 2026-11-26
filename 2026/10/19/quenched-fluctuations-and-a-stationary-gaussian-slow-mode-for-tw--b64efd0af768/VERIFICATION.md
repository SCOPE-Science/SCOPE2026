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

The row-vector action is exactly X'=(1-εB)X+εR. The coefficient is positive and at most 1-2cε, uniformly below one (the upper bound itself can be attained), and the interval [0,1] is invariant. Starting farther in the past gives a unique pullback weight measurable before the next environment, so the mean is θ. Centering gives an innovation η=R-θB with zero mean; the mixed second-moment term vanishes by independence of the previous centered weight from the entire current pair, without requiring independence of B and η. Solving the second-moment identity gives the stated variance with positive denominator; conditional mean iteration gives every lag. Zero variance at one leakage is equivalent to η=0 a.s., hence to the constant instantaneous ratio and zero variance at every leakage. The coupled deterministic-coefficient recursion differs by D'=(1-εm)D-ε(B-m)(X-θ); the mixed term again vanishes by past measurability, giving the exact O(ε²) stationary mean-square discrepancy. For any finite set of slow times, truncate the independent-innovation array before ceil(ε^(-2)) steps prior to the earliest observation; the normalized squared tail is O(exp(-κ/ε)) for some κ>0. Each coefficient of any fixed linear combination is O(sqrt(ε)), so the finite triangular-array Lindeberg argument applies whenever the limiting variance is positive, and the zero-variance projections converge in L². The covariance tends to σ² exp(-m|t-s|)/(2m); stationarity allows any real times and the degenerate case. This proves exactly finite-dimensional convergence, not tightness in a path space. The replay path is RESULT.md lines 59–113 with the indicated truncation. An independent exact-rational enumeration of the two-rate example over histories of length up to ten corroborated lag two, finite-step variance, and squared coupled discrepancy. Frozen verify.py and VERIFICATION.md were inspected, not executed; notably, the script's geometric covariance comparison multiplies two already-equated variances by the same lag factor, so that check does not independently establish the lag law.

## originality

PASS

Credit is limited to the evaluated finite-leakage lag law together with the stationary slow-time finite-dimensional limit for the random invariant weight in this model. The pullback representation and averaged limit are known; the variance and no-fluctuation criterion agree exactly with an indexed finite-type result and are not credited on that overlap. The variance and lag algebra is generic for scalar affine recursions, not a novel method. The strongest general stationary Gaussian theorem checked in full gives one-time marginals for an additive linear recursion, whereas the strongest process-level lead found in classical stochastic approximation could be checked only at abstract level. Neither comparison established coverage of the stationary multi-time conclusion under the admitted same-environment dependence. This is a qualified best-of-knowledge distinction, not a claim of first discovery of OU approximation or of the elementary scalar moment identities.

## value

PASS

For random invariant weights the entire stationary lag profile and joint Gaussian scaling quantify how long the averaging error persists, rather than just its instantaneous spread. This is a natural question in a metastable approximation, and two rate laws with identical averaged rates really have different answers. The exact comparison of dependent multiplier noise to a stationary deterministic-drift recursion makes the longitudinal conclusion usable without tracking particle-observable CLTs or assuming a functional limit. The value is this quantitative stationary description, not novelty of the autoregression identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
