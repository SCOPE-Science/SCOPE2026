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
# Reproducible verification

The general theorem is proved by separating upsets and the stability witness argument in `RESULT.md`. The finite checks are independent corroboration, not certification of all preorders or all cardinalities.

`checker.cpp` uses direct semantic evaluation, not SNDR, to count every chain frame for \(n=1,2,3\) worlds, enumerating all \(2^{n2^n}\) neighbourhood assignments and every upset valuation. It confirms the all-parameter counting formula at those sizes and independently compares the predicate with SNDR on additional examples.

`verify_posets.py` enumerates the 19 labelled three-element posets and tests random neighbourhood assignments against direct axiom semantics and the downset-refinement condition. It also generates additional random four- and five-world posets, tests the strict three-world witness, and exhaustively checks every concrete assignment on each labelled two-world poset. The randomized tests use a fixed seed.

Run from a directory containing the two artifacts:

```sh
c++ -O3 -std=c++17 checker.cpp -o checker && ./checker
python3 verify_posets.py
```

The executed outputs were:

```text
chain_n=1 semantic_census=4 predicted=4
chain_n=2 semantic_census=241 predicted=241
chain_n=3 semantic_census=16690673 predicted=16690673
ALL_CHECKS_OK exhaustive_n=1,2,3 randomized_n=3..5 cases=15000
ALL_POSET_CHECKS_OK: 19 labelled three-world posets, 8700 random cases on n=3..5, three-world strictness witness, all 2-world frames
```

Limits: Exhaustive chain census is performed only through three worlds; cases at four and five worlds use sampled frames. General exactness comes from the proof. No external independent assessment was performed.
