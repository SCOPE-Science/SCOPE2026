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

# Reproduction and limits

Run `python checker.py` with Python 3.8 or later. It requires no external packages or data. The test independently enumerates every edge subset of the labeled graph for n=2 through n=6 and fugacities corresponding to p=1/5, 1/2, and 4/5. It directly computes exact rational covariance matrices and validates all entries against the theoretical formulas; it then multiplies by the independently specified precision matrix and checks the identity matrix entry by entry.

Observed output: `EXACT_OK assertions=2250`.

This enumeration verifies only the finite test domain. For the complete theorem, inspect the four-mode diagonalization, the positivity of A=t-nt^n, and the inequality AB>(n-1)uh^2 in `RESULT.md`; no computational extrapolation is used to establish all n or continuous p.

Independent audit: not performed.
