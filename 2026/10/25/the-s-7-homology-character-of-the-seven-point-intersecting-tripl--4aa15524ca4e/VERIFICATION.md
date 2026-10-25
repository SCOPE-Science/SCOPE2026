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

The standalone script `verify_s7_kneser.py` uses only Python's standard library and terminates with `VERIFY_OK` when every exact assertion succeeds. Execute from the directory containing the script via `python3 verify_s7_kneser.py`. The corresponding captured output is `character_table.txt`.

It checks the seven six-symbol cross-polytopal supporting complexes, their chosen ten-triple maximal facets, and the fact that each facet has no common neighbor among the other 35 triple vertices. It independently checks all 720 permutations on each standardized six-point cross-polytope for the orientation sign rule. For each of the 15 conjugacy types of \(S_7\), it constructs the orbit incompatibility graph and compares a memoized independence-polynomial recurrence against a direct nonmemoized enumeration of every invariant simplex. Character calculations are exact integer counts. At the identity type, the direct enumeration covers 1,278,686 faces including the empty face.

The proof additionally invokes Feng's published arXiv Theorem 18 (arXiv:2610.17394v1) for the rational Betti dimensions and vanishing outside degrees six and nine. This script does not independently reprove that external non-elementary theorem. It does not test integral torsion, integral homotopy type, or larger ground sets. Independent scientific audit remains unperformed.
