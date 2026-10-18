---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The cited convex halving-pair lemma gives delta=perimeter/(2 h_min). Opposite boundary halves of normalized trapezoid are exhausted by base-base, base-leg, and leg-leg regimes; direct chord quadratics give h=min{sqrt(S²-x²),1+x²/S,sqrt[(S-x)(S+1)²/(2S)] where 1<=S<=1+2x}. The ratio functions A,B decrease in imbalance x, C increases; their triple balance has quintic P(S) with P(1)=-8, P(2)=109 and Descartes unique positive root. Exact symbolic derivatives of the two crossing branches have opposite sign. Independent symbolic factor and 2,000 random trapezoid global lower-bound checks reproduced the constant. The proof (not finite grid) establishes uniqueness and quantifies all x in [0,1), S>x.

## originality

PASS

Original primary halving-chord paper (full 12-page author-hosted conference text inspected, theorem/lemma pages as original) proves convex-curve reduction and centrally symmetric n-gon sharp bound, and a weaker all-polygon bound; it has no trapezoid theorem. The present optimized genuine unequal-base family is not covered by a centrally symmetric bound (indeed delta*<2). Related published kite optimum belongs to a different quadrilateral subclass. Unindexed standalone elementary trapezoid calculation remains risk.

## value

PASS

Isosceles trapezoids form the most elementary reflection-symmetric but noncentrally-symmetric enlargement of parallelograms. A complete sharp dilation minimum, unique extremizer and exact algebraic equality criterion fill a natural geometric extremal gap rather than a contrived slice or table, and strictly improve the centrally symmetric quadrilateral value 2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
