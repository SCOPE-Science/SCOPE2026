---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

At corank 1 the symmetric adjugate is λvvᵀ and gradient w.r.t a_t equals λ[z^t](Σv_i z^i)². Singular on a_k=0 iff that square is a single monomial, so k even=2j, v=e_j, equivalent to jth row zero. Corank≥2 points singular automatically. On extra L_j the complementary minor B has explicit nonzero ±a_{j−1}^j a_{j+n}^{n−1−j} and hence generic corank1. Schur complement yields nondegenerate quadratic normal slice −det(B)rᵀB⁻¹r. Rank≤n−2 secant locus has dimension 2n−5, intersected with coordinate hyperplane at most 2n−6; extra L_j dimension n−2 gives codimension n−2 in Y of dim2n−4, so for n≥4 singular codimension≥2. Hypersurface S2 plus regular in codimension 1 gives integral normality. At n=3 even k=2 equation −a0a3²−a1²a4 irreducible nonnormal; for odd k=1,3 cubics have A1+A5 isolated points. Independently verified 10 exact complementary minor identities for n3..6 and cubic A5 coordinate change. No scheme-theoretic radical primary decomposition claimed.

## originality

PASS

Single interior coefficient deletion is distinct from published terminal consecutive-zero degeneration. The exact parity jump in reduced singular support, extra linear stratum, transverse quadratic form and normality boundary were not identified in the inspected primary source. The adjugate and Schur methods themselves are standard and not claimed as new.

## value

PASS

Canonical interior sections of classical Hankel determinant hypersurfaces exhibit structural even/odd singularity jump, a higher-dimensional linear component with uniform transverse type and a sharp normality exception at n=3; useful as explicit singularity geometry complement to known terminal cuts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
