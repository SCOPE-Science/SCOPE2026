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

# Verification of the colored-equivalence classification

The pure Python 3 artifact `verify.py` uses no external dependencies. It enumerates nonempty set partitions as labeled equivalence relations and all complete unary colorings for the tested sizes. It independently computes the proposed two-level truncated profile and a semantic signature at quantifier rank six: signatures are iteratively refined on states with zero, one, or two assigned variables using both possible existentially rebound variables. Within each test universe the resulting sentence-signature classes coincide exactly with the classes given by the proposed profile; no false merges or splits occur.

Run `python3 verify.py`. The output includes:

```
FORMULA {'q': 1, 'local_profiles': 2, 'theory_count': 8, 'maximum_minimal_size': 6}
FORMULA {'q': 2, 'local_profiles': 8, 'theory_count': 6560, 'maximum_minimal_size': 36}
FORMULA {'q': 3, 'local_profiles': 26, 'theory_count': 2541865828328, 'maximum_minimal_size': 162}
EF {'q': 1, 'n': 6, 'structures': 278, 'profiles': 8, 'qrank': 6, 'rank_states': 64}
EF {'q': 2, 'n': 5, 'structures': 1954, 'profiles': 71, 'qrank': 6, 'rank_states': 1087}
COLORED_EQUIVALENCE_FO2_VERIFY_OK
```

The finite checker covers only the listed carrier sizes and six rounds, not all structures. The all-arity theorem is instead proved by a complete infinite-duration two-pebble back-and-forth argument and characteristic formulas in `RESULT.md`. The exact upper and lower bounds follow from an explicit finite construction and a forcing sentence, independently of any sampled cases. No independent audit has been performed.
