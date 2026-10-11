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

The standalone script `artifacts/verify.py` contains the complete facet set and uses exact integer arithmetic only. It reconstructs the face vector, contracts a spanning tree of the complete one-skeleton, builds the integral facial-relation matrix, verifies a primitive null functional, and checks a \(35\)-dimensional unimodular relation minor with determinant \(-1\). These checks prove that the quotient first homology is torsion-free of rank \(1\).

It then enumerates all \(120\) graph triangles, distinguishes the \(70\) facial and \(50\) empty triangles, evaluates every empty triangle in the integral quotient, constructs all five cyclic orbits, and tests every possible cone apex. The output file records the expected \(40\) primitive nonzero cycles, \(10\) null cycles, five size-\(10\) orbits, and the cone-fillability equivalence.

The verification proves only the finite combinatorial statement for the supplied triangulation. It does not certify geometric lengths or any all-manifold generalization.
