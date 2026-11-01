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

For a uniform surface-area point X on the unit cube and vertex o, three adjacent faces have squared geodesic radius u²+v²; an opposite face point (1,y,z) has exact radius² 1+y²+z²+2min(y,z). Two unfolded 2-face paths attain the latter. The source provides a finite exhaustive comparison of 80 simple face walks, reduced to 24 integer coefficient classes each satisfying the necessary affine inequalities at all four chamber vertices; the argument that a shortest path can be shortened if it visits a face twice justifies path reduction. Analytic integration over the incident quarter-disk and two opposite triangles yields the displayed A(r),B(r) and F=(A+B)/2, transitions at 1 and sqrt2 and endpoint sqrt5. Direct rational polynomial integration gives E[R²]=3/2,E[R⁴]=61/18; endpoint rescaling gives 1-F~(5-r²)²/48. Independent numerical integration by Monte Carlo using 45,000 independently generated pairs compared the analytic CDF at 5 radii (errors bounded by 0.006); this corroboration is not proof of metric optimality. Critical exact face-walk code was read and its inequalities traced. No two-random-point formula is asserted. An additional independent, exact integer planar unfolding generator reconstructed all 80 face-simple routes and precisely 24 quadratic coefficient classes and verified all four chamber-vertex inequalities for every class. The corresponding path-completeness proof then establishes the pointwise intrinsic metric, not Monte Carlo.

## originality

PASS

Fuchs 2016 treats geodesic vertex-to-vertex endpoints, Goldstone-Roca-Suzzi Valli 2020 treat shortest paths between opposite face interior points, Davis 2023 treats cube cut loci and geodesic complexity, and Mathai et al 1999 Euclidean straight-line distances. None inspected states the uniform-surface-point intrinsic vertex-centered CDF, moments and sharp tail. The general shortest-path algorithm is compatible but no immediate exact density formula follows without new integration.

## value

PASS

The complete intrinsic-distance CDF from a cube vertex to a uniformly random surface point is a natural metric-geometric probability law. Its support, phase radii, exact moments and sharp far-tail encode nontrivial effects of surface shortest paths beyond Euclidean distance and enable later benchmarks without redoing the cube unfolding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
