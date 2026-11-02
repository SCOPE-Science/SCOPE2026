# Scientific review: least-prime-factor distribution of nice integers

## Correctness — PASS

The cited criterion is an exact equivalence for every integer \(n>1\), not merely a necessary condition. Counting prime multiples and distinct pairs gives the displayed first and second moments with floor errors bounded by \(\pi(z)\) and \(\pi(z)^2\). Choosing \(z=\lfloor X^{1/3}\rfloor\) loses at most two distinct large prime factors, so the variance bound \(O(X\log\log X)\) follows without an unproved normality hypothesis. Chebyshev gives an exceptional set of size \(o(X/\log\log\log X)\). Outside this set, the published exact criterion traps nice integers between two least-prime-factor thresholds. Inclusion–exclusion is accurate because \(2^{\pi(y)}=o(X/\log\log\log X)\) for \(y\) any fixed power of \(\log\log X\). Mertens' product supplies the constant \(e^{-\gamma}\); the separate cases \(t<1\), \(t=1\), \(t>1\) cover the threshold boundary. The finite verifier checks algebraic identities but is not substituted for infinite estimates.

## Originality — PASS, with residual risks

Adenwalla's 2025 Sections 3–5 prove necessity, analyze coverage of integer residues for individual congruence sets, and pose sufficiency. Jia–Li's 2025 Theorem 2 and Sections 3–4 settle residue-assignment existence, but neither work states a counting asymptotic of \(n\le X\) nor a conditional Pareto distribution of \(\log P^-(n)\). The old disjoint-progressions paper concerns optimizing families of arbitrary distinct moduli rather than counting integers satisfying the entire divisor-moduli property. No equivalent statement appeared in targeted literature/record comparisons. The structural characterization combined with Mertens implies the new theorem **only after** the written concentration, threshold-sandwich, and fixed-tail arguments; known classification alone is not the claimed distributional result. The primary residual risk is an unpublished/unindexed corollary giving the same law, not a known stronger result.

## Mathematical value — PASS

The existing combinatorial theorem classifies qualifying integers but leaves their typical size and prime-factor geometry undetermined. The new result supplies their exact zero-density decay scale, universal leading constant, and a nondegenerate heavy-tailed conditional limit distribution, showing that prime-factor thresholds at distinct fixed powers of \(\log\log X\) retain different asymptotic masses. This is a natural global invariant of the full solution family, not a one-off small cutoff or a mere restatement of the criterion. It does not solve the covering problem again or assert a universal effective error rate.

## Closest literature and limitations

The closest sources are Jia–Li, arXiv:2504.09579 (complete criterion) and Adenwalla, arXiv:2501.15170 (necessary condition and original conjecture). Classical Mertens estimates provide arithmetic input, not the conditional limiting law. A similarly titled 2013 study of pairwise-disjoint progressions counts a different optimization parameter. Fixed \(t\) is essential; unindexed prior treatments remain possible.

Self-review: passed. Independent audit: not yet performed.
