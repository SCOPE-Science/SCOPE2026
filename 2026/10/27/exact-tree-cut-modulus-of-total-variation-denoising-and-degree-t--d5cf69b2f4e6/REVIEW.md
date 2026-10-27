# Scientific review

## Correctness — PASS
The theorem is proved for every finite unweighted tree and every positive denoising strength. The proof identifies all affine chart derivatives via KKT conditions, realizes every connected-block partition on an open cell, reduces every seminorm operator norm to tree-edge cut steps, and evaluates these exactly by boundary counts. It verifies actual attainment. The exact-rational checker exhausts all 1,441 labeled trees through six vertices and validates two concrete proximal KKT pairs; these checks are supplementary rather than the basis of the infinite family theorem.

## Originality — PASS
The original fused-lasso paper introduces fused edge penalties, while the generalized-lasso paper establishes local Euclidean affine projection geometry. The graph-ROF convex-minimality paper treats a single data vector and convex potentials rather than the two-input graph-variation metric. The available published-record comparisons do not imply the exact tree-cut expression. An equivalent unindexed result remains possible, and the online supplement to the generalized-lasso article was not separately inspected.

## Mathematical value — PASS
The stability problem uses precisely the variation geometry motivating the estimator. The cut formula is a natural structural invariant, provides complete sharp stability for all trees, and demonstrates unbounded two-input amplification even on maximum-degree-three combs. The path and star cases are concrete sharp comparisons, not arbitrary finite slices.

## Scope and limitations
Only finite simple unweighted trees, unit vertex masses, Euclidean squared fidelity, and anisotropic graph variation are proved. No weighted, cyclic, infinite, or other-fidelity extension is asserted; a comb lower bound is not claimed as its exact modulus.

Self-review: passed. Independent audit: not yet performed.
