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

The analytical proof in `RESULT.md` is the source of the universal statement. `verify.py` is a self-contained Python 3 standard-library program. It checks the exact extremal ratios for commuting diagonal errors in many randomly selected rational matrix/noise cases, the rational GMRES(1) endpoint residual construction, the flat optimality at the sharp critical noise, and two distinct safeguard minima on deterministic numerical grids.

Run `python verify.py` from the directory containing that script. Observed output:

```
VERIFY_OK exact_endpoint_enumerations= 2100 exact_worst_GMRES1_witnesses= 2100 exact_critical_phase_equalities= 9 numerical_minimax_grid_checks=20002
```

The test enumeration uses only the endpoint choices of noise. The reason those endpoints suffice for the full uncertainty set is the independently written monotone-ratio argument in the proof; finite enumeration does not certify that reduction. The numerical grid verifies selected instances but does not certify global minimization. No independent scientific audit or formal proof assistant was used.
