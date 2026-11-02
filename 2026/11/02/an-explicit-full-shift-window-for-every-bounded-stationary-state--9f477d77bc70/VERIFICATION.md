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
Run `python verify_nagumo.py` in a directory containing the extracted package. The code verifies exact radical identities and derivative bounds, then computes sixteen independently sampled cyclic stationary profiles below the cutoff and checks their residuals. Finite cyclic tests do not establish uniqueness for all infinite sequences; that assertion is supplied by the complete Banach-contraction and maximum-principle proof in `RESULT.md`.

No external independent mathematical audit has been performed. The published comparisons have the source-access limitations listed in `REVIEW.md` and `AUDIT.json`.
