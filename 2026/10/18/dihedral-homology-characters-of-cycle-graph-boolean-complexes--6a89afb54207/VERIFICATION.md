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
# Verification of the character formula

The result concerns the regular Boolean cell complex of the simple cycle and its geometric vertex relabeling action. The cellular orientation sign is the permutation parity on the selected vertices.

`verify_orbit_counts.py` enumerates the fixed oriented cells directly for every rotation and reflection with 3 through 11 vertices, and compares all traces with the closed formulas. `verify_cellular_chains.py` separately assembles exact signed boundary matrices of the commutation-class cells for 3 through 6 vertices; computes their rational homology; and obtains dihedral traces on the top kernel from linear-algebra restrictions. The two scripts use dissimilar verification methods. Both passed.

For the full chain calculation the cell counts by dimension are 3,6,6 for the triangle; 4,10,16,14 for the four-cycle; 5,15,30,40,30 for the five-cycle; and 6,21,50,84,96,62 for the six-cycle. Their top reduced homology ranks are 2,5,9,16, respectively, matching the Lucas formula. All tested group traces agree with the stated characters. Python 3 is required for both scripts; SymPy is required for the chain script.

These tests are exhaustive **only within the stated small ranges**, not for all \(n\). All-parameter validity follows from the proof's homology concentration, Lefschetz trace, cycle coloring transfer and reflection recurrence. The scientific assessment is a self-review only; no independent audit or external certificate has been performed.
