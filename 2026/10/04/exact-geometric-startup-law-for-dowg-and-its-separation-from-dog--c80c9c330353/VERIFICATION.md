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
The package verifies the constant-subgradient startup recurrences for DoG and DoWG.

`verify.py` replays both source algorithms, checks the exact DoG product, reconstructs the reduced DoWG map, isolates the unique positive cubic fixed point, tests monotone convergence and the limiting multiplicative ratio, and checks the predicted first-hit scaling numerically over increasing distance ratios.

The numerical checks are transcription guards. The infinite-sequence asymptotics and hitting-time laws are proved analytically in `RESULT.md`.
