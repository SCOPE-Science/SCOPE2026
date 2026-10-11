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

The analytical proof is in `RESULT.md`. The standard-library script `verify.py` checks twelve rhombus aspect/scale settings by enumerating angles and positive side-length ratios. For each sampled rectangle it computes all vertex gauges directly and compares the feasible area with the exact proposed maximum. It additionally samples both possible equal-radius boundary branches and checks the determinant bounds.

Run `python verify.py`; an observed run from this package source returned `VERIFY_OK: 12 dimensions, centered rectangle grids, and boundary regimes`.

The finite checks are illustrative and cannot prove the universal claim or uniqueness. The proof of all parameter ranges uses the boundary/orthogonality dichotomy, strict concavity, AM-GM, and exact equality conditions; it requires no external numerical certificate. No independent audit has been performed.
