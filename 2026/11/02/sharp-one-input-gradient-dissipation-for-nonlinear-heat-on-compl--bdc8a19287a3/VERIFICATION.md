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

# Verification of the sharp multipartite edge-gradient dissipation theorem

The reproducible standalone source is `verify_multipartite_pheat.py`. Execute `python3 verify_multipartite_pheat.py` in a Python 3 environment with `numpy` and `scipy`. The program does not require external data or the historical research corpus.

Observed checks:

```
EXACT_RANDOM_EDGE_DERIVATIVE_INEQUALITIES_OK 2855
EXACT_SHARP_WITNESS_IDENTITIES_OK 60
FLOW_SHORT_TIME_CHECK_OK (6, 1, 1) 3.0 growth 1.999640027e-05
FLOW_SHORT_TIME_CHECK_OK (7, 1, 1, 1) 1.5 growth 1.999860001e-05
FLOW_SHORT_TIME_CHECK_OK (5, 1, 1, 1) 3.0 growth -2.399775934e-09
FLOW_SHORT_TIME_CHECK_OK (2, 2, 2) 4.0 growth -2.499911878e-05
GLOBAL_SHARP_RATE_FORMULA_OK 350
ALL_MULTIPARTITE_PHEAT_TESTS_OK
```

Exact-rational checks use integer powers. Exponents \(3/2,4,5\) and flow integration involve floating-point diagnostics. The exhaustive statements across all graph sizes and exponents come from the analytic proof in `RESULT.md`—not the finite tests. The code's witness states are reconstructed from part labels; its vector field uses the original graph edge list rather than the closed-form expression. Critical boundary cases and the two-part case are included. No external independent scientific audit has occurred.
