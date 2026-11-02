# Self-review

## Correctness

PASS. For every nondegenerate tetrahedron, negative origin-barycentric coordinates are precisely the facets whose outward halfspaces contain the origin. The interior-point convex-combination lemma rules out three negative coordinates for vertices on one convex boundary with the origin in the body's interior. Conditional antipodal symmetry yields sixteen equally weighted signs of a one-dimensional linear dependence, partitioned as \(2+8+6\); the count is invariant under the normalizing denominator's sign. The proof needs no isotropy or identical sampling law. Exact rational enumeration and independent sign-based facet tests reproduce the three counts. Simulations on the spherical, ellipsoidal, and \(\ell_4\)-boundary models are auxiliary. General-position and strict-side hypotheses are explicit.

## Originality

PASS, subject to historical-priority uncertainty. Wendel's 1962 absorption theorem includes the zero-visible probability and must not be claimed as new. Bonnet–O'Reilly's 2019 preprint / 2022 published work gives general expected signed-facet-height counts for *uniform spherical sampling*, which together with Wendel and simple tetrahedral restrictions can imply the numerics in that narrower model. The surviving claimed contribution is the **complete shape-independent and distribution-independent law for four potentially different antipodally symmetric measures on the boundary of any centered symmetric three-dimensional convex body**. This extension is not established by the inspected scalar absorption formula or spherical height expectation, and searches for equivalent visible-face and barycentric-sign formulations found no direct source. The primary references and limitations are identified in RESULT.md. A specialized geometric-probability reference outside the searches could conceivably contain the same full extension; independent priority review remains necessary.

## Mathematical value

PASS. The negative supporting-facet count is a natural intrinsic visibility statistic for an inscribed random tetrahedron, refining the classical event that the origin lies in the hull. Its complete three-value law is universal even for nonidentical anisotropic sample distributions and arbitrary centrally symmetric convex boundary shapes. The deterministic bound \(V\le2\) explains the universality, and an exact interior-sampling example demonstrates why the support restriction is mathematically essential. This is a self-contained complete classification, not a fitted distribution or a single benchmark recomputation.

## Limits of verification

The analytic result concerns four independent boundary samples under antipodal symmetry and plane-null general position. Numerical diagnostics are finite; the algebraic argument establishes the universal assertion. Historical noncoverage is provisional; independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
