# Self-review

## Correctness — PASS
The tree-spacings change of variables has exact triangular Jacobian \(\prod_v(1-B_v)^{h_v-1}\), yielding independent \(\operatorname{Beta}(1,h_v)\) increments and the classical hook volume. Centered transfer coordinates are orthogonal martingale innovations; direct variance multiplication yields the covariance determinant and invariant factor \(F(h_v)\). A strict analytic derivative inequality and sorted subtree-size domination prove both extremal rigidities. The actual standalone checker independently integrates rational first and second moments over linear-extension simplices for 157 trees, obtaining 7602 exact comparisons. It cannot by itself certify all dimensions.

## Originality — PASS (qualified)
The marked-poset transfer and the order-polytope setup are prior work [1,2], as is the rooted-tree hook-volume formula. Inspection of relevant definitions, results and applications in [1], together with searches on covariance, conditional beta spacings, isotropic factorization, transfer-parameter minima and extremal rooted trees, disclosed no theorem covering the new conjunction or its individual nontrivial formulas. A nearby established minimum-inradius theorem concerns a different metric functional; isotropic results for Hanner polytopes concern a different family. There remains the meaningful risk that the beta-increment calculation or its determinant has appeared independently in probabilistic order-statistics terminology.

## Mathematical value — PASS
The exact affine-invariant isotropic law classifies sharp extremal tree shapes for every dimension, rather than checking a small finite census. The covariance-orthogonalizing transfer gives a constructive canonical Euclidean position and uniquely solves a natural metric optimization within an existing polytope deformation. These facts are not implied by the standard hook volume and distinguish geometry from combinatorial volume equivalence.

## Checked source context and limits
[1] Fang–Fourier–Litza–Pegel, *A Continuous Family of Marked Poset Polytopes*, arXiv:1712.01037v1; transfer-map theorem and geometrical sections examined in accessible full text. [2] Stanley, *Two poset polytopes*, Discrete Comput. Geom. 1 (1986), 9–23, original order-polytope context. Public database searches return related radius and Hanner-invariant theorems, not a directly stronger covering statement. Lack of a found statement is not proof of global uniqueness; independent mathematical review has not taken place.

Self-review: passed. Independent audit: not yet performed.
