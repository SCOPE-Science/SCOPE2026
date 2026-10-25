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

# Reproduction
Run `python3 verify_dense_local.py` (Python 3.10+, standard library only). The checker exhaustively generates all labeled tournaments on one through six vertices, filters local transitivity, groups score multisets, and explicitly tests isomorphism; it enumerates the two six-point witnesses' complete one-vertex extension patterns and proves their distinct regular-five counts by finite exhaustive search. The same checker tests the stated transitive-substitution witnesses at sizes six through seventeen.

The companion `verify_dense_local.out` is the direct successful execution output, ending in `ALL_CHECKS_PASS`. Finite experiments for larger chain lengths corroborate, but do not establish, the infinite claim, which rests on the substitution/degree/regular-five proof in the result. Independent scientific audit remains unperformed.
