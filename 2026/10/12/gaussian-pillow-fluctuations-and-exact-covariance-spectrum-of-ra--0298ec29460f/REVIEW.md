# Scientific review

## Correctness — PASS

The deterministic permutation-matching covariance identity gives the exact finite-mesh separable kernel. Uniform convergence of the one-dimensional kernel follows from an explicit within-cell variance correction, without exchanging unproved limits. The independent-exponential representation provides a genuine triangular-array Lyapunov central limit theorem: the third-moment remainder is bounded by a constant times \(k^{3/2}/\sqrt{k!}\). Eighth-moment increment estimates, uniform in \(k\), establish tightness in continuous functions on the square; the scalar Dirichlet normalization is asymptotically one. The tridiagonal inverse gives the spectrum, and a summable Chebyshev–union bound plus Borel–Cantelli establishes the unscaled uniform almost-sure assertion. The standalone checker tested finite kernels, eigenpairs, and simulated variance. These checks supplement, not replace, the infinite-dimensional proof.

## Originality — PASS, with priority limits

The full 2026 *Random discrete copulas* article defines the exact model and proves pointwise mesh variance; its Lemma 4.2 reduces its covariance to the random-permutation law, so those ingredients are acknowledged. The full article's conclusion expressly proposes mesh-limit convergence as future work. It does not supply the explicit continuous covariance kernel and sine spectrum or a factorially rescaled weak limit in the supremum topology. Relevant general Dirichlet-Gaussian and exchangeably weighted empirical-process work was compared by implication: general finite-dimensional normal approximation does not itself state this exact model-dependent functional result; however, a sufficiently general already published functional theorem might imply it after checking hypotheses. Uniform Birkhoff matrices are a different probability law. Targeted published-result comparisons yielded no explicit covering statement; negative search is not proof of global novelty. Unindexed/contemporaneous priority remains a residual risk.

## Value — PASS

The originating article identifies growing-mesh convergence as an open direction. The theorem supplies its strong unscaled answer and, critically, identifies the unique factorial standardization that reveals a nondegenerate continuous Gaussian field. The exact tensor covariance and finite-grid eigenmodes enable uncertainty quantification and spectral simulation of the random copula field. Neither generic variance decay nor a pointwise law determines these functional and spectral properties.

## Limits of this review

This examination is confined to the stated Dirichlet permutation-mixture model, and neither asserts an independent audit nor claims novelty from a failed search. The complete text of one broad exchangeably weighted empirical-process antecedent was not inspected and remains a scholarly-priority risk. All finite computations were replayed from the accompanying source; none is treated as an infinite-dimensional certificate.

Self-review: passed. Independent audit: not yet performed.
