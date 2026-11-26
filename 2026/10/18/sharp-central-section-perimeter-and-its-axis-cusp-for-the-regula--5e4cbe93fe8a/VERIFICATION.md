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

The facets |x_i|+|x_j|=2 in each fixed sign pair are rhombi with two axis and two cube vertices. Their support function equals half the sum of the four absolute tetrahedral dot products (sort |z_i| and separate |z_1|≥|z_2|+|z_3| from its complement). Thus planar projection is a zonogon, and Cauchy's formula bounds the section perimeter by twice the sum of the projected generator lengths. For Q_j=(u_j·n)^2 the mean is 1, and Σ(Q_j−1)^2=16Σ_{i<j}n_i²n_j². Applying f''≤−1/(12√3) to f(t)=√(3−t) and including the factor 2 gives the stated deficit, with the endpoint by continuity. It forces axes for equality; each axis section is a diamond with four edges of length 2√2. For the chamber formulas, the crossed edges follow from the facet rhombi and opposite signs. For example, cyclically adjacent vertices (2c,2c,−2(a+b))/S and (−2b,2(a+c),−2b)/S differ by 2(−(b+c),a,a)/S; in the octagonal chamber the next vertex is (−2b,2(a−c),2b)/(a+b−c), giving the term with denominator (a+b−c)S. The opposite pair at the corner cut gives the (a−b−c) term, and exchanging b,c gives the last pair. In the hexagonal chamber the next vertex instead is (−2(b+c),2a,2a)/S, giving the remaining terms by cyclic symmetry. Degenerate walls follow by continuity of convex central sections, including the apparent singularity of the octagon formula at (a,a,0). Strict convexity on the clipped normalized simplex gives the six-chamber minimum at the equal triple and maximum only at permutations of (1/2,1/2,0). At a=1 the two terms carrying √2 each contribute −4√2(b+c) to first order; the other terms contribute +8(b+c). The denominators near the axis are bounded, giving the uniform quadratic remainder and opposing-direction slopes that preclude a linear differential. The packaged checker is finite; these arguments cover the full sphere.

## originality

PASS

The checked matches cover section combinatorics and crossing data, neighboring area and angular statistics, or the perimeter problem for a different polytope. Credit the projection/zonotope facts and existing section-combinatorics ingredients; the supported distinct contribution is the intrinsic perimeter analysis, especially the global extremum and explicit deficit and the directional cusp. No claim of historical priority for the section combinatorics or edge construction is needed.

## value

PASS

The intrinsic directional perimeter of the FCC Voronoi polytope is a natural section invariant. In addition to a complete maximum/equality result, the theorem distinguishes quantitative global stability from a nonsmooth, anisotropic local loss, which cannot be read off from the number of sides or section area. The explicit chamber expressions permit evaluation even away from the extremizers. No optimality of the deficit constant is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
