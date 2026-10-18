# Scientific review: equilateral triangles in circular cylinders

## Correctness — PASS

The result quantifies over all finite Euclidean dimensions at least three, all positive transverse radii, all nonnegative cylinder heights, and all placements and orientations of an equilateral triangle. Ordering the three axial coordinates loses no cases. For every candidate the projected squared side lengths follow from Pythagoras. Their Heron area identity is exactly \(16\mathcal A_\perp^2/s^4=3-4k^2+4uv\). The minimum-enclosing-circle radius is the circumradius only in the acute case; the proof also handles the competing obtuse case and shows it cannot beat the subsequent acute minimum. The derivative in the single product parameter \(p=uv\) locates the three unique minimizing splits and their boundaries \(k^2=1/2,4/7\). The resulting envelope is strictly decreasing, so the outer optimization has a unique crossing until the exact saturation height, followed by the endpoint optimum. Explicit spatial vertex reconstruction proves attainability and classifies equality, including a degenerate transverse projection at saturation. The exact formulas agree at all three phase boundaries.

The independent computational formulations in `verify.py` use three-dimensional distance reconstruction, minimum-circle calculation, deterministic orientation samples, and exact rational branch identities. Their finite checks supplement and do not establish the universal theorem. The verifier successfully checked 2,000 maximizing witness configurations, 77,088 admissible projected configurations, and 132,000 spatial orientations. Floating-point sensitivity near the flattened endpoint is addressed by evaluating the projected area in a cancellation-resistant factored form. The analytic proof covers the endpoint exactly, independently of floating-point arithmetic.

## Originality — PASS, with residual literature risk

The initiating work is Á. G. Horváth, *Triangle in a brick*, arXiv:1010.1607v1 (2010-10-08). Its full six-page text was inspected. Horváth's sharp configurations concern equilateral triangles inside unit-volume rectangular bricks with a lower bound on every box edge and specifically vertices on skew brick edges. Neither its hypotheses nor its resulting length inequality determines the maximum in a circular cylinder as an explicit function of the continuously varying height-to-radius ratio. The classical smallest-circle theorem is an ingredient, not this optimized three-phase projected-radius envelope. The IMO 1984 cylinder problem is about tetrahedral volume, not maximal equilateral-triangle side length. Comparison searches using inscribed/circumscribed equilateral triangles, minimal circular cylinders, bounding-circle projections, and exact threshold aliases found no stronger or equivalent result; this negative evidence cannot establish absolute priority.

The named checks, full-source inspection, published scientific-record comparisons and remaining risks are supplied in `AUDIT.json`. A general theorem on minimum enclosing cylinders or an obscure historical geometry source could still imply the formula; this remains a priority uncertainty requiring later human examination.

## Value — PASS

The result completely solves a natural geometric placement problem in a canonical family of convex solids, not merely one special aspect ratio. Its two internal orientation transitions are genuinely structural: the optimal axial pattern changes from two vertices sharing one height, to a continuously varying asymmetric three-height pattern, and then to equally spaced heights; a final threshold produces an exact flat saturation of the maximal side length. The proof identifies a nontrivial intermediate envelope \(k\sqrt{1-k^2}\) that would be missed by guessing only symmetric or endpoint configurations. Both the sharp formulas and all maximizer types persist in every finite ambient dimension at least three. Such phase data are natural benchmarks for geometric packing and smallest-enclosing-cylinder problems and are not implied by the classical zero-height circle case.

## Remaining limits

The result is restricted to circular cross sections and equilateral triangles; it does not solve arbitrary triangles, arbitrary bodies, or noncircular cylinders. It is supported by an explicit proof and reproducibility diagnostics, not by an independent expert audit. Historical priority remains uncertain.

Self-review: passed. Independent audit: not yet performed.
