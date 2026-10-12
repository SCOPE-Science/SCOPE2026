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
The standalone script `verify_wiener_truncation.py` uses high-precision `mpmath` to evaluate the source's continuous Brownian-range CDF series, whose integer differences define the discrete PMF.

It replays the finite integer support on the source's stated market intervals
\[
[2,8]\times[1,7],\qquad T=1,
\]
and returns published total mass
\[
86.7321789530702265665\ldots,
\]
published mass at the lower-left atom
\[
65.7651669084577193031\ldots,
\]
and corrected conditional mass at that atom
\[
0.7582556751403938133\ldots.
\]

At \(T=0.1\) on the marginal interval \([0,1]\), it reproduces the published zero-cell value \(158.70343733965314\ldots\), compared with correct conditional value \(0.99373839400918\ldots\).

The checker compares 80-term and 100-term values and explicitly bounds the positive omitted series tail. These numerical checks supplement but do not replace the exact telescoping proof and the analytic Brownian scaling/reflection argument. No claim about other computational implementations is made.
