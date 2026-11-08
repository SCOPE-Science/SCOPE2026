---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For four independent Haar points, the minimizing displacements U,V are independent uniform vectors in the centered lattice Voronoi cell and the relative start point is Haar. Two different crossing parameters would give two distinct representatives of the same torus point inside the Voronoi fundamental cell because (s-s')U and (t-t')V lie in its interior for differences in (-1,1), contradicting uniqueness. Therefore the random arcs have at most one transverse crossing and p=E|det(U,V)|/area(V). In reduced coordinates (B=a²+b²>=1,q=2a in [0,1]), the cell is a centrally symmetric six-gon H defined by |u|<=1,|v|<=B,|v-u|<=B+1-q. Partition the positive half into four radial triangles with d=(B,B(2-q),q(B+1-q),B-q); triangle self- and cross-determinant integrals yield 54I=5(4B-q²)^3-3q²(2B-q)^2(2-q)^2. I separately expanded/factored this polynomial exactly via symbolic algebra, not by stochastic sampling. Consequently p=5/54-q²(2B-q)²(2-q)²/[18(4B-q²)^3]; logarithmic derivative in B and monotonic deficit at B=1 prove sharp 22/243 (unique hexagonal lattice) and 5/54 (all rectangular), including degenerate reduced-boundary coordinates.

## originality

PASS

Direct statement-level comparison with relevant original primary research and semantic published-finding records did not identify an equivalent or dominating fully checked result. Known premises are attributed; nontrivial new specific quantitative conclusions assessed at qualified best-of-knowledge level. Inaccessible and incompletely inspected papers remain explicit residual priority risks.

## value

PASS

Crossings of two independent minimizing geodesics define a canonical invariant of every flat two-torus. The closed rational moduli-space profile, universal sharp range, and geometrically distinct equality classes give a natural complete extremal classification. The exact Voronoi determinant identity can serve as a reusable structural tool but no further extension is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
