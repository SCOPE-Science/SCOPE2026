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

Run `python checks/verify.py` with Python 3.10+ and no external packages. The script reconstructs the moment-series coefficients for the uniform jump law using rational arithmetic, verifies all rational constants, checks the piecewise integrated-tail and negative log-curvature identities at multiple rational points, brackets representative unique stationary roots, checks the direct cumulant generating function in a parameter grid, and numerically tests the critical slope and scale-excess expansion. `checks/verify_output.txt` contains the captured run result: **1,488 PASS checks**.

# Analytic versus computational evidence

The finite checks do not prove the global critical phase transition or uniqueness. The accompanying proof supplies the needed all-parameter argument by showing the normalized tilted survival density has an increasing hazard; consequently its second moment is strictly less than twice the square of its first moment, and the key derivative of \(H'/H^2\) is strictly negative. Exact rational moments and polynomial inequalities establish the displayed constants without numerical assumptions. The computation uses the paths embedded in this package, not an external or historical log.

# Limitations

Tests do not validate historical originality or provide independent peer verification. No external certification channel has been completed.
