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

# Verification of the torus-saturation theorem

The bundled `check.py` was executed with a local SymPy installation and returned `CHECK_OK`. It constructs the Sylvester matrix for the quadratic forms in the second projective coordinate, verifies the full symbolic resultant \(A^2(\varepsilon^2-B\varepsilon-A^2)\), and specializes to \(-A^4\). It also checks representative coprime affine pairs with rational degrees one, two, and four, including a case whose missing affine pole lies at projective infinity.

The independent mathematical steps not certified by the script are reconstructed in `RESULT.md`: simple real projective poles of nonconstant rational Herglotz functions; exhaustive base-locus enumeration; local multiplicity two from the implicit-function theorem at each branch; preservation under coordinatewise Cayley transformations and invertible range normalization; and the standard rational-inner representation. Finite examples and symbolic identities are used to check algebra, not to infer the all-degree theorem by enumeration. Extremality of the Nevanlinna measure and the rational-inner conversion are grounded in the cited primary literature. Independent verification is not performed.
