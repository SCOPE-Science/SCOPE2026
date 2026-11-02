# Scientific review: sharp two-scale generalized Petersen spectral design

## Correctness — PASS
The theorem defines independent nonnegative edge conductances on \(GP(n,2)\), all integer sizes \(n\ge13\), and a total budget of \(n\). The proof uses a rigorously checked Rayleigh upper certificate for arbitrary, potentially nonuniform weights; its strict gap is reduced to a positive elementary trigonometric inequality. For the lower bound, cyclic Fourier diagonalization yields exact \(2\times2\) blocks, explicit low- and half-frequency limits, and a uniform bound excluding all intermediate modes. Expanding the isolated first mode gives the claimed \(n^{-3}\) correction. Necessity of the spoke scale and parity-dependent rim threshold follows from trial quotients and a sharp scalar minimization. The Python checks are finite corroboration only and do not substitute for the argument.

## Originality — PASS on inspected evidence
Dudek (arXiv:1412.3531v1; Dec. 11, 2014) and Gera–Stănică (2011) provide unweighted generalized Petersen spectra; Boyd (2006) provides a general spectral optimization framework; Shakeri et al. (arXiv:1510.06785v1) optimize links between fixed layers. None of their inspected statements implies the unrestricted, all-edge, parity-sensitive two-term optimum here. Beenker–van Lint (1988) study generalized Petersen extremality in graph size and diameter rather than this objective, based on the checked opening page. Public related-results searches and the available historical claim ledger did not locate equivalent conductance results. This is a qualified, same-authority evidence assessment, not a priority guarantee. The complete scanned 1988 article was not read, and specialist overlapping literature remains a residual risk.

## Mathematical value — PASS
The model poses a natural optimal allocation of edge conductance for algebraic connectivity, connecting global spectral performance to budget-splitting across three structural edge classes. The sharp two-term optimum exposes an \(n^{-1}\) spoke scale and separate parity-dependent \(n^{-2}\) stabilizing thresholds for the outer edge family. The result supplies an explicit near-optimal construction without artificially restricting the competitor class to symmetric weights.

## Limitations
The proof gives a two-term asymptotic optimum, not the exact finite-size maximizing conductances or their uniqueness. It treats only \(GP(n,2)\) for integers \(n\ge13\) with equal edge prices, and no unrelated stability or stochastic mixing theorem follows. The verifier checks finitely many graph sizes and numerical examples. No independent mathematical audit or external priority confirmation has been performed.

Self-review: passed. Independent audit: not yet performed.
