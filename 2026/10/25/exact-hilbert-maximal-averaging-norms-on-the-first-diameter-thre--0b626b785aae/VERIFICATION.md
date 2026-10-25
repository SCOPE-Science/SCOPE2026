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

Execute `python3 verify_cycles.py`. The standalone program enumerates every one of the \(4^6=4096\) and \(4^7=16384\) radius masks, checks exact leading principal minors for every losing mask, verifies rational Rayleigh witnesses and isolating upper bounds, and reconstructs the characteristic polynomials as integer signed principal-minor sums. Success is indicated by `ALL_CERTIFICATES_OK`.

The proof of the nonlinear-selector reduction and classification of equality cases is in `RESULT.md`. The complete enumeration is finite and establishes no untested infinite-family statement. Approximate decimal values are illustrative. Independent audit: not performed.
