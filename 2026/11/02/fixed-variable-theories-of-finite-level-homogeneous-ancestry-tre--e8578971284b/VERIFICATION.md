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

# Reproducible finite checks

Run `python3 code/support_check.py` and `python3 code/logic_refinement.py` using Python 3 standard library only. Their printed output should exactly match `verification/support_output.txt` and `verification/logic_output.txt` respectively. The source scripts use explicit prefix-address trees, no external data, and raise on each failed asserted comparison.

The support checker enumerates every vertex of each tested level-homogeneous tree. For two pebbles it records the depth of the surviving anchor and the four order possibilities for a new vertex; for three and four pebbles it records all selected depths and pairwise longest-common-prefix depths. It then compares complete one-vertex extension support tables. It exhausts all branching profiles from the displayed finite domains at heights \(0\) through \(3\), plus four four-variable boundary pairs.

The independent logical-type checker computes the exact finite fixed point of noncounting \(k\)-variable first-order types by simultaneous partition refinement on all *partial* assignments (unassigned pebbles included). It compares the unassigned initial states on nine pairs and reports the stabilization iteration. No approximation or randomized search occurs.

These checks are finite corroboration. The all-height and all-branch-factor theorem is established by the explicit two-pebble and \(k\)-pebble back-and-forth proofs in `RESULT.md`; none of these computations alone proves infinite generality. Independent audit has not been performed.
