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

Execute `python3 verify.py` in a clean Python 3 environment using only the standard library. The test independently generates the defining anti-recurrence by maintaining its increasing complementary sequence, then compares the output with a substitution-based generator for each parameter and index in the declared finite sample. It separately enumerates all states and digits for \(1\le a\le200\), confirming the algebraic three-case identity and the invariant alphabet.

Observed successful output:

```text
VERIFY_OK tested_greedy_terms=75000 distinct_a=8 transition_cases=5576800 a_max=200 all_exact=yes
```

The generator and all comparisons use exact integer arithmetic. These computations are not an exhaustive check of unbounded parameters or indices, and they are not an independent mathematical audit. The universal conclusion follows from the combinatorial construction and symbolic inequalities in RESULT.md.
