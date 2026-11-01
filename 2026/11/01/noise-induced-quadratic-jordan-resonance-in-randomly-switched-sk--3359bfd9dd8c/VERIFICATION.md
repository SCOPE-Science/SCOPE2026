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

The stationarity and transfer identities were proved by explicitly listing the two inverse branches, and the covariance is obtained from the invariant centered quadratic polynomial space. `CHECK.py` independently integrates full forward branch cylinders with rational weights for three selected parameter laws (23 finite-horizon identities), then checks the specialized formula at 25 lags and verifies the sign transition and diagonalizability of each mixture component.

The tests use exact rational arithmetic and can be reproduced by running `python CHECK.py` in the directory containing the accompanying files. They are not exhaustive over all parameter laws or time horizons; the universal statements require the analytical transfer and Jensen arguments. There is no external audit or independent certification.
