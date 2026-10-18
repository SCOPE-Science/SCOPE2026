# Scientific review

## Correctness — PASS

The claim concerns every finite family of Euclidean planks of total width at most \(W<1\). The volume-preserving Bang map is reconstructed from its maximizing-sign-vector formula: after sign-flip comparison, its translated image of the square's eroded core lies outside every open plank, with disjoint measurable translation cells. This yields the universal uncovered-area lower bound \((1-a)(1-b)\). The exact unit-vector dispersion identity and a two-regime scalar inequality give the stated global upper bounds and stability. A centered square-strip convolution calculation constructs equality in both regimes. Equality of the upper bound for a single plank determines the angle, and strict shift monotonicity of the convolution density fixes its center. The analytic proof covers arbitrary finite families, not only tested cases.

The standalone checker is executed from `checks/verify.py` and reports `VERIFY_OK symbolic_identities=5 attaining_directions=49 families=340 random_single_planks=340`. Its geometry checks independently construct strip–square intersection polygons. The test suite is finite; the result is not inferred from enumeration.

## Originality — PASS (historical-priority risk remains)

The closest source is Bakaev–Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483 (first public July 29, 2026), whose Section 2 supplies the Bang map and whose Theorem 12 proves that a single plank suffices for every planar convex body. That existence theorem is acknowledged and is not claimed as new. Its inspected theorem, proof, and surrounding sections do not give the square's closed sharp two-branch value, changing unique single-plank direction, inverse target-coverage width, or quantitative all-family dispersion inequality. Bakaev–Yehudayoff, *Volume stability of plank covers*, arXiv:2609.30409, studies a different stability regime: covering punctured convex bodies and overlap. Searches of mathematical-research records for square-specific partial-plank area, angle transition, inverse widths, and corresponding erosion bounds returned no covering mathematical statement. The closest records concern a square separation body and a circular annulus fractional plank cover, distinct functionals. Earlier unindexed literature might contain an equivalent optimization; search is not historical-priority certification. The second source was compared at title/abstract level; its full text was not read, an explicit residual limitation.

## Mathematical value — PASS

The new result determines a natural, all-budget extremal invariant of the square against unrestricted finite strip families, with a genuine interior optimal-angle phase transition at \(W=1/\sqrt2\) and covered fraction \(3/4\). Its inverse answers the operational geometric optimization question of the least total strip width needed to cover a prescribed area. The quantitative angular-dispersion bound applies to all finite families and is stronger than the prior existential single-plank theorem; it controls near-extremizers in the symmetry-reduced direction space. This is a complete sharp classification and structural stability estimate, not an arbitrary numeric slice. It does not generalize automatically to rectangles or multi-plank equality classifications.

## Scientific limits and closest literature

Bakaev–Polyanskii (2026), arXiv:2607.27483, is foundational for the area-preserving Bang map and general planar single-plank theorem. Bakaev–Yehudayoff (2026), arXiv:2609.30409, addresses a different covering-stability objective. The theorem is limited to finite families in a Euclidean unit square. Unindexed exact-square calculations remain a historical-priority possibility. There has been no external replication or independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
