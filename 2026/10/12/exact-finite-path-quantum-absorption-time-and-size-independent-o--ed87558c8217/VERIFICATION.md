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

The analytic all-length result is proved in `RESULT.md` by a matrix Lyapunov identity. The companion `verify_mean_absorption.py` is standalone Python 3, requires no external packages, and checks the entire proposed matrix identity using exact rational real and imaginary parts for path lengths \(1\le N\le40\) at four positive rational hopping/loss pairs. The observed output is:

```
VERIFY_OK 88560 exact rational Lyapunov matrix entries
```

The checker also validates the diagonal expression at all tested sites, including the directly absorbing starting state. Because the script samples finitely many lengths and parameters, it does not establish the universal quantifiers by itself. The analytic proof handles all positive real parameters and all integer path lengths. No external independent audit has been conducted.
