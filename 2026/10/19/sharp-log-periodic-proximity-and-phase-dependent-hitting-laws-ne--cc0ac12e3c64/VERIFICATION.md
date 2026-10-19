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

# Verification notes
The analytical proof reduces the problem to (i) exact cylinder weights, (ii) deterministic gap-to-Cantor distance bounds, (iii) whole-level separation, (iv) step-function squeezing, and (v) geometric waiting times. The companion `verify.py` is independently runnable with Python's standard library and tests the elementary identities in finite exact-rational cases. Its output reports the number of passed diagnostics and the predicted constants.

Finite checks use integer parameters only, and neither numerical tests nor partial symbolic enumeration prove the universal real-parameter or all-scale limits. Absolute continuity, a spectral gap, and a law at every intermediate shrinking radius are not assumed or asserted. Bibliographic novelty remains contingent on the inspected sources and has not received an independent audit.
