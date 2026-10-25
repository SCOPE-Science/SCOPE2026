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

# Reproduction instructions

Run the bundled file `verification/check_hull.py` with Python 3 and the standard library. The checker constructs a planar monotone-chain convex hull from literal vertex coordinates, independently determines which inner points are exposed, and checks the analytic angular criterion. It samples 15,000 seeded configurations over multiple coprime/noncoprime polygon orders and radii, 4,290 deterministic critical-radius configurations, and 19,200 uniformly spaced orientation cases. It also checks the arithmetic near-circle limit along gcd classes.

Actual execution returned:

```
INDEPENDENT_MONOTONE_CHAIN_ANGULAR_HULL_CASES_OK 15000
DETERMINISTIC_COPRIME_AND_NONCOPRIME_THRESHOLDS_OK 4290
FULL_ORIENTATION_GRID_TWO_ATOM_PROBABILITY_OK 19200
ARITHMETIC_CRITICAL_WINDOW_VARIANCES_OK
ALL_PLANAR_ROTATION_HULL_CHECKS_OK
```

The script requires no network access or third-party modules. Its numerical orientation integration, finite random tests, and finite asymptotic samples are **corroboration**, not a proof for arbitrary integers or all real parameters. The analytic support inequality, periodic lattice reduction, uniform-offset occupancy law, endpoint treatment and Taylor expansion in the main result establish the complete statement. No independent scientific audit has been performed.
