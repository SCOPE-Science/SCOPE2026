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

The included `verify_singleton.py` uses Python 3 standard-library arithmetic only. Run `python3 verify_singleton.py` from the directory containing this file. It enumerates all \((n-1)!\) recursive parent sequences and \(2^n\) site assignments for each \(n\le6\), at five exact rational retention probabilities; every probability and moment in this enumeration is a rational number. It then checks rational evaluations of the Gaussian covariance integral and numerical second-moment recurrences through \(n=3001\).

Actual output: `PASS: 180 independent exact/limit assertions; all n <= 6, five rational retention parameters; n=3001 moment recurrences.` The numerical large-size comparisons are tolerance checks only. The infinite-size covariance and central limit theorem are proved analytically in `RESULT.md`, independently of finite-size enumeration. No external audit or independent validation has occurred.
