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

# Verification and reproducibility

Run `python verify.py` with Python 3; the script uses only the standard library. It constructs all fifteen vertices of the outer polytope with exact rational arithmetic and checks the unique maximum, second-largest vertex value, \(q_0\), \(D^2\), \(t_*\), the rational gap, and the final upper bound. It also checks the exact characteristic-polynomial data for the displayed integer matrix and the rational endpoint comparisons used in the proof.

The proof of the operator-norm separation uses Weyl's eigenvalue inequality and the displayed Frobenius-norm estimate. The result does not rely on a finite experiment for any universal claim. The matrix criterion is a necessary condition for APPT spectra, not a sufficient characterization used in the proof. The bound is non-sharp. No independent audit or external validation is claimed.
