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

# Verification record

The analytical theorem is established by the six numbered proof steps in `RESULT.md`. The program `verify_limit.py` is standalone and requires Python 3 standard library only. Running `python3 verify_limit.py` produced the exact output `PASS: 53 deterministic finite-step and integral checks` for the delivered code.

The checker uses legal finite-step probabilities \(p_k=c/(k+2c)\), whose leading coefficient is \(c/k\) and which are strictly between zero and one for each positive step. It updates exact finite-time moment recurrences through fourth order and an independent exact cross-moment recursion. For specified coefficients and observation times, their normalized outputs are compared with the beta moments and analytic limiting covariance. A separate Simpson quadrature tests selected integral identities and continuous density normalizations. The sampled convergence and numerical quadratures do not establish weak convergence, prove tail behavior for all \(c>0\), or constitute a certificate of scientific originality.

The independence, limiting-coefficient, and initial-state hypotheses are essential for the stated claim. No simultaneous \(N,t\to\infty\) bound is proved. The limiting beta density for the continuum \(c/t\) telegraph model is already in Garra and Orsingher; the asserted result concerns discrete functional convergence and its multitime aging consequences.
