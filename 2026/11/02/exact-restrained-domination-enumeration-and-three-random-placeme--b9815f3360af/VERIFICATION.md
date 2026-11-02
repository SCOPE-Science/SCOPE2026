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

# Verification record

Execute `python3 verify_rook_restrained.py` from the directory containing that standalone file. Only the Python standard library is used. The checker implements the literal restrained-domination predicate for each omitted vertex and a distinct incidence-graph predicate; it compares both for every selected subset on the six indicated labeled boards. It separately expands the exact double inclusion--exclusion formula with integer coefficients and compares the complete complement-size distribution.

The observed terminal summary was:

```text
2x2: 16 subsets; 5 restrained dominating sets; polynomial OK
2x3: 64 subsets; 33 restrained dominating sets; polynomial OK
2x4: 256 subsets; 175 restrained dominating sets; polynomial OK
3x3: 512 subsets; 307 restrained dominating sets; polynomial OK
3x4: 4096 subsets; 2967 restrained dominating sets; polynomial OK
4x4: 65536 subsets; 52539 restrained dominating sets; polynomial OK
TOTAL: 70480 direct-subset and structural comparisons; all passed
```

The proof separately verifies the exact factorial-moment identities and all asymptotic limits. The numerical moment diagnostics only provide finite sanity checks. No infinite theorem, unindexed-literature completeness, or independent audit is certified by these computations.
