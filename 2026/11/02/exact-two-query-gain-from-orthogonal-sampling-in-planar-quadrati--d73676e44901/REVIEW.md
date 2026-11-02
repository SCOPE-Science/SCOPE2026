# Scientific review: exact two-query orthogonal-sampling identity

## Correctness — PASS

The claim is an exact finite-dimensional expectation identity, not a numerical extrapolation. Diagonalizing and rescaling the real symmetric positive-definite Hessian preserves both direction distributions. The exact line minimization becomes a rank-one energy-orthogonal projection. The two schemes have two different, explicitly integrated expected energy matrices, shown in the proof to be scalar multiples for every initial error. The singular-looking partial-fraction derivation is used only for \(\kappa>1\); the isotropic case \(\kappa=1\) is separately proved using complementary orthogonal projectors. The matrix identity, angular integrals, and equality cases have independent symbolic and high-precision tests in `verify.py`.

Risk: only the exact quadratic, two-dimensional, two-step model is proved; no finite-precision or longer-horizon consequences are inferred.

## Originality — PASS, qualified

Kozak et al., arXiv:2107.03941, develop independent random orthogonal direction matrices for derivative-free projected-gradient steps and general expected convergence results. The inspected algorithm and proof/discussion sections do not establish an exact sequential two-direction line-search comparison. Berglund et al., arXiv:2202.04612, study randomized subspace Newton and give complexity bounds, without the Haar-paired comparison. Gürbüzbalaban et al., arXiv:1803.08200, contrast random permutations of a fixed coordinate set with independent coordinate selection on quadratic objectives; that sampling experiment is not independent continuous random directions versus a fresh Haar frame. General sketch-and-project theory covers individual randomized projections but the inspected material does not imply the precise two-query matrix proportionality.

Related published mathematical records on coordinate Gauss–Seidel transients, two-step steepest descent, and exact Haar moments were queried and compared by their actual statements; none provides the paired-continuous-direction identity. The equality of the whole expected quadratic form, rather than only an isotropically averaged trace, is the distinctive claim. A specialized earlier calculation might contain an equivalent relation despite these checks; independent priority verification has not been done.

## Value — PASS

Two objective evaluations/line solves form a natural finite-query budget for random-direction optimization. The result gives the exact benefit of using directions from one orthogonal Haar frame rather than two independent draws, uniformly over starting-error orientations. It makes the conditioning dependence explicit: perfect two-step solution for a spherical quadratic, a strict gain at every finite nonspherical condition number, and relative benefit that disappears in the ill-conditioned limit. This is a structural quantitative sampling-design statement, not merely a restatement of the one-step expected contraction.

## Closest literature and scope

- Kozak et al., *Zeroth order optimization with orthogonal random directions*, https://arxiv.org/abs/2107.03941 (original preprint posted 2021-07-08).
- Berglund et al., *Zeroth-Order Randomized Subspace Newton Methods*, https://arxiv.org/abs/2202.04612 (2022).
- Gürbüzbalaban et al., *Randomness and Permutations in Coordinate Descent Methods*, https://arxiv.org/abs/1803.08200 (2018, journal 2020).

The conclusion is not samplewise stochastic dominance, a claim for arbitrary dimension, or a guarantee for inaccurate line minimizers.

Self-review: passed. Independent audit: not yet performed.
