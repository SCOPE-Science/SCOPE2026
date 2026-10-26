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

Running `python3 verify.py` from the extracted package returned:

```text
EXACT_COMPONENT_PALM_PASS 3 2 1/4 1 8
EXACT_COMPONENT_PALM_PASS 3 2 2/3 1 8
EXACT_COMPONENT_PALM_PASS 4 2 1/4 3 64
EXACT_COMPONENT_PALM_PASS 4 2 2/3 3 64
EXACT_COMPONENT_PALM_PASS 5 2 1/4 7 1024
EXACT_COMPONENT_PALM_PASS 5 2 2/3 7 1024
EXACT_COMPONENT_PALM_PASS 4 3 1/4 1 16
EXACT_COMPONENT_PALM_PASS 4 3 2/3 1 16
EXACT_COMPONENT_PALM_PASS 5 3 1/4 4 1024
EXACT_COMPONENT_PALM_PASS 5 3 2/3 4 1024
EXACT_COMPONENT_PALM_PASS 5 4 1/4 1 32
EXACT_COMPONENT_PALM_PASS 5 4 2/3 1 32
EXACT_COMPONENT_PALM_PASS 6 4 1/4 5 32768
EXACT_COMPONENT_PALM_PASS 6 4 2/3 5 32768
THRESHOLD_STRICT_ORDER_PASS
VERIFY_OK 44 component-shape strata 69872 hypergraph states
```

The checker constructs each hypergraph explicitly, locates its connected components, marks the internal edge count of every nontrivial component, and accumulates exact rational mixed factorial moments for the isolate count and each component-type count. It independently compares these with the displayed deletion consequences. The monotonicity checks are finite numerical diagnostics and cannot prove the all-parameter statement; the analytic proof uses a strictly increasing logarithmic quotient and an elementary monotone average. The test is not an independent audit and does not establish external priority.
