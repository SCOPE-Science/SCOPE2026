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

Run `python3 verify_graph_oscillation.py` with the standard Python library. The executed output was:

```
EXACT_RATIONAL_SHARPNESS_OK 490
EXACT_RATIONAL_OSCILLATION_BOUNDS_OK 3920
FLOATING_EXPONENT_DIAGNOSTICS_OK 1750
EXACT_DIAMETER_TWO_RIGIDITY_OK 27475
ALL_WEIGHTED_P_HEAT_OSCILLATION_CHECKS_OK
```

Exact rational checks use independently assembled weighted vertex-flow derivatives at exponents \(p=2\) and \(p=3\); real-exponent inequalities use seeded numerical samples. Connected labeled graphs of order at most six were exhaustively considered in the topology diagnostics. These finite computations cannot prove the claims for arbitrary graph sizes, positive real parameters or every real exponent. The proof in `RESULT.md` supplies universal quantifiers via the scalar power minimization, active-extrema Dini derivative, equality construction and parameter-limit calculation. Tests for arbitrary exponents are diagnostics, not a certificate of exhaustive real-arithmetic validity. The linear diameter-two implication was known previously. Independent mathematical audit has not been performed.
