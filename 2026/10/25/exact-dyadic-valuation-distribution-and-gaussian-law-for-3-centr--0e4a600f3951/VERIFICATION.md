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

From the package root, execute `python3 verify.py` with Python 3's standard library. The checker uses the independently derived recurrence for the valuations of the original coefficients to count every index in complete blocks \(0\le n<4^L\) for \(0\le L\le7\), and matches each entire polynomial against the transfer matrix. It checks the closed formulas for exact rational means and variances and the characteristic polynomial/eigenvalue derivatives.

All checked integer arithmetic and moments are exact. These finitely many cases are not a proof of the unrestricted formulas, and numerical agreement does not independently establish the Gaussian limit. The general proofs are in `RESULT.md`. Independent audit: not performed.
