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

# Reproducible checks

Execute `python verify_rule90.py` with Python 3 and no third-party packages. The script uses a polynomial-time bit-level Krylov rank implementation, a separate direct inversion-orbit enumeration, and complete finite fair-noise transition-history enumeration. The results are 107493 rank/time checks, 40 full noise-history laws, and 65 direct dual-orbit counts, all PASS. The infinite proof is in RESULT.md, not in these finite checks.

All scientific checks concern the precise two-site fair additive-noise model. Independent scientific audit has not been performed.
