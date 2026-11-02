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
# Verification

Run `python scripts/check_threshold.py` after installing `requirements.txt`. The script exactly reconstructs the ODE factorization and the mutation odds logarithmic derivative, and checks the nonnegative central-difference identity symbolically. It then constructs 144 random strictly positive rational multiplayer games (group sizes 2–7) at the threshold, between the threshold and 1/2, and at 1/2. For each it counts stationary points on the closed simplex using exact Sturm root counting. Six further exact rational test games below their respective thresholds have three interior roots, and the explicit d=3 cubic factorization is checked.

All checks succeeded on the packaged source. The mathematical theorem rests on the analytic Bernstein logarithmic-derivative inequalities in RESULT.md; finite sampling is not a proof for arbitrary payoffs or group sizes. No independent audit or formal proof assistant was used.
