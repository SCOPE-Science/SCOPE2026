# Scientific review

## Correctness — PASS

The proof gives the complete Fourier/core eigenspace decomposition and proves that automorphism averaging cannot worsen SLEM. Each scalar minimization is derived with its original feasibility constraints: the core-eigenvalue choice is feasible, the rim-balancing choice is feasible because the two cycle eigenvalue endpoints sum to more than four, and the final crossing/boundary minimax has a unique \(a\) optimum. The residual core-eigenvalue inequality gives the exact interval and both edge-activation transitions; nonnegative group averaging transfers the forced-absence/necessary-presence conclusions to unrestricted optimizers. A standalone program reproduced 3,929 finite checks, including independent LP solutions and exact-rational small-cycle cases. Finite checks do not prove the family theorem; the analytic proof does.

## Originality — PASS, subject to stated residual risk

The closest explicit predecessor is Boyd–Diaconis–Parrilo–Xiao, Section 5.4.3, which treats the single-hub wheel \(K_1\vee C_m\) with one core vertex. Jafarizadeh's clique-lift theorem (Section 3, Theorem 1) reduces this kind of topology to a weighted-base optimization but does not explicitly solve the nonuniform-stationary wheel base problem, specify all invariant optima, or give the two nontrivial core-edge-use boundaries. Actual searches of research records, published sources, title/alias forms, and different parameter formulations found no exact statement implying all asserted conclusions. Generic SDP solvability is not equated with explicit coverage. The most substantial remaining risk is an unindexed analytic solution of the nonuniform wheel base problem, or an equivalent clique-lift specialization in a thesis.

## Value — PASS

The optimum is not merely a numerical SDP instance: it covers every pair of integer graph sizes, provides exact transition allocations and the complete symmetry-invariant optimizer interval, and distinguishes three qualitatively different support regimes. The first regime forces all optimal unrestricted walks to ignore the clique edges; the last forces all optimal unrestricted walks to use at least one of them. The two large-size activation boundaries at core/rim ratios \(1/2\) and \(1\) and the piecewise mixing-rate limit give a motivated design law for complete-core periodic networks, beyond the classical one-hub wheel.

## Risks and limitations

The unrestricted optimizer family is not fully classified, only the invariant subfamily and two global edge-support constraints. The study concerns SLEM, not finite-time mixing, and reversible uniform-stationary kernels, not arbitrary Markov chains. The 2020 clique-lifting reduction covers a key step and related theses could contain an equivalent closed-form specialization. Computational verification is supplementary and independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
