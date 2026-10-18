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

# Reproduction and limits

Run `python verify.py` after installing `requirements.txt`. The script, executed before packaging, verified the two independent exact triangle-integral values, the polynomial identity over dimensions 2 through 99 at three rational widths, positivity in that domain, exact repeated-edge cumulants, mesh quadrature of the three-point geometry at three widths and three resolutions, and the three skewness asymptotic regimes at three sample sizes. All assertions passed.

The proof of the exact identity requires only elementary integration and diagram cancellation. The numerical meshes corroborate the circle-wrapping boundary and the integrals but do not prove the infinite-dimensional assertions. The stated asymptotic equivalences follow by algebra from the proved formula, without using numerical convergence as a proof.
