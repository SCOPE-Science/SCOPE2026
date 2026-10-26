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

# Reproduction and limitations
Execute `python3 check.py` with NumPy and SciPy. Its backward-boundary ODE computation differs algebraically from its separate rational-polynomial evaluator. Tests include 1,500 independent random physical instances of those two forms, 1,500 finite-difference derivative comparisons, 250 bounded optimization comparisons, analytic threshold-side checks, four endpoint-asymptotic scales, and 30,000 independent event-driven particles for each of three control rates. All ran successfully in this package; precise numerical tolerances and seeds are in the code. Numerical concordance checks normalization and implementation, but cannot prove uniqueness over infinitely many parameter choices; the latter is proved by the monotone derivative numerator in `RESULT.md`. No external formal or independent audit has been performed.
