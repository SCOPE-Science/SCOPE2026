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

# Reproducibility and proof boundary

Run `python3 verify.py` with Python 3 and its standard library. The script uses exact rational arithmetic, with no external packages or network access. It independently checks the composition of multiple finite flow and pulse maps against the combined fractional map; checks the explicit iterate formula in two mathematically distinct evaluation orders; verifies a rational example in which pulse timing alters survivor abundance without changing the winner; and verifies an exact fixed point on a neutral simplex, including trace and determinant of its linearization. It also exercises the subcritical, critical, supercritical, and tied-multiplier branches on finite iterates.

The resulting execution output was:

```
PASS: exact rational composition, iterate, timing and fixed-simplex checks
```

The general theorem is proved analytically in `RESULT.md`. Finite arithmetic checks are not exhaustive and do not establish the asymptotics, absence of periodic cycles, or the Floquet spectrum for every admissible parameter. These follow from the closed-form proof. The statement is restricted to predetermined periodic pulse times, rank-one shared crowding, positive multiplicative pulse factors, and positive seasonal competition integrals. A recent motivating full preprint was not inspected, and no independent mathematical or historical-priority audit has been performed.
