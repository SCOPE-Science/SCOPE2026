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

The source premises were checked in the full text of arXiv:2601.09795v1. Proposition 3.3 gives a semialgebraic homeomorphism of pairs between the cornet cell and the slit disk, and Proposition 3.5 transfers sections while preserving the pair formed by a section and its closure. Proposition 3.10 supplies the same deformation pattern in the one-loop case.

For each \(m\ge1\), the polynomial
\[
h_m(x)=\prod_{j=0}^{m}\left(x+1-\frac jm\right)
\]
has exactly \(m+1\) distinct zeros on \([-1,0]\). The two limiting branches \(z=\pm h_m(x)\) therefore form a connected graph with \(m+1\) vertices and \(2m\) edges.

The homotopy
\[
F((x,y,z),s)=
\left(
\frac{(1-s)(x+|x|)+(x-|x|)}2,
(1-s)y,
z
\right)
\]
was checked by cases. For \(x<0\), it keeps \(x\) fixed and preserves the sign of \(y\) until the endpoint, so the graph value \(z=\pm h_m(x)\) remains valid. For \(x\ge0\), the graph value is \(z=0\) and the first two coordinates are scaled within the closed disk. At \(s=1\), every point lies on the two-branch limiting graph; that graph is fixed pointwise. Hence this is a strong deformation retraction.

The graph cycle rank is
\[
2m-(m+1)+1=m,
\]
so it is homotopy equivalent to \(\bigvee^m S^1\). The transferred CAD-cell closure has the same homotopy type. No finite experiment, numerical approximation, or unproved classification is used.

The proof does not claim anything about torsion homology, higher-dimensional homology, all possible CAD-cell closure types, or minimal ambient dimension.
