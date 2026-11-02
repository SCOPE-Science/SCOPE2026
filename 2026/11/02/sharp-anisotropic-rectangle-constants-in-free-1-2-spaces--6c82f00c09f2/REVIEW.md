# Self-review

**Correctness — PASS.** The four-vertex free \(1/2\)-norm is reduced rigorously to 16 exact tree costs by concave cycle elimination. The bilinear secant identity reduces the global operator norm to directional tangent loads. Two tree flows bound each one-signed and vertical-mixed region, while a positive concave combination of three exact tree costs gives the global upper bound in the horizontal-mixed region. The 16-tree cut-flow table proves a matching lower bound at a concrete midpoint and direction for every aspect ratio; strict monotonicity follows by differentiation. The independent implementation of cut-flow enumeration in `verify_rectangle.py` passed all 3,192 programmed comparisons (finite checks corroborate, but do not replace, the proof).

**Originality — PASS, with historical-priority qualification.** The original coordinatewise-affine constructions and cube bounds (Albiac et al. 2020; Bíma 2023) do not provide the unequal-sided exact profile. The published square-cell theorem gives an exact value only at equal sides. Uniform-over-aspect upper bounds and the limiting value are not new; this proof determines the previously unclassified exact value for every finite aspect ratio and proves strict variation. Targeted scientific semantic and literature searches did not retrieve a stronger pre-existing profile; unindexed equivalences are a residual risk.

**Value — PASS.** Unequal cell dimensions are intrinsic to anisotropic discretizations, and even at a fixed quasi-Banach exponent the optimal interpolation distortion was unknown at finite aspect ratio. The sharp formula gives the full continuum of constants, an explicit 16-tree certificate, an attained optimizer, strict aspect-ratio sensitivity and quantitative approach to the known supremum. This is a natural complete parameter classification, not a small isolated computation.

**Limits.** The exponent is only \(1/2\); arbitrary free exponents, more vertices and arbitrary extensions are not classified. There is no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
