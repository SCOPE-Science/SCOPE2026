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

# Reproducible checks

Run `python3 verify.py` in the directory containing `canonical_classes.json`. Python's standard library suffices. The program regenerates the 357-state breadth-first quotient rather than trusting the manifest, verifies 714 outgoing transitions, and computes an independent rank-three type by recursively collecting complete adjacency-and-equality diagrams of tuples of lengths at most three. The independent checker gives 357 distinct types and confirms the transition predictions for every state. A supplementary exhaustive enumeration covers all 8191 binary creation words of length 0 through 12. The observed output is embedded in `verification_output.txt` and ends with `VERIFY_OK`.

## Logical bridge to arbitrary orders

Any threshold graph is built by iteratively adding an isolated or universal vertex. Three-round elementary equivalence is preserved by each operation: the isolated-vertex assertion is witnessed by the disjoint-union Ehrenfeucht–Fraïssé strategy, and the universal-vertex assertion follows by graph complementation. Therefore finite closure of the state graph is sufficient to cover creation words of arbitrary finite length. The BFS assignment of first-reached states certifies that the two listed 17-vertex classes have no smaller threshold-graph representatives.

## Scope and limitations

Computations use exact integer bit masks and immutable finite sets. A finite experiment without the stated closure argument would be insufficient. No independent external review or formal proof-assistant certification was performed. The reported minimal order concerns threshold-graph representatives only.
