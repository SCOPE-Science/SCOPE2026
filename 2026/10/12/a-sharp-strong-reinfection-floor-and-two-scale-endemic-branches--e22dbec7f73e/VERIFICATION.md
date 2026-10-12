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

From the extracted directory run `python3 verify.py`; the program requires only the Python standard library. It performs exact Fraction checks of the reconstructed five-state stationarity equations and the scalar infected equation at rational test points; the reproduction threshold constants \(K,H,c,L\), and the leading fold coefficients; the cubic numerator's leading and constant terms; and the two opposite sign intervals certifying two positive equilibria at \(B=100\). A passing execution prints `VERIFY_OK`.

The proof of the singular large-reinfection threshold is not a consequence of finite computations. Its uniform localization, strict concavity at the rescaled fold, and implicit-function-theorem steps appear explicitly in `RESULT.md`. Computations do not certify an exhaustive literature search, global stability of trajectories, or uniform estimates in varying demographic parameters.
