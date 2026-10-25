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

# Reproducibility and verification

The theorem is proved analytically by mixed-area reduction and an exact trigonometric lattice sum in `RESULT.md`; it is not inferred from finite experiments. The independent script `verify_orientation.py` enumerates all pairwise vertex sums and evaluates their convex-hull area, not the mixed-area expression. Its output on the supplied script was:

```
PASS: 559 hull area comparisons, maximum absolute error 7.105e-15
PASS: 13 independent uniform-orientation mean comparisons
```

The 13 test pairs cover equal and unequal, coprime and noncoprime, even and odd side counts. For each pair 40 reproducible pseudorandom orientations over two full turns plus three predicted special angles are tested, with radii 0.7 and 1.3. The mean comparison uses a 1001-point trapezoidal integral on one complete period and checks the known perimeter-product kinematic formula. Run `python verify_orientation.py` with dependencies in `requirements.txt`.

The computations establish only the tested numerical cases. Exact quantifiers over every side count, orientation and radius are discharged by the analytic proof; the numerical tolerance is not treated as a proof of global equality.
