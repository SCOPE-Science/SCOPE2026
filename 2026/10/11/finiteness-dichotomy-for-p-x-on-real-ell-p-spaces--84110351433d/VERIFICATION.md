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
For finite \(p\ne2\), the verification target is the quotient
\[
Q_p(b)
=
\frac{N_p(b)}{D_p(b)}
\]
for
\[
x=(1,0),
\qquad
y_b=(b,1).
\]
The proof establishes a sign-changing zero of \(D_p\) and a nonzero same-sign numerator on the appropriate side.

For
\[
p>2,
\]
\[
D_p(0)=2-2^{2/p}>0,
\qquad
D_p(-1)<0,
\]
and the numerator is positive at the boundary zero in \((-1,0)\).

For
\[
1\le p<2,
\]
\[
D_p(0)=2-2^{2/p}<0,
\qquad
D_p(1)=2^{2/p}>0,
\]
and the numerator is negative at the boundary zero in \((0,1)\).

For
\[
p=\infty,
\]
\[
N_\infty(b)=1,
\qquad
D_\infty(b)=2-(1-b)^2,
\]
so the pole is exactly at
\[
b=1-\sqrt2.
\]

`verify.py` uses the standard library only. It bisects the sign-changing zero for representative exponents on both sides of \(2\), checks the numerator sign, and confirms quotient values above a large threshold when approaching the zero from the admissible side. It separately checks the exact \(p=\infty\) branch and the Hilbert quotient \(-1\).

The finite exponent sample is a reproducibility check only; the universal quantifiers are proved by the endpoint inequalities in `RESULT.md`.

No independent audit or independent validation has been performed.
