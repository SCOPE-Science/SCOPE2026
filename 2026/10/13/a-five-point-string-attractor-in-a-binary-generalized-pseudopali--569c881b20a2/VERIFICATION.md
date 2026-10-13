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
# Verification of the finite counterexample

Run `python3 verify.py`. No external dependencies, random choices, optimization packages or online resources are needed.

The checker independently computes shortest palindromic/antipalindromic closures for all five directive symbols by testing every possible suffix length. It checks the exact resulting word and its length, and searches **all occurrences** of each of the six factors used in the lower-bound proof. It confirms four pairwise disjoint factor-support sets, the competing fifth and sixth factor constraints, and all 1,200 possible four-position choices that select one position from each of the four supports.

For the upper bound, it verifies the zero-based five-position witness `9,16,23,33,39`; checks the maximum unmarked run is nine; and computes both factor sets independently for lengths one through nine: all occurring factors and factors with an occurrence crossing the witness. Equality at each length finishes the proof for this 44-character word.

Observed successful output:

```text
VERIFY_OK length=44 closures=5 lower_witnesses=6 four_position_candidates=1200 five_attractor=9,16,23,33,39 checked_factor_lengths=1..9 max_unmarked_run=9
```

This is an exact finite certificate for one constructed prefix, not a proof of a universal upper bound or of minimality of its length. No external independent review has been performed.
