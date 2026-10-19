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
# Verification boundaries

The exact source-model transition and the state-independent star shell criterion are written explicitly in `RESULT.md` and `verification.py`. Run `python3 verification.py` with Python 3.9 or later. The script runs finite exact-rational checks of the sharp threshold for \(2\le k\le6\) on a five-point grid, frozen binary shells, exact hub transitions, every binary composition cylinder up to nine steps, and stationary moment identities. The analytical proof, not code, establishes the claims for every \(k\ge2\), arbitrary continuous leaf opinions, infinite random trajectories, empirical weak convergence, and Hausdorff dimensions.

A successful script run is an internal reproducibility check, not independent review or a computer-assisted proof of almost-sure statements. In particular no finite simulated trajectory can certify a dense \(\omega\)-limit set. The result is limited to one independent uniformly selected edge each step, an unchanging star, \(\sigma=0\), strict receptivity, and \(0<\rho\le1/2\); the singularity assertion requires \(\rho=1/2\) and odd \(k\).
