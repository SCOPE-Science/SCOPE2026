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

The verifier constructs the natural degree-\(4\) alternating group, checks its point stabilizer and hence its \(2\)-transitivity, and generates the complete transformation monoid obtained after adjoining
\[
f=(0,0,1,1).
\]
For every element of that monoid it confirms that \(\{0,1\}\) and \(\{2,3\}\) have equal image cardinalities.

A separate pair-state traversal checks the proof invariant directly: every reachable ordered pair is either two singletons, two identical two-subsets, or two complementary two-subsets.

As a supplementary stress test, all \(84\) rank-\(2\) and all \(144\) rank-\(3\) transformations on four points are exhausted. There are \(36\) rank-\(2\) failures of the strong condition and no rank-\(3\) failures. The main separation proof uses only the explicit displayed rank-\(2\) witness.

Independent audit has not been performed.
