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

# Verification of finite regional proximality and monoid normal forms

The bundled `verify.py` performs independently computed finite-state algebraic checks from the two generator definitions: complete semigroup closure by tuple composition, the proposed disjoint normal forms, image-rank spectra, all ordered-pair mergeability relationships, backward diagonal relation and minimality for every \(2\le m\le16\). It also exhaustively visits the two-letter transformations on two and three states and tests all minimal examples for relation transitivity.

Command: `python3 verify.py`.

Actual output:

```
PASS: exact transformation-monoid and pair-relation tests
Even-cycle systems tested: m=2,...,16
Individual indexed pair/normal-form checks (lower bound): 6055
Strongly connected two-letter automata checked at n=2,3: {2: 5, 3: 149}
Unbounded claims require the accompanying proof, not this finite run.
```

These are exact finite checks, not evidence that all \(m\) or all possible generator families have been exhaustively enumerated. The unbounded and arbitrary-monoid claims rely on the mathematical normal form and invariant nonmergeable-pair arguments in `RESULT.md`. The code depends only on the Python standard library. No external independent audit has been performed.
