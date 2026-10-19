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

# Mathematical verification

Execute `python verify.py` with `sympy` and `scipy` installed as described in `requirements.txt`.

The program was executed and all its assertions passed. It symbolically checked: conservation of \(H\), exact evolution \(\dot S=-bVW S\), invariance and equality of the two vector fields on \(U=(b/d)VW\), positive nonzero mixed derivative \(b\), and the derivative of the closed expression for \(\int_0^t VW\,ds\). It numerically integrated the higher-order system for three normalized on-/off-surface initial conditions and compared the exact \(S\) formula, and compared the higher-order and pairwise trajectories on the surface at multiple times.

The periodic-orbit existence, exact all-time model equivalence, and asymptotic exponent are proved in `RESULT.md` analytically. Finite numerical checks cannot certify infinite-time assertions, generic parameter coverage, novelty, or independent audit. No independent scientific audit has been performed.
