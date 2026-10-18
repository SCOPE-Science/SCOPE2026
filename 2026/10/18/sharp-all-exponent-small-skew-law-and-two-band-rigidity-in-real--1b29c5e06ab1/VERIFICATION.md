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

# Reproducibility

Run `python verify.py` using Python 3 and SciPy. The script checks scalar stationarity, the two-band equality witness, eleven exponents, and 2,222 deterministic diagnostics for selected ratios and small positive perturbations. Exact universal inequalities, equality classifications, and asymptotics are established by the analytic proof in `RESULT.md`, not by these finite tests. The published source's first-version date and MSC ownership were checked separately. No independent scientific audit has been performed.
