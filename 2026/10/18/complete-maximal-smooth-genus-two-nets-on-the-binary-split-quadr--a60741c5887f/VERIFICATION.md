---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Four standard affine charts cover P1xP1. For each of 4095 nonzero bidegree-(2,3) sections over F2, geometric smoothness is equivalent to all Jacobian ideals (f,fx,fy) being unit ideals; the symbolic source verify_geometry.py uses exact Groebner bases, not rational-only sampling. An independently coded characteristic-two bivariate polynomial/gcd smoothness test reproduced exactly 1116 smooth masks, including all seven of the exhibited net. Independent XOR subspace census yielded 44070 pencils and 250992 pencil/extension incidences; each 3-space has seven pencils and four extension vectors, so 250992/28=8964 distinct nets. Recomputed every net’s 9-point F2-rational spectrum: exactly the stated 14 types with counts summing 8964; independent transformation of all 36 polarized PGL2(F2)^2 automorphisms gave 249 orbits, each size36. A 4-dimensional section subspace has a nonzero kernel of the three-dimensional first-jet evaluation at any rational point, so contains a singular member; the 3-dimensional example proves sharpness. Adjunction gives genus two on smooth (2,3). Exhaustive finite coefficient enumeration is genuine exhaustive proof for this fixed finite vector space, not extrapolation to other fields.

## originality

PASS

Best-of-knowledge assessment from exact implication comparisons of same mathematical objects; known special cases and general mechanisms are credited; actual full primary texts read when accessible and residual priority risk recorded. The retained exact result is not proved covered by the identified sources.

## value

PASS

All-smooth linear systems on varieties over finite fields form a motivated extremal problem. A complete census for the first genus-two bi-graded linear system on the smallest split quadric, including every maximal net, projective automorphism orbit and all member point-count spectra, refines generic existence and jet bounds with exact arithmetic geometry. The fixed finite object and orbit invariant are canonical, not a fabricated numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
