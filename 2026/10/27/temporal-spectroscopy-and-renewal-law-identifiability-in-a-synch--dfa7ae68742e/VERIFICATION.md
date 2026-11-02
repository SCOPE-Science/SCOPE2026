---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For a stationary two-sided renewal process with W>0, mu=E W>0, E W² finite, equilibrium inspection gives E f(A,R)=(1/mu)E integral_0^W f(a,W-a) da. Conditional Brownian covariance at nonnegative lag t equals 2D A iff residual R>t, and vanishes after reset by independence, giving C(t)=(D/mu)E[(W-t)_+²]. Conditional cross-particle position covariance vanishes despite common reset times. Differentiation yields C’(t)=-(2D/mu)E(W-t)_+ and C’’_+(t)=2D/mu P(W>t), hence full waiting-law identification. Two integrations by parts give absolutely convergent positive spectral formula 4D/(mu omega²) integral_0^infty P(W>s)(1-cos omega s)ds. Riemann-Lebesgue gives universal 4D/omega² ultraviolet; dominated convergence or Fatou gives finite zero-frequency value iff E W³ finite, equal 2D E W³/(3mu). Elementary tail substitution gives exact Lomax power-law/logarithmic regimes for alpha>2. Independent exact/numerical checks covered deterministic and exponential renewals and four Lomax moment limits; the unrestricted analytic argument is separate. Formula interpreted as improper cosine transform for nonzero frequencies, no claim of absolute C integrability for infinite third moment.

## originality

PASS

Compared mathematical objects and implications, not merely similar titles: De Mauro et al., original 35-page PDF, model and Sections II–III, focus on time-evolving ONE-TIME distributions, same-time squared-position cross-particle correlators and stationary density/order/spacing/counting, not C(t0,t0+t) or its spectrum. Knowing a stationary single-time Gaussian mixture and its equal-time inter-particle squared correlations does not alone give conditional survival across a lag; the new proof explicitly uses the joint age–residual inspection law and Brownian increments. Poisson spectra cannot imply all waiting distributions or third-moment equivalence. Residual priority risks documented, including uninspected plausible original sources; absence of search hits is not assumed to certify novelty.

## value

PASS

The complete recovery of an arbitrary reset waiting-law from a single stationary Brownian trajectory covariance and a sharp third-moment spectral cutoff are natural inverse and fluctuation results in the same non-Poissonian reset gas, extending the previously studied equal-time observables and Poisson-only spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
