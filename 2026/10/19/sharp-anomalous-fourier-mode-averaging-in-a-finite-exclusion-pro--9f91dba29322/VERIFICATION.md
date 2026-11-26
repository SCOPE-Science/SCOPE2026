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

A bond exchange moves the sine weights by the discrete Laplacian; the first-mode eigenvalue is −4 sin²(π/L). The geometric sine sum over the occupied half equals csc(π/L). Conditioning on the full clock leaves the age observable Y=e^(−λ_L A) with mean m=H(λ_L)/μ and leaves only an exponentially bounded same-cycle conditional SEP covariance, contributing O(1) to the covariance primitive and O(T) to the variance. The age/residual density yields the frozen n+b*g decomposition, with ∫b=m, ∫rb(r)dr finite, and g=k*U for k(t)=e^(−λ_L t)f(t). Independently verify the heavy-tail renewal expansion by writing d(t)=∫_t^∞f(v)dv: U*f=1 gives U([0,T])−T/μ=(U*d)(T)/μ. The continuous interarrival law is nonlattice, so Blackwell's theorem gives U increments of width 1 tending to 1/μ. Partitioning into unit bins backward from T and bracketing by the decreasing d on each bin then gives (U*d)(T)~μ⁻¹∫₀ᵀd; fixed early-renewal bins are negligible, and the integral diverges for both 1<α<2 and α=2. This recovers the expansion without needing the higher-order Doney refinement or its erratum. Convolution of the primitive with k and b multiplies the divergent correction by H(λ_L)m; replacing the convolved linear term by its linear asymptote costs only O(1) because both kernels have finite first moments. Thus the covariance primitive is asymptotic to (bar F)²/μ times ∫₀ᵀd. One more integration with the factor 2 gives the stated Pareto constants, including (bar F)²t₀ at α=2 since μ=2t₀. For α>2, sum the centered full-cycle rewards over cycles begun before T; the indicator that each is begun is predictable in the cycle filtration, giving an exact martingale variance equal to the mean number begun times the cycle variance. The last crossing-cycle correction in a fresh process has squared norm o(T): bound it by a constant times the sum over unit bins of E[τ² 1_{τ>j}], using the positive minimum spacing t₀ to bound the number of starts per bin and independence of each next τ. The Cesàro mean of those tail expectations tends to zero. The stationary initial residual truncation also has squared norm o(T), since its survival is O(T^(1−α)); the remaining fresh horizon is independent of future cycles. The renewal rate is 1/μ and Cauchy–Schwarz controls boundary cross terms. The conditional expected uncentered cycle reward is bounded by F_*/λ_L, while the subtraction bar F·τ is unbounded with τ, proving strict positivity.

## originality

PASS

Prior work gives the same resetting model, the mean from the renewal density, and current statistics; the distinct content is the stationary fixed-ring time-integrated nonzero density mode, its exact variance regimes and sharp amplitudes. General renewal-function asymptotics are an acknowledged input, not a novelty claim.

## value

PASS

The step excites the slow first sine mode at a finite system size where internal dynamics alone have an exponential spectral gap. Quantifying how an external equilibrium-renewal clock nevertheless slows stationary time averaging, with the exact critical logarithm and nonzero amplitudes on each side, is a motivated transport/statistical fluctuation result rather than a current normalization or finite fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
