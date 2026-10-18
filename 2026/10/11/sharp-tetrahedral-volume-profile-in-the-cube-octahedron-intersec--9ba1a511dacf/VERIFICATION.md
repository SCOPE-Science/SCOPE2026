---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The polytope has exactly 24 signed-permutation vertices of (1,t,0) for 1<c<2 and (1,1,u) for 2<c<3; degeneracies at c=1,2,3 are limits of valid vertices. The signed four-point tetrahedron determinant is separately affine in its vertices, so its absolute maximum occurs on vertex quadruples. Independently reconstructed all 10,626 quadruples per branch as exact affine-coordinate polynomials (109 distinct in the lower branch, 97 in the upper) and verified all degree-three rational Bernstein coefficients of each E±p on [0,1/2],[1/2,1],[0,1] nonnegative, with actual matching determinant polynomials. This proves a CONTINUOUS all-parameter bound, not finite parameter sampling. Direct cap subtraction gives Vol(K_c)=4/3(1+3t+3t²−2t³) for c≤2, and 4/3[6−(1−u)^3] for c≥2. Independently verified factorizations 6(1+t+2t²)−4F=2(t+1)(2t−1)^2, 6t−F=(2t−1)(t²−t+1), and derivative sign for last ratio as −(u^4−16u+3)/(u³−3u²+3u+5)^2. Together prove unique global 1/6 minimum at c=3/2, second higher local minimum at unique u∈(0,1) solving u^4−16u+3=0, and witnesses in source. Checker source inspected but independent certificate computation implemented in independent_checks.py, not trust in saved VERIFY_OK.

## originality

PASS

The result gives an exact parameter-uniform three-phase maximal tetrahedron determinant and normalized-volume minimizer for the entire clipped-cube K_c. Akopyan–Glazyrin gives a general center-containment condition, not these determinant extremal profiles; Horváth–Lángi treat maximal polytopes inscribed in spheres, not tetrahedra inside K_c. Resultary same-object hits about Mahler products and illumination treat different invariants; the exact same-result index is this very record and is not independent earlier coverage. No stronger prior theorem deriving the three sharp pieces was identified in the actual bounded searches and primary comparisons; this is best-of-knowledge rather than a universal negative search proof.

## value

PASS

Maximal simplices of a polytope are a standard, nontrivial affine extremal invariant. The K_c family connects two classical symmetric polytopes with combinatorial changes, and the exact three regimes, exceptional global minimizing truncated octahedron at c=3/2, and secondary local minimum resolve a natural full-parameter volume-fraction question. This is not merely an arbitrary single instance or recomputation from a known value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
