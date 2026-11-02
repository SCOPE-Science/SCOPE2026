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

The theorem is proved for all finite alphabet sizes at least two and all lengths at least two by an explicit canonical-shape separation argument in `RESULT.md`. The verifiers provide finite corroboration only.

Run `python3 verify_direct.py` and `python3 verify_shapes.py` using Python 3 (standard library only). They enumerate direct descendant sets and structurally indexed shape outputs, respectively. Recorded transcripts are included in `verify_direct.out` and `verify_shapes.out`; exact finite scopes are also stated in `RESULT.md`.

No result about general longer duplication blocks, three errors, or maximum error-correcting codebooks is claimed. No independent audit has been performed.
