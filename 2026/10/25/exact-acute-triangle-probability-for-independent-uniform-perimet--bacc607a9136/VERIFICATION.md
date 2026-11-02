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

The full probability space comprises 3^3 side-label patterns, with single-side degeneracy 1/9, two-side mass 2/3 and three-side mass 2/9. In the two-side case, ordered endpoints x<y on AB and t on AC are acute exactly when x<t/2<y and (t/2-x)(y-t/2)<3t²/4; integrate the product-of-gaps region on t∈(0,1/2) and (1/2,1). This yields f(t)=(3/2)t²[1+log((2-t)/(3t))] and t(1-t/2), giving 4log(4/3)-5/6. A distinct three-side obtuse-angle integration yields (27/2)log(4/3)-7/2. Strict right-angle and vertex cases have measure zero. All mixtures and normalizations were checked independently via numerical quadrature, symbolic identities and 1.2 million direct randomly placed sample triples; no simulation is used as proof.

## originality

PASS

PASS for exact unconditional perimeter probability and two-occupied-side conditional value only. Exclude known one-per-side law (OEIS A394836), old original Seitz 1878, and the 2024 triple-integral question. Full priority remains qualified because an elementary integration might exist in unindexed recreational or geometric-probability literature.

## value

PASS

A classical natural geometric probability question with a published unsolved full-perimeter integral receives an explicit closed form and exact decomposition; the previously tabulated one-point-on-each-side result is not treated as new. The exact two-side value is a reusable analytic benchmark for random inscribed-triangle models; despite elementary calculus, it fills a precise motivated finite-shape probability gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
