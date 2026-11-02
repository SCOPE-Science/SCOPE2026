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

# Verification and limits
The proof's nonstandard step is the coordinatewise convex-order transfer for a perpetuity: finite truncations are multiaffine in the independent squared multipliers, and positive-part stop-loss transforms converge in \(L^1\) because the perpetuity has finite mean. That is an analytical argument, not a finite numerical claim.

The included `verify.py` was run with the local Python interpreter and SciPy/NumPy and reported: `PASS: 365 checks; exact rational moments, Fourier central densities and reproducible stochastic corroboration.` It independently compares generator-derived rational moments with the direct perpetuity binomial recurrence, checks kurtosis extremizers and finite higher moments, uses Fourier inversion of the known deterministic characteristic function for central densities, and simulates 48,000 stationary conditional variances per protocol with a fixed random seed.

Monte Carlo has sampling uncertainty and is not an exhaustive proof. Exact rational moment comparisons do not prove all convex functional inequalities. The full scope and proof are in RESULT.md. Independent audit: not performed.
