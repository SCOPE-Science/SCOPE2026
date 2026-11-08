---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The twelve rhombic facets from the inequalities give exactly fourteen vertices (six axial, eight cube) and twenty-four cube-to-axial edges. A generic plane intersects precisely the edges with opposite endpoint signs. After sign/permutation symmetry of weighted normal m_i=s_i u_i, the three positive weights produce either 8 crossings if m_max>sum others or 6 otherwise; no other generic side count. Each dominant-coordinate event is a triangular spherical cone with rays e_i, (s_j/s_i)e_i+e_j, (s_k/s_i)e_i+e_k. Evaluated the standard determinant/dot-product solid-angle formula: each cone angle is 2 arctan e^(-q_i), and eight octants give 4/pi sum_i arctan e^(-q_i). Taylor expansion Q(x)=asinh(e^x), F(y)=arctan(e^-y) gives positive transverse Hessian and the claimed coefficient. Independently enumerated 24 edges, checked 20,000 Gaussian normals over four stretches against the exact 6/8 criterion and frequency formula; compared the one-axis t=100 asymptotic coefficient. These corroborate the analytic proof.

## originality

PASS

No checked prior statement entails the full assigned claim. Knowing a moment algorithm or solid-angle identity does not imply the particular identified cones, evaluated P8, Hessian or t^-1 coefficient without substantive application. General chamber machinery could be adapted but the inspected statements do not give the evaluated rhombic-dodecahedron Haar side-count distribution nor the anisotropy Hessian; other polytopes cannot be substituted by a formal duality without changing sections to projections.

## value

PASS

The law evaluates a natural discrete section-type distribution of a regular polyhedron and all positive diagonal affine stretches, with a sharp local stability coefficient and asymptotic degeneration. Such exact Haar type measures are meaningful in stochastic convex geometry and not inferred by merely listing polyhedron vertices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
