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

The theorem is verified symbolically.

For the algebra with \(e_1^2=e_2\) and \(e_2^2=e_1+d e_2\), the structure matrix has determinant \(-1\), so the square spans the whole algebra in every characteristic. For \(x=a e_1+b e_2\), direct expansion gives
\[
x^2=b^2e_1+(a^2+d b^2)e_2.
\]
Thus \(x^2=x\) forces \(a=b^2\). If \(b=0\), then \(x=0\); otherwise the second coordinate equation is equivalent to
\[
d=b^{-1}-b^2.
\]
Hence a parameter outside the image of \(K^\times\to K\), \(b\mapsto b^{-1}-b^2\), eliminates every non-zero idempotent. The image has at most \(q-1\) elements and \(K\) has \(q\), so such a parameter always exists.

The dimension lower bound is independent: a one-dimensional algebra satisfies \(e^2=\lambda e\); \(\lambda=0\) is solvable, while \(\lambda\ne0\) gives the non-zero idempotent \(\lambda^{-1}e\).

Boundary checks: over \(\mathbb F_2\), \(d=1\) is omitted by the parameter map; over \(\mathbb F_3\), \(d=2\) is omitted. These examples are checks only and are not used to infer the general theorem.
