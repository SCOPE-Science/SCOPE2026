---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the Gaussian-tree sign–energy law

The mathematical proof is contained in `RESULT.md`. This file records finite corroboration and reproducibility, not independent certification.

Run `python3 verify.py` using Python 3 and only its standard library. The standalone code independently checks the Gaussian-regression algebra with exact rational arithmetic; uses Simpson quadrature on the actual conditional Gaussian density (rather than the asserted closed form) for nine positive and negative correlations; compares double-sum and collapsed chain identities exactly through 25 vertices; checks branching-tree path-product substitutions and an exact non-tree boundary counterexample; and simulates 250,000 reproducibly seeded Gaussian-tree samples to test each local covariance numerically.

Successful local execution yielded: `PASS: 446 finite checks (exact rational, Gaussian quadrature, branching tree, seeded simulation).`

The quadrature and simulation are finite numerical checks with explicitly relaxed numerical tolerances. They cannot establish infinite-dimensional or all-size claims, which depend on the integration, regression and tree-factorization proof. The code requires no external files except its own source and makes no network calls. The closest inaccessible historical full text is Sinn and Keller (2011), DOI: 10.1137/S0040585X97984991. The scientific novelty assessment remains historical-priority qualified.
