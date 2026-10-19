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

# Reproducibility and scope

Run `python verification.py` using Python 3 standard library. It enumerates power-zero points over F_2 and F_3 for exponents 2 and 3, compares all three explicit linear subspaces in the nonmodular cases, and checks product counts for two independent endomorphism images. The program has been executed and returned `VERIFY_OK`. This finite evidence corroborates, but does not replace, the general proof based on coefficient extraction and the differential of the power map. Geometric nonreducedness follows from the displayed generic tangent-versus-component dimension comparison, not from finite enumeration. No independent audit has been performed.
