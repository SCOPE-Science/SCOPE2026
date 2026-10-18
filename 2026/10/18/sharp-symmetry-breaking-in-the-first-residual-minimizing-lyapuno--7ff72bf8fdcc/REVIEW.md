# Scientific assessment: two-mode ADI residual-shift bifurcation

## Correctness — PASS

The Lyapunov ADI rank-one residual factorization is verified by direct multiplication. Equal spectral forcing masses reduce its Frobenius norm to the sum of two squared real Cayley factors. An explicit bijective Cayley coordinate and a derivative with affine sign determine every critical point globally, including a quartically flat uniqueness boundary. The claimed factor-two supremum follows from a strictly positive rational derivative. The exact witness has rational entries and radical minimizers. The executable confirms 3,722 algebraic/numeric assertions; finite probes are not substituted for the exact proof.

## Originality — PASS, with limited publication-priority risk

Established ADI residual factorization and the **general** data-dependent residual minimization problem are credited to the motivating and earlier literature. The examined 2018 shift-optimization full text formulates a general numerical minimization but does not state the two-active-mode balanced-mass threshold \(7+4\sqrt3\), a geometric-mean *local maximum*, the two reciprocal global minimizers, or the sharp ratio approaching \(2\). The examined 2014 article differentiates classical spectral minmax shifts and residual-sensitive heuristics without the exact bifurcation. The examined 2024 ADI framework concerns derivations and connections of ADI-like algorithms, not this exact global shift classification. Related indexed mathematical-record queries did not locate a covering theorem; failure to retrieve a result is not proof of absence, and an unindexed equivalent calculation remains possible.

## Value — PASS

First-step residual minimization is a central algorithmic component of large-scale Lyapunov ADI. The theorem reveals a nontrivial global bifurcation exactly where the classical geometric-mean spectral-minimax shift ceases to be merely suboptimal and becomes locally maximally bad for the measured residual. The precise condition-number threshold, two optimizers, and sharp near-twofold penalty are meaningful analytic guidelines and adversarial benchmarks for adaptive shift strategies; they are not a cosmetic reformulation of the general optimization objective.

## Scope and remaining risks

One step, real negative shift, exactly two distinct active eigenvalues and balanced rank-one forcing, with arbitrary eigenspace multiplicities. Full-text priority comparison was performed for the highly relevant 2024 and 2018 arXiv papers and the 2014 published article. Other unindexed treatments of the same special case remain a possible priority limitation. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
