# Review of the nonnegative cyclic Gabor rigidity theorem

## Correctness

**PASS (self-review).** The spectral formula follows from the orthogonal decomposition into residue classes modulo the translation step and Fourier diagonalization of each circulant block. In the positive class, the zeroth Fourier mode and Parseval's identity yield a bound on the sum of all but the largest tap in each block: \(r\le7\delta/6\). The dominant tap differs from unit size by less than \(5\delta/8\). Combining these yields the dimension-independent squared bound \(1009\delta^2/576\) for each normalized fiber, strictly better than the advertised \(16\delta^2/9\). The exact-zero case and the two-tap sharp-exponent witness are algebraic consequences. The supplementary `CHECK.py` returned `CHECK_OK 576`, comparing the direct Gram matrices with the independent Fourier-block calculation and testing the claimed inequality. These tests are finite, and the analytical argument is the universal proof.

## Originality

**PASS relative to the literature and indexed results inspected, with residual risk.** The closest primary source is Asipchuk–De Carli–Rodriguez, arXiv:2605.16139, which provides finite Gabor block-equivalence and diagonalization tools. Its inspected main theorems do not give a positivity-dependent inverse stability law: \(\|S_g-I\|\le\delta\) forcing a fixed-distance approximation of the window by a flat transversal, uniformly over all cyclic dimensions. Nicola's arXiv:2305.02738 concerns exact maximally localized Gabor orthonormal bases. Salanevich–Strachan's arXiv:2509.01325 concerns frame robustness and erasure stability, not this structural inverse conclusion. Liehr's arXiv:2605.29984 concerns real-line compactly supported Gabor bases. Closely related published finite Gabor measurement-rank findings and continuum sharp-frame results address distinct operators or settings. The exact transversal characterization itself is not claimed as the new mathematical step. An unindexed general stability theorem could dominate the estimate and is a genuine residual risk.

## Mathematical value

**PASS.** At critical sampling, exact Parseval conditions are algebraic, but nearly Parseval window design requires control of deviations. This theorem supplies an explicit, deterministic, dimension-free inverse modulus on a natural positivity cone: the frame-operator defect determines proximity to a precisely classified sparse orthonormal design. The two-tap witness proves that the rate \(O(\delta)\) cannot be improved in this uniform family. The restriction to positivity is mathematically substantial, not a substitution of known complex-window statements; without positivity, non-sparse flat-Fourier windows are possible.

## Literature and limitations

The frame operator is on \(\ell^2(\mathbb Z_{pq})\), not \(L^2(\mathbb R)\); translations are by \(q\) and modulations by \(p\). The coefficient \(4/3\) is not proved optimal, only the linear exponent. Neither complex-phase rigidity nor other lattice geometries follow. The source's abstract and main claims are not evidence of an exhaustive absence of equivalent earlier treatments; expert novelty review remains necessary.

Self-review: passed. Independent audit: not yet performed.
