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
Run `python3 verify.py` using only the Python standard library. Expected output begins `VERIFY_OK:` and reports independent numerical quadrature comparisons, exact-field reconstruction at sampled states, the small-parameter limit, and agreement with the published \(n=2\), \(\kappa=1\) time period. Tests cover a finite set of even orders and coefficients and are not an exhaustive validation of the infinite theorem. The main proof is fully analytical. No independent audit has been performed.
