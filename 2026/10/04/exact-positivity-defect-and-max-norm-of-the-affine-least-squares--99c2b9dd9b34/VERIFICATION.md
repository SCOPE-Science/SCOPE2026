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
The verification artifact uses exact rational arithmetic.

For every \(1\le d\le50\), it constructs the \((d+1)\times(d+1)\) barycentric Gram matrix
\[
G_{ij}=\frac{1+\delta_{ij}}{(d+1)(d+2)}
\]
after normalizing \(|T|=1\), and checks the stated inverse by exact matrix multiplication. It verifies kernel normalization from the barycentric first moments.

The vertex negative-mass integral is evaluated by expanding \((1-t)^{d-1}\) exactly and integrating term by term over \(0\le t\le1/(d+2)\). The result is checked against
\[
(d+1)\left(\frac{d+1}{d+2}\right)^d-1.
\]
Low-dimensional constants and the relation between negative mass and the \(L^\infty\) operator norm are also checked exactly.

The checker does not replace the convexity argument that proves vertex optimality over all evaluation points. That infinite-family step is proved analytically in RESULT.md.
