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

# Reproduction and limits
Execute `python3 artifacts/verify_diamond.py` and `python3 artifacts/verify_gf4.py` with Python 3. No third-party packages are required. The scripts enumerate the defining equations directly and check the Gaussian-sum formula in the documented finite cases. The second script uses actual multiplication in the four-element field; modular integer multiplication is not substituted for it. Exhaustive small-field tests are not an infinite proof. The general proof is the image-subspace factorization argument in RESULT.md. This work has not undergone an independent external audit.
