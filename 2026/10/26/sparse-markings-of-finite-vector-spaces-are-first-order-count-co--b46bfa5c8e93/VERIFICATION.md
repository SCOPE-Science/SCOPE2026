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

The proof is mathematical; no external proof certification is claimed. The finite reproducibility checker tests independent marked-set counts for dimensions one through five over the binary field, an exhaustive two-round EF game for three representative pairs, and six numerical Poisson factorial-gap cases at unit intensity. Its output is `VECTOR_SPARSE_FO_FINITE_OK 19 EF2_3 POISSON_GAPS6`. Run `python check_vector_fo.py` in a directory containing this file and the checker. Tests are deliberately finite; they do not establish the asymptotic quantifiers, the general finite-field EF lemma or originality.

Scientific limits: fixed finite field, fixed positive intensity and ordinary first-order language. The numerical probability spectrum is known in the different random ordered-bit-string structure (St. John, 1997); the finite-field vector-space collapse is the assessed claim. Independent review has not been performed.
