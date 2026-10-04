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

The global part of the proof is the centering lemma. For any equal-area disk center \(x\), rotate the intersection \(P_n\cap(x+B_s)\) through the full cyclic symmetry group. All rotated intersections have the same area, their Minkowski average lies in \(P_n\cap B_s\), and Brunn--Minkowski implies that the centered intersection has at least that area. This directly addresses the translation infimum in the Fraenkel asymmetry.

After centering, the equal-area radius \(s\) satisfies
\[
R\cos(\pi/n)<s<R.
\]
Therefore the disk crosses each side but does not reach a polygon vertex. The \(n\) excluded pieces are disjoint circular caps, each with half-angle
\[
\beta_n=\arccos\!\left(\frac{R\cos(\pi/n)}s\right)
\]
and area
\[
s^2(\beta_n-\sin\beta_n\cos\beta_n).
\]
Since the polygon and disk have equal area, doubling the total missing cap area and normalizing by \(\pi s^2\) yields the claimed formula.

Taylor expansion at \(t=\pi/n=0\) gives
\[
\beta_n=\frac{t}{\sqrt3}+O(t^3),
\]
and hence
\[
\mathcal A_F(P_n)=\frac{4\pi^2}{9\sqrt3}n^{-2}+O(n^{-4}).
\]
Combining this with the exact unit-area perimeter \(2\sqrt{n\tan(\pi/n)}\) gives the constant \(3\sqrt{3\pi}/4\).

The embedded `verify.py` was replayed from its package path before packaging and returned:

`VERIFY_OK regular polygon Fraenkel asymmetry`

It independently integrates the radial intersection for selected \(n\) and checks the two asymptotic constants numerically. Those finite computations are consistency checks only and are not used as an infinite proof.
