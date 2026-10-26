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
Run `python3 verify.py` with Python 3 standard library. The program enumerates every ball-to-box assignment for \(2\le m\le5\), \(2\le n\le6\), compares independent exact rational covariance formulas, checks sign blocks on \(m\le80\), and tests the critical asymptotic at large box counts. The proof in RESULT.md, not the finite script, establishes the all-parameter theorem. Independent audit: not performed.
