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

The exact finite checks concern the graph on seventeen vertices with nonzero-square edge differences. `verify_faces.py` is standard-library-only and reconstructs all 17 vertices, 68 edges, 68 triangles and no tetrahedra, proves the 52-dimensional image of the triangle boundary through a determinant-minus-one certificate, and verifies signed fixed-face traces for all 136 affine elements. Its signed count yields the reduced homology character distribution (one value 16, sixteen values minus one, 119 values zero).

`verify_integral_module.py` requires `sympy`. It independently forms the 68-by-68 simplicial boundary matrix, computes its full exact rational kernel, verifies an integral full kernel basis via the free-coordinates identity, calculates the integral action matrices of translation and quadratic-residue multiplication, and checks the translation order, group conjugation identity, norm zero, and a unimodular orbit determinant of minus one.

The finite matrix identities prove the claims for this finite complex. Rational character comparison uses the standard finite-group semisimplicity theorem. No independent audit has been performed, and computational checks are not claims about an infinite family.
