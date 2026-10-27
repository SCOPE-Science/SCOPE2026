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
# Verification

- The six deleted-vertex constraints count each of the fifteen edge weights exactly four times, yielding \(S\le15a+6\).
- At sum \(15a+6\), integer smoothing reduces the second-product upper bound to the three predecessor multisets listed in RESULT.md; exact ratios show that \(a^{10}(a+1)^4(a+2)\) is the largest nonmaximum candidate.
- At any smaller sum, the integer arithmetic-geometric mean bound is at most \(a^{10}(a+1)^5\), strictly below the candidate.
- The construction with one edge of weight \(a+2\) and a disjoint \(4\)-cycle of edges of weight \(a+1\) has excess degree two at every vertex, so all six five-set constraints are tight.
- Equality forces the same weight multiset and excess-degree pattern, proving uniqueness up to relabeling.

These checks verify the mathematical claim stated in RESULT.md. Independent audit and independent validation have not been performed.
