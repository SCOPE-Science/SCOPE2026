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

The standalone `verify.py` requires only standard Python 3 and can be run with `python3 verify.py`. It tests exactly the model and star formulas in the result, not an independently audited external implementation.

The replay reports 1,302 exact two-by-two characteristic-polynomial and finite-limit comparison identities, 20 exactly solved star graph-energy identities, one additional nonstar graph energy, and the exact 21-patch threshold witness; it also checks numerical convergence against the analytic first-order correction. The universal theorem rests on the explicit mathematical proof in `RESULT.md`; finite checks do not certify arbitrary graph sizes or real parameters. Direct model interpretation is quasi-stationary, and historical priority has not been independently certified.
