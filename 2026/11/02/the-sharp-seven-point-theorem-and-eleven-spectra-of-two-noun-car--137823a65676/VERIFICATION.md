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

# Verification evidence

`python3 checker.py` first evaluates all 64 raw sentence forms on every four-cell vector of positive total size at most \(10\), confirming exact equivalence to the normal-form invariant. It then checks the truth-profile reduction for every four-cell vector of positive total size at most \(30\), covering 46,375 vectors. It verifies support and comparison-sign conservation, the seven-element witness bound, and exactly 67 distinct semantic profiles; it checks explicit spectra through size \(28\). Execution returned `ALL_CHECKS_OK`.

The general theorem is proven using four-cell semantics, a complete sign-chamber reduction, direct profile counting, Jiang's general finite-spectrum classification, and explicit all-size witnesses. The script does not establish all infinite cases or historical priority. No independent audit has been performed.
