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

The standalone `verify_tail.py` uses the Python standard library. Executing `python3 verify_tail.py` gave `PASS: 319 independent finite assertions`, with two convergent envelope coefficients independently computed as `1.159391053821` and `1.693211347383` for the indicated parameter example. The check uses finite binary reset-factor trees, a finite geometric-mixture distribution, product truncation, explicit two-sided Laplace convolution tails and rigorous analytic remainder bounds (numerically with floating-point tolerances). All infinite statements, including the stationary construction, conditional exponential moments, sharp equality cases and exact limiting asymptotic, require and have the written mathematical proof; the executable only checks representative finite cases.
