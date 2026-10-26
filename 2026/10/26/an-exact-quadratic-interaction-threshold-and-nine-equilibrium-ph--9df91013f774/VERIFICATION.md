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

# Verification details

The included `verify_quadratic_urn.py` was executed with Python 3 and SymPy. Its output appears in `verification_output.txt` and records 27 passing symbolic/high-precision checks: the subtraction identity, eliminated sum factorization, parameter derivative and endpoint, stability eigenvalues, and four explicit substitution examples.

The script does not exhaust continuum values or prove the probabilistic stochastic-approximation theorem. Those portions are argued analytically in RESULT.md and supported by the cited primary source. In particular the probability of domination at the exact critical parameter has not been proved.
