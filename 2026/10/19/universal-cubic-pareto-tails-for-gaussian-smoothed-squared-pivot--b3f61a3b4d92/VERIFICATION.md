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

Run `python reproduce.py` using Python 3, NumPy and SciPy. The executable checks 175 realized-matrix oriented-minor identities and simulates 2,000,000 independent real Gaussian 2-by-2 matrices, 1,200,000 2-by-3 matrices, and 900,000 3-by-3 matrices, sampling each exact pivot by normalized entry-square weights. It compares finite-sample scaled tail frequencies with the explicit analytic constants and squared residual means with the previously established formula. The 2-by-2 coefficient also has an independent symbolic special-value check.

Observed run: oriented-minor identities 175 PASS; analytic tail constants respectively 0.387008828552, 1.06384608107, 2.81995680896; at threshold 11, empirical scaled estimates respectively 0.391314, 1.0947475, 2.92228444444. Squared means simulated 1.32353563568, 3.01039186165, 6.6435752574, versus exact 1.33333333333, 3, 6.54545454545. All programmed finite tolerances passed. Simulation does not establish tail limits, integrability thresholds or the noncentral generality; these rely on the analytic proof in RESULT.md. This document carries no independent audit evidence.
