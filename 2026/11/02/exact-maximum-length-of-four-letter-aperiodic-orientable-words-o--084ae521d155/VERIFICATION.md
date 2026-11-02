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

# Reproduction

Use Python 3 with NumPy and SciPy (HiGHS mixed-integer optimization backend); run `python verify.py`. It regenerates all allowed four-grams, their reversal pairs, 64 three-gram vertices, the binary flow-incidence matrix and the start/end constraints. It also checks all windows of the 113-letter witness directly, before invoking the solver, and checks every resulting integer constraint after solving. The observed output in the packaged reproduction was:

```text
QUATERNARY_APERIODIC_ORIENTABLE_4_VERIFY_OK
length=113 factors=110 pairs=120 variables=368 constraints=186
optimal_edges=110 mip_dual_bound=110 mip_gap=0
```

The upper-bound computation relies on the named finite MIP solver's optimality/dual-bound certificate rather than a formally verified external checker. Every coefficient of the optimization model is regenerated from exact combinatorial definitions and is integral. No infinite claim is extrapolated from finite observations. An independent mathematical audit has not been performed.
