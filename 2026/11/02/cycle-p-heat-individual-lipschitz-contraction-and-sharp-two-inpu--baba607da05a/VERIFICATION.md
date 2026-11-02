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

# Reproducibility

Execute `python verify_cycle_p_heat.py` with Python 3.9+; the code uses only the Python standard library. The program produced:

```text
EXACT_EDGE_FLOW_IDENTITY_OK n=3..12 at p=3
TWO_INPUT_INSTANTANEOUS_GROWTH_OK cases= 30
INTEGRATED_GROWTH 4 1.5 gain= 1.000005000478
INTEGRATED_GROWTH 4 3 gain= 1.000597765481
INTEGRATED_GROWTH 8 1.5 gain= 1.000005001353
INTEGRATED_GROWTH 8 3 gain= 1.000197059511
ALL_CYCLE_P_HEAT_CHECKS_OK
```

The exact rational checks concern the discrete orientation identity for selected orders. Numerical tests verify selected perturbations and short-time trajectories; their finite coverage cannot prove statements for all \(n\ge3\) and \(p>1\). The proof in `RESULT.md` supplies the quantifiers and handles the singular derivative behavior for \(1<p<2\) by choosing each background edge nonzero before passing to small perturbations. No independent audit has been performed.
