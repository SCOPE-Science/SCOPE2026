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

# Reproducibility and verification

Execute `python3 verification/check_crown.py` in a Python 3 environment; no third-party packages are needed. The program rebuilds graph distances directly, constructs all invariant vectors and expected eigenvalues independently from the block form, and checks 5,152 vector/eigenvalue identities for crown sizes 3–25 at eight exponents. It also checks the endpoint root signs and three large-order asymptotic approximations. The recorded result was:

`CHECK_OK 5152 explicit vector/eigenvalue tests; 23 boundary tests; 3 asymptotic tests`

These tests are finite corroboration. Infinite-size and all-parameter assertions rely on the exact proof in `RESULT.md`. The method's nontrivial external premise is Schoenberg's equivalence between conditional negative type and positive definiteness at every bandwidth. Literature overlap was checked through actual scholarly full text and independent indexed-result searches, with remaining uncertainty documented in `AUDIT.json`. Independent audit and independent validation have not been performed.
