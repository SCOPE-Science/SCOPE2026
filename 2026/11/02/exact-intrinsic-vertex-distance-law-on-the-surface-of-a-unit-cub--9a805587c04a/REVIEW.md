# Review of the exact intrinsic cube vertex-distance law

## Correctness — PASS
The six-face metric is established without finite-grid extrapolation: the candidate distance is realized by a straight feasible two-face unfolding and is globally 1-Lipschitz by facewise gluing. Thus no longer face sequence can beat it. Symmetry reduces the surface measure to a square and two congruent triangles per opposite face. Their radial angular widths integrate exactly to the claimed law. The moment calculation and the sharp terminal corner asymptotic are independent analytic checks. The bundled `verify_cube.py` performs supplementary quadrature and randomized consistency checks; no numerical output is used as an infinite proof.

## Originality — PASS, with priority qualification
The closest source-unfolding result (Miller–Pak, arXiv:math/0312253) supplies general wavefront machinery and cube examples but not the fixed-vertex probability law. Goldstone–Roca–Suzzi Valli (arXiv:2003.06096) examines paths between opposite-face interiors and the incidence of four-face minimizers. Mathai–Moschopoulos–Pederzoli (1999) computes ambient Euclidean distances, which are not intrinsic: the opposite cube vertex is at ambient distance \(\sqrt3\) but surface distance \(\sqrt5\). The public-index, synonym, and implication comparisons identified no equivalent or dominating explicit distribution. The earlier ambient-distance paper could only be read in abstract, and unindexed priority remains uncertain.

## Value — PASS
This computes the *entire* natural metric-measure radial invariant of a cubic surface, rather than a chosen sample point or isolated integral. It identifies all three positive geometric transition radii, the nontrivial one-sided curvature changes of the CDF, an exact second moment, and the sharp maximum-distance tail coefficient. The square–triangle geometric decomposition also provides a compact benchmark for source wavefront calculations on polyhedra.

## Limitations
The source is a fixed vertex of a unit cube, not a variable point or a random pair. Surface intrinsic and ambient metrics are intentionally distinguished. No independent mathematical validation or definitive literature-priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
