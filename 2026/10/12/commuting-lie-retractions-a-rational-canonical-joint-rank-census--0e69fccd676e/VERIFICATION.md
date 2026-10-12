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

# Computational verification

Run `python3 verify_commuting_retractions.py` with Python 3.9 or later and no third-party libraries. The checker computes actual Lie brackets, tests idempotent Lie-homomorphism equations on all linear maps in the listed small prime-field cases, and counts commuting ordered pairs by matrix multiplication. It compares the entire joint-rank histogram with the independent module-type formula and prints `VERIFY_OK` on success.

Exhaustively checked uniform Jordan examples: (field size, blocks, length) `(2,1,1)`, `(3,1,1)`, `(2,2,1)`, `(2,1,2)`, `(2,1,3)`; additional full-map checks cover an irreducible quadratic over `F2`, two distinct nonzero eigenvalues over `F3`, and the mixed partition `(2,1)` over `F2`. Some cases overlap to exercise both formula implementations. Larger cases merely evaluate the formula and check that the pair count does not exceed the square of the single count; they are **not** exhaustive experiments.

The result over all finite fields and arbitrary dimensions follows from the proof's module decomposition and automorphism-group arguments, not from these finite checks. No formal proof-assistant or independent external verification is asserted.
