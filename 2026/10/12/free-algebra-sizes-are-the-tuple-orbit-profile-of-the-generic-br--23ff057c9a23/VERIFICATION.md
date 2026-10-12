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

The bundled `verify.py` independently reconstructs the free two-generated implicative semilattice from finite Kripke semantics. It enumerates all 23 labeled posets on one, two, or three points and all 564 choices of two monotone valuations on those frames, then closes the two generator signatures under meet and implication. The closure has exactly 18 elements.

On the resulting 18-element algebra it verifies the residuation law exhaustively, enumerates every deductive filter, proves computationally that exactly 18 occur and that all are principal, and constructs the congruence associated to each filter. Each induced relation is checked for equivalence and compatibility with both operations, and the 18 resulting congruence partitions are distinct.

Terminal output:

`VERIFY_OK 556584 exact assertions; 23 labeled posets, 564 Kripke models; free F_2 size=18; filters=congruences=18`

This is an independent low-arity anchor for \(|F_2|=|\operatorname{Con}(F_2)|=18\). The theorem for arbitrary arity is the universal-algebra/Fraïssé proof in `RESULT.md`; no finite extrapolation is used.
