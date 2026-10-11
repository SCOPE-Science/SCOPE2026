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
Put \(r=2-\sqrt3\). After reducing one unit vector to the reference edge, the six direct relative-edge certificates are
\[
2,\quad 2-rd,\quad \frac{4-d}{\sqrt3},\quad 1+\sqrt3-d,\quad 4-\sqrt3 d,\quad (2+\sqrt3)(2-d).
\]
Their pointwise minimum on \([0,2]\) is
\[
M(d)=\begin{cases}2-rd,&0\le d\le1,\\1+\sqrt3-d,&1\le d\le\sqrt3,\\(2+\sqrt3)(2-d),&\sqrt3\le d\le2.\end{cases}
\]
Moreover \(M\) is decreasing and \(M(M(d))=d\), so central symmetry covers the opposite six edges.

The bundled `verify.py` checks the signed-facet certificates symbolically, verifies every affine-line comparison at exact algebraic interval endpoints, proves the involution identities, and verifies all three equality families by exact facet domination. No finite numerical search is used to certify the continuum theorem.

No independent audit or independent validation has been performed.
