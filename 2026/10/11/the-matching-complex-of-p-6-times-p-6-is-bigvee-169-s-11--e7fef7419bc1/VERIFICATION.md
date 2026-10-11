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

The accompanying `verify_p6p6_matching.py` is a standalone Python standard-library verifier. It performs the following exact checks:

- reconstructs the categorical product on 36 vertices and 50 edges;
- verifies the two parity classes are connected, have 18 vertices and 25 edges each, and are isomorphic by reflection;
- enumerates every one of the 12,900 nonempty matching faces of one component;
- verifies the face vector \((25,244,1195,3139,4377,3001,846,72,1)\);
- replays the fixed 6,443-pair face-poset matching;
- reconstructs all 63,027 Hasse covers and proves acyclicity by a complete topological sort;
- verifies that the only critical cells are one in dimension \(0\) and thirteen in dimension \(5\);
- independently computes all mod-\(2\) simplicial boundary ranks, obtaining reduced Betti rank 13 only in degree \(5\).

These checks establish the finite component homotopy type used in the proof. The final join step is a mathematical identity for matching complexes of disjoint unions. The verification does not test or claim any parameter values beyond \((6,6)\).
