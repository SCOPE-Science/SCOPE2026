---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The augmented determinant bound shows global maximizers exactly the O(d) orbit of regular simplices. Decompose every tangent array into skew-symmetric rotation A and tracefree symmetric S, with w_i=A u_i+(I-u_i u_i^T)S u_i. The mapping from tracefree S to tangent normals is injective by unique all-ones relation among regular vertices and has correct dimension. Hessian of -log volume from geodesic determinant twice differentiation is H(S,T)=2tr(ST)-(2d+1)/(d+1) sum_i q_i(S)q_i(T); metric G(S,T)=(d+1)/d tr(ST)-sum_i q_i q_i. The tracefree symmetric space splits into span{u_i u_i^T-I/d} (rank d, eigenvalue 1) and its Frobenius orthogonal complement (eigenvalue 2d/(d+1)). All other null modes are rotations. Compact tubular-neighborhood Taylor formula yields uniform sharp r^2 constants; normal eigendirections attain both.

## originality

PASS

Horváth and Lángi prove global maximal volume and equality regular simplex, but those results do not imply the precise Riemannian Hessian, its two nonzero eigenlevels and Morse–Bott stability. Medgyes treats 7/8-vertex dimension-4 volume certificates; Grote–Kabluchko–Thäle scalar random-simplex laws do not resolve directional Hessian. Published SCOPE nine-vertex spherical Hessian concerns different object.

## value

PASS

A complete all-dim local rigidity spectrum for the classical regular inscribed simplex specifies two distinct deformation stiffnesses and the sharp quantitative distance-to-orbit deficit. Distinct from the well-known global maximizer, useful for stability and perturbation analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
