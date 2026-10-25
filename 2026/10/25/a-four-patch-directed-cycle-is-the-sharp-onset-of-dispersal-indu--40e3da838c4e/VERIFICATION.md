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

# Reproducibility and limits

Run `python verify.py` using only the Python 3 standard library. This checks the dimensionless characteristic equation, the explicit imaginary-frequency branch, the sign and value of the crossing derivative for representative positive parameters, the comparison of the three-patch and four-patch first thresholds, the nontrivial four-patch switch bracket, and the exact half-rate witness. The numerical program was executed successfully and returned `PASS`.

The proof in `RESULT.md` gives exhaustive analytic characterization over the stated dimensions, positive physical parameters and all finite delays. The script does not prove all-parameter statements and is not represented as an independent audit. The argument does not establish the nonlinear type of any Hopf bifurcation or global attractivity. The threshold at equality has neutral linear spectral directions, so no nonlinear stability claim is made there.
