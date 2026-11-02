# Scientific review

## Correctness

PASS. The reduction uses the exact discrete 1-form for **three-color cyclic cellular automata** in Theorem 3 of Gravner, Lyu and Sivakoff (2016), rather than the different Greenberg--Hastings form. Integer graph integration proves a bijection with rooted one-Lipschitz heights, including the factor three for the root color. The three-entry vertical difference and zero Fourier coefficient enforce every cyclic closure. The determinant factors into one linear and one quadratic term; its unique Fourier spectral maximum gives the stated Gaussian factor and the open-versus-closed ratio. Two separately implemented exhaustive checks agree for all \(597780\) prism configurations across \(n=3,4,5,6\), and the open-ladder count is also checked directly through six rungs; longer exact transfer runs independently corroborate the asymptotic ratio. The derivation covers every integer \(n\ge3\).

## Originality

PASS, qualified. Gravner--Lyu--Sivakoff's full accessible primary text supplies a general topological criterion and an upper bound, but does not compute the circular-ladder coefficient sequence, exact transfer polynomial, spectral constant, or cyclic-seam comparison. Searches for circular-ladder CCA, zero-winding height enumerations, and the first terms did not identify an equivalent primary result or known table. The closest accessible published material treats different graph families or different dynamics. A hidden earlier transfer-matrix enumeration under height-homomorphism terminology is a residual risk. The general irrotationality criterion and standard transfer-matrix technique are acknowledged, not claimed as new.

## Mathematical value

PASS. The exact probability that a uniformly randomized finite excitable network synchronizes is a natural invariant. The theorem replaces a general qualitative cycle criterion with an exact expression for an infinite canonical family, identifies its algebraic exponential rate, and isolates the additional square-root penalty caused by one global winding constraint. Comparison with a graph of equal vertex count but open ends makes the topological effect explicit and quantitatively usable. The fact is not a single-parameter recomputation or a small finite enumeration.

## Closest source and limitations

Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, Theorems 3 and 5, first available 2016-10-24. Only the three-color CCA synchronization basin is counted. Other attractor types and Greenberg--Hastings dynamics are out of scope. The original literature comparison cannot rule out every unindexed earlier height-function enumeration.

Self-review: passed. Independent audit: not yet performed.
