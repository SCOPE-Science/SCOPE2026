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

# Verification instructions and limits
Run `python3 build_certificates.py` and then `python3 verify_separable.py` from a directory containing the three supplied files `build_certificates.py`, `certificates.json` and `verify_separable.py`. Python 3's standard library suffices.

The builder's exact version-space recurrence asks whether a nonempty set of candidate permutations can shatter a binary comparison tree of prescribed depth. Each candidate split partitions the set according to whether a fixed earlier position contains the lower value. The recursion requires both children to shatter one less level. It serializes every internal query and each terminal witness, without relying on sampling or output logs alone.

The verifier uses a separate sum/skew closure enumeration and a forbidden-pattern scan, checks that both descriptions produce identical separable permutation families, checks all stored tree nodes and all leaf-witness evaluations, and verifies that adjacent queries realize every Boolean labeling. It explicitly verifies \(1023\) internal queries and \(1024\) distinct terminal witnesses at seven positions. For each size, the exact concept count supplies an upper depth bound by \(2^d\le|\mathcal S_n|\). The final expected output line is `SEPARABLE_ALL_NEW_CHECKS_PASS`.

Recorded successful execution on the packaged input gave depths \(0,1,2,4,6,8,10\) for sizes one through seven. The all-size VC statement and all-size lower bound on the adaptive-static gap are proved separately in `RESULT.md`; no finite program substitutes for those inductions. Priority in the unexamined literature and exact dimensions beyond seven remain open to further assessment.
