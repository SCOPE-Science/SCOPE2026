---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For phi=(1+sqrt(5))/2, the six explicitly given vertices form the convex midpoint-corner truncation H of the affine-regular pentagon. The five-vertex P using apex (0,1/2) lies in H (the apex is the midpoint of H’s top edge). An explicit four-halfplane trapezoid contains H and its exact shoelace area is q=2+3sqrt(5)/4. For the lower bound, the published DePano/Park/Hong optimal-configuration lemma specialized to a strictly convex pentagon admits a minimizing quadrilateral with at least three sides flush with the five P edges and a fourth either flush or balanced at a vertex. For three chosen flush sides and a balanced vertex v, the fourth normal must lie on ±[(h_j−n_j·v)n_i+(h_i−n_i·v)n_j], as follows from opposing half-segment endpoints and midpoint v. This yields exactly 10*(2+3*5*2)=320 candidates. I independently reconstructed the five edge normals from P’s vertex coordinates in Q(sqrt(5)), recomputed all candidate normals and exact four-line intersections/halfplane feasibility and shoelace areas, and obtained 35 feasible (20 flush-four-edge, 15 balanced-vertex), with every area >= q and one exact equality witness (flush sides 1,2,3, fourth top side through v=(0,1/2)). The independent checker also confirmed |H|=9/4+sqrt(5)/2 and q/|H|=(42+11sqrt(5))/61. Thus q(P)>=q and P⊂H⊂Q force q(H)=q. The finite enumeration proves global optimality only because the referenced structural theorem exhausts all candidate optima; it is not a generic sampling argument.

## originality

PASS

Best-of-knowledge comparison of the exact affine-equivalence class and enclosing-area invariant found no independent published formula or stronger theorem determining q(H). Hong–Ismailescu–Kwak–Park and the earlier DePano algorithm give the necessary three-flush-side/midpoint reduction and the global pentagon extremal factor 3/sqrt(5), not the specialized evaluated optimum for the six-vertex midpoint truncation. Fodor–Grundbacher gives a general convex-body upper bound, not a matching lower bound. Vígh 2026 studies Kuperberg-type quadrilateral ratios, generic near-regular-pentagon perturbations and a different irregular hexagon, without an evaluated midpoint-cut example. The finite Q(sqrt(5)) optimization is the additional fact. Exact-radical, shape-alias and stronger-form searches did not find independent coverage; this is not absolute priority proof.

## value

PASS

The sharp affine-invariant quadrilateral area-enclosure ratio is a natural classical convex-geometric invariant; the regular pentagon is a sharp/extremal comparison body in the Kuperberg quadrilateral enclosure problem. Removing a corner at its two incident edge midpoints is a geometrically canonical first six-vertex deformation. Knowing its EXACT minimum, not merely a universal upper bound or an exhibited trapezoid, supplies a credible quantitative stability/benchmark example for exact enclosure algorithms and for understanding how the extremal pentagon behaves under a controlled corner cut. The genuinely new mathematical component is a complete shape-specific lower certificate using the structural lemma and exact algebraic enumeration, not a renaming of q or substitution into a precomputed table. The narrow result does not claim any general stability modulus, but researchers comparing near-extremal polygon families could reasonably need this independently evaluable exact value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
