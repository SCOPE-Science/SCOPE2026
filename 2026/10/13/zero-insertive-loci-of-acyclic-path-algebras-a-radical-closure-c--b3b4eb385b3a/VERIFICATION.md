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
# Reproducibility and proof scope

Run `python3 verify.py` with the Python standard library. The script exhaustively checks all triples of elements in the binary path algebras of the directed three-vertex line and of the directed source–sink fork; it finds six and four zero-insertive elements respectively, with direct coefficientwise comparison to the asserted descriptions. The script also independently enumerates radical coefficient triples for field sizes two, three and five and checks the displayed sharp deficit formula.

Expected final output: `VERIFY_OK`. These finite checks are bounded verifications. The all-field, all-finite-acyclic-quiver theorem follows from the vertex-quotient argument, the source/sink factorization, the three-vertex quotient rank obstruction, and the path-coordinate count in the written proof. In particular, no computational run over finitely many fields is treated as proof for all fields or all quivers.

The zero-insertive locus need not be a subspace in the non-square-zero case; all set equalities in the proof use the displayed definition with a single sandwich triple, not finite sums of sandwiches.
