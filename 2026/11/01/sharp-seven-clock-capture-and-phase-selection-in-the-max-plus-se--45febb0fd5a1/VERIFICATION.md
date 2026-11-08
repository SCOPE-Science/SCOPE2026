---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Original-time dynamics is F_B(X,Y)=(Y+max(0,2X),B-max(0,2X)), with scale B removed by normalization. On the canonical arclength segment r in (0,1], direct piecewise iteration (also published primary itinerary) splits R=(0,1/16], U=(1/16,1/8), G=[1/8,1]. G has length 14/16 and hits c0 at time 6; R has length 1/16 and hits c0 at time 7; U returns after exactly seven original updates via r->16r-1, bijectively onto the entire interval. Thus survivor cylinders have exact measure 16^-k, and disjoint exits have probabilities 14/16^(k+1), 1/16^(k+1) at times 7k+6,7k+7. Both exits land c0, giving the two phase atoms with limiting weights 14/15,1/15. At n=7q+m, uncaptured non-atomic mass is exactly 16^-q for m<=5 or 2*16^(-q-1) for m=6; captured masses are componentwise bounded by phase limits, so total-variation equals that residual. The null exceptional endpoints do not affect probabilities. Independently checked exact rational iterations, 7-cycle and renewal lengths. No inference from finite k to the infinite law is needed, since the inverse branch is an exact affine bijection.

## originality

PASS

Best-of-knowledge comparison of exact conclusions and logical implications, not titles or equal parameter words. Return-map coordinates encode the dynamics, but the exact probability generating function and phase-resolved pushforward law are additional probabilistic statements. No equal ensemble distribution appears in the inspected full primary results. Earlier dynamic basin classifications do not determine the probability law until one also selects a particular initial distribution and computes inverse-branch measures, then follows exact physical-time phase labels. Full text materially read for the closest primary original. Residual source-access risks and credited antecedents are explicit.

## value

PASS

A deterministic attracting cycle does not by itself determine the law of how a naturally uniform transversal ensemble arrives, its physical-time residue classes, or its nonstationary limiting phase composition. The exact proper first-hit distribution, mean 98/15 and sharp total variation for every time form a complete and motivated statistical observable for the original discrete map. The derivation is short once published branch clocks are known but not a purely decorative parameter substitution or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
