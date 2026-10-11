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
P_{m,\beta}(z)
=
|z|^{2m}
+
\beta |z|^2\operatorname{Re}z^{2m-2},
\]
direct complex differentiation gives
\[
(P_{m,\beta})_{z\overline z}
=
m^2|z|^{2m-2}
+
\beta(2m-1)\operatorname{Re}z^{2m-2}.
\]
Adding
\[
|z|^{2m+2}
\]
contributes
\[
(m+1)^2|z|^{2m}.
\]
Therefore the Levi entry is positive for
\[
z\ne0
\]
under
\[
\beta<\frac{m^2}{2m-1}.
\]

For
\[
S_t(z,w)=(e^{-t}z,e^{-mt}w),
\]
weighted homogeneity gives the exact identity
\[
\rho(S_t)
=
e^{-2mt}(\rho+1)-1
+
\left(e^{-(2m+2)t}-e^{-2mt}\right)|z|^{2m+2}.
\]
Differentiating at zero yields
\[
-2m(\rho+1)-2|z|^{2m+2},
\]
which is at most
\[
-2m
\]
on the boundary.

At the divisor singularity
\[
p=(0,1),
\]
\[
f_\lambda(S_\tau p)
=
(e^{-m\tau}-1)^2,
\]
so the source's finite-order escape condition is satisfied.

For the resonant supporting-graph case, the negative directions are
\[
\theta_j
=
\frac{\pi}{2m-2}
+
\frac{j\pi}{m-1},
\qquad
0\le j\le2m-3.
\]
Their \(2m\)-th powers form a complete nontrivial root-of-unity orbit and satisfy
\[
\sum_j e^{i2m\theta_j}=0.
\]
Thus a degree-\(2m\) holomorphic correction cannot be positive on every negative direction of
\[
P_{m,\beta}.
\]

These identities verify the family-specific hypotheses needed by the inspected continuity theorem. No numerical computation is used.
