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
The package verifies the GaLore refresh-block staircase on the isotropic matrix quadratic.

`verify.py` recomputes the top-\(r\) singular subspace at each refresh, reuses it between refreshes, and checks active block annihilation, every zero compact-gradient interval, the zero current-gradient retention ratio, and the first zero iterate \((K-1)T+1\).

The computations are transcription guards. The exact trajectory is proved by induction in `RESULT.md`.
