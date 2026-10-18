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

# Verification of the exact claim

The proof is complete and self-contained for all real \(t>0\): the two symmetric volume slicing integrals \(\int_0^1 (1-s)^4\,ds=1/5\) and \(\int_0^1 (1-s)^2\,ds=1/3\) give the volume expectation, and the two four-facet classes give the surface expectation. The barycentric triangle formula follows from the Dirichlet \((1,1,1)\) simplex moments, or by direct integration. Subtraction produces the exact sign factor. No finite enumeration is used to infer its universal sign.

A numerical independent check directly integrated all triangle vertex-coordinate second moments, weighted them by their Euclidean areas, and compared them to the slice formula. At \(t=12\) the surface-minus-volume difference is about \(0.24482898996\); at \(t=13\) it is about \(-0.12101978856\); at \(t=\sqrt{161}\) the exact radical factor vanishes. These checks support, but are not substitutes for, the algebraic proof.

The minimum-vertex assertion follows directly from antipodal pairs spanning \(\mathbb R^3\), requiring at least three pairs. Only self-review was performed; independent audit and external validation were not performed. The extent of primary literature inspection and remaining priority risks are in the review files.
