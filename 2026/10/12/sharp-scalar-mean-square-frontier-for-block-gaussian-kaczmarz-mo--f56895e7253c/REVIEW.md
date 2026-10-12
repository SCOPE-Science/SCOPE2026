# Self-review

## Correctness — PASS

The precise object is the pseudoinverse-free, *unnormalized* scalar Gaussian mBGK process in Han–Xie §5.6, with fixed positive stepsize, constant nonnegative momentum below one, independent blocks of arbitrary fixed finite width, and equal nonoptimal initial states. The full proof derives the covariance map from \(\chi_p^2/p\), proves primitivity (or handles zero momentum directly), establishes that the initial rank-one covariance sees the Perron eigenvalue, and checks all stability boundaries from \(\det(I-M)\). The global rate optimum is certified by an exact quadratic-discriminant calculation together with \(\det M=\omega^3\). The exact rational script replayed 1,890 determinant cases and all eight claimed example moments. These finite checks support, but are not substituted for, the universal algebraic and cone arguments. Mean-square and mean convergence are expressly distinguished.

## Originality — PASS with residual priority risk

Han–Xie's full original preprint specifies mBGK, sufficient second-moment bounds, and separate acceleration for norms of expected iterates; it does not supply the exact necessity-and-sufficiency scalar stability boundary or the global joint-parameter second-moment lower bound. Loizou–Richtárik treat projector-normalized sketch Hessians, which become deterministic in one dimension and do not imply the chi-square-multiplier result. Kidambi et al. analyze a distinct multi-directional random-regression distribution and derive broad lower bounds, not these sharp all-width identities. Bollapragada–Chen–Ward analyze finite-sum minibatches. Indexed studies of momentum, coordinate sampling, randomized Kaczmarz, and scalar random curvature have been checked for implication, not just wording. No inspected result dominates the exact claim; an unindexed specialized statement remains possible.

## Value — PASS

The motivating source distinguishes faster *expected iterates* from bounds on expected squared solution error, so a sharp actual-risk frontier resolves a meaningful algorithmic uncertainty. The calculation provides a necessary-and-sufficient stability region at every Gaussian block width, a unique optimal fixed-parameter rate, and a concrete parameter choice for which the mean contracts yet the mean square diverges. This is a structural limitation of the published unnormalized randomized method, rather than an arbitrary parameter recomputation. It does not promise multidimensional or adaptive no-acceleration.

## Closest literature and scientific limitations

Primary comparisons: Han–Xie (arXiv:2208.05437), Loizou–Richtárik (arXiv:1712.09677), Kidambi et al. (arXiv:1803.05591), Bollapragada–Chen–Ward (arXiv:2206.07553). Exactness is restricted to one-dimensional consistent systems with independent standard-normal unnormalized sketches and fixed finite width; possible obscure identical analyses remain a priority risk. No independent audit is represented.

Self-review: passed. Independent audit: not yet performed.
