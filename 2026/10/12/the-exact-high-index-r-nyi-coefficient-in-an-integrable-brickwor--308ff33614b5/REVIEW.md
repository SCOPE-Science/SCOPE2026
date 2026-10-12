# Scientific review

## Correctness — PASS

The conclusion is a two-sided bound for the full coherent coefficient matrix, not a sum of separate branch entropies. The published source establishes count-orthogonal row/column projectors and the flat nonzero singular values for each count branch. For each fixed count difference, the blocks form a direct sum and thus have exactly additive \(2\alpha\)-Schatten moments. The centered binomial maximum and a uniform convolution estimate give the difference-block upper bound, while a convergent exponential difference sum and the Schatten triangle inequality handle coherent cross-difference interference. Averaging count phases contractively projects onto the diagonal, where a positive-density central binomial window yields the matching moment lower bound. The argument covers every fixed real \(\alpha>1\) and specifies logarithm normalization and infinite-volume-before-long-time quantifiers. The packaged program independently checks the finite-count premises through time four; the proof, not the numerical checks, establishes the asymptotic result.

## Originality — PASS, with documented residual risk

The original flat branch spectra and general \(\Theta(\log t)\) assertion belong to Pozsgay's published work. In the full publicly available arXiv manuscript, Section IV C, Eq. (S51), the coefficient is explicitly left open for finite \(\alpha>1\). The derived exact coefficient follows from a new coherent-block strategy: sum Schatten norms along fixed count difference, then pinch the count diagonal for a matching exponent. Searches for exact-coefficient aliases, source parameters, finite-index Rényi moments, and neighboring published claims identified no stronger covering theorem. Nearby operator-entanglement work on Yang–Baxter classifications and classical simulability studies different conclusions. The September 4 preliminary version's PDF could not be opened, so it and unindexed implicit derivations remain residual priority risks; the specific unresolved statement in the later full source nonetheless provides direct positive evidence of a gap.

## Value — PASS

The model's coexistence of square-root von Neumann growth and logarithmic high-index growth is a central diagnostic of its broad entanglement spectrum. Resolving the *coefficient for every fixed high index*, rather than merely confirming logarithmic order, yields the exact purity coefficient \(3/2\), a testable all-index curve, and a precise complement to the established endpoint coefficient one as \(\alpha\to\infty\). The same argument treats a physically different product-state quench. No general theorem for unrelated integrable circuits is asserted.

## Closest literature and limits

The principal comparison is Pozsgay, arXiv:2609.39401, supplementary (S38), (S51), and its September 4 preliminary Zenodo record 22306151. See also arXiv:2609.05121 and arXiv:2603.05656. Fixed \(\alpha>1\) and infinite-volume-first are essential. The proof does not determine exact Rényi moment constants or the vicinity of the critical index one.

Self-review: passed. Independent audit: not yet performed.
