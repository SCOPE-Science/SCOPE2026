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

# Reproducibility

Run \(\texttt{python3 artifacts/verify.py}\) from the package root with any standard Python 3 environment. No nonstandard modules, external files, network access, or random seeds are required.

The checker separately propagates the occupied-bin probability vector for each definite photon number, mixes photon-number weights using a finite truncation whose omitted probability mass is checked, and calculates the click mean and variance without calling the analytic generating function. It then compares to the closed analytical click formula. Other checks reconstruct the strict fixed-order cutoff and its monotonicity, and evaluate the near-ceiling optimum in logarithmic arithmetic for six decreasing gaps to avoid underflow. Expected output begins \(\texttt{VERIFY_OK}\) and reports 240 independent click distributions, 120 cutoff identities, and six essential-limit grids.

These are finite corroborations only. The all-order thermal ceiling, strict boundary cases, optimizer existence and sharp near-ceiling exponent are proved analytically in the proof text; the checker does not certify absence of an earlier equivalent theorem.
