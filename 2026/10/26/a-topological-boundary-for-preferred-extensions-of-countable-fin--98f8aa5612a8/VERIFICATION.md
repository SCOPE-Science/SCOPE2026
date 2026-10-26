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

The code `checker.py` uses only the Python standard library, constructs finite cyclic analogues of the explicit framework, verifies each argument has at most three attackers and three targets, enumerates every subset of the non-self-attacking core vertices, and checks the exact admissible and preferred families. Reproduction: `python checker.py`. The observed output is:

```
OK rows=2, cycle_period=2, core_subsets=16, admissible=3, preferred=2
OK rows=3, cycle_period=3, core_subsets=512, admissible=4, preferred=3
OK rows=4, cycle_period=4, core_subsets=65536, admissible=5, preferred=4
FINITE_ANALOGUES_OK
```

The infinite construction is not computationally exhausted. The proof relies on explicitly quantified finite attacker sets, forced adjacent row members, mutual inter-row conflicts, and a pointwise convergence argument. The compactness projection lemma and closedness assertions are mathematical deductions, not experimental extrapolations. No independent external audit was performed.
