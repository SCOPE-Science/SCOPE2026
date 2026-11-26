---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The tetrahedral segment sum has exactly the required hull: in the positive orthant the pair-sum inequalities give the axis vertices and (1,1,1), besides points already in their signed hull. Width gives section perimeter at most projection perimeter; the projected segment lengths have sum of squares 8, so twice their sum is at most 8√2. Equality requires all four squared scalar products to equal 1; their expansion in the four tetrahedral signs gives ab=ac=bc=0. Axis sections are diamonds attaining the bound. In the local chart with nonnegative u,v, the corner at (y,z)=(2,0) loses adjacent edge lengths asymptotic to 2√2u each and gains a chord of length 4u, with errors O(u(u+v)); the z corners exchange u and v. The cuts on adjacent opposite-sign edges are disjoint since the sum of their edge parameters divided by 2 is [a(u+v)−(u−v)^2]/[a^2−(u−v)^2]<1, and same-sign edges are immediate. The lift changes edge metrics by O(u²+v²). Reflection gives the uniform absolute-value cusp. Continuity follows locally by writing the section radial function in a continuous orthonormal plane frame as 2 divided by the maximum of the three pairwise absolute coordinate sums on each unit ray, and applying perimeter continuity for planar convex bodies. Compactness then localizes the tail to six charts. Each contains asymptotically a diamond of area 2(ε/C)^2 with C=8(√2−1), and the sphere chart Jacobian tends to 1. Division by 4π gives 3(3+2√2)/(64π), without a further antipodal factor.

## originality

PASS

The inspected material covers the tetrahedral zonotope representation, cube perimeter optimization and an analogous cube cusp/tail, and Haar side-count laws for the same rhombic dodecahedron. It does not establish the stated solid-section perimeter endpoint, equality set and local law together, or the rhombic-dodecahedron cusp and its tail constant. This is a best-of-knowledge assessment of the specified claim, not of priority for projection-width methods.

## value

PASS

This gives an exact metric statistic of a canonical polyhedron under the natural isotropic law, not just a finite list of large examples. The linear and anisotropic deficit explains why rare near-maximal orientations in this two-dimensional orientation space have a quadratic probability with a calculable prefactor, rather than the leading behavior of a smooth quadratic maximum. Side counts and projection perimeter cannot replace this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
