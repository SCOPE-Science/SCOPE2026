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

The finite-difference filter and independent common factor give the claimed spectral measure and diagonal covariance K=W_m/t+κ/d. Jensen gives EN=r²/t−r²I′(t), with I the circular mean of log(W_m+κt/d). The continuous log-derivative contribution is O(t^(1/(2m)−1)), negligible at t^(α−1). At θ=t^α x, dW_m/t tends to x^(2m+2) for x≠0; the logarithmic derivative factors t d_t/d and t W_{m,t}/W_m vanish there and are bounded globally. The lower bounds W_m≳t+|θ|^(2m), d≳t²+θ² yield an integrable majorant C/(1+|x|^(2m+2)). The rescaled mean therefore gives α κ^α csc(πα) with a minus sign in EN. For the intensity at x≠0, differentiate at fixed θ first: tH_t/H→κ/(κ+x^(2m+2)), t²H_tt/H→0, and ∂θθ log H=O(t^(−2α)), for H=tK. Combining with the exact baseline from −log t gives the stated squared term. At x=0, −log d is harmonic and log(1+dW_m/(κt)) has bounded Laplacian: along the ray W_m(t,0)/t is smooth through t=0, and angular derivatives at zero use d=O(t²), W_m=O(t), and vanishing first angular derivatives. Proof applies to fixed m≥1 and κ>0; the checker was inspected, not executed, and would only corroborate finite cases.

## originality

PASS

The explicit fractional angular layer and disk-count deficit for an atom located at a zero of the continuous density are distinct from the checked continuous-only, atom-plus-flat, and band-edge laws. A prior spectral representation applies, but does not evaluate this joint singular limit. No equivalent evaluated law was found in the checked sources.

## value

PASS

Co-location of an atomic line and a continuous spectral zero is a natural boundary case not resolved by either component alone. The finding quantifies how the order of the continuous zero sets the angular width and how the two components change both the local intensity and the leading global deficit. The explicit coefficients and profile give useful benchmarks for more general stationary spectra even without a fluctuation theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
