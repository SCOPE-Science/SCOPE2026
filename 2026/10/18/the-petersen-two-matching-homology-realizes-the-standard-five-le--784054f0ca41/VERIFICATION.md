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

# Reproducibility of the rational symmetry calculation

Run `python3 verification/verify_character.py` in this package. The implementation uses only the Python standard library, reconstructs all vertices and edges of the Petersen graph as disjoint pairs of two-subsets, and enumerates every valid degree-two edge subset. The calculation is complete for this finite graph, not an extrapolation.

The verifier independently checks the full face vector, constructs the explicit repeated-toggle Morse matching, validates each incidence and each matched cover, and tests absence of directed cycles by a topological sort of all Hasse nodes. This proves the nonequivariant homology premise rather than assuming the older published result.

For all seven conjugacy classes of \(S_5\), it computes the character in two independent ways: alternating counts of admissible unions of edge-orbits and direct signed Lefschetz traces on every setwise invariant simplex. Both match the standard character. The complete expected output from the included program is `verification/verification_output.txt`.

The inference from character values to a rational representation is standard semisimple character theory. The subgroup-quotient homology follows from invariant rational chains after barycentric subdivision. The checks do not identify an integral lattice, integral quotient torsion or absolute originality. No independent scientific audit has been performed.
