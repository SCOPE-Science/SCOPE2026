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

# Verification status

The finite and symbolic tests were executed using `python checker.py` from the supplied standalone package. The checker returned `PASS` after exact symbolic identities at six index values, polynomial factorizations for both finite-support claims, the explicit rational negative example, and 400 exact-rational parameter/index checks. The monotonicity of \(H(t)\) for all real \(t\ge1\), its first-value sign, and its limiting sign provide the infinite-index proof and are not replaced by computation. All parent probabilities are explicitly normalized and supported on the domains stated in RESULT.md.

Scientific peer review, independent replication, and independent novelty validation have not been performed.
