# Scientific review

## Correctness — PASS

For the explicitly defined symmetric sign-coupled map, the strict two-cycle follows from the coordinate-exchange symmetry and affine equations. The two branch Jacobians give \(M=K^2\), with \(\det(\lambda I-K)=\lambda^3+a^2\lambda-2ab\). The real root is always strictly inside the unit disk for \(0<b<1\). Its complex companion pair crosses the unit circle precisely at \(a^2(1+4b^2)=1\); the null case \(a=0\) is covered separately. The strict itinerary ensures an open affine neighborhood. At equality the exact quadratic form \(H(\xi,\eta)=\xi^2-s\xi\eta+\eta^2\) on the center plane proves the invariant ellipses rather than inferring them from an approximation. The standard-library `verify.py` replay confirms 320 independent exact rational parameter instances and the local neutral identity. The continuum theorem rests on algebra and the positive-definite quadratic-form argument, not finite sampling.

## Originality — PASS, subject to priority risk

Lozi [1], equations (34)–(45), already defines the map and gives the quadrant-changing two-cycle as an algebraic solution, including sample coordinates. That known orbit is explicitly excluded from the novelty assertion. The inspected primary manuscript discusses stability spectra of fixed points and the numerical role of the two-cycle in its attracting sheets, but does not state the sharp all-parameter Floquet trichotomy or the invariant-ellipse foliation. Bilal–Ramaswamy [2] is a distinct time-delay Lozi extension with different state equations. Targeted mathematical-record queries returned related planar Lozi fixed-point statistics and period-two spectra of other maps; none is implication-equivalent to the statement for this three-dimensional sign-coupled map. An equivalent unpublished or unindexed computation remains possible. The symbolic reduction is sufficiently short that an independent priority check is worthwhile.

## Mathematical value — PASS

The period-two orbit is a structural object identified in the originating study as a possible skeleton for its sheet attractors. Locating the exact sink-to-index-two-saddle boundary separates attractor-compatible and expanding transverse behavior, while ruling out an intermediate index-one saddle. At the boundary, affine dynamics force an entire nontrivial local continuum of invariant ellipses, not the isolated invariant circle expected from a generic nonlinear Neimark–Sacker picture. These are naturally motivated stability invariants of the published map rather than an arbitrary numerical parameter slice.

The result is local to the strict quadrant itinerary and does not settle global basin boundaries, other cycles or hyperchaos. First-public-source evidence is the 11 May 2023 public preprint. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
