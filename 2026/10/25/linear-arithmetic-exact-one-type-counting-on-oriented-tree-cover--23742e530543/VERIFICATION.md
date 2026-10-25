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

The proof uses a uniqueness lemma for the branching point of an antichain's common lower bounds in a directed tree. The lemma is proved in RESULT.md by uniqueness of undirected paths. For each \(v\), \(D_v\) and \(U_v\) count ideals and filters in directed principal subtrees, and \(J(P)\) is computed by an independent two-state ideal dynamic program on the undirected tree.

The standard-library-only file `verify_tree_posets.py` independently enumerates all three-way labels for a new point, checks cover monotonicity and cross-relations via reachability, and compares its count with the formula. Reproduction command: `python verify_tree_posets.py`. Expected final line: `ALL_TESTS_PASS`.

A successful run checked 43,614 exhaustive oriented labeled tree configurations through six vertices, 480 larger randomized configurations, and six named examples. The exact stdout is saved as `verification_output.txt`. None of the finite checks are offered as proof of the infinite family. Completeness of prior-literature coverage and publication priority remain unverified; the 1980 insertion-position paper was available only at abstract level.
