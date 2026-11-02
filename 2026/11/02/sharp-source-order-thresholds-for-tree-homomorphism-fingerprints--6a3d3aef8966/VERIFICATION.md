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

`verify_tree_profiles.py` is a Python-3 standard-library-only complete enumerator for all source trees through eight vertices and target trees through thirteen. It verifies exact profile partitions at every target order four through thirteen, the minimum budget sequence, collision orders, the unique order-thirteen collision, and the five size-eight distinguishing probes. It independently checks small DP counts by direct mapping enumeration. Final marker: `ALL_BOUNDED_TREE_SOURCE_PROFILE_CHECKS_PASS`.

`verify_tree_profiles_alt.py` uses the independently developed `networkx.generators.nonisomorphic_trees` and another rooted recursion. Its final marker: `INDEPENDENT_BOUNDED_PROFILE_CROSSCHECK_PASS`. It requires NetworkX installed separately. Results of both executions appear in `verification_output.txt`.

The proofs of enumeration completeness and the homomorphism recurrence appear in `RESULT.md`. These are exact computations over finite sets, not statistical experiments. No target of order above thirteen was exhaustively checked or asserted. Outside scientific review/validation has not been performed.
