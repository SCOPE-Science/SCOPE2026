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
# Verification

Run `python3 verify.py` from the directory containing the package files. The script requires only the Python standard library, independently implements a recursion for full chain-type profiles and performs exhaustive partial-injection checks in small degrees.

Observed output:

```
VERIFY_OK_FULL_CHAIN_TYPE_DOMINANCE
brute_elements 2000 profile_cells 251 layer_compositions 56
coefficient_dominance_checks 18196 strict_unbalanced_cases 909
```

The exhaustive brute-force comparison covers nonempty ordered-layer compositions in degrees 1 through 6, with at most 4 levels. The coefficientwise balanced-dominance comparison covers degrees 2 through 11 with up to 5 levels. These are finite checks, not a proof in arbitrary degree; the unlimited proof is the path-graph embedding and falling-factorial smoothing argument in RESULT.md. An independent mathematical audit is not performed.
