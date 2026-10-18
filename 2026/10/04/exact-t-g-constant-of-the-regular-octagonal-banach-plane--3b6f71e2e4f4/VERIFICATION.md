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

For N(s,t)=max(|s|,|t|,(|s|+|t|)/sqrt2), the admissible unit-distance sphere pairs are covered by three active supporting-facet equations. Their rank is three (a dependent parallel-normal triple would force a signed support-value difference 0 or ±2, not ±1), reducing each feasible cell to an affine bounded interval. On each output-facet dominance region, N(x+y)*N(2x−y) is one quadratic over Q(sqrt2), whose maximum is at an endpoint or a concave interior critical point. Inspected exact `verify_octagon_tg.py` enumerates all facets and dominance intervals and bounds all candidate products by 9−4sqrt2; the explicit admissible x=(1,sqrt2−1), y=(3−2sqrt2,1) gives both factors 2sqrt2−1. Therefore exact T_G=2sqrt2−1; source records 112 feasible cells. No finite-grid inference.

## originality

PASS

The original 2022 Ahmad–Xie–Li work supplies the invariant, universal bounds, Hilbert and square calibrations, not the octagon exact value. Importantly a LATER October 11, 2026 Resultary full-text theorem proves both shifted norms are separately at most 2sqrt2−1, mathematically dominating and implying the October 4 result. The October 11 article explicitly cites the October 4 target as prior art, so this later theorem does not preempt the earlier dated October 4 originality; both current implication and chronology are documented.

## value

PASS

The regular Euclidean octagon is a canonical symmetric intermediate Banach plane. Its sharp two-median product invariant and an explicit maximizer require nontrivial exact facet optimization and give an independent benchmark. A later stronger pointwise theorem confirms mathematical relevance, while not retroactively eliminating historical novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
