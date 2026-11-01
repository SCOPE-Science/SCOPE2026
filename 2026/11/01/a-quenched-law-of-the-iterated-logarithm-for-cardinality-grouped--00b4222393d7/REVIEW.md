# Scientific review

## Correctness — PASS

The conditional parity identity follows by counting odd binomial coefficients with Lucas's theorem. Conditional on the complete sign trajectory, independent environment rows yield independent bounded signs whose means have magnitude at most \(q^{2^{w(S_n)}}\). The count process visits a sparse set of low-binary-weight integers only \(N^{o(1)}\) times almost surely, by geometric holding-time bounds and binary counting. Consequently the means contribute \(N^{o(1)}\), the centered conditional variance sum is \(N-N^{o(1)}\), and Kolmogorov's bounded non-identically distributed iterated-logarithm theorem proves the two-sided limit. Fubini and the bounded-jump martingale functional central limit theorem establish the precise quenched conclusion. A standalone exact checker passed 12,002 assertions; it is supplementary and does not purport to verify infinite convergence by enumeration.

## Originality — PASS, with historical limits

Hamza and Tournier, arXiv:2610.01658v1, Section 4.2, state annealed normality for independent time levels and leave quenched normality open in the adjacent remark. Their Section 3 result assumes independent subset coefficients, whereas the present coefficients are identical within each cardinality class. Their Section 5 treats a different, totally-unordered basis. Collevecchio et al., arXiv:2010.16000, supply the general limit criterion without proving the conditional bracket limit in this random cardinality-grouped case. Independent-time fully uniform Boolean-function constructions are less constrained than the cardinality-grouped model and do not imply the present statement. Searches for quenched one-factor bootstrap normality, cardinality-based Bernoulli transforms, and the source's unresolved Corollary 9 case revealed no directly covering result. Search visibility is not proof of priority, and unindexed work remains a residual risk.

## Mathematical value — PASS

This settles a clearly identified quenched-versus-annealed gap for a natural class of random adapted transformations, under the source's full elliptic independent-time assumptions. The more precise law of the iterated logarithm identifies the optimal almost-sure fluctuation envelope of the predictable cross-variation, rather than merely proving asymptotic decorrelation. The binary-digit sparsity mechanism also explains why only a polynomial number of random coefficients per time level suffices for pathwise normality despite their strong within-level sharing.

## Boundaries

No statement is made for dependent time rows, vanishing ellipticity, or the time-constant coefficient model. No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
