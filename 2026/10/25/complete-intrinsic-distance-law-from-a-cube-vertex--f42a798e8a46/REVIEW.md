# Scientific review: cube vertex surface-distance law

## Correctness

**PASS.** The metric is intrinsic and the probability measure is normalized over six unit-area faces. A complete simple-face-walk argument reduces the opposite-face geodesic distance to the shorter of two feasible two-face unfoldings. All 80 simple face sequences, grouped into 24 exact affine-distance classes, satisfy a four-vertex inequality that is sufficient on both triangular chambers of the opposite face. The resulting square-and-circle area integral yields the displayed CDF with correct boundary values. Exact polynomial integration independently gives \(\mathbb E[R^2]=3/2\) and \(\mathbb E[R^4]=61/18\). The far-tail coefficient follows from a two-dimensional rescaling near the unique opposite vertex. The accompanying checker uses only exact integers and rational fractions for its certificate and moments; numerical quadrature is explicitly supplementary.

## Originality

**PASS (best-knowledge self-review).** Fuchs (2016) treats vertex-to-vertex geodesics and endpoint frequencies, not the radial distribution for a uniform surface-area point. Goldstone–Roca–Suzzi Valli (2020) treat shortest paths between points in two opposite face interiors. Davis (2023) describes cube cut loci and geodesic motion planning, including the six branches from the opposite corner, but gives no complete radius-to-area law. The Mitchell–Mount–Papadimitriou shortest-path algorithm can evaluate individual geodesics but does not establish this explicit distribution. Euclidean cube line-picking formulas concern a different metric. A related complete radial law on the tetrahedron does not imply the cube's three-dimensional unfolding certificate or square-face integration. Specific searches and literature material are recorded in `AUDIT.json`. Residual risk: an unindexed elementary derivation or unpublished source might already state the formula; no claim of proof of global uniqueness is made.

## Mathematical value

**PASS.** The intrinsic geodesic ball area of a cube centered at a singular vertex is a canonical invariant, unlike an arbitrary subfamily or arbitrary parameter. The result supplies its complete area profile, not merely one local coefficient or an isolated sample, identifies two geometrically distinct transition radii, determines the unique farthest point, and provides exact moments and a sharp terminal tail. It is a reproducible benchmark for surface-geodesic sampling and polyhedral cut-locus geometry. The cube's six-branch opposite-vertex cut locus and 80 candidate face walks make it structurally distinct from a regular tetrahedron.

## Limits

The result concerns a fixed vertex source on a regular cube, not generic source locations or two random endpoints. It remains possible that an unindexed source contains an equivalent specialization. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
