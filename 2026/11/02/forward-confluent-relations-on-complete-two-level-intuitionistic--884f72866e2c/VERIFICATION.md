---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a strict comparison of sources m<t, an upper target must occur in both rows, whereas a lower target is witnessed by any upper target in row t or, if that row has no upper targets, only by itself. This gives precisely the two intersection restrictions; reflexive source comparisons impose nothing. For zero empty upper parts, the column sum is H^b without the nonempty-row condition, and the empty-row completions have no all-one columns: subtract B^b-(B-1)^b. For z>0 empty upper parts, each lower target gives 2^z-1 ordinary patterns and one all-present pattern with 2^a lower-source completions, accounting for every term of the exact formula. In the proposal law the factor 2^a on each all-one column cancels its 2^a equally likely lower-source completions, so conditioning on confluence is exactly uniform. One upper row is empty with probability (2^{b-1}/H)^b, independently across columns, giving the claimed bound by a union over rows, not by assuming row independence. Dividing by 2^{(a+b)^2} gives 2^{-ab}(1+2^{a-b}-2^{-b})^b for the relaxation; replacing the base by 1+2^{a-b} costs relative error at most b2^{-b}, uniformly in a, and gives all stated regimes. The audit's separate up-set evaluation checked every relation for all six positive (a,b) with a+b<=4, including 185 versus 281 and 11,401 at (2,2).

## originality

PASS

Credit the rooted-fork specialization and established FIK semantics. The strongest indexed overlaps, including a same-day two-sided census, do not give the unrestricted one-direction count with both sizes free or its sampling and uniform error analysis. This is a bounded statement-level finding, not a priority certification.

## value

PASS

Complete two-level orders are a natural branching family beyond chains and rooted forks. The census retains the asymmetry of the two levels and distinguishes the balanced and strongly unbalanced rarity regimes. The same structure gives exact uniform sampling with at most two proposals in expectation, an independently useful way to generate valid frames without the rarity cost of rejecting from all relations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
