---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

Run `python3 verify_dodeca_shadow.py`. This standalone checker requires only the Python standard library and generates its own exact field coordinates, sign chambers, polar vertices and viewing directions.

The checker verifies 32 realizable sign chambers (20 triangles and 12 pentagons), all 20 exact triangular-chamber linear and quadratic identities, the ten/twelve-vertex silhouette classification, 400 independently reconstructed projected convex hulls with normalized brightness comparisons, and 240,000 deterministic sphere quadrature directions. The numerical type-weighted moment comparisons had errors approximately \(9.16\times10^{-5}\) in the twelve-vertex probability, \(2.529\times10^{-4}\) in the weighted first moment, and \(6.984\times10^{-4}\) in the weighted second moment.

The exact classification uses integer sign comparisons in \(\mathbb Z[\varphi]\) and a proof that every sign-chamber vertex arises from a pair of bounding great circles. The spherical divergence identities, not quadrature, prove the continuum statements. The total second moment uses the established absolute-product kernel; the numerical hull and quadrature checks are corroborative rather than certified infinite proofs.

No independent external audit has been performed.
