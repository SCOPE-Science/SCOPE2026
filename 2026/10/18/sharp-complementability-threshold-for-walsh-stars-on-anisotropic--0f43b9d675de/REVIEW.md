# Scientific review

## Correctness — PASS

The exact projection norm is proved rather than guessed from numerical tests. Averaging over the weighted-cube translation group reduces the unrestricted projection problem to its unique invariant Fourier projection. The first-coordinate gradient is an extremal linear functional over bounded one-Lipschitz functions on a smaller cube. Permutation and antipodal symmetrization reduce this to radial levels; nested pairs of levels produce a sharp pointwise bound, attained simultaneously by a clipped affine function. The remaining coordinate gradients are contractive rank-one Walsh projections. The elementary random-sign second-moment identity gives the precise norm-one threshold. An independent full-edge linear program matched the result in 24 finite instances; these experiments are not substituted for the universal proof.

## Originality — PASS; residual literature risk

Defant et al. (arXiv:2208.06467, Theorem 8.1.1; arXiv:2302.00233, Theorem 3.1) optimize projections in the sup-norm of Boolean functions. Their norms and outputs are insensitive to the edge length \(w\), unlike this theorem's Lipschitz metric. Hájek and Russo (arXiv:2102.02778) study polynomial subspaces of Lipschitz functions on continuous Banach balls, with results not specializing to the finite anisotropic cube. A previous unit-weight Walsh edge-gradient formula covers the \(w=1\) slice but gives no all-weight sharp phase transition. Targeted searches found no equivalent weighted Walsh-star norm formula. Undiscovered equivalent calculations remain a risk; absence from searched resources cannot prove uniqueness.

## Mathematical value — PASS

This supplies a closed finite binomial expression valid for every dimension and every positive continuous metric parameter, plus an exact necessary-and-sufficient condition for norm-one complementation. The transition at \(w=m\) is structural: changing one coordinate length moves the same Fourier subspace from noncontractive to contractive complementability. This is a natural relative projection invariant rather than an arbitrary isolated finite computation, and the clipped extremizer explains the transition.

## Scientific limits

The theorem is restricted to real functions, a single variable coordinate weight, and a star Fourier spectrum. No complex extension or classification of all minimizers is claimed. The finite LP checks use floating point, so are not formal certificates. Independent mathematical assessment remains necessary.

Self-review: passed. Independent audit: not yet performed.
