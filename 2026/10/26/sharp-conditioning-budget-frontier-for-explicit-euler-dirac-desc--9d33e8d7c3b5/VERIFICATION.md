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

Run `python verify.py` with Python 3 and NumPy installed. The checker constructs the full seven-dimensional filled-triangle Dirac Euler matrix, verifies the chain relation, evaluates actual induced singular-value norms in five coupling/complex scenarios, compares them against the proved formulas across multiple weight budgets and time steps, and checks the exact stationary optimization formulas and their one-sided inequalities. All included assertions passed when executed on the packaged source.

The exact constants in the triangle example were independently simplified symbolically: \(K_{\mathrm{crit}}=256/9\), \(h_*=209/817\), and the minimal norm \(456\sqrt3/817\). Symbolic stationarity and optimal-norm identities were checked by substitution into their defining polynomial relations. Finite floating-point checks are diagnostics, not a proof for all chain complexes, all stepsizes, or the strict equality boundary; those statements are proved in `RESULT.md`.

No claims are made about non-isotropic or nonlinear functions, general SPD degree weights, floating-point robustness of an implementation, statistical optimization, or independent audit.
