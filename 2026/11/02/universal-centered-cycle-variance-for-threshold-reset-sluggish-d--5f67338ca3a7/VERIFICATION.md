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

# Reproduction and limits

Run `python verification.py` with Python 3 and SymPy installed. It checks a formal symbolic identity for an arbitrary positive real exponent, the regenerative centering identity, 108 exact rational evaluations through a second Green-function formula, and 24 numerical quadratures at noninteger exponents. The reference output is embedded as `verification_output.txt`.

The analytical proof is in `RESULT.md`: the Green kernel, Dirichlet Poisson solution, stochastic-energy identity, and regenerative central limit step are the critical mathematical dependencies. No finite test is treated as a proof of a continuum law. No independent mathematical audit or independent verification has been performed. Claims of literature noncoverage are confined to the inspected material and comparisons stated in `REVIEW.md` and `AUDIT.json`.
