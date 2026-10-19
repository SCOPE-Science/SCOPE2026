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

# Reproducibility and verification

Run `python3 verify.py` in a standard Python 3 environment. The script prints `VERIFY_OK` if all assertions succeed and needs no third-party packages.

The first check enumerates the thirteen reachable states of the pair-memory transfer system for triple commuting idempotents. With its exact integer matrix, the initial triple counts are `1, 8, 46, 254`, and it checks thirteen consecutive terms of the fourth-order recurrence. Cayley–Hamilton in dimension thirteen then establishes the recurrence at *every* later term, not merely the checked range. The script checks further coefficients and tests the general finite-state transition construction at other arities.

The second check constructs each parabolic longest permutation and Demazure product for zero through six Coxeter generators, independently constructs the matching Catalan retractions, and verifies pairwise commutation reflection and product matching exhaustively. It also counts all ordered pairwise-commuting triples for zero through five generators and compares with the rational coefficients.

The general commutation reflection rests on the parabolic-cut argument in the proof, not on finite enumeration. The only external algebraic lemma is the standard characterization of idempotents in the 0-Hecke monoid and the Bruhat-maximal-product property cited in the result. All calculations use exact integer arithmetic. No independent mathematical audit has been performed.
