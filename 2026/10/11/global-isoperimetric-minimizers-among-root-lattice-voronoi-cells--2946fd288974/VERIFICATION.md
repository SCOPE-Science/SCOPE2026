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
# Verification

The proof has two exact reductions.

First, every root facet of the Voronoi cell has distance
\[
\frac1{\sqrt2}
\]
from the origin. Hence
\[
\operatorname{vol}(V_\Lambda)
=
\frac{1}{d\sqrt2}\,
\mathcal H^{d-1}(\partial V_\Lambda),
\]
and therefore
\[
\mathcal I_d(V_\Lambda)
=
d\sqrt2\,\operatorname{covol}(\Lambda)^{1/d}.
\]

Second, since
\[
\operatorname{covol}(\Lambda)^2=\det(\Lambda),
\]
the problem is exactly determinant minimization. For irreducible root lattices,
\[
\det(A_m)=m+1,\qquad
\det(D_m)=4,\qquad
\det(E_6)=3,\qquad
\det(E_7)=2,\qquad
\det(E_8)=1.
\]
The residue lower bound
\[
h=(1,2,3,4,4,4,3,2)
\]
satisfies
\[
h(a)h(b)\ge h(a+b\bmod8)
\]
for all residues \(a,b\), and equality occurs only when one residue is zero.

The bundled checker verifies this complete multiplication table and, independently, computes the exact minimum determinant and all equality decompositions through rank \(256\). It confirms the periodic determinant sequence
\[
1,2,3,4,4,4,3,2
\]
modulo \(8\), with the rank-zero residue represented by \(E_8\)-blocks.

The finite dynamic program is supplementary. The infinite proof is the residue inequality together with the classical irreducible determinant formulas.

No computation or proof here addresses arbitrary non-root lattices, because no such claim is made.
