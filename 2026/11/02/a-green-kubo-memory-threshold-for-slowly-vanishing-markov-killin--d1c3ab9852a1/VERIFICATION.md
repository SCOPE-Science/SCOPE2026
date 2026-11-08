---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Reconstructed stationary Poisson solution (I-P)g=c-pi c, positive martingale variance from full-support transitions, analytic Perron pressure f(t)=log rho(diag(e^-tc)P) with f(0)=0,f'(0)=-pi c,f''(0)=sigma_GK^2. Uniform Birkhoff projective contraction of normalized row transitions gives O(k^(-gamma-1)) tracking of instantaneous left eigenvector and a summable O(k^(-2gamma-1)) error in the log-survival/Perron-product ratio. The pressure O(t^3) remainder sums iff gamma>1/3, yielding positive finite constant. Exact two-state covariance rho^j gives sigma^2=(1+rho)/(1-rho), so critical powers range (0,infinity). Independent numerical second-derivative checks for rho=-0.8,...,0.8 were performed; finite checks do not prove n->infinity.

## originality

PASS

Classical Feynman-Kac normalized flow contraction and Perron perturbation are prior work. Accessible Champagnat–Villemonais establishes contraction/relative asymptotic but not this absolute slowly varying log-normalizer; Petersson treats fixed perturbation varying with observation horizon. The stated second-cumulant threshold and fixed-marginal continuum of critical exponents were not found directly in the material compared. Potential older adiabatic positive-product/mod-Gaussian theorem can dominate: substantive residual risk.

## value

PASS

A natural time-inhomogeneous survival model has a sharp threshold where temporal correlations change a logarithmic correction while the one-step hazard distribution remains fixed; the strictly positive full relative prefactor and two-state power continuum refine leading-order survival estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
