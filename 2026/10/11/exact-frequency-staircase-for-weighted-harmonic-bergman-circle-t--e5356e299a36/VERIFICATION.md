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

For
\[
f(z)=c_0+\sum_{n\ge1}(c_nz^n+d_n\overline z^n),
\]
orthogonality gives
\[
I_\alpha(f)
=
B(1,\alpha+1)|c_0|^2
+
\sum_{n\ge1}
B(n+1,\alpha+1)
\left(
|c_n|^2+|d_n|^2
\right)
\]
and
\[
J_{\alpha,r}(f)
=
2\pi r(1-r^2)^{\alpha+1}
\left[
|c_0|^2+
\sum_{n\ge1}
r^{2n}
\left(
|c_n|^2+|d_n|^2
\right)
\right].
\]

Thus the optimal coefficient is the largest diagonal ratio
\[
2\pi r(1-r^2)^{\alpha+1}
\max_{n\ge0}
\frac{r^{2n}}{B(n+1,\alpha+1)}.
\]

Writing
\[
T_n=\frac{r^{2n}}{B(n+1,\alpha+1)},
\]
the beta recurrence gives
\[
\frac{T_{n+1}}{T_n}
=
r^2\frac{n+\alpha+2}{n+1}.
\]
Hence the sequence increases until
\[
n+1
\]
crosses
\[
s_{\alpha,r}
=
\frac{(\alpha+1)r^2}{1-r^2},
\]
with exactly one adjacent tie when this number is an integer.

The complete equality space is therefore the direct sum of the maximizing harmonic Fourier eigenspaces. Solving
\[
s_{\alpha,r}=m
\]
gives
\[
r_m^2=\frac{m}{m+\alpha+1}.
\]

For the source-normalized norm,
\[
\|f\|_{a_\alpha^2}^2=(\alpha+1)I_\alpha(f).
\]
When the constant mode is maximal,
\[
\frac{C_\alpha(r)}{2\pi r}
=
(1-r^2)^{\alpha+1},
\]
so the source coefficient is approached as
\[
r\downarrow0.
\]

No numerical computation or finite enumeration is used.
