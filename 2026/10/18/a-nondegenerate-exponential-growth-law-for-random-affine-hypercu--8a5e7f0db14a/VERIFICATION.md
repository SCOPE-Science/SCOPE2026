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

# Reproduction and scope

Execute `python3 check_affine_cube.py` with Python 3 standard library. The reproducible test reported `AFFINE_CUBE_RANDOM_EXPONENT_OK comparisons=155`, with rate midpoint \(I(\mu/2)=0.0867339256\ldots\) and median exponent \(0.6064132549\ldots\). Checks cover exact Boolean-edge counts, Boolean boundary inequalities, exact offset-integrated means in sampled low dimensions, and numerical properties of the deterministic large-deviation rate function. The high-dimensional convergence and tail asymptotics rest on the written proof, not finite enumeration. The Gaussian normalization and width-biased direction law are explicitly handled in the proof. No independent audit or formal proof certificate is supplied.
