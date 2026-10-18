# Review of the anisotropy-invariant Walsh projection theorem

## Correctness

**PASS.** The domain is the real finite weighted Hamming cube with strictly positive weights; the range is the span of nonconstant Walsh characters vanishing at the chosen basepoint, for a support invariant under a transitive group of coordinate permutations. Translation by coordinatewise sign multiplication remains isometric for every weight vector. Averaging arbitrary projections therefore reduces the minimization to the unique Fourier spectral projection. The Lipschitz norm is exactly the maximum of weighted edge gradients. Restricting each gradient to its coordinate fiber gives the \(L^1\) directional-kernel upper bound. A normalized sign-gradient in a least-weight coordinate is globally Lipschitz because every transverse edge is at least that long; it attains the directional upper bound. Spectral transitivity makes all directional norms equal. The binomial specialization follows by exact sign counting, and the finite checker verifies selected rational cases independently of the universal analytic proof.

The norm proof was reconstructed for arbitrary \(n\geq2\), positive weights, all permitted spectral families, including the zero-kernel/sign convention and degree endpoints. Nothing about untested dimensions or arbitrary weights is inferred from enumeration.

## Originality

**PASS, subject to the stated literature risk.** The nearest inspected primary theorem on Walsh spectral projection constants, Defant et al. (arXiv:2302.00233, Theorem 3.1), works in the supremum norm; it does not compute relative projection norms for anisotropically weighted Lipschitz geometries. Cúth–Doucha (arXiv:2104.11519, Sections 3–4) obtain projections onto orbit-invariant Lipschitz subspaces, rather than onto nontrivial Walsh spectral isotypic sums, and supply no directional sharp constant. Neither statement, nor their conjunction without the explicit least-weight gradient construction, covers the all-weight equality claimed here. Classical translation averaging and the unweighted Walsh/Krawtchouk ingredients are acknowledged as prior tools, not claimed as new results.

Searches for weighted Walsh projection, anisotropic Hamming Lipschitz projection, Fourier spectral projections and equivalent derivative-kernel formulations did not uncover a covering published statement. The remaining risk is a differently indexed treatment of anisotropic Boolean Lipschitz multipliers, or that the weight-insensitivity is implicitly obtainable by adapting an unweighted argument. A negative search is not a proof of novelty.

## Mathematical value

**PASS.** The theorem exactly computes the relative projection constant of every coordinate-transitive Walsh spectral space on **every** finite weighted Hamming cube, rather than only a special example or an unweighted instance. The key structural assertion is complete insensitivity to arbitrary positive coordinate anisotropy—even where coordinate permutations cease to be isometries. This is not generic for nontransitive spectral supports. The result applies to all homogeneous spectral degrees, arbitrary transitive support groups, and unbounded weight ratios, and produces exact Krawtchouk evaluations. These are natural geometric invariants of finite Lipschitz spaces, with an explicit attaining projection and extremizing Lipschitz functions.

## Closest literature and limits

Defant et al. provide supremum-norm spectral projection constants; Cúth–Doucha provide general group-action complementability. The present theorem is a finite real Lipschitz statement. The proof does not claim general nontransitive weight-independence, arbitrary metric products, or absolute projection constants. Reproducible finite checks support but do not replace the analytic proof.

Self-review: passed. Independent audit: not yet performed.
