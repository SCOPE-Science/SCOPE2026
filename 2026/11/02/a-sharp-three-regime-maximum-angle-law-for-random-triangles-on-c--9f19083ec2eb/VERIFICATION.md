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

The theorem is established by the exact ordered-gap density and the integration recorded in `RESULT.md`. The computation `arc_max_angle_verify.py` uses only the Python 3 standard library and requires no downloaded datasets or network access. Run:

```sh
python arc_max_angle_verify.py
```

The completed execution produced these messages:

```
ORDER_STATISTIC_INTEGRAL_AND_MONTE_CARLO_PASSED
CRITICAL_LOWER_TAIL_EXPONENTS_PASSED
ACUTE_TRANSITION_AND_FULL_CIRCLE_BENCHMARK_PASSED
ALL_CHECKS_PASSED
```

Tests numerically compare the closed form against an independently evaluated piecewise-cubic gap integral, direct Monte Carlo sampling on seven arc apertures, and the stated leading lower-tail coefficients in every regime, including the isolated critical cubic regime. The full-circle acute probability agrees with the previously known value \(1/4\). Finite numerical checks cannot establish universal correctness or historical originality; those claims depend on the proof and the explicitly limited literature comparison.
