---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The known uniform-triangle halfspace depth is D=4min(αβ,βγ,γα) for nonnegative barycentric coordinates with sum one. In chamber α≥β≥γ, the minimum is βγ and central set reduces to β≥max(γ,q/γ) and β≤(1−γ)/2, q=τ/4. The two ranges γ∈[r,√q] and [√q,1/3], r=(1−√(1−8q))/2, yield I=∫((1−γ)/2−q/γ)+∫((1−3γ)/2). Six chambers and simplex coordinate area 1/2 give normalized F=12I; independently symbolically integrated and evaluated at five interior levels, recovering F=(3/2)√(1−2τ)−1/2+(3τ/2)log[2(1−√(1−2τ))/(1+√(1−2τ))]. Endpoint max depth 4/9 follows pair-product maximum only at α=β=γ=1/3; F(0)=1, F(4/9)=0. Independent symbolic series for wet part is (3τ/2)log(1/τ)+(3τ/2)−(3τ²/4)+O(τ³). Known pointwise depth is a premise, not new. The Monte Carlo method in verify.py is corroborative and not infinite proof.

## originality

PASS

Full 1999 primary depth paper derives pointwise depth and plots triangle central regions but does not report their *normalized area function* in the materially inspected §5.3; later survey establishes floating-body equivalence and gives contour illustrations, not exact region-volume profile. Schütt–Werner polygonal theory supplies leading-order asymptotics, not all τ. The new closed log profile and lower terms require explicit area integration; no cover from searched accessible work.

## value

PASS

The full affine-invariant floating-body area profile for *every* triangle is a canonical exact non-smooth convex-geometric invariant, finer than the classic logarithmic wet-part order and prior pointwise-depth contour plots. Sharp extinction threshold and explicit lower-order wet-part coefficients provide complete benchmark data for depth trimming and polygonal asymptotics. Exact motivated result need not generalize to all polygons to carry independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
