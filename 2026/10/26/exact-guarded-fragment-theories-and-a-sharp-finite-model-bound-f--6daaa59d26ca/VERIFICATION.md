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

The structural argument is an all-size guarded back-and-forth proof on one-equivalence, unary-coloured structures, with equality but no other relational symbols. Only guarded singleton/pair moves are needed; profile multiplicities \(0\), \(1\), and \(\ge 2\) give exactly the local supply for those moves. The class-profile existence predicates are explicit rank-at-most-three guarded formulas. Their complete conjunction forces one representative of every nonzero profile, proving the sharpness of the finite-model bound.

Run `python verify_guarded_equiv.py` with Python 3 and no third-party modules. The script exhaustively checks \(1954\) labelled equivalence structures with one unary predicate on up to five points, including \(418\) finite back-and-forth tests, and independently checks deletion minimality of the canonical extremal models for \(1\), \(2\), and \(4\) unary colours. Expected signals include `SHARP_PROFILE_BOUND_OK 2 8 18` and `CANONICAL_GUARDED_EQUIVALENCE_OK 1954 418`.

The finite enumeration is not an infinite proof. The theorem is restricted to constant-free signatures with a single equivalence relation and unary predicates, without further binary guards. Historical priority is qualified: the general guarded-bisimulation theorem and small-model constructions precede this calculation, and the possibility of an earlier explicit special-case computation remains.
