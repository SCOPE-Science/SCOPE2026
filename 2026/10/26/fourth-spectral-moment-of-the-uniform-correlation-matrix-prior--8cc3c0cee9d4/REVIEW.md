# Review

**Correctness (C): PASS.** The Gram representation reduces the trace to three disjoint index-pattern classes. Their counts are \(p(p-1)(p-2)(p-3)\), \(2p(p-1)(p-2)\), and \(p(p-1)\); the corresponding expectations are \((p+1)^{-3}\), \((p+1)^{-2}\), and \(3/((p+1)(p+3))\). The exact-rational checker agrees with the closed form on the stated finite ranges, while the proof covers every integer \(p\ge2\).

**Originality (O): PASS, with residual priority risk.** The inspected LKJ/restricted-Wishart paper supplies the distributional representation and uniform case but does not state this fourth spectral moment. The claim is the explicit moment evaluation and its asymptotic expansion, not a new distributional characterization. The literature search was targeted, not exhaustive.

**Value (V): PASS.** The fourth spectral moment is a natural finite-dimensional invariant of a widely used correlation-matrix prior. The decomposition separates genuine four-cycle contributions from repeated-edge/backtracking contributions and gives an exact benchmark with leading growth \(3p\) for spectral calibration.

Closest inspected source: Wang, Wu, and Chu (2018), arXiv:1809.04746v1. Limitation: only the uniform case \(\eta=1\) is covered.

Self-review: passed. Independent audit: not yet performed.
