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

# Finite semantic verification

Run `python3 verify_conditionals.py` using Python 3 with only its standard library. The checker computes subteams, universal antecedent tests, indicative/epistemic/counterfactual truth conditions, and lax splits directly, then reconstructs the proposed normal forms. It enumerates every union-closed family containing the empty team over abstract valuation sets of sizes \(1,2,3,4\): \(2,7,61,2480\) families, respectively, for each of the two expressive conditionals. This totals \(5100\) conditional/family comparisons, with each characteristic exact-team formula checked. It also compares the counterfactual on every pair of flat predicates in those domains (\(340\) comparisons), tests all pairs of flat splitting operands at four valuations (\(256\) pairs), random union closure under arrows, and strict depth examples.

Observed terminal output:
```
FLAT_SPLIT_PAIRS_OK 256
ALL_UNION_CLOSED_NORMAL_FORMS_OK 1 2
ALL_UNION_CLOSED_NORMAL_FORMS_OK 2 7
ALL_UNION_CLOSED_NORMAL_FORMS_OK 3 61
ALL_UNION_CLOSED_NORMAL_FORMS_OK 4 2480
NORMAL_FORM_FAMILIES_CHECKED 5100
COUNTERFACTUAL_FLAT_PAIR_TESTS 340
SHARP_DEPTH_SEPARATIONS_OK
VERIFY_OK
```

The abstract four-valuation case corresponds to two propositional variables. The three-valuation stress test is not a Boolean valuation cube but checks the purely set-theoretic construction. Exhaustive bounded tests are not proofs for unbounded vocabulary size. The manuscript proof supplies the general result. No third-party formal or independent audit has been performed.
