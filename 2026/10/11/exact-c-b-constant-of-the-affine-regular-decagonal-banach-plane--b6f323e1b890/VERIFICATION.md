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
The analytic proof reduces every Birkhoff-orthogonal unit pair, up to the dihedral symmetries of the regular decagon, sign, and symmetry of the objective, to
\[
x=(1,t),
\qquad
-\tan\frac{\pi}{10}\le t\le\tan\frac{\pi}{10},
\qquad
y=\left(0,\sec\frac{\pi}{10}\right).
\]

For this family, the directions of \(x+y\) and \(x-y\) stay in the adjacent facet sectors, so
\[
\|x+y\|
=
\cos\frac{\pi}{5}
+
\sin\frac{\pi}{5}
\left(
\sec\frac{\pi}{10}+t
\right),
\]
\[
\|x-y\|
=
\cos\frac{\pi}{5}
+
\sin\frac{\pi}{5}
\left(
\sec\frac{\pi}{10}-t
\right).
\]
Thus the defining \(C_B\) objective is a positive constant times \(t\), and the maximum occurs at \(t=\tan(\pi/10)\).

`verify.py` symbolically checks the sector endpoints, the ten facet/vertex incidences, the equality-pair norms, and the simplification
\[
\frac14
\left[
\left(\frac{1+\sqrt5}{2}\right)^2
-
(\sqrt5-1)^2
\right]
=
\frac{5\sqrt5-9}{8}.
\]

No finite sampling is used to prove the continuum maximum. No independent audit or independent validation has been performed.
