# Scientific review

## Correctness: PASS
The proof explicitly defines the data matrix, Gaussian sketch, pivot, row projection and comparison norm. Direct Gram diagonalization yields the global rank-one optimum; direct rowwise projection gives exact losses for every possible pivot. Orthogonal Gaussian sum/difference coordinates yield an independent normal ratio, whose standard Cauchy law gives the exact pivot probability. The reciprocal-arctangent asymptotic gives the unbounded expected ratio. The standalone verification script passed exact rational identities and independent angle counts. No finite sample is used in place of an infinite proof. Boundaries \(t=1/2\), \(t\to\infty\), and arbitrary positive sketch-column count are explicitly handled.

## Originality: PASS, qualified
The self-review includes searches for Cauchy Gaussian sketch pivot failure, one-column LU row skeleton selection, unbounded expected first-pivot approximation loss, exact row-skeleton parameter families, and aliases. Relevant primary material was inspected: Pearce et al., arXiv:2310.09417 (sketch+LUPP, Sections 2.4, 3.1, 4.1, numerical appendix); Dong et al., arXiv:2309.16002 (adversarial sampling and sketchy LUPP comparison); and Pan et al., arXiv:1406.5802 (Gaussian range projection, Section 7). The former studies full algorithms but does not provide the displayed sharp first-pivot Cauchy classification; the latter uses an orthogonal range projector rather than an original-row selection. Prior internal exact spike-sketch results concern continuously projected ranges, not discrete max-score row pivot selection. These comparisons do not prove universal novelty; specialized earlier pivoting arguments remain a residual literature risk.

## Value: PASS
The simultaneous high-probability success and unbounded expected squared-error ratio is a substantive limitation of a natural primitive used in fast randomized row IDs. The sharp invisibility threshold and sketch-width invariance explain why extra columns alone do not change the *first* pivot's tail, while not claiming that oversampling cannot help a complete algorithm. The example is nonnegative, full column rank and fixed at the smallest dimension with three distinct row choices. The distinction between selecting a basis row and directly projecting onto the whole random sketch is essential, rather than a renaming of a standard bound.

## Limits and closest comparisons
One selected row, exact arithmetic, iid real Gaussian sketch, squared Frobenius loss, and optimal refitting after first pivot. No claim about any complete adaptive rank-selection algorithm. The classical Cauchy and Eckart--Young ingredients are known; publication precedence for this exact use of those ingredients is not independently certified.

Self-review: passed. Independent audit: not yet performed.
