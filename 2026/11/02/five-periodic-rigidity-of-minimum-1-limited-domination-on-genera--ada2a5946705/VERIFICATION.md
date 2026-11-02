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
# Verification details

The proof in `RESULT.md` uses only a cubic degree-counting bound, two local spin identities, a cyclic difference recurrence, and a complete length-five binary-word classification. These steps establish the theorem for every integer \(n\ge5\).

Run `python3 VERIFY.py` with the standard Python 3 library. The verifier constructs the graph's edges independently of the word-based description; checks each of the 250854 half-size subsets for orders 5 through 10; compares the **actual labelled sets** to the formula; tests proposed sets at every order through 120; and separately counts the twelve admissible cyclic five-words.

Exact replay:

```
BRUTE 5 12
BRUTE 6 2
BRUTE 7 2
BRUTE 8 2
BRUTE 9 2
BRUTE 10 12
VERIFY_OK brute_subsets 250854 orders=5..10 construction_orders=5..120 period5_words 12
```

This finite replay is supporting evidence, not certification of the universal claim. The general claim relies on the mathematical proof. Independent audit and comprehensive historical priority assessment have not been performed.
