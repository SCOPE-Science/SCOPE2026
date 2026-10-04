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

Write
\[
f(z)=c+\sum_{n\ge1}a_nz^n+\sum_{n\ge1}b_n\overline z^{\,n}.
\]
For the normalized radial weight,
\[
\beta_n
=
\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)},
\qquad
\beta_0=1,
\]
and therefore
\[
\|f\|_{a^2_\alpha}^2
=
|c|^2+\sum_{n\ge1}\beta_n(|a_n|^2+|b_n|^2).
\]

For every \(|\zeta|=1\), define
\[
F_\zeta(w)
=
c+\sum_{n\ge1}(a_n\zeta^n+b_n\overline\zeta^{\,n})w^n.
\]
Then, identically for \(0\le r<1\),
\[
F_\zeta(r)=f(r\zeta).
\]
Its exact analytic Bergman norm is
\[
\|F_\zeta\|_{A^2_\alpha}^2
=
|c|^2+\sum_{n\ge1}\beta_n
|a_n\zeta^n+b_n\overline\zeta^{\,n}|^2.
\]
Using
\[
|u+v|^2\le2(|u|^2+|v|^2)
\]
gives
\[
\|F_\zeta\|_{A^2_\alpha}^2
\le
2\|f\|_{a^2_\alpha}^2-|f(0)|^2.
\]

The inspected analytic Riesz–Fejér theorem gives
\[
\int_0^1|F_\zeta(r)|^2(1-r)^{\alpha+1}\,dr
\le
\lambda_\alpha\|F_\zeta\|_{A^2_\alpha}^2.
\]
Substitution proves the ray claim. Since
\[
F_\zeta(-r)=f(-r\zeta),
\]
the two half-rays give the stated diameter inequality.

Boundary checks: if \(f\) is analytic, then the shadow is just the rotated analytic function and the factor two disappears. If \(f(z)=z-\overline z\) and \(\zeta=1\), then the shadow is zero and the ray trace vanishes exactly.

No numerical experiment, finite truncation, or limiting inference is used in the proof.
