---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For identical additive two-agent valuations w_t∈{1,2}, maximum instantaneous pairwise envy equals absolute signed load gap. Folding any signed allocation gap mod 4 to distance in {0,1,2} never increases cost and realizes all folded transitions by valid allocations. The only optional edge is (state 1, unit good) ->0 or 2; selecting 0 instead of 2 cannot raise cumulative cost through the next unit, since intervening doubles alternate 0 and 2 and both paths meet at state 1 on the next unit. This proves greedy lower-load-first exactly optimal for each fixed order. The free-order lower bound from w_t<=|D_t|+|D_{t-1}|, parity, and the zero-return unit/double/mixed blocks gives u[b+ceil(a/2)+1_{a=0 and b odd}]. The u,u,3u,u counterexample genuinely beats greedy: 4u versus 6u. Independently tested all 4095 fixed words over {1,2} of lengths ≤11 against exact DP and all 81 count pairs a,b≤8 against free-order DP; proof, not testing, supplies unbounded quantifiers.

## originality

PASS

Best-of-knowledge PASS for exact positive-two-level greedy optimality and all-(a,b) free-order formula. The earlier binary {0,1} theorem and general pseudopolynomial DP do not immediately imply these results, because replacing 2u items with two u rounds changes intermediate-round cost. The very close 2026 primary source was only accessible in abstract/selected summaries, leaving a material full-text comparison risk.

## value

PASS

The source cumulative-maximum-envy objective is temporally sensitive. An exact online policy that is offline optimal for every arbitrary sequence and a closed optimal reordering law for two denominations are natural, useful benchmark theorems beyond an approximation guarantee. The sharp failure at ratio 3 distinguishes a nontrivial alphabet boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
