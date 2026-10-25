---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

Conditional on T=t, the normalized multipole energies are theta times independent Gamma(at, rate b) variables times independent normalized chi-square factors. Their exact first-fourth moments and bounded degree-dependent chi-square errors yield the strong-law limits for M1, M2 and D; the method-of-moments estimators then recover t and theta. The bivariate iid Gamma CLT for the leading terms, the O(log L) accumulated chi-square perturbations and the delta method give the displayed covariance. In the global model S_l=W R_l with R_l->1 a.s., so W is recoverable and the entire array is generated from W by a parameter-free kernel. Positive densities make scaled W laws equivalent, whereas consistent gamma-model estimators give singularity. The dispersion test follows from D_L->positive in the gamma model and an O(log L/L) expectation bound in the global model. The 780 finite rational identities check algebra only; the asymptotic and measure arguments are analytic.

## originality

PASS

The accessible older spherical-field and Gamma-estimation literature does not cover the paired experiment. The newly posted grey-field paper is a plausible direct source for the field constructions and high-frequency moments; its abstract was read but the full text could not be accessed after arXiv HTML/PDF attempts and an Oxford retrieval error. No explicit abstract evidence establishes coverage of the joint estimator, conditional covariance, or law-equivalence dichotomy; this is a best-of-knowledge PASS with a material residual risk.

## value

PASS

The two models have identical second-order covariance but radically different information from one complete realization: the gamma-clock family identifies both amplitude and realized clock and yields an explicit conditional uncertainty law, while the global-clock family cannot consistently distinguish distinct amplitudes at infinite resolution. This is a motivated information-theoretic distinction relevant to single-sky inference, not merely the classical Gamma method-of-moments formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
