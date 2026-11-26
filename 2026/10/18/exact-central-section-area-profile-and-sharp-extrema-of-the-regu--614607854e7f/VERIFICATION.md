---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The signed pair inequalities give the cube and axial vertices and the 24 cube-to-axis edges. Sorting absolute normal coordinates and taking a>b>c>0 leaves just two possible vertex sign patterns, separated by a=b+c. I independently clipped all twelve facet inequalities after substituting x=-(by+cz)/a. The exact vertex shoelace sums in yz coordinates give 6 vertices and projected area 12a/(a+b+c), or 8 vertices and projected area equal to the second frozen formula with rho replaced by a. The order and active edges cannot change within either open chamber, since no vertex crosses the plane. Multiplying by rho/a gives the intrinsic area. Continuity follows by rotating the planes and using the continuous bounded radial function of K; separate exact clips at (1,1,1), (1,1,0) and (1,0,0) confirm the important boundary values. In the hexagonal chamber Cauchy–Schwarz is tight only at a=b=c. The inequality (a+b+c)^2-2rho^2=4bc-(a-b-c)^2 is strict for c>0 since |a-b-c|<=c and b>=c; c=0 in this chamber forces a=b. In the octagonal chamber s=b+c<1 after rescaling a=1, the area factors P,Q and denominator are positive (Q>=(1-s)(1+2s)>0). The independent replay converts the squared upper-bound polynomial to Bernstein form and checks all 28 coefficients; the positive first row makes the inequality strict for s<1. The logarithmic derivative numerator decreases in t=(b-c)^2, so a minimum at fixed s occurs at an endpoint. Direct differentiation of the squared endpoint profiles gives minima 3sqrt(6) and 5sqrt(10)/2, both strictly above 4sqrt(3). The equality wall belongs to the closed hexagonal formula. Undoing signed permutations yields exactly the stated eight and twelve unit normal directions, with antipodal identification for planes.

## originality

PASS

The supported contribution is the compact, evaluated directional area profile for this polytope together with its sharp minimum and maximum and complete equality orbits. Generic vertex-sign chambers, rationality and exact section-volume algorithms are known; the combinatorial hexagon/octagon classification also overlaps the indexed literature and is not credited separately as original. The closest same-body area source computes a directional mean, not pointwise area or extreme directions. General slicing algorithms can produce unsimplified section formulas and optimize them with further input-specific work; none of the inspected statements evaluates both chambers and proves the two exact sharp bounds and strict equality classes here. This is not a claim of historical priority.

## value

PASS

This is a motivated exact invariant of a classical FCC Voronoi cell: the Euclidean area perpendicular to any direction, not an arbitrary isolated slice. The closed formulas replace per-normal polytope clipping, and the sharp range with full equality directions gives an exact anisotropy benchmark not supplied by the known side-count or mean-area laws. The body has two distinct symmetry orbits realizing the extrema; these equality statements require global control across the piecewise area landscape, not just evaluations on high-symmetry axes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
