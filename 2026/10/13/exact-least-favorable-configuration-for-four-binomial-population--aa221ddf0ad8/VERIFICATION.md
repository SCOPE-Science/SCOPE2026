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

# Verification

Run `python3 check_exact.py` after extracting the exact accompanying file. The program independently enumerates \(81\) quadruples of two-trial binomial counts and \(24\) orderings of the auxiliary continuous tie-break ranks. It computes exact rational coefficients and checks equality of the complete bivariate polynomial in gap and displacement against the closed form in RESULT.md. It also checks three rational gaps and their interval endpoints; these additional examples are not the source of the universal assertion.

The run completed: `PASS: independent 24-ranking/81-count enumeration; full polynomial identity; boundary tests`, with \(26\) count configurations of nonzero success weight and \(14\) nonzero polynomial monomials.

The analytic step is to minimize the bracket at \(|h|=(1-\delta)/2\) and prove its value exceeds \(7+110\delta+11\delta^2\) for \(0<\delta<1\). This verifies unique minimization of the full symbolic polynomial. For the general preference zone, the separate finite-sample coupling and its strict interior equality statement appear in Wu--Chen, Proposition 2.1 and Appendix A. No symbolic-checker result alone establishes the underlying stochastic reduction. The theorem does not cover other sample counts or selection group sizes, and independent audit has not been performed.
