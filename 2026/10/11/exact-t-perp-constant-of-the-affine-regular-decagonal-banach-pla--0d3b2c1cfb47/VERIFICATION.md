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
The verification target is
\[
\sup_{x,y\in S_{X_{10}},\ x\perp_B y}
N_{10}(x+y)N_{10}(2x-y)
=
\frac{2+5\sqrt5}{4}.
\]

`verify.py` uses exact rational-pair arithmetic for \(\mathbb Q(\sqrt5)\). It reconstructs the ten signed facets and ten vertices of the unit decagon and verifies all incidences.

For every smooth-edge point \(x\), the unique norming facet forces \(y\) to one of the two unit intersections with its kernel. The checker treats all ten edges and both signs. It partitions the edge parameter wherever either norm envelope changes active facet, then maximizes the resulting quadratic products exactly. The certified smooth-edge maximum is
\[
\frac{63-5\sqrt5}{16}.
\]

For every vertex \(x\), the checker imposes the exact sign-straddling condition for the two adjacent support functionals. Across all unit edges this yields twenty nonempty allowed subsegments. The same affine-envelope partition and exact quadratic maximization gives
\[
\frac{2+5\sqrt5}{4}.
\]

Finally the checker verifies the explicit maximizing pair, its Birkhoff sign condition, the two factor norms
\[
\frac{3\sqrt5-1}{4}
\quad\text{and}\quad
\frac{7+\sqrt5}{4},
\]
and their product. All algebraic comparisons and ordering decisions are exact in \(\mathbb Q(\sqrt5)\); no floating-point arithmetic is used by the certificate. No independent audit or independent validation has been performed.
