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
The universal threshold is proved analytically.

For two Lanczos steps,
\[
y_2(t)=p(A)b
\]
with \(p\) the linear interpolant of \(e^{-t\lambda}\) at the two Ritz values. If
\[
\mu\le\theta_1<\theta_2\le L,
\]
then for every \(\lambda\ge\theta_2\),
\[
p(\lambda)
=
e^{-t\theta_1}
-t e^{-t\xi}(\lambda-\theta_1)
\ge
e^{-t\theta_1}
\left[
1-t(\lambda-\theta_1)
\right]
\]
for some \(\xi\in(\theta_1,\theta_2)\). Hence
\[
t(L-\mu)\le1
\]
is sufficient.

For sharpness, on
\[
A_r
=
\operatorname{diag}
\left(
\mu,\,
\mu+r(L-\mu),\,
L
\right)
\]
the limiting two-point interpolation polynomial satisfies
\[
p_0(L)
=
e^{-t\mu}
\left[
1-\frac{1-e^{-t(L-\mu)r}}{r}
\right].
\]
As \(r\downarrow0\), the bracket tends to
\[
1-t(L-\mu).
\]
Thus every value above one yields a negative limiting upper-endpoint polynomial value, and continuity gives a strictly positive three-component start with a negative Lanczos component.

The embedded `verify.py` reconstructs the explicit witness
\[
A=\operatorname{diag}\!\left(1,\frac65,3\right),
\qquad
b=\left(1,1,\frac1{100}\right)^{\mathsf T},
\qquad
t=1.
\]
It computes the \(2\times2\) Lanczos matrix from the recurrence and evaluates its exponential with a closed symmetric-matrix formula using high-precision decimal arithmetic. The verified third component is negative, while the exact exponential component is positive.

Finite computation corroborates the witness only; it is not used to prove the all-dimension statement.

Unproved limits include higher Krylov dimensions, nonsymmetric Arnoldi, rational or restarted Krylov methods, finite-precision loss of orthogonality, and non-diagonal matrices.
