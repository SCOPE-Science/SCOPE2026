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

The exact script `verify_cap.py` constructs the thirteen projective points and all lines over the three-element field, cross-checks a separate thirteen-line table, and enumerates every possible arc of size one through five. It verifies the complete line-incidence design, all \(52\) missing triangular boundaries, the complete face vector, the two consecutive chain identities, and the integral Smith forms of all three nontrivial simplicial boundaries. It additionally determines the rank of the top boundary modulo three using separate finite-field Gaussian elimination.

Run `python3 verify_cap.py` with the package dependency specified in `requirements.txt`. The executed stdout is `verification.out`; the final line `VERIFY_OK` appears only after every asserted condition succeeds. This is an exhaustive calculation for the specified finite complex, not an experiment on a growing sequence of examples.

The homotopy equivalence uses a separate mathematical argument: simple connectivity of the second skeleton, the Hurewicz and homological Whitehead theorems for its two-dimensional CW structure, and Smith reduction of the attaching-degree map. No assertion of independence or third-party certification is made. The original ordered noncollinear-tuples chain complex is excluded from the computational scope.
