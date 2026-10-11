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
The arbitrary-parameter proof is given in `RESULT.md`.

Critical checks:
- the source vertex set is one exceptional basis \(v_0\) plus all \(r(n-r)\) one-for-one exchange vertices;
- symmetry and uniqueness force a center
  \[
  c(q)=\left(1-\frac qr\right)\mathbf1_A+\frac q{n-r}\mathbf1_B;
  \]
- with \(a=n/(r(n-r))\), the two orbit squared distances are
  \[
  d_0(q)^2=aq^2,
  \qquad
  d_1(q)^2=2+aq^2-2aq;
  \]
- the quadratics cross at \(q=r(n-r)/n\);
- if \(r(n-r)\le n\), this crossing occurs before the exchange-orbit minimum and yields
  \[
  R^2=\frac{r(n-r)}n;
  \]
- if \(r(n-r)\ge n\), the exchange-orbit minimum \(q=1\) is optimal and yields
  \[
  R^2=2-\frac{n}{r(n-r)};
  \]
- the contact barycenter identities certify global minimality, and the two orbit distances give the complete contact phase.

`verify.py` constructs all vertices for \(2\le n\le30\) and every rank, checks the closed centers, radii, and contact sets directly, and independently minimizes the scalar max-of-quadratics objective numerically. Finite computation is corroborative only and does not assess originality.
