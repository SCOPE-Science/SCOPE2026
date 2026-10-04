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

The exact verifier is `verify_resection_collinear_node.py` and requires Python 3 with SymPy.

It reconstructs the six world points and checks that every four-point determinant is nonzero. It builds the square six-focal matrix directly from the published focal construction, computes its determinant, and checks multilinearity. On the symbolic collinearity parametrization \(p_i=[1:y_i:a+b y_i]\), it verifies two independent left-kernel vectors coming from the two-dimensional relation space among the six world points.

At the exact point \(p_i=[1:i:0]\), it checks focal-matrix rank \(16\), zero gradient, Hessian rank \(4\), an \(8\)-dimensional collinearity tangent space contained in the Hessian kernel, equality of those two spaces by dimension, and a nonzero normal Hessian minor of determinant \(484\).

Expected terminal output begins with `VERIFY_OK`.

The verifier does not compute the complete global singular locus and does not claim that collinearity is its only component.
