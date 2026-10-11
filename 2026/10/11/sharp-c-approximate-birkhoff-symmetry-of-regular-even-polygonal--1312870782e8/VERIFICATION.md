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
Put
\[
\alpha=\frac{\pi}{N},
\qquad
c=\cos\alpha,
\qquad
s=\sin\alpha.
\]
For the reference edge,
\[
x=(c,t),
\qquad
-s<t<s,
\]
Birkhoff--James orthogonality forces the second vector onto the perpendicular diameter.

If
\[
4\mid N,
\]
that diameter meets the sphere at an edge midpoint, so the reverse support residual is
\[
\frac{|t|}{c}<\tan\alpha.
\]
At a vertex
\[
x=(c,s),
\]
the complete Birkhoff sector consists of two half-edges around the perpendicular vertex. Their smooth support functionals evaluate \(x\) as
\[
\tan\alpha
\quad\text{and}\quad
-\tan\alpha.
\]
The endpoint edge midpoint therefore gives the sharp residual
\[
\tan\alpha.
\]

If
\[
N\equiv2\pmod4,
\]
the perpendicular to a smooth edge is a vertex whose two support values on \(x\) are
\[
s+t
\quad\text{and}\quad
t-s,
\]
which straddle zero. For a vertex \(x\), its Birkhoff sector is one edge with a supporting functional perpendicular to \(x\). Hence every reverse residual is zero.

The bundled `verify.py` independently enumerates sampled boundary pairs for all even \(N\) from \(6\) through \(80\), detects Birkhoff--James orthogonality from norming facets, and checks the exact predicted maxima numerically. The finite enumeration is supplementary to the analytic support-functional proof.

No independent audit or independent validation has been performed.
