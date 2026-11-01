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
# Verification record

The accompanying `verify.py` was run with Python 3, `numpy` and `mpmath`. Its exact Fraction calculations verify 300 telescoping identities and nonnegative mass differences; additional deterministic asymptotic constant checks bring the total to 328 passed assertions. The report `verification_output.txt` contains the reproduced output including finite Monte Carlo at three crossover values. No simulation is an infinite proof or a full empirical confirmation of asymptotic rates at finite horizons. The proof uses the exact return-time product, clipped-mean convergence, Chebyshev and union bounds, iid rare-mark Laplace functionals, and shrinking-index-band control of incomplete excursions. No independent validation was performed.
