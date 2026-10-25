# Scientific review: exact gcd-resolved rotated-polygon hull law

## Correctness — PASS

The stated geometric event and normalization are unambiguous: integers \(n\ge m\ge3\), outer circumradius one, \(0<\rho<1\), one uniformly distributed relative rotation, and the extreme-vertex count of the joint planar convex hull. The support-functional proof separates the guaranteed outer vertices from inner vertices; for the latter, it proves both directions of the outer-facet normal criterion. Crucially, the assumption \(n\ge m\) guarantees that an inner vertex crossing the corresponding facet is also the unique inner support maximizer in that direction, rather than merely lying outside the outer polygon. The gcd multiplicity reduction and exactly two floor/ceiling arc counts establish the distribution without sampling assumptions. Solving the zero-variance condition proves the complete rigidity set; inverse-cosine asymptotics yield the critical window, including its endpoint. The bundled independent monotone-chain and threshold checks were run successfully. Risks: exceptional alignments are null events; numerical tests do not replace the analytical proof.

## Originality — PASS relative to inspected evidence

Har-Peled, arXiv:1111.5340v1, treats independent spatially sampled points rather than a rigid random rotation. Kiss–Vidnyánszky, arXiv:1402.5452v1, treats nonconvex unions of congruent regular polygons and perimeter/area, not extreme points of the convex hull of two differently sized and differently ordered nested polygons. O'Rourke–Zaimi (2015) treat intersections of equal-circumradius polygons and report gcd-driven side counts; the difference between intersection and hull does not alone establish novelty because polarity might relate them, but the polar configurations have unequal radii here and the cited claim supplies neither continuous radius thresholds nor the random phase law or critical-window limit. Complete published RESULT.md materials on radial coverage of congruent rotated unions and expected intersection area for randomly rotated tangential polygons were inspected and do not imply this claim. The elementary lattice floor/ceiling count and the general gcd pattern are explicitly not claimed as new. Risks: old technical-report full text not recovered, and mathematical non-coverage cannot be conclusively established by database searching.

## Mathematical value — PASS

For the natural convex-hull complexity of two concentric rotational point lattices, the result gives the complete law, not an isolated special value. Every deterministic aspect ratio is classified, including coprime and noncoprime cases. The exact variance and a sharp near-circular critical scaling reveal persistent arithmetic fluctuations even when the polygons converge in radial scale; for six inner vertices, distinct subsequences have limiting variance zero versus nine. These structural facts are natural benchmarks for coherent (as opposed to independent) point-set perturbations. The narrow planar setting and lack of downstream applications are limitations, not claims of generality.

## Sources and limitations

Actual comparisons include the full primary mathematical text of Kiss–Vidnyánszky (arXiv:1402.5452v2), the full 2015 O'Rourke–Zaimi problem and response, the Har-Peled arXiv abstract and author summary, and complete scientific RESULT.md texts of two published related records. The main risk is an unindexed or inaccessible historical special case; independent audit remains outstanding. The finite checker is corroboration only.

Self-review: passed. Independent audit: not yet performed.
