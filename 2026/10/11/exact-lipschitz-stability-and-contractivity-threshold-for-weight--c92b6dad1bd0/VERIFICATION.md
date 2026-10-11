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

# Computational verification

Run `python3 verify.py` using Python 3.10+ and the standard library only. The expected output is:

```
VERIFY_OK checks=1240 random_seeds=240441 all_scenarios_passed
```

Checks: 1,200 random finite weighted KKT-projection tests over five dimensions and six exponents; 18 analytic two-coordinate norm witnesses, 18 finite-difference realizations, and four strict three-coordinate expansion checks (1,240 in total). The calculation uses floating-point arithmetic and does **not** certify the universal quantifiers, any exact real inequality, or the global formula in arbitrary dimension. The paper supplies the necessary analytic proof independently.
