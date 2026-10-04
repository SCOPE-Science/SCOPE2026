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
The verification package contains `certificates.json` and `verify.py`.

`verify.py` reconstructs every length-\(2\) palindromic duplication and every valid inverse palindromic deletion from each binary word of length \(6\). It constructs each conflict graph both by direct pairwise descendant-set intersections and by inverting the source-to-descendant relation, then asserts that the edge sets coincide.

It verifies the \(40\)-word duplication code and the \(42\)-word deletion code, checks the \(24\) disjoint conflict pairs used for the duplication upper bound, and checks the eight conflict triangles, six conflict pairs, and \(28\) remaining singletons used for the deletion upper bound. The expected replay ends with `VERIFY_OK`.

The computation is finite and exhaustive over all \(64\) source words. No claim is made beyond the stated alphabet, source length, duplication length, and one-error radius.
