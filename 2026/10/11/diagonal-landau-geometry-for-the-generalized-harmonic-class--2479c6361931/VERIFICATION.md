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

On the positive diagonal
\[
\delta=\gamma>0,
\]
the defining differential inequality has a common factor \(\gamma\), so division by that factor gives the parameter-free class
\[
\operatorname{Re}\!\left(
\frac{h(z)}z+h'(z)
\right)
>
\left|
\frac{g(z)}z+g'(z)
\right|.
\]

The published coefficient estimate reduces exactly to
\[
|a_n|+|b_n|
\le
\frac4{n+1}.
\]

For a bounded harmonic map with
\[
J_f(0)=1,
\]
the standard harmonic Schwarz estimate gives
\[
\lambda_f(0)\ge\frac{\pi}{4M}.
\]
The line-segment estimate therefore reduces to the positive-term series
\[
S(r)
=
4\sum_{n=2}^{\infty}\frac{n}{n+1}r^{n-1}.
\]
Direct summation gives
\[
S(r)
=
4\left(
\frac{r}{1-r}
+\frac1r
+\frac12
+\frac{\log(1-r)}{r^2}
\right).
\]
Its Taylor expansion is
\[
S(r)
=
\frac83r
+
3r^2
+
\frac{16}{5}r^3
+
\frac{10}{3}r^4
+
O(r^5).
\]

The covering antiderivative is
\[
T(r)
=
4\sum_{n=2}^{\infty}\frac{r^n}{n+1}
=
-\frac{4\log(1-r)}r-4-2r,
\]
and
\[
T'(r)=S(r).
\]
Hence, at the unique root
\[
S(\rho_M)=\frac{\pi}{4M},
\]
the covering quantity is
\[
R_M
=
\frac{\pi\rho_M}{4M}-T(\rho_M)
=
\int_0^{\rho_M}
\left(
\frac{\pi}{4M}-S(t)
\right)dt
>0.
\]

Since
\[
S(r)=\frac83r+O(r^2),
\]
one has
\[
\rho_M
\sim
\frac{3\pi}{32M}.
\]
Since
\[
T(r)=\frac43r^2+O(r^3),
\]
substitution gives
\[
R_M
\sim
\frac{3\pi^2}{256M^2}.
\]

The identities were replayed from the displayed series and independently checked coefficientwise. No finite sampling or numerical extrapolation is used to prove the theorem.
