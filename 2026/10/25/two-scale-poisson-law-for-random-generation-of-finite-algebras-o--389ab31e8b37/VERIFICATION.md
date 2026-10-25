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

The theorem is proved by explicit finite-algebra selectors and a separate factorial-moment argument. The checker uses no nonstandard library; run `python checker.py` with Python 3.9 or newer. It exhaustively enumerates ordered generator tuples in twelve small algebras, closes under the primitive operations, and compares counts against the falling-factorial identity; its final success marker is `ALL_CHECKS_OK`.

The exhaustive diagnostic does not certify any infinite-parameter statement. No independent audit, formal proof assistant, or external certification has been performed. Source-based priority risk is described in `REVIEW.md` and `AUDIT.json`.
