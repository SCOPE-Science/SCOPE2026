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

The included `verify.py` directly checks the degree-at-most-one definition on labeled squared cycles and constructs all exchanges by changing exactly one token. Exhaustive enumeration of all subsets for lengths 7 through 16 agrees exactly with the independent block generator; the exchange graph and the formulas are checked through length 32. Separate longer checks at lengths 33, 34, 35, 38, 42, and 46 also agree.

The general theorem uses the cyclic-block counting argument and local-exchange case classification in `RESULT.md`. Finite test coverage is not an infinite-proof claim. The main residual risk is possible earlier equivalent literature; no independent scientific audit has been performed.
