---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Verified the volume law and all unrestricted equality cases on the open interval 1<t<3. Signed coordinate and cube-diagonal linear functionals expose all 14 vertices. Separate affinity reduces the maximum to vertex quadruples. An independent exact replay interpolated the homogeneous 4×4 determinants from t=0,1,2,3 (degree at most three), recovering all 18 classes, all 1001 multiplicities, exactly the two alternating and eight opposite-axis configurations, and maximum pairwise intersection two among these ten. The strict inequalities in RESULT.md:66 exclude every other class throughout the open interval. A positive maximizing determinant expanded over support vertices is an average of signed determinants ≤ that maximum; two support choices at one corner would give distinct maximizing quadruples sharing three vertices, impossible. For the volume dissections, representative side planes are x+(t−1)y=t for t≤2 and x+y+(t−2)z=t for t≥2; all generators satisfy their halfspace inequalities, and signed permutations give the exterior faces of the respective pyramid unions. This gives 8t and 4t², agreeing at t=2. The fraction decreases to τ and increases thereafter, and the independently recomputed decimals agree. Endpoint equality counts are not asserted. Replay for the finite and decimal checks: python review_evidence/finite_checks.py (section labelled 2); the continuum and rigidity steps are analytic.

## originality

PASS

Pass for the full parameter transition and optimizer rigidity of the frozen claim, not for an isolated t=2 calculation. A later record explicitly covers the entire claim and more; this establishes equivalent present catalogue coverage, not earlier publication. The same-day four-generator zonotope result gives exactly the t=2 slice; the order of those two records is not determined. No inspected earlier result gives or implies the varying-hull transition.

## value

PASS

The natural hull interpolation has a discrete switch of optimizing geometry and a uniquely least efficient shape, at a crossover distinct from the facet-regime change at t=2. The exact profiles and no-nonvertex equality result are useful in simplex packing/shape comparisons beyond the special rhombic dodecahedron or a finite enumeration alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
