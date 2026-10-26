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

The analytic proof is in `RESULT.md`. Running `python verify_bipartite.py` with NumPy and SciPy performs a separate direct matrix-exponential and linear-programming comparison for all \(1\le a,b\le7\) at the five listed times. The script also checks the explicit, time-independent norming potential and critical-peak identities in selected asymmetric examples. The maximum numerical difference in the principal transport tests is expected below \(10^{-11}\).

The script is a finite consistency check, not a proof for untested graph sizes or a certificate of novelty. The general transport construction, equality case, and derivative argument supply the all-integers proof. Only the stated graph class and norms are validated.
