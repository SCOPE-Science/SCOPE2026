# Scientific review

## Correctness — PASS

The claimed numerical family is reproduced directly from equation (29) of the motivating source. Its characteristic matrix is computed from the recurrence for every positive integer lag. A Schur polynomial \(\sigma\), an exact boundary positive-real identity for \(\rho/\sigma\), and a harmonic minimum-principle argument control each diagonal factor outside the unit circle. Perron–Frobenius comparison with \(D^{-1}B\) proves sufficiency. The threshold and its unstable side follow by evaluating at one and continuously varying an explicitly nonnegative real matrix. The three-node witness is established with an exact symmetric characteristic polynomial and an exact all-parameter lower bound. The included symbolic and finite numerical checks succeeded. The proof does not require numerical root enumeration for infinitely many parameters.

## Originality — PASS, subject to historical-priority uncertainty

The October 2026 paper establishes the scalar stability disk and a generalized-field-of-values **sufficient** test (Theorem 3.8 and Corollary 3.9); it does not state the necessary-and-sufficient Perron-root criterion for all nonnegative networks nor a single pair that escapes every real-power numerical-range test. The explicit witness demonstrates that their sufficient hypothesis is not equivalent to the new criterion. The 2024 IMEX–BDF article analyzes different scheme coefficients. Castro and coauthors' 2019 exact/nonstandard difference schemes require commuting matrices and use a different scheme; the current graph class includes noncommuting pairs. Rosales and coauthors' 2017 unconditional ImEx analysis provides general theory for nondelay schemes. Published research-record and accessible prior-claim comparisons showed no matching claim, but historical coverage is not exhaustive; the 2019 full publisher page returned an access error, and the 2017 full manuscript was not materially inspected. Neither limitation is evidence of originality on its own.

## Mathematical value — PASS

The result gives an **exact**, dimension-independent network stability test preserving the classical positive-system gain threshold under all admissible discretization parameters. It separates a spectral-radius condition from all one-exponent field-of-values sufficient tests in a concrete noncommuting three-node network. It is useful when a generalized numerical-range condition rejects an actually stable coupled DDE discretization and supplies a clean benchmark for numerical-stability certificates. The classic continuous-time threshold is not claimed to be new; the contribution concerns exact preservation by this specific second-order family and its certificate gap.

## Closest literature and boundaries

J. Rodríguez-Gutiérrez and J. Martín-Vaquero, arXiv:2610.33780v1, sections 2–4; A. Tercero-Báez and J. Martín-Vaquero, arXiv:2412.12297v1, sections 2 and 5; M. Á. Castro et al., *Mathematics* 7 (2019) 1038; R. R. Rosales et al., SIAM J. Numer. Anal. 55 (2017) 2336–2360; classical positive-delay systems and M-matrix tests. The proof applies only to constant grid-aligned delays, nonnegative delayed coupling, and the specified \(0<\beta<1\) family. It does not assert nonlinear stability or floating-point preservation.

Self-review: passed. Independent audit: not yet performed.
