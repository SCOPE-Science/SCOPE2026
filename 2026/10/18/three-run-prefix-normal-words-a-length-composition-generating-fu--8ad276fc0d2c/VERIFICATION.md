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

Execute `python3 verify.py` with Python 3 and no third-party packages. The script independently tests the run inequalities by direct sliding-window factor counting, enumerates all positive run-parameter tuples for lengths \(5\) through \(26\), and computes the bivariate rational-function coefficients using integer recurrence inversion. Successful execution prints a `VERIFY_OK` line plus selected length/count samples.

The length-\(26\) cutoff is a finite check, not a computational proof of a general identity. The proof of the complete claim is the gap-window and generating-function argument in `RESULT.md`. Independent external review has not occurred.
