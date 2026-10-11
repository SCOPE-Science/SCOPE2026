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

For the central rank-one square, the source Hodge table gives
\[
\dim E_1^{0,1}=2,
\qquad
\dim E_1^{1,0}=1,
\qquad
E_1^{2,0}=0.
\]
The source topology gives
\[
b_1=2.
\]

The class in
\[
E_1^{1,0}
\]
survives. Its only incoming first differential is induced by \(\partial\) on constants and is zero. Its first outgoing target is
\[
E_1^{2,0}=0,
\]
and later possible outgoing bidegrees have negative antiholomorphic degree. Therefore
\[
\dim E_\infty^{1,0}=1.
\]

Convergence in total degree one gives
\[
\dim E_\infty^{0,1}=2-1=1.
\]
No differential enters bidegree \((0,1)\). The only higher outgoing map after \(d_1\) could be
\[
d_2:E_2^{0,1}\to E_2^{2,0},
\]
but its target is zero. Hence
\[
E_\infty^{0,1}
=
\ker\left(
d_1:E_1^{0,1}\to E_1^{1,1}
\right).
\]
Its kernel dimension is one inside a two-dimensional domain, so
\[
\operatorname{rank}d_1^{0,1}=1.
\]

For every punctured fiber, the source proves degeneration at \(E_1\), hence the same differential has rank zero there.

No numerical computation, finite enumeration, or assumption about uncomputed higher differentials is used.
