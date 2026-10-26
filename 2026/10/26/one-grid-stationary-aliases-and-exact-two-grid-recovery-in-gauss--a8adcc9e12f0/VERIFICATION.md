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
# Verification details

The included `check_stationary_ou.py` is standalone Python 3 standard-library code. Execute `python check_stationary_ou.py` after extracting it. The executed checker produced `PASS: 63 exact-rational configurations; universal conclusions require the analytical proof.` The tests use rational matrix arithmetic, diagonal and rotated symmetric drifts, two different step sizes, multiple unknown diffusion intensities, all eight single-grid aliases in a diagonal three-dimensional example, three repeated-eigenvalue representative rotations, a sharp precision perturbation witness, and both signs of a skew rotational drift.

The universal claims are proved by: (i) the exact discrete Lyapunov geometric series; (ii) symmetric square-root spectral decomposition, including repeated eigenspaces; (iii) affine interpolation of inverse covariance matrices in the timestep; (iv) a trace identity for recovering scalar isotropic noise; (v) an explicit two-dimensional skew-drift Lyapunov solution. In particular, numerical tests cannot prove the continuum of projector choices, exact necessity and sufficiency, or general-dimensional uniqueness.

Independent audit: not performed. Unproved extensions: unknown anisotropic covariance, nonlinear drifts, nonsymmetric drift identification, finite-sample confidence sets, and quantitative joint unknown-noise perturbation rates. Classical scalar AR(1) variance identities are acknowledged as antecedents.
