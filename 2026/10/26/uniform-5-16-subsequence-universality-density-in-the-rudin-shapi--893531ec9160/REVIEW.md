# Scientific review: Uniform \(5/16\) subsequence-universality density in the Rudin–Shapiro word

## Correctness — PASS
The binary-digit definition yields the four-state substitution via the two identities for even and odd indices. The arch-counting procedure computes the fixed-binary-alphabet subsequence-universality index. The complete three-input-state transfer table is directly checked at level four and propagated inductively by the four substitutions; this yields all integer levels, not an extrapolation from a finite test. An aligned dyadic partition has at most two blocks at each scale, and the block estimate holds for an arbitrary entering state. It follows that every factor has the uniform stated discrepancy. The exact dyadic formula is the `a`-block entry in the same table. The standalone checker verifies the finite bases, algebraic transfer recurrences, independent binary-digit coding, and many direct subsequence tests.

## Originality — PASS (with residual literature uncertainty)
The closest primary works inspected are Barker et al. (arXiv:2003.04629), Schnoebelen–Veron (arXiv:2304.11932), and Meleshko et al. (arXiv:2207.10171). Their statements concern general arch algorithms, compressed-word signatures, and pseudoperiods, respectively. None of the inspected relevant sections asserts the uniform Rudin–Shapiro factor density or computes the exact dyadic correction. Public mathematical-record comparisons also located results on Rudin–Shapiro string attractors and the distribution of universality over **all** binary words, whose statements do not imply the present deterministic sequence-specific bound. No search can exclude every unpublished or unindexed equivalent formulation.

## Mathematical value — PASS
The result identifies a natural exact asymptotic density, \(5/16\), of universal scattered-subsequence coverage across **every** long factor of a classical automatic word, with an explicit finite-size error uniform in the factor location. It also gives a parity-sensitive exact formula at all dyadic scales. This measures a concrete deletion-robustness invariant rather than recoding a previously tabulated statistic. The substitution transfer lemma is structural and independently reusable for studying other morphic words; no new general theorem beyond the proved one is claimed.

## Limitations
The optimal size of the error term is not resolved. The result concerns the fixed binary alphabet and the classical Rudin–Shapiro word, not arbitrary automatic sequences. Exact computations support but do not replace the induction. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
