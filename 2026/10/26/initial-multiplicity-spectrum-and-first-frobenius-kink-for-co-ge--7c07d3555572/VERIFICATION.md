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

# Reproducible arithmetic checks

Run `python3 verify.py` with Python 3.8 or newer; no additional packages are needed. The script constructs the generating-function coefficients by dynamic programming separately for the three denominations, and independently computes the fundamental-rectangle layer sum for every integer in its finite test window.

For every coprime pair \(2\le a\le40\), \(a<b\le45\), it checks the complete equality of two denumerant calculations and the formulas for zero representations and all multiplicities up to \(k=a+1\), including each exact level count, cumulative count, and last integer below the threshold. The tested window through \(3ab+a+b\) exceeds every potential low-multiplicity layer under the theorem's proof.

Actual result:

`CERTIFICATE_OK pairs=575 exact_denumerant_values=952360`

These are finite corroborations. The theorem for all coprime pairs depends on the explicit fundamental rectangle, layer-exclusion proof, and exact maximum comparisons, not on computational extrapolation. There has been no independent mathematical audit.
