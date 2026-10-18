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

# Reproducibility and limits

Run `python verify.py` with the Python 3 standard library. The checker enumerates all \(r	imes m\) binary contexts in specified small dimensions and independently recomputes the number of concept extents. It compares these counts with integer inclusion–exclusion and computes numerical critical-window probabilities. Successful execution prints `VERIFY_OK`.

The general exact formula and asymptotic claims rely on the coatom-column characterization, disjoint-type inclusion–exclusion, factorial moments, and concentration inequalities given in `RESULT.md`; numerical experiments alone do not establish them. No independent external mathematical audit has been performed.
