# Scientific review of the square Monge incenter classification

## Correctness — PASS
The affine-hyperplane projected coordinate facet normals have norm \(\sqrt{1-n^{-2}}\), and adjacent Monge facet normals have norm \(2\). Rescaling the inball slack system produces a nonnegative array with adjacent Monge slack at least one. The baseline quadratic array has every slack one and total mass \(n^2(n^2-1)/12\). Monge permutation-exchange optimality, permutation averaging, and its equality case prove both the sharp mass lower bound and the complete affine-cube equality locus. The center normalization, all boundary cases \(n\ge2\), and the facet-tangency count follow exactly. Standard-library exact arithmetic and a separate full-facet HiGHS linear program corroborate the formulas. The infinite-dimensional family conclusion rests on the proof, not the finite tests.

## Originality — PASS, with residual access risk
The closest primary source, Erickson–Kretschmann, arXiv:2311.07522, proves the normalized Monge facet system, vertices and two-row volume formulas, not the Euclidean inradius, a sharp normalized-slack equality classification, the entire incenter set or its contacts. Rudolf–Woeginger (1995) addresses extremal rays of the cone. Erickson–Jones, arXiv:2609.09508, gives a lattice-path model for volume and Ehrhart data according to its abstract. Its full text was not accessible and remains a coverage risk, not a whole-document noncoverage assertion. Searches for Monge inballs, Chebyshev centers, Monge assignment-equivalence, exact incenter cubes, and published result databases found no claim implying this all-dimensional statement. Failed search alone is not proof of novelty.

## Value — PASS
The normalized Monge cost polytope is a natural and researched family of high-dimensional convex bodies. An exact Frobenius robustness margin of order \(n^{-4}\), together with the unexpected full \(n-1\)-dimensional cube of optimal centers and a complete tangent-facet spectrum, resolves a concrete geometric invariant not read off from the known facet list. The equality case of the Monge assignment bound supplies the structural mechanism; the result is not a numerical substitution or a routine coordinate check.

## Scope and remaining limitations
Only square matrices, the precise mass-one normalization, and the intrinsic Frobenius metric are covered. No independent external validation has been carried out; one same-family 2026 primary full text remains uninspected.

Same-model review: passed. Independent audit: not yet performed.
