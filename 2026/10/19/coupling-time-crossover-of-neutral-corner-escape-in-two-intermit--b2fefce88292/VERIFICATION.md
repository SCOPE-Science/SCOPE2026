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

The accompanying `check.py` runs under Python 3 without third-party packages and prints `VERIFY_OK` if finite checks succeed. It verifies the exact scalar threshold and endpoint areas at the allowed exponent \(p=3/2\), an independently integrated sample of the coupled ODE, the exact scaled recurrence at coupling \(\varepsilon_n=2/n\), and strong-coupling scalar relaxation. The sample tests have no logical bearing on the almost-everywhere or all-sequence limits; their proofs are the localization, comparison, convergence, and area arguments in `RESULT.md`. The finite interior coefficient remains implicit as a well-defined planar ODE survival area. Independent audit has not been performed.
