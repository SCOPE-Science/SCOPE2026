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

# Verification record

Run `python verify_threshold.py`. The self-contained checker constructs the exact two-group transmissibility matrix and independently bisects its Perron-threshold equation. It also verifies determinant and trace identities using rational arithmetic, small-contrast/near-segregation asymptotic regression, fixed-h sensitivity, and a neutral case where the trace-only approximation makes the wrong supercritical prediction. Every regression is finite; the proof's global and asymptotic quantifiers require the analytical arguments in RESULT.md. The reviewed open preprint is arXiv:2601.21743; the journal publication date is January 8, 2026. No independent scientific audit has been performed.
