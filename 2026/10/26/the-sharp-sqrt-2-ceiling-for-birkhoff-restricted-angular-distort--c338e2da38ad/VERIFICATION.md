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

Writing x=||x||u and y=||y||v gives the stated profile with t=||x||/||y||, and positive scaling preserves Birkhoff orthogonality. For D=tu−t⁻¹v and d=||D||, the orthogonality and reverse triangle inequalities give d≥t and d≥|t−t⁻¹|. For t≤1 the identity u−v=tD+(1−t²)u gives bounds 2t below t=1/√2 and 1/t above it. For t≥1 the identity u−v=t⁻¹D−(1−t⁻²)v gives 2/t−1/t³, maximized at √(3/2) with value 4√6/9<√2. Thus equality forces t=1/√2 and equality in the d lower bound there, i.e. ||u−2v||=1. Conversely the chord is on the sphere by convexity and orthogonality, so ||u−v||=1 and the quotient is √2. The square and diamond witnesses are unit Birkhoff pairs by the indicated norm-one functionals. The lower bound follows from t=1 and a norming functional's nontrivial kernel; Hilbert spaces give exactly 1 since d²=t²+t⁻² for an orthonormal pair. In finite dimension the unit Birkhoff-pair set is closed and compact and the bounds 2/t and 2/|t−t⁻¹| give uniform decay at the two ends. So attainment holds, and strict convexity excludes the required chord.

## originality

PASS

The restricted invariant and the normalized profile are already explicit in Du et al.; the lower sharp endpoint is not new. Their Proposition 2.5 and Example 4.4 explicitly claim sharpness at 2 for the very same restricted invariant. The proved upper bound √2 contradicts that sharpness and the frozen result gives an exact extremizer criterion. A distinct later-published indexed result proves the same √2 bound using the same inequalities in s=t² and includes more ℓ∞ examples; it does not state the pointwise iff, though the iff is obtainable by tracing its sharp endpoint. This is substantive duplication of the theorem, not a different invariant; the catalog entries and the preprint's ambiguous date metadata do not establish an earlier priority for the distinct result. The available earlier statements do not give the claimed sharp comparison. The Pass is for the supported improvement and equality analysis, not certified absolute priority.

## value

PASS

This settles a natural sharpness question raised for exactly the same restricted Banach-space invariant. The improvement from an asserted sharp 2 to attained √2 changes the conclusion materially. The exact unit-sphere chord criterion also answers when a pair realizes the universal bound and explains the finite-dimensional strictly convex obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
