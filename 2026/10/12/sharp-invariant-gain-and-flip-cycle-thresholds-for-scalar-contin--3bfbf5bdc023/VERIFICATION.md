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
# Reproducibility and verification

From this directory run `python -m pip install -r requirements.txt` as needed and then `python verify.py`. The latter uses SymPy exact radicals and rational polynomial simplifications; it prints `PASS exact scalar LQR gradients, normalization, two-cycle, multipliers, critical thresholds, rational witness` on success. The checked identities include the gradient of the gain objective, the conjugacy to the normalized inverse-square update, the critical positive-minimum formula, the two-cycle parameterization, its derivative multiplier, the exact critical root, and a stable radical witness. These are checks of the cited mathematical identities from the local package, not exhaustive searches of real parameters or independent proof/certification. The universal conclusions follow from the analytic inequalities and monotonicity in `RESULT.md`.

The nonhyperbolic cases and the global basin problem are not covered. No external auditor has assessed this package.
