# Scientific review: Gaussian mean-width transition in partial permutohedra

## Correctness

**PASS.** The vertex-optimization rule follows by a pairwise swap and inclusion argument. The exact angular orbit weights follow from exchangeable Gaussian signs and orderings. The Gaussian-support scaling follows from empirical-quantile convergence in first Wasserstein distance; the stated uniform-integrability bound justifies convergence of means. The integration-by-parts identity reproduces the explicit Gaussian-tail profile, whose one-sided third derivatives are unequal. Gaussian Poincaré concentration and spherical normalization prove the directional law. The exact saturated mean is independently obtained through pairwise positive-part minima. The conic-polynomial identity invokes, and explicitly credits, the known type-B Weyl-chamber formula.

The included standalone checker tests brute-force support maximization, angle normalization, Gaussian integrations, quantile asymptotics, and conic-polynomial coefficients. It does not replace the infinite-family proof.

## Originality

**PASS, qualified.** The foundational Heuer–Striker vertex description and the Behrend–Castillo–Chavez–Diaz-Lopez–Escobar–Harris–Insko face/volume theory are established prior results, not reasserted as new. Godland–Kabluchko already derive the type-B cone polynomial; that component is imported, not newly discovered. Specific searches and comparisons did not reveal the derived explicit \(\operatorname{erfc}\) leading spherical-width function for partial permutohedra, its sharp \(C^2\)-but-not-\(C^3\) transition, or the joined angular saturation law. The closest general coverage is classical Gaussian order-statistics and Weyl-cone theory; the risk that a broader result already entails the specialized asymptotic as an unstated corollary remains.

## Value

**PASS.** Mean width is a canonical Euclidean geometric invariant, and the family joins permutohedral/stellohedral and partial-assignment structures. The limiting width has a sharp, explicit third-order transition exactly where the typical supporting vertex becomes sign-limited rather than rank-limited. The full finite-dimensional vertex-angle partition explains the transition geometrically and quantifies its finite-size critical window. The result is not proposed as a new general theory of Gaussian L-statistics or an independently new type-B chamber evaluation.

## Closest literature and limits

The two partial-permutohedron source manuscripts treat vertices, facets, face lattices, volume and Ehrhart theory. The Weyl-chamber source provides a crucial already-established conic intrinsic-volume formula. The explicit leading mean-width phase function and coupled exterior-angle saturation law were not found in those relevant sections or in the checked research records. No finite-size Gaussian-width CLT, fixed-rank extreme-value regime or complete higher conic volumes of saturated-rank normal cones is claimed. Independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
