---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Equality in the facet-area Cauchy–Schwarz bound S<=8/sqrt(3)*sqrt(det A)*sqrt(tr(A^-1)) requires equal edge scales and constant diagonal of U^T C U. A vertex y is the normalized sum of orthonormal columns u_j, so projected columns in y-perp form an equilateral triple at angles phi+2pi(j-1)/3. The constant-diagonal residual is a sum of first and second harmonics. On this triple, second harmonics alias first with phase 3phi; vanishing of all three residuals iff d1^2+d2^2=2(b1^2+b2^2), including the degenerate zero/zero case. This is equivalent to tr_{y-perp}(D^2)=4||P C y||^2 and expands exactly to F_C(y)=0. An independent exact SymPy check verified axial factor (a-b)^2(t-1)(9t-1), and the formula handles coincident eigenvalues and ball. All vectors real, y unit, C positive definite.

## originality

PASS

The closely matching 2026 Kania paper solves unrestricted maximal facet area and reduces prescribed-point feasibility to barycentric constant-diagonal orthogonal bases; it treats prescribed eigenvector directions in dimension three and poses the general pair classification as Problem 6.1. The explicit all-direction quartic and non-principal latitude solutions solve that natural outstanding 3D case. General simultaneous almost-hollow results do not force the two exact hollow constraints. No stronger reviewed source covers the quartic criterion.

## value

PASS

A motivated exact existence criterion and constructive phase reconstruction for a prescribed boundary vertex of an ellipsoid’s unrestricted maximal-area parallelepiped; extends the established eigenvector-only result and settles the general 3D boundary-point question. The axial latitude phenomenon is a substantive geometric distinction, not renaming an old bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
