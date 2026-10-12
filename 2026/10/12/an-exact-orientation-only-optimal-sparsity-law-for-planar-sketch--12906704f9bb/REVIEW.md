# Scientific review

## Correctness — PASS

The update is exactly a Euclidean orthogonal projection for the linear system \(A^\top x=b\). In singular coordinates the two input support patterns each produce a pair of orthogonal sketch directions; the normalized image projectors have an explicit trace-one two-component representation. Direct algebra completes a square in the mixture probability, giving the exact projector minimum eigenvalue and a unique optimum when the singular values are unequal. The independent standard-library checker verifies 1,152 exact rational identities on representative matrices. The checker does not replace the all-real algebraic proof.

## Originality — PASS with residual priority risk

The original generalized sketch-and-project framework already characterizes uniform expected contraction using the smallest eigenvalue of an expected projector **and supplies a semidefinite program for optimal discrete sampling probabilities (Section 5.1)**. The new contribution is a closed-form optimizer for a natural constrained Bernoulli-sign density, not the generic discrete optimization formulation. The most relevant sparse-sketch analysis treats leverage-score sparsified sketches and general nonasymptotic projector bounds; it does not give the exact optimum over conditioned Bernoulli–Rademacher densities in dimension two. A separate expected-projection paper gives large-stable-rank surrogate formulas rather than this finite-dimensional optimization. Related published results optimizing coordinate-only sampling probabilities and Haar sparse subspace descent do not imply optimization over a coordinate-versus-dense-sign sketch mixture. Search cannot rule out every equivalent unindexed calculation.

## Value — PASS

The finding completely solves a natural one-parameter sampling-design question for the smallest nontrivial invertible sketch-and-project problem. It exhibits a strict interior sparsity optimum for generic eigenvector orientations and an unexpected independence of the optimizer from the condition number. This gives a sharp benchmark for balancing sparse and dense sign sketches. It does not claim that acquiring the optimal orientation, implementing it, or extending it to higher dimensions is cost-free.

## Scientific boundaries

The claim concerns a two-dimensional, fixed-distribution, independently sampled, one-equation Euclidean projection algorithm. It does not optimize wall time, all sketch distributions, higher-dimensional rates, or instance-specific long-horizon errors. An independently repeated audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
