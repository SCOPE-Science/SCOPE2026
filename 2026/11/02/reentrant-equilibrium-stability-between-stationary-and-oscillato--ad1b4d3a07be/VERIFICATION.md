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

Execute `python verification.py` with Python 3, SymPy, NumPy and SciPy installed. The script reconstructs the exact dispersion polynomial from the actual four-component matrix, verifies the quartic Hurwitz determinants by symbolic identities, checks rational inequalities separating the three thresholds, and proves the sign of the derivative numerator of the higher-mode oscillatory threshold on \(t\ge2\).

The disk separation \(\kappa_2=(j'_{2,1}/j'_{1,1})^2>5/4\) is a classical fact following from the Bessel derivative-zero ordering; the script additionally compares these zeros against coarse numerical brackets. Sample eigenspectra corroborate the predicted stable–unstable–stable–unstable sequence but are **not** used as an exhaustive spectral argument.

At the three critical strengths the equilibria are nonhyperbolic. The computation does not prove existence of patterned states, nonlinear bifurcation branches or global attraction. Analytic proof steps and exact quantifiers appear in `RESULT.md`.
