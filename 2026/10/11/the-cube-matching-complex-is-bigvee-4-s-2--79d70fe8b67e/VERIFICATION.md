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

`verify.py` reconstructs the cube matching complex directly from the twelve graph edges. It exhausts all edge subsets, checks the matching condition, and obtains \(107\) nonempty simplices with face vector \((12,42,44,9)\).

The program then replays the fixed sequential element matching in the order \(2,3,9,10,8,1,6,11,4,0,5,7\). It verifies \(51\) disjoint matched Hasse pairs and finds exactly one critical \(0\)-simplex and four critical \(2\)-simplices. The entire directed Hasse graph on \(107\) simplices and \(252\) covers is topologically sorted, proving acyclicity.

As an independent chain-level check, augmented boundary ranks over \(\mathbb F_2\) are \((1,11,31,9)\), so reduced mod-\(2\) homology has rank \(4\) in degree \(2\) and vanishes in the other represented degrees. The Euler characteristic is \(5\).

The finite checks establish the exact named complex. They do not constitute a classification of matching complexes of higher-dimensional cubes, and no independent audit has been performed.
