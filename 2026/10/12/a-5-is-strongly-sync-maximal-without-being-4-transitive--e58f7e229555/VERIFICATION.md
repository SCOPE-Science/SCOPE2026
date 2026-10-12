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

Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the \(60\) even permutations on five points and checks that the natural \(A_5\) action is transitive on both ordered-pair types of distinct \(2\)-subsets: intersecting and disjoint.

It then exhausts all permitted non-permutations:
\[
300\text{ rank-\(2\) maps},\qquad
1500\text{ rank-\(3\) maps},\qquad
1200\text{ rank-\(4\) maps}.
\]
For each map and every ordered pair of distinct \(2\)-subsets, it finds an even permutation \(g\) such that applying \(g\) and then the map collapses exactly one of the two subsets.

A separate constructive check reconstructs the local intersecting and disjoint witness pairs from the fiber structure used in the proof.

Independent audit has not been performed.
