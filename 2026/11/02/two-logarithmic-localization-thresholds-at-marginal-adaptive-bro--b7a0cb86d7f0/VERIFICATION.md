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

The original formulas are correct; the repaired claim makes the exact Green equivalent the finding, states the relative O(1/log r) error already available from the tail argument, and derives exact stationary tail masses. Independently checked the physical-branch identification in the replacement proof: conditional survival and Tonelli give ∫κG≤1, yielding local integrability on compact sets. The distributional source equation follows by the Brownian product rule and heat-kernel domination of the terminal term. With z=log r and a=d+2, the substitution G=r^(−d)h gives h''−a h'−q h=0. Factoring g=z^(−β)(log z)^(−γ) cancels the two nonintegrable terms exactly; the residual is O(z^−2). The Volterra kernel is bounded by exp(−a(t−s)/2); its norm on the tail is O(1/z₀), and differentiation gives u'=O(z^−2) and recovers the ODE without differentiating the rate. Reduction of order has growing branch r²(log r)^β(log log r)^γ, since the logarithmic derivative of the reduction integrand tends to a. A positive coefficient of that branch would violate ∫κG≤1, and a negative one would violate positivity. This proves that the actual killed Green function has positive slow-branch amplitude. Testing the Green equation with expanding cutoffs proves ∫κG=1; the discarded Laplacian term is bounded by R^−2 times at most logarithmic powers on the cutoff annulus. The shell integral is exactly of z^(−β)(log z)^(−γ) type, including divergence when β=γ=1. Integration of the equivalent gives both displayed tail-mass constants. For stationarity, bounded resetting gives the killed variation-of-constants formula, and the uniform Gaussian bound makes the initial term vanish on compact tests for any invariant probability. Thus only the finite-mean regenerative normalization can be stationary and it is unique. The argument includes d=1 via the same density equation and sphere factor 2.

## originality

PASS

This pass is for the repaired exact positive-amplitude Green tail, not the original positioning of the two stationarity thresholds as previously unresolved. That central originality claim fails: the October 18 record states both one-dimensional thresholds and equality cases, and its one-dimensional comparisons transfer to the radial equation by rescaling logarithmic time. The repair explicitly credits that coverage and retains the substantive unmatched claim: an equivalent with nonzero finite amplitude and controlled relative error for the physical killed density, normalizable or not, and its exact stationary-tail-mass consequences. The inspected prior threshold proof bounds logarithmic exponents but does not supply that ratio limit.

## value

PASS

The original threshold-only positioning would largely duplicate existing science. The surviving rate-to-density equivalent gives a materially finer invariant than threshold values or logarithmic slopes: it identifies the complete spatial scale and a nonvanishing amplitude of the actual occupation measure even at critical nonnormalizability and with a merely continuous perturbation. Where a stationary law exists it gives the leading multiplicative constant in the functional tail shape and the correct normalization relation, not just the slopes in a log–log plot. This is a natural marginal regime where the distinction between exponent bounds and a density equivalent matters; the proof gives a quantitative relative error and a direct check of which branch the process selects.

The dated certificate retains the supplied scientific assessment, sources and limitations.
