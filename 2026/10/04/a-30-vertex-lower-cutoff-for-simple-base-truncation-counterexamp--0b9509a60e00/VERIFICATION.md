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

`verify.py` performs an exact finite replay of the stated domain. It generates connected simple cubic graphs on \(4\), \(6\), and \(8\) vertices, merges isomorphic copies, checks the expected type counts \(1,2,5\), builds every truncation and its strong-edge conflict graph, verifies a local six-clique, searches for a 6-coloring, and checks the resulting coloring on every conflict edge.

The recorded run used NetworkX 3.6.1 and produced connected labeled-generation counts 1, 70, and 19,320, with all eight isomorphism representatives passing. The finite experiment proves only the bounded statement through base order eight; it is not evidence for base order ten or above.
