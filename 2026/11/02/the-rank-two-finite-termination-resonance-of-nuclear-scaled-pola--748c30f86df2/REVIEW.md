# Self-review

## Correctness — PASS
The exact thin-SVD update is \(E_+=U\operatorname{diag}(s_i-t\sum_j s_j)V^\top\). Differentiating the one-variable quadratic along the nuclear-scaled polar direction gives the exact line-search parameter \(t=1/r\). For rank two this centers two positive singular values and makes their absolute deviations equal, hence the next step is zero; for rank three and above the positive two-level spectrum \((1,\ldots,1,r-1)\) is an invariant geometric ray of factor \((r-2)/r\), never reaching zero. Equal initial singular values force any universally terminating fixed step to use \(t=1/r\). The rank-discontinuity formula follows from two explicit diagonal updates. The rational and dense-matrix checks reproduced from `verify.py` passed (7,401 checks). These checks are finite corroboration, not an infinite proof.

## Originality — PASS within the inspected comparison
Jawanpuria–Garai–Mishra, arXiv:2610.27747v1, prove general nuclear-scaled linear convergence, identify line-search normalization, and give immediate termination only on selected equal-spectrum invariant rays; their Appendix C explicitly leaves general directional dynamics unresolved. Lau–Long–Su, arXiv:2505.21799v4, develop the polar optimizer and its rank-dependent rate bounds; Gonon–Muşat–Boumal, arXiv:2602.11948v1, address unscaled polar updates. None of those inspected materials states or dominates the all-rank finite-termination classification plus the two-step rank-two theorem. Searches for singular-value mean-centering, spectral-norm steepest descent, rank-two termination, and corresponding mathematical research records found related but mathematically different results. An older specialized sign-descent theorem might cover a diagonal analogue, so historical-priority risk is not zero.

## Mathematical value — PASS
The exact line-search choice is natural, not an arbitrarily tuned special case; the result provides a complete rank dichotomy for whether that geometrically motivated descent algorithm uniformly terminates. Rank two exhibits an exact algorithmic speedup from nonlinear spectral equalization; rank three already defeats finite termination despite geometric convergence. The discontinuity quantifies why rank-two behavior cannot be assumed robust under small rank-raising perturbations. This improves understanding of the finite-step behavior beyond general linear-rate guarantees.

## Remaining limitations
This is exact-arithmetic isotropic-quadratic science, not a production optimizer guarantee. Possible specialized prior work on \(\ell_\infty\)-steepest descent or nonlinear sign dynamics merits independent checking. No expert or independent mathematical validation is asserted.

Self-review: passed. Independent audit: not yet performed.
