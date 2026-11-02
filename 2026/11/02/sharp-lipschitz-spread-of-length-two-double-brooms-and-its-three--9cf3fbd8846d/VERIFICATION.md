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
# Reproduction and limitations

Run `python3 verify_double_broom.py` using Python 3 standard library. The program independently enumerates all signed edge-increment vertices for 25 parameter pairs, computes exact vertex variances in the straight and reflected-spine cases, compares 784 optimizer-count profiles with the closed formula, and checks 147 leaf-budget balance chains plus phase-boundary cases and asymptotic diagnostics.

Observed terminal markers:

```text
EXACT_FULL_EDGE_CUBE_AND_REFLECTION_DOMINANCE_OK 25
EXACT_ALL_OPTIMIZER_MULTIPLICITIES_AND_PARITY_OK 784
STRICT_FIXED_LEAF_BUDGET_BALANCING_OK 147
EXACT_FIRST_PHASE_TIES_AND_LIMIT_DIAGNOSTICS_OK
ALL_DOUBLE_BROOM_SPREAD_CHECKS_OK
```

These tests are exact for enumerated finite cases. The limiting calculations are tolerance-based diagnostics; they do not prove the real limit, and enumeration is not a proof for unbounded leaf sizes. General validity follows from the separate analytic proof in `RESULT.md`. No external or independent audit has been performed.
