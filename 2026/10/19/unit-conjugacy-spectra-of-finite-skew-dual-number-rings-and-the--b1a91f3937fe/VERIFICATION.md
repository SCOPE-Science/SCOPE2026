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

# Reproducibility

Run `python verify.py` using Python 3 and its standard library. The checker independently enumerates all elements, unit conjugators and commuting pairs in finite skew dual-number rings of field orders 4, 8, 9, 16 and 25, for all nontrivial Frobenius twists in each field. It checks orbit sizes against the closed formula, counts commuting pairs exactly, verifies the radical square is zero, and tests that products of units are units. The expected terminal message is `VERIFY_OK`.

The proof of the general result is in RESULT.md. The computation does not establish the infinite statement on its own, nor does it exhaustively enumerate the 32-element-field counterexample, which is justified by the cyclic Galois-group calculation. No independent scientific audit or third-party certification has occurred.
