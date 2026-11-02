# Scientific review: disk-clipped regular-polygon Mahler interpolation

## Correctness — PASS

The sector decomposition is derived directly from the polygon radial function and the polar identity \((A\cap B)^\circ=\operatorname{conv}(A^\circ\cup B^\circ)\) for convex bodies containing the origin. The area factors in the product cancel exactly. Differentiation gives a negative derivative across \(0<\beta<\pi/n\); the potentially positive \(\tan^2\beta-1\) term is controlled on \([\pi/4,\pi/3]\). Separate Taylor expansions establish both endpoint orders and the uniform cubic large-polygon limit. A standard-library checker passed 417 numerical comparisons of independently constructed areas and asymptotics. Principal risk: approximation in the numerical checker; not needed for the symbolic proof.

## Originality — PASS (self-review)

The most relevant full-text source is Böröczky–Makai–Meyer–Reisner, arXiv:1507.01481, Theorem 3 and Corollary 4, which give a sharp lower bound for rotationally symmetric planar bodies. Those statements imply a lower bound and endpoint equality, but not the precise product, monotonic ordering of radii, or universal deficit profile. Meyer–Reisner's 2011 polygon-extremal result is not a formula for intersections with disks. Harrell–Henrot–Lamboley's local-minimizer and functional-concavity statements are not a universal monotonicity result for this particular nested family. The closest related earlier computation for outer parallel rounding of a regular polygon uses Minkowski addition, not intersection, and cannot be identified with this family by polarity. Targeted mathematical record searches found no equivalent formula. Residual risk: possible unindexed historical computation for disk-clipped polygons.

## Value — PASS

This is a complete, non-arbitrary, all-\(n\) interpolation between the extremizers in two classical planar Mahler inequalities. It quantifies the actual change in the affine-invariant volume product along a canonical geometric deformation, not only the known bounds. The nonanalytic \((r-1)^{3/2}\) disk-side onset, linear polygon-side onset, and the universal cubic many-sided profile identify structurally different regimes. No extension to other nested deformations is claimed.

Self-review: passed. Independent audit: not yet performed.
