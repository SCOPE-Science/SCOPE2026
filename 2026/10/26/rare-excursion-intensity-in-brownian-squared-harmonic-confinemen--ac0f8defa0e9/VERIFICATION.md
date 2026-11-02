---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For the independent Brownian drivers dX_t=−(κ+σ B_t²)X_t dt+√2dW_t, κ,σ>0, X_0 deterministic, conditionally X_t is Gaussian with decaying deterministic mean and conditional variance V_t=2∫_0^t exp[−2κs−2σ∫_{t−s}^t B_v²dv]ds. Brownian time reversal and endpoint conditioning yield the joint rare endpoint local limit: √t P(|X_t|>u)→(2π)^−1/2∫_R E[erfc(u/√(2V_a))]da, V_a the perpetual variance functional driven by Brownian motion started at a. The Brownian quadratic Feynman–Kac transform F_s(a)=cosh(2√σ s)^−1/2 exp(−√σ a² tanh(2√σ s)) provides Gaussian-in-a domination integrated over positive s, justifying exchange of limits and large |a| tails, while κ>0 ensures long-time integrability. The vague limit is on R\{0}, not claimed as a probability weak limit. At threshold u↓0, scaling a=b/u yields V_{b/u}/u²→1/(σb²) for b≠0 and the explicit erfc integral yields uJ(u)→2/(π√σ). Independently integrated the resulting second-moment gamma ratio for three (κ,σ) and small-u erfc normalization; this is corroboration, not an independent proof of the infinite-time convergence.

## originality

PASS

Qualified PASS after reading the complete Gupta–Klapp 2026 primary preprint (24 pages, including Section 5 and Summary) for precisely the same Brownian-square stiffness model. That paper obtains the first four moments, algebraic even-moment t^−1/2 decay, thermodynamic work and heat, but does not provide a fixed-u exceedance tail intensity, its distribution-valued rare-event limit, or its exact small-threshold 1/u coefficient. Their method already gives central Feynman–Kac moments, and the current result depends on that foundation; novelty is limited to the rare-excursion measure and asymptotic tail crossover. The stationary OU-stiffness predecessor treats different dynamics. A separate broader Gaussian-mixture rare-event theorem might imply this result, and remains a risk.

## value

PASS

The full tail-intensity function describes rare order-one particle displacements when the bulk distribution collapses to zero under ever-increasing stochastic confinement. It distinguishes the law of large rare excursions from finite-moment decay, gives an explicit conditional-perpetuity representation, and derives a universal inverse-threshold singularity 2/(π√σ). These are motivated probability-limit objects and sharp boundaries, not redundant moment calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
