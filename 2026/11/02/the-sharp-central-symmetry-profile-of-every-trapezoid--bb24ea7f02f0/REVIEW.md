# Self-review

## Correctness

**PASS.** Affine normalization preserves the point-symmetry area ratio, and at each horizontal slice the overlap of two centered intervals is maximized by aligning their centers. A nonzero horizontal center is strictly suboptimal at a positive-measure set of slices, proving uniqueness in that coordinate. Exact integration gives an explicit quadratic in the vertical center; its constrained maximizer crosses \(y=1/2\) at \(t=1/3\). Differentiation independently checks the one-sided derivatives and the inversion threshold. The symbolic and rational-clipping checker passes, but it does not certify the all-parameter theorem by itself.

## Originality

**PASS, historical priority provisional.** The classical \(2/3\) bound, affine invariance, and fixed-instance polygon-overlap computations are prior work, not claimed as discoveries. Full open versions of Goenka–Moore–Sun–White (arXiv:2309.12597) and Chan–Hair (arXiv:2504.18352) were inspected in their relevant main results; the former studies axial reflection and folding, and the latter gives an algorithm for fixed polygons. Neither states the complete closed trapezoid profile, unique center, sharp \(1/3\) transition, or optimal inverse exponent. Semantic searches of indexed results and comparisons with accessible earlier geometric findings found no implication of those claims. A 1998 overlap algorithm and a 2015 book could not be inspected in full and remain historical risks. Being able to compute fixed instances does not by itself provide the stated symbolic parameter classification, but earlier equivalent specialized calculations remain possible.

## Value

**PASS.** The Kovner–Besicovitch index is a natural affine symmetry invariant whose \(2/3\) extremal behavior is foundational. An all-trapezoid exact profile replaces instance-by-instance optimization with a complete parameter theorem; the switching optimizer gives a sharp geometric phase transition. The inversion and square-root conditioning quantify precisely what this scalar invariant identifies and why it is unstable near the triangular boundary.

## Scope and limits

The theorem assumes nondegenerate planar convex trapezoids and exact overlap ratios. It recovers the base ratio, not full Euclidean shape; no statistical stability under noise is claimed. The literature search cannot establish absolute priority, particularly given inaccessible older full texts.

Self-review: passed. Independent audit: not yet performed.
