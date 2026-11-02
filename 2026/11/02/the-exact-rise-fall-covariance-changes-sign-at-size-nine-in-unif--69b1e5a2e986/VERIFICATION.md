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

# Verification of the rise–fall covariance sign boundary

Run `python3 verify.py` with Python 3 and no external packages. The test program checks exact integer coefficient recurrences of two independent rational generating functions through size 240, the derived moment and covariance formulas through size 240, exhaustive enumeration of all 4096 compositions at size 13 (and every smaller size), and strict positivity of the analytic error-bound margin from size 9. A direct run returned `PASS 1218 exact assertions cov(n=8)= -49/16384 cov(n=9)= 335/65536`.

The proof's unbounded step uses a monotone positive linear term dominating a decreasing exponential envelope, with strict verified rational inequality already at size 9. Finite enumeration serves as an implementation check, not a proof for arbitrary sizes. The program does not audit historical priority or independently validate publication claims.
