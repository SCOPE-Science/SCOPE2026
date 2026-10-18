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
The complete checker `checks/check_wheel.py` uses only standard-library Python and is run with `python checks/check_wheel.py`. `checks/check_output.txt` is the actual expected output, including `ALL_WHEEL_CHECKS_PASS`. It independently generates each wheel, enumerates its perfect matchings without using the closed formula, checks its simplicial facet-nerve isomorphism with cyclic intervals, checks every free endpoint-edge interval and exact remaining subcomplex, checks the Euler characteristic, and computes exact integer alternating signed Lefschetz sums for every dihedral rotation and reflection through the cases \(2\le r\le8\). It also checks all faces of the six-vertex ordinary matching complex, including the five added one-faces.

These finite checks do not establish the universal quantifier; the proof in `RESULT.md` gives the general combinatorial matching classification and explicit collapses. The general inclusion nullity for \(r\ge3\) also depends on the precise wheel homotopy theorem in reference [1]. A separate independent mathematical audit has not been performed.
