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

The nine nonnegative type×recipient counts completely determine additive EF1, equivalent to U_i(s)+max_{g∈S_j}v_i(g)≥v_i(S_j) for all ordered i≠j. Backward induction on the finite adversarial game has exact alternation ∃type∀recipient over h remaining turns. The actual STRATEGY.json contains 42 reachable fair nodes, and a separately implemented exact-integer check confirms all 126 allocator responses: 74 immediate failures and the rest guaranteed fair successor states in the policy with no surviving seventh-turn branch. An independent exhaustive exact minimax recursion gives W_6(0)=false and W_7(0)=true; an independent dynamic program verifies prefix-EF1 feasibility for all 3279 fixed streams of 1..7 arrivals. This is an exhaustive finite proof for the fixed valuation vectors, not a sample. The universal two-type positive side is imported from cited literature and not re-proved by this certificate.

## originality

PASS

Unlike the published failure of one particular cyclic online EF1 rule at three types or a longer stream that defeats even clairvoyant allocation, this certificate rules out every deterministic online rule for one small fixed three-type vector system while proving every length≤7 fixed stream admits some hindsight solution. The positive two-type boundary is prior; the finite adaptive-vs-clairvoyant separation is assessed as new with the closest 2026 text incompletely accessible.

## value

PASS

The exact item-type boundary is naturally motivated by the known 2-type universal guarantee. A compact 3-type adversarial strategy proves intrinsic online impossibility even though every individual seven-arrival stream admits a fair hindsight trajectory; the latter quantifier separation is valuable for fair online mechanism design and cannot be inferred from a mere algorithm-specific counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
