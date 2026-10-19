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

# Reproducible checks

Run `python verify.py` with Python 3, NumPy, SciPy, and SymPy available. The script takes no inputs and uses a deterministic pseudorandom seed. The output observed on a clean replay was `PASS 4038 assertion groups`.

The test reconstructs one thousand independently specified real-symmetric \(3\times3\) matrices and checks the two smallest eigenvalues and the original-system nullspace residual against the exact formulas. It independently evaluates conditional means with Gaussian quadrature and tests exact symbolic moment constants and the weak-perturbation correlation.

The proof establishes the all-amplitude strict covariance sign analytically. The finite tests merely check implementation and numerical consistency; they do not prove the universal assertion. This calculation has not undergone independent audit or validation.
