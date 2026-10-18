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

# Reproducible checks and limits

Run `python check.py` using SymPy, NumPy and SciPy. The program verifies the exact mass normalization, all fifteen symbolic stationary balance equations, each stated rational covariance and the rate-zero / high-rate limiting expressions. It independently solves the complete stationary generator for \(N=4,5,6,7\) and rates \(r=0.01,0.5,1,20\), checking agreement with the resolvent numerical solution in the four-site case and high/low sign trends for separated sites. The program prints the unique positive four-site sign-crossing root.

The all-size claims are proved by the analytic renewal identity and two-step generator expansion; finite computations only guard against algebraic and rate-convention errors and do not certify all ring sizes. The source-literature originality review is not an independent audit. No external validation or claim of formal certification is made.
