# Scientific review

## Correctness

**PASS.** The precise unnormalized Gaussian-Hermite definitions imply the displayed Gram matrix by fourth moments. Three explicit orthonormal vectors give the entire scaled spectrum. A common-denominator Rayleigh argument, exploiting identical coordinate magnitudes of the extreme eigenvectors, proves the global lower bound over all positive diagonals and its equality case. The Jacobi spectrum gives the exact asymptotic coefficient. The accompanying symbolic and numerical checker passed, but the global theorem depends on the proof, not finite sampling.

## Originality

**PASS within historical-priority limits.** The raw covariance-dependent Gram entries are not new: they occur explicitly in the prior full-text source by Lyman (2026) and follow from Rahman (2017) and Lyman–Iaccarino (2021). The claimed new fact is the *global diagonal-congruence condition-number optimum* (unique, independent of correlation) together with the exact \(9/8\) near-degeneracy gap over variance-normalization. General optimal diagonal-scaling algorithms, including Qu et al. (2022), solve a larger class procedurally but the inspected material does not already state this closed-form special-family optimum. The residual possibility that symmetric-square literature implies the formula by another name remains.

## Value

**PASS.** A weakly orthogonal correlated-chaos mass block is an actual finite subsystem in stochastic Galerkin coefficient recovery. The best attainable diagonal conditioning is a natural sharp invariant; the covariance-independent \(\sqrt2\) scale provides an exact benchmark and shows the standard unit-variance normalization is not universally optimal. The result is a meaningful closed classification of the minimal nontrivial degree-two block, not a gain claimed for generic full PDE solvers.

## Closest sources and limits

Rahman (2017), Lyman–Iaccarino (2021), and Lyman (2026) give definitions and moment identities; Qu et al. (2022) supplies general diagonal optimality machinery. The result neither rediscovers these moments as new nor claims better conditioning than dense whitening. It is restricted to two correlated standard Gaussian inputs, the degree-two block, and positive diagonal congruences. A specialized historical equivalence remains possible.

Self-review: passed. Independent audit: not yet performed.
