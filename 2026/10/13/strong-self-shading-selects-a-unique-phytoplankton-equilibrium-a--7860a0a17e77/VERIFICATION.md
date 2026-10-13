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

## Reproduction
Run `python verify.py` from the directory containing the accompanying `verify.py` and `requirements.txt` after installing NumPy and SciPy. The verifier independently constructs the limiting and finite-attenuation boundary-value systems from the stated differential equations. For one admissible positive parameter set with nonzero advection, it checks solver convergence, positive solutions, the exact photon-budget identity to numerical tolerance, and convergence of the rescaled biomass and nutrient deficit over attenuation coefficients 5, 20, 100, 500, and 2000. The recorded run printed `VERIFY_OK`. This is a finite numerical consistency test, not an exhaustive or computer-certified proof of the theorem.

## Proof verification notes
The analytic argument checks the exact zero-flux mass balance, the bounded positive resolvent for \(\mu_p>0\), exclusion of a zero limiting biomass by strict supercriticality, the sign of the scalar Wronskian and of the shooting Jacobian derivative, and the two integrations that recover the nutrient deficit. In particular, the implicit-function theorem is used only after its determinant is shown to be nonzero, and a compactness argument is used to exclude remote positive branches. No nonlinear long-time stability, threshold at an explicit finite attenuation, or independent validation is claimed.
