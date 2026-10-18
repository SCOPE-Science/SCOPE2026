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

# Reproducibility and proof boundaries

Run `python3 checker.py` using Python 3 (standard library only). It exhaustively tests covering-array sizes for two columns at strength two and for four columns at strengths two and three, giving \(4,5,8\). The checker then evaluates the dependence predicate and selected flat-graph disjunction on all teams up to the stated size limits, totaling \(11+37+93=141\) teams. An explicit six-row, eight-column pairwise array meets all \(112\) required column-pair output patterns. Singleton semantics and full-graph families of sizes four and sixteen are separately checked.

The universal theorem is supported by a written bidirectional mathematical proof, not by bounded search. The exact strength-two minimum is imported from the published covering-array theorem; no independent proof of that combinatorial extremal theorem is asserted. General larger-strength covering-array minima are not computed or certified here.

The accompanying structured review is a self-review only. Independent audit has not been performed.
