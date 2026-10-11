# Review

## Correctness
**PASS.** The barycentric-coordinate formula gives the exact slab model
\[
K_n=\{x:|v_i\cdot x|\le1/n\}.
\]
This immediately fixes the inradius. The tight-frame identity sends the circumradius problem isometrically, up to the scalar \(1/\sqrt{n(n+1)}\), to maximizing squared norm in the zero-sum section of the cube. Strict convexity forces a maximizer to an extreme point; parity then forces either all coordinates to be balanced signs or one zero coordinate plus balanced signs. This proves the radius formulas and classifies every farthest point. The bundled verifier independently checks the identities and complete finite vertex sets through dimension \(10\).

## Originality
**PASS, with a classical-polytope residual risk.** The closest primary source was materially inspected in full. It identifies \(S\cap(-S)\) as the largest centrally symmetric subset of a regular simplex and studies its volume and projection body, but does not give Euclidean radius formulas or the parity law. A later projection-body paper in primary MSC \(52A40\) does not cover them either. Exact-object and alias searches under central kernel, reflected-simplex intersection, Euclidean inradius/circumradius, central cube sections, and parity returned no implication-equivalent result. The remaining risk is that the short cube-section radius computation may appear in unindexed hypersimplex or polytope literature.

## Value
**PASS.** The body is not an arbitrary intersection: it is the canonical Fáry--Rédei symmetry kernel of the simplex and the centrally symmetric candidate singled out in Brannen's projection-body extremal problem. The theorem gives its complete Euclidean roundness profile in every dimension, including all farthest points, and exposes a genuine parity transition in the geometry of the central cube section. These data are natural for metric comparison and for quantitative study of the canonical symmetric simplex kernel.

Same-model review: passed. Independent audit: not yet performed.
