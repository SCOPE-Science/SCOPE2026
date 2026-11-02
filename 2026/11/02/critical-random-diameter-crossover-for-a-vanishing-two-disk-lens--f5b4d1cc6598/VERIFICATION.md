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

# Verification and reproducibility

The analytic proof is in `RESULT.md`. It verifies the radial boundary formula, lens area, uniform near-antipodal scaling, \(16/15\) local integration coefficient, and the connected-overlap \(O(n^{(2-v)/5})\) estimate needed to conclude Poisson factorial moments. The disk endpoint is independently consistent with the exact previously published unit-disk limiting law.

The included `verify.py` performs independent numerical quadrature and seeded finite-sample Monte Carlo using rejection sampling from the exact lens and convex-hull diameter evaluation. Run with `python verify.py` after installing NumPy and SciPy. The simulation is not an infinite proof, has visible finite-\(n\) bias, and supplies neither publication priority nor independent auditing.

No independent scientific audit has been performed.
