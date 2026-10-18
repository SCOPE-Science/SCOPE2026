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

Run `python verify.py` to reproduce all finite weighted-count comparisons. The verifier exhaustively enumerates all binary contexts of sizes one to four and computes the complete concept-size partition, checking it against independent exact expectation expressions at three rational incidence probabilities. The finite checks establish the specified finite identities on tested sizes, not the asymptotic bound; the analytic proof supplies the unbounded quantifiers and the rooted-overlap variance estimate.
