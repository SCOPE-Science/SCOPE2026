# Scientific review

## Correctness

PASS. The necessity follows because the inverse image of a target face under a ball-preserving map intersects the ball in a face and must contain the source minimal face. For sufficiency, the exposed source and target faces have tangent subspaces of dimensions \(k\le l\); an isomorphism of supporting hyperplanes can embed the first tangent subspace in the second. The rank-one-plus-small-invertible map explicitly defined in `RESULT.md` preserves all source vertices: source-face vertices enter the target face, their negatives are handled by central symmetry, and all remaining vertices converge into the interior of the target ball. A common small parameter exists because the vertices are finite, and invertibility is certified by the recovering functional. This proves the full quantified result. The optional exact-rational checker tests a non-cubical three-dimensional model but is not used as an infinite proof.

## Originality

PASS under the checked-literature evidence, with the bibliographic risks stated below. Cabello Sánchez–Cabello Sánchez (2022) provide the semigroup setting, one special planar orbit classification, and the flat-target lemma. That lemma already implies that every polyhedral-sphere point has a dense orbit, so that consequence is not an originality claim. A published-finding corpus finding classifies real/complex coordinate cubes and cross-polytopes and explicitly declines a general polyhedral extension. Neither source implies the complete intermediate-face comparison for an arbitrary centrally symmetric polytope. The proof here supplies an all-polytope sufficiency construction; searching general face rank, facial dimensions, and equivalent semigroup terminology did not identify a covering statement. One 2019 article on large contractive automorphism semigroups was accessible only by abstract, so a hidden equivalent assertion there remains a genuine risk.

## Mathematical value

PASS. The natural classification problem asks which points of a finite-dimensional unit sphere can be connected by an invertible norm-one-or-less linear map, a central question in contractive-automorphism semigroup dynamics. This result resolves that question completely for all real polyhedral norms with exactly one integer invariant—the dimension of the minimal face—regardless of vertex simplicity, facets, or norm symmetry. In dimensions at least three it determines all intermediate edge-to-face and edge-to-edge reachability that neither the planar case nor the flat-target criterion resolves. The global \(n\)-class chain is a structural statement rather than a marginal numerical improvement. The short proof is nontrivial because the same operator must be invertible, contractive on *every* vertex, and map the designated source exactly onto the designated target.

## Closest literature and limits

The closest explicit prior classification is the coordinate \(\ell_1/\ell_\infty\) published-finding corpus finding identified in `RESULT.md`, which is strictly narrower. The directly read 2022 and 2021 semitransitivity texts do not state a universal arbitrary-polytope face-rank criterion. The 2019 full article was not accessible for detailed inspection; the available abstract emphasizes qualitative near-transitivity. The result is limited to real finite-dimensional polyhedral balls and does not estimate the inverse contraction norm. An equivalent unindexed theorem remains possible.

Self-review: passed. Independent audit: not yet performed.
