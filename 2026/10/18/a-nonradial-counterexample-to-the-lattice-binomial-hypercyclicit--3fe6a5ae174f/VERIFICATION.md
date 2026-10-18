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

# Verification and limitations
The accompanying standalone `verify.py` evaluates the four-term binomial convolution by two explicit constructions and checks, for every integer \(0\le n\le200\), the exact identity
\[
\sum_{r=0}^{n+3}c_{n,r}^2
=\frac{120\binom{2n}{n}}{(n+1)(n+2)(n+3)}.
\]
It also checks the cancellation \(\sum_r c_{n,r}=0\), a Cauchy–Schwarz norm inequality, and the central-column weight identity at selected larger orders.

The proof of the result for every \(n\) is analytic: Parseval, Euler's beta formula, Stirling's central-binomial asymptotic, and Hoeffding's tail estimate. The finite checker is **not** a proof of the asymptotic limit, an exhaustive proof of nonhypercyclicity, or evidence of independent certification. No classification of arbitrary nonradial weights is asserted.
