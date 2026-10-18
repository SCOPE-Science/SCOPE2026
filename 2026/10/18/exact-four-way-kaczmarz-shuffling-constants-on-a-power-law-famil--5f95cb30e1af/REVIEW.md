# Scientific review

## Correctness
PASS. The full-rank paired-row construction gives Gram eigenvalues \(1\pm c_j\). Rank-one orthogonal-projector products turn the squared Frobenius error into the exact count of row-label switches. SS, RR and FlipFlop have explicit switch counts; the IID count is binomial, with conditional independent fair switches. The finite inequalities follow from \(c^2\le h\le1\), \(h\ge c\), Jensen, and positivity. A monotone quadrature estimate of order \(N^{-1}\), dominated convergence after \(\lambda=v/t\), and \(t^\beta/N\to0\) establish all four leading constants. The standalone program passed 414 checks, including rational exhaustive cases. Finite checks are supporting evidence only.

## Originality
PASS, subject to ordinary unindexed-literature risk. The primary 2026 power-law SGD paper gives precise Gaussian-model constants at exponent \(1/2\) but does not contain the present coherent-pair four-policy finite formulas or the exponent-dependent \(2^\beta\) advantage. Earlier SS-versus-RR matrix inequalities and a general RR rate theorem do not imply the stated four-way constants. Published mathematical research records were searched for aliases, paired row projections, gamma constants and four-policy shuffling profiles; the closest two-row Kaczmarz record concerns a different relaxed cyclic finite-horizon operator-norm question. A result hidden in broader alternating-projection or shuffling literature remains possible.

## Value
PASS. The 2026 motivating paper explicitly asks how sampling constants behave for general power-law spectral edges. The construction supplies a fully solvable non-Gaussian benchmark with finite-sample comparisons for four widely used policies, including RR, and computes how the strong shuffle advantage scales with the spectral exponent. It isolates the role of row coherence in addition to the spectral CDF. It neither claims that the local two-projection identity is new nor claims universality from one family.

## Scope and residual risks
The family is paired, consistent, row-equilibrated, and uses exact orthogonal Kaczmarz projections with isotropic initialization. The limit requires growing dimension and epochs jointly. The source paper's formal positive-gap conjecture is not disproved; only an exponent-independent numerical interpretation of its Gaussian ratio is excluded for this family. Further literature may contain an equivalent paired-row aggregation or asymptotic constant calculation.

Self-review: passed. Independent audit: not yet performed.
