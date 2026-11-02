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

The standalone verifier `verify_leibniz.py` exhaustively enumerates bracket-preserving matrices over eight prime-field presentations, independently computes compositions, tests idempotence, and determines commuting adjacencies. All runs passed, covering orders 3, 5, 7, and 11 with split and nonsplit coefficients. The independent `verify_gf9.py` implements the extension field of order 9 using explicit addition and multiplication tables and checks one parameter of each square class. Both scripts require only Python standard-library modules and execute by `python verify_leibniz.py` and `python verify_gf9.py`.

The first script ends with `VERIFY_OK`; the second ends with `VERIFY_GF9_OK`. Neither finite enumeration is a proof over all finite fields. The general classification follows from the rank-one idempotent normal form and the two-dimensional isotropic geometry, with no appeal to the computations for infinite quantifiers.

Self-review: passed. Independent audit: not yet performed.
