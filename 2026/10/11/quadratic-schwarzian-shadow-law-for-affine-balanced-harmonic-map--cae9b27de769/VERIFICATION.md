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
Q
=
P_H-P_F
=
\frac{\overline\Omega\,\Omega'}{1-|\Omega|^2}.
\]
Then
\[
S_H-S_F
=
Q_z-P_FQ-\frac12Q^2
=
\frac{\overline\Omega\,\Omega''}{1-|\Omega|^2}
-P_FQ+\frac12Q^2.
\]
This identity accounts for every term in the Schwarzian difference.

For an analytic self-map \(\psi\) of the disk, conjugating the source point to zero and applying Schwarz--Pick twice gives
\[
(1-|z|^2)^2|\psi''(z)|
\le
2(1+|z|)(1-|\psi(z)|^2)
\le
4(1-|\psi(z)|^2).
\]
With
\[
\Omega=k\psi,
\]
this yields
\[
(1-|z|^2)^2
\frac{|\overline\Omega\Omega''|}{1-|\Omega|^2}
\le
4k^2\frac{t(1-t^2)}{1-k^2t^2},
\qquad
t=|\psi(z)|.
\]
Using
\[
\max_{0\le t\le1}t(1-t^2)=\frac{2}{3\sqrt3}
\]
gives the first term in the upper bound. The other two terms follow from the source estimate
\[
\|Q\|\le\mathcal C(k).
\]

For the lower witness
\[
F_k(z)=z+\frac{k}{3}\overline z^{\,3},
\qquad
\Omega_k(z)=kz^2,
\]
one has
\[
Q(z)=\frac{2k^2z\overline z^{\,2}}{1-k^2|z|^4}
\]
and
\[
S_H-S_{F_k}
=
\frac{2k^2\overline z^{\,2}}{1-k^2|z|^4}
+
\frac{6k^4z^2\overline z^{\,4}}{(1-k^2|z|^4)^2}.
\]
At
\[
|z|^2=1/3,
\]
the weighted modulus is
\[
\frac8{27}k^2+O(k^4).
\]
Also
\[
\|P_{F_k}\|
\le
\frac{2k^2}{1-k^2},
\]
so this witness lies in every fixed positive pre-Schwarzian budget for sufficiently small \(k\).

For \(M=0\),
\[
(P_F)_{\overline z}
=-\frac{|\Omega'|^2}{(1-|\Omega|^2)^2}
\]
forces \(\Omega\) to be constant. Balancing makes that constant zero, hence the mapping is affine analytic and the Schwarzian gap vanishes.

All checks are symbolic analytic identities; no numerical certificate or finite experiment is required.
