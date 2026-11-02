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

The exact Green-kernel inverse identity (1+theta^2)w_i-theta(w_{i-1}+w_{i+1})=(1-theta)^2 phi_i for w=P phi follows by direct convolution. Substituting P phi=rho D phi yields a Jacobi recurrence whose perturbation epsilon_i=(1-theta)^2/(theta rho mu_i) is absolutely summable because alpha>1. Independently checked the Volterra difference equation Delta_i=theta^2 Delta_{i+1}+theta epsilon_i z_i under w_i=theta^i z_i: backward summation has tail contraction norm <= theta/(1-theta^2) sum_{k>N}|epsilon_k|. Reduction of order produces a growing branch, excluded by w in l1. A positive decaying solution has nonzero positive amplitude; spectral simplicity and reflection give equal +/- tails. Geometric dominated convergence proves the exact two-tail mass and the boundary moment converges precisely since sum n^{-alpha} is finite. This does not estimate truncated eigenvector error and requires both symmetry and alpha>1.

## originality

PASS

Best-of-knowledge original model-specific tail, omitted-mass and exact critical moment law, while the Perron equilibrium and general summable Jacobi perturbation arguments are prior work. Pollett explicitly stops before detailed eigenvector-tail analysis. General Jacobi asymptotics may make the recurrence step a known corollary, so novelty is only the verified translation for this mutation/mortality model, with remaining priority risk.

## value

PASS

The sharp tail exponent and multiplicative polynomial factor are natural quantitative descriptors of an established infinite-trait equilibrium: the omitted mass tells researchers how much equilibrium population lies beyond a computational trait cutoff without pretending to bound normalized finite-section eigenvectors; the exact critical moment differentiates exponential tail regimes. It is a motivated model-specific spectral lemma with boundary information, not a claim of a new general Jacobi theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
