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

# Verification of the stated cutoff

The self-contained proof uses a smooth positive Dulac multiplier and the classical Hopf theorem, not an inference from numerical orbits. The included `verification/check.py` symbolically recomputes every nontrivial polynomial/rational identity used in the proof, including the complex third-order first Lyapunov formula at the sharpness point. A zero exit status indicates that the identities reproduced exactly under the declared normalization. This does not test a continuum of ODE trajectories experimentally and does not constitute independent external validation.

Command from the extracted package root: `python verification/check.py` (after installing the package dependency in `requirements.txt`). The only domain of the cutoff is the open positive quadrant of the specified smooth two-dimensional vector field; the full nonlinear economic model and global convergence questions lie outside the claim.
