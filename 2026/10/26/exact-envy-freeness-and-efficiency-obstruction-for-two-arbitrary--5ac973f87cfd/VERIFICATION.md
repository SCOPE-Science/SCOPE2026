---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For nonidentical Boolean tables choose a subset of differing value and give it to the agent who values it 1. If (1,1) is realizable it is immediately EF+PO; otherwise this allocation is envy-free and has (1,0) or (0,1), which is on the binary Pareto frontier. For equal valuations an identical 11 complementary pair yields (1,1); if none, all Pareto allocations with a 1/0 utility split envy the winner, except the identically zero table, which is trivially EF+PO. EF alone requires equal valuations on both bundles in some complement pair, giving the all-01/10 excluded class. The 2^m bundles partition into L complementary pairs, each with 00,01,10,11; exclude 11 for all L and remove globally zero -> 3^L-1, while no-EF forces 01/10 ->2^L. Independently exhaustively checked all 65,808 ordered truth-table pairs for m=1..3 directly from EF inequalities and PO dominance, reproducing (2,8,80) failure counts.

## originality

PASS

Fresh best-of-knowledge statement-level comparison with relevant published Resultary findings and primary articles, acknowledging known general methods and narrower ancestors; no inspected stronger theorem implies the exact final result. Priority is qualified by explicit residual risks.

## value

PASS

This is a complete natural two-agent exact fairness-and-efficiency existence classification in the broad Boolean nonmonotone domain, distinguishing EF nonexistence from EF/PO incompatibility and quantifying obstruction rarity for a stated independent-table benchmark. The benchmark distribution is mathematically explicit, not a realistic preference model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
