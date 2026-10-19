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

The standalone `checker.py` runs deterministic exact-rational symbolic checks (requires Python and SymPy). Command: `python checker.py`.

It checks 40 rational direct-transform evaluations and numerator degrees/endpoint noncancellation cases for one through five intervals; 28 equal-height interlacing and representative upper-root examples; and 28 exact quadratic/discriminant tests spanning four two-pulse geometries with seven positive weight ratios. Total: **96** parameter cases. The tests ran successfully and their standard output appears in `checker_output.txt`.

The general proof is analytic and uses no extrapolation from finite tests. The chamber maxima over arbitrary real endpoints and weights were not interval-certified numerically; their exact sign characterization is proved. No external expert or independent audit was conducted.
