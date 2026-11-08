---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Poisson thinning gives independent rate-lambda*theta reset and rate-lambda*(1-theta) flip clocks. A common reset yields uniqueness and exponential coupling. At a stationary exponential reset age, a geometric number of alternating exponential displacement runs has Fourier transform theta*h_plus*(1+(1-theta)*h_minus)/(1-(1-theta)^2*h_plus*h_minus). Direct partial fractions give the two positive decay rates d±, amplitudes A,B, normalization A/d_+ +B/d_- =1, jump A-B=lambda*theta/c, and no atom. Integrating yields negative mass 1/2+[v(1-2theta)-c]/(2D) and mean [c-v(1-theta)]/[lambda*theta*(2-theta)], proving both sharp inequalities and endpoint theta=1. Independent transform and polarity checks corroborate; theta=0 and nonexponential renewal times are not addressed.

## originality

PASS

The source 2026 paper already proves existence of the stationary distribution and gives the first moment; no priority is taken for these or Poisson thinning. In the source article the density is represented by a local-time integral and its explicit evaluation is not supplied in the inspected passage. The closed elementary asymmetric density and the exact majority-vs-mean polarity region are further calculations, with generic Markov-fluid resolvent theory as material priority risk.

## value

PASS

An explicit stationary law and its tails are natural observables in a non-symmetric stochastic resetting model. The strict region with positive-location majority but negative stationary mean quantifies an interpretable discrepancy between typical sign and large adverse excursions, while simultaneously evaluating the previously integral-defined local-time term across all stated positive parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
