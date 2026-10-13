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
The variance identity was checked directly from the cumulant-generating function \(\log f_X(e^t)\). The conjugate-pair contribution simplifies exactly to
\[
q(r,c)=\frac{r(2r-(r^2+1)c)}{(r^2-2rc+1)^2}.
\]
The proof then uses the exact identities
\[
q(r,c)=q(r^{-1},c),
\]
\[
\frac{\partial q}{\partial r}=
\frac{(r-1)(r+1)(2c^2r+c(r^2+1)-4r)}{(r^2-2rc+1)^3},
\]
and
\[
\frac{\partial q}{\partial c}=
-\frac{r(r^4-6r^2+1+2cr(r^2+1))}{(r^2-2rc+1)^3}.
\]
For \(r\ge1\) and \(-1\le c\le0\), the first derivative is nonpositive. The numerator controlling the sign of the second derivative is affine and strictly increasing in \(c\), so any interior stationary point in \(c\) is a maximum. These observations exhaust the compact rectangle after inversion symmetry and prove the endpoint minimum.

The sharpness examples were checked from their PGFs: the first is binomial with all zeros \(-R\), and the second, for even degree, is the law of twice a binomial variable with all zeros \(\pm iR\). The crossover equation reduces to \((R+R^{-1})^2-2(R+R^{-1})-4=0\), giving the unique stated threshold for \(R\ge1\).

No finite numerical experiment is used to prove the quantified statement. The unresolved scope is the sharp constant for sector angles strictly below \(\pi/2\), and exact attainment of the imaginary-axis branch in odd degree is not claimed.
