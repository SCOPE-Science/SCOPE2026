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
Run `python verify.py` from a directory containing NumPy. It builds actual finite-dimensional block matrices independently of the Gram construction, checks their exact numerical-radius identities to numerical tolerance, and tests the first-order angular coefficient. These finite tests are supplementary; they do not prove the claims for all words or arbitrarily large Hilbert spaces. Those conclusions are established analytically in RESULT.md. Independent audit has not been performed.
