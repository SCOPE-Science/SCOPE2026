# Scientific review

## Correctness — PASS

The exact formula is derived from the product formula for degree-\((d-1)\) equispaced Lagrange basis coefficients. Disjoint endpoint stencils make each continuation row's absolute sum the positive blend of the two extrapolation Lebesgue functions, and the real \(\ell^\infty\) norm is the maximum such sum. A center-row argument yields the lower bound; an explicit polynomial symmetric-beta family proves even-\(C\) attainment and odd-\(C\) approximation while strict increase excludes equality in the latter case. Summing polynomial leading coefficients proves the asymptotic. Exact-arithmetic checks are supporting finite evidence, not a substitute for the general proof.

## Originality — PASS with bibliographic risks

Méndez-Cruz–Amlani (arXiv:2610.19797) define the same discrete extrapolation/blending operator, yet focus on periodic smoothness and FFT differentiation. Albin–Pathmanathan (DOI 10.1137/130932533) use related approximate-step blending and provide smooth-function bounds, but not this sharp arbitrary-data norm minimax or parity of optimizer existence. De Camargo–Mascarenhas (arXiv:1409.2808) give a different extended-interpolation Lebesgue instability result; Nainwal–Anand (arXiv:2605.04765) treat FC-Gram methods. Searches of mathematical records and available literature found no directly covering theorem. Residual risk: a generic, older unindexed lemma on minimax blends might imply this corollary without matching terms.

## Mathematical value — PASS

The result gives an unavoidable perturbation-amplification barrier for a natural high-order Fourier-continuation operator and identifies when a legal smooth blend can actually attain it. The \(d=9\), \(C=64\) parameters used in the motivating numerical tests already force a lower bound of \(17{,}527{,}209{,}985\) for arbitrary sample noise. This separates worst-case data stability from excellent results on smooth test functions and provides a precise constraint when choosing continuation width and extrapolation order. The parity/nonattainment effect is a structural boundary of the admissible smooth-step class, not a claim of superiority in spectral accuracy.

## Limits

The result assumes \(d\ge2\), \(C\ge2\), \(N\ge2d\), exact interpolation, strictly increasing symmetric flat-ended transitions and the input/output supremum norm. It does not control the derivatives or spectral resolution of transitions approaching the step function, does not include extra rounding error in recurrence implementations, and may not apply to overlapping stencils or other extension methods.

Self-review: passed. Independent audit: not yet performed.
