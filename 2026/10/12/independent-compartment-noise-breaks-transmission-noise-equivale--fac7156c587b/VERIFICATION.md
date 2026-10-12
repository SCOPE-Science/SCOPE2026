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

The proof was checked at the level of the displayed stochastic system and the simulation diffusion. The independent-driver covariance is diagonal and gives sum-direction variance \(2g^2\); the shared-transmission covariance is rank one and gives sum-direction variance zero. The latter also creates a mixed second-derivative term in the forward operator that the independent diagonal model lacks.

The upper-face obstruction is analytic: for initial points \(\varepsilon\) inside a finite positive upper face and times proportional to \(\varepsilon^2\), Brownian displacement is first order in \(\varepsilon\) while drift is second order, leaving a positive limiting exit probability. This establishes non-invariance without a finite simulation or exhaustive enumeration.

`verify.py` was replayed from the extracted package path after serialization. It checks only the exact covariance identities and that the source control ceiling \(\alpha=0.85\) leaves positive normal diffusion at positive upper faces. Its successful output is `VERIFY_OK`.

Limits: no claim is made about reflected SDEs, unbounded domains, or alternate correlated-noise choices. The bounded zero-flux PDE may remain mathematically valid as a separate confined model.
