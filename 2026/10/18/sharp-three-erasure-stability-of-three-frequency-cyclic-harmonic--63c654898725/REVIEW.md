# Scientific assessment

## Correctness — PASS
The cyclic Fourier rows are orthonormal. A unimodular column rotation makes each erased three-column Gram matrix real with off-diagonal kernel \(1+2\cos(2\pi h/N)\). The retained lower frame bound is one minus its top eigenvalue divided by \(N\). For \(N\ge8\), strict entrywise/Perron comparison against the consecutive triple proves uniqueness of the worst geometry. The exceptional six- and seven-cycle inequalities are handled separately with explicit exact bounds. The middle-symmetry eigenvalue formula is reconstructed algebraically, and retained spanning follows from a three-column Vandermonde minor. The packaged standard-library program independently tests all \(211861\) three-site erasure patterns over orders \(6\) through \(48\).

## Originality — PASS (best knowledge)
The closest exact indexed result for two-row harmonic frames determines worst erasures in a genuinely different two-dimensional space. The closest exact three-row Riesz result minimizes a ratio of Gram eigenvalues, not the single largest eigenvalue determining our fixed-size erasure loss. The reviewed 2018 publications concern random-subset expected moments, uniform-subframe-bound characterizations, and general clustered-node bounds, respectively. None of these inspected results gives or logically forces the sharp formula and all \(N\) three-erasure maximizers. A historically unindexed finite-prolate statement with exactly these quantifiers remains a concrete residual risk, not evidence of coverage.

## Mathematical value — PASS
Worst-case loss of a small number of sensor readings is a canonical stability question for an oversampled Fourier frame. The theorem resolves the first nontrivial three-row, three-erasure instance for every cyclic order, gives a closed sharp noise-amplification bound and proves a unique geometric obstruction (three adjacent losses). The proof handles the sign-changing Dirichlet kernel rather than assuming an unjustified continuous rearrangement principle. The result has an exact, nonlocal combinatorial equality classification and is not just an evaluation for a chosen mask.

## Boundaries and related work
The result does not extend to arbitrary frequency bands or arbitrary numbers of erased coefficients. Finite tests supplement the analytical argument and do not establish the infinite claim. Closest results: Haikin–Zamir–Gavish (arXiv:1801.04548), Cheng–Lv–Sun (DOI:10.1016/j.laa.2018.05.025), Batenkov–Demanet–Goldman–Yomdin (arXiv:1809.00658), and the two published specialized Fourier-frame results named in RESULT.md. Literature equivalence beyond inspected indexed sources is a risk.

Self-review: passed. Independent audit: not yet performed.
