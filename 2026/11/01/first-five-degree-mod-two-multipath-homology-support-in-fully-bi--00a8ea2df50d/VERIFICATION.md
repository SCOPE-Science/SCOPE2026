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

# Exact finite verification

The accompanying standard-library-only script `verify_bidirected_wheels.py` runs complete enumerations for each rim length from three to ten. For each graph, it uses an arc-reachability inclusion/exclusion enumerator and a separate undirected-path-forest/orientation enumerator, and requires *equality of every encoded simplex*, not merely agreement of counts. It forms all simplicial boundary columns over \(\mathbb F_2\), computes exact binary ranks, verifies the Euler–Poincaré identity, checks connectedness, and asserts the complete claimed reduced Betti dictionaries. All counts and boundary ranks are captured in `verification_output.txt`. The largest case has \(220395\) faces, and the complete ranks in successive positive degrees are \(39,571,4089,15631,32333,34778,18082,4238,340\). The full calculation ran to successful completion and emitted `BIDIRECTED_WHEEL_FIRST_FIVE_DEGREES_EXACT_GF2_VERIFIED`.

This is a finite exhaustive computational proof. It does not verify integral torsion, homotopy equivalence, or results outside the specified eight cases. Independent review has not occurred.
