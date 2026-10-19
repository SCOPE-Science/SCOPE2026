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

# Reproducibility checks

The included `verify_sixth.py` was executed with Python 3 and SymPy. It directly constructs the stationary Fourier-generator moments of orders two, four and six, verifies the connected-cumulant subtraction and the exact displayed rational numerator, constructs the resultant rather than reading a precomputed polynomial, uses exact Sturm root counts on rational intervals, verifies strict positivity of shifted polynomial coefficients, and checks weak-confinement asymptotics. It reports the critical root to high precision only after the exact root-location checks.

All assertions passed. The proof of infinitely many parameter values comes from the exact recurrence, polynomial convexity, resultant/Sturm counts and positivity certificate, **not** from floating-point root searches. No independent audit or external validation is claimed. The technical full text of arXiv:2404.09650 and supplemental material of related papers were not fully inspected, leaving a mathematical-priority risk.
