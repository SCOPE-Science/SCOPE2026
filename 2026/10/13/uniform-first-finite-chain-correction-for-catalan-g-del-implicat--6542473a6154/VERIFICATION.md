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

# Reproducibility and mathematical limits

Run `python3 verify.py` from this directory. The script uses only the Python 3 standard library. Its final line is `VERIFY_OK`; it evaluates critical-radical derivative products at every cut for \(m=2,3,4,5,10,20,50,100,200,500,1000,2000\), compares their corrected asymptotics, and separately recomputes finite truth-table counts from the Catalan split recurrence for \(m=2,3,4,5,6\), \(n=1,\ldots,8\). The error diagnostic is \(m^2\) times the maximum cutwise absolute error, not a proved global upper bound.

The analytic certificate is the proof in `RESULT.md`: the uniform discrete expansion of \(X_j=u_j^2\), a uniform second-order logarithmic expansion, and finite-interval Euler summation. Numerical verification is a finite check; it cannot certify all chain sizes or prove the asymptotic remainder. The order of limits is essential: fixed chain \(m\), bracketed-variable number \(n\to\infty\), then \(m\to\infty\). Published exact probability product and leading limit are treated as prior results, not as new discoveries. No independent mathematical review has been performed.
