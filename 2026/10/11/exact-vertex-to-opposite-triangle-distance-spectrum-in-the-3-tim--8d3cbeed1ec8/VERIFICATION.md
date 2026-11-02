---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For four distinct sites of L={0,1,2}^3, a nonzero oriented volume determinant is exactly the full-dimensional tetrahedron condition. Each unordered four-site set generates four and only four marked point/opposite-triangle pairs. For triangle a,b,c, the squared Euclidean distance is the minimum of the convex quadratic ||p-a-u(b-a)-v(c-a)||^2 over u,v>=0,u+v<=1. Its unique unconstrained stationary point is found from the nonsingular 2x2 Gram matrix; when feasible it is the minimum, otherwise compactness and strict convexity force the minimum on one of the three closed edges, solved by clamped rational segment projections. This covers all faces/boundaries with exact rational arithmetic. The independent implementation loops over all C(27,4) unordered sets and each of four markings, checks nonzero determinants, uses its own Gram/active-face formulas and 48 cube isometries, and reproduces 14,632 tetrahedra, 58,528 marked pairs, 19,744 feasible perpendicular feet, the full 88-value CSV and all three specified orbit partitions. The source CSV is byte-exact to its Git blob SHA-1 91d88e..., and the assigned source tree object SHA is independently reconstructed. The enumeration is a proof for the finite domain only; no extrapolation to other k is made.

## originality

PASS

Best-of-knowledge originality survives for the complete 88-level distribution, the sharp second level 1/21 above the published minimum 1/29, and two equality orbits. Deza-Pournin 2026 Theorem 1.1 and Proposition 4.1 prove the global minimum and unique orbit but not next gap or multiplicities; earlier 2024/2025 Deza-Liu-Pournin papers give stronger general minimum frameworks for different statistics, not a complete closed-face census. Resultary searches produced the assigned record itself, excluded from independent priority evidence, and no supported earlier exact duplicate. Negative searches remain limited and do not establish priority by themselves.

## value

PASS

The 27-point ternary lattice cube is the first nonbinary fixed cube in the natural series of lattice (3,k)-simplices. Point-to-closed-opposite-face separation is a motivating flatness/facial-distance quantity in the primary research. The complete exact 88-value probability/multiplicity profile and its sharp isolated next rank are not automatically obtained from the known global minimum; 1/21 supports a genuine quantitative nonminimizer gap with two geometrically inequivalent achieving symmetry orbits. The finite classification is a reproducible exact benchmark for testing vertex-facet distances, extremal stability assertions and constrained versus affine-hull distances. This is narrow, but represents a natural complete discrete classification rather than an ad hoc slice or a known table being recopied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
