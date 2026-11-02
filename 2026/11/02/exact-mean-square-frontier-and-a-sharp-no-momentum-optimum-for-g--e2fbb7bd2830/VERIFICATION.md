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

The `verify.py` script independently reconstructs the exact moment-transfer polynomial, its determinant, threshold identity, derivative at zero stepsize, and sharp completed-square certificate in symbolic arithmetic using SymPy. It evaluates the spectral radius of 60 independent rationally specified cases across five dimensions, three momentum levels, and four relative step sizes, checks the momentum-free equality case, and verifies the Gaussian fourth-moment coefficient from coordinate moments.

Execute with `python verify.py` after installing the dependency listed in `requirements.txt`. The expected success marker is `VERIFY_OK`. The full asymptotic theorem relies on the analytic proof in `RESULT.md`, including the primitive positive-map argument and polynomial sign analysis; numerical spectra or finitely many moments cannot certify an infinite-horizon bound. All precision-sensitive, parameter-global claims are stated and proved symbolically; the checks only corroborate them.

No independent scientific audit has been performed.
