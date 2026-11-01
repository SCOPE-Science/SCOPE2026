# Scientific review: horocyclic Toeplitz symbol tomography

## Correctness — PASS
The scope is the combinatorial-harmonic Bergman space on an infinite \((q+1)\)-regular tree, \(q\ge2\), with \(\alpha>1\), and all bounded complex horocyclic symbols. The complete wavelet basis is established in De Mari–Monti–Rizzo [1, Theorem 14]. A separate same-horocycle Gram calculation proves that its wavelets are pairwise orthogonal even after restriction to each fixed level. Exact weighted descendant counts give the claimed convolution coefficients and norm. The transfer rational function follows by three geometric sums. Since \(r,rs,rs^2<1\), the displayed inverse converges on \(\ell^\infty(\mathbb Z)\); the alternating coefficients of its rational part give its exact norm. Direct finite-tree checks and symbolic calculations are reproduced by `checker.py`. Finite checks do not replace the completeness and infinite-convolution proofs. No unsupported extrapolation to general tree multipliers or the endpoint \(\alpha=1\) is made.

## Originality — PASS, with historical-priority risk
The closest full text [1] already constructs the wavelet basis and Bergman projection, but its Theorem 14 and later kernel and projection sections do not establish horocyclic Toeplitz diagonalization, bounded invertibility of the symbol filter, sharp condition number, or a full symbol-algebra identification. The later related paper [2] studies the forward Laplacian and \(L^p\)-boundedness of Toeplitz-type kernels; its operators and hypotheses do not imply this combinatorial-harmonic compression theorem. Searches of relevant published mathematical records, general Bergman/Toeplitz literature, and source aliases did not find a covering result. An unindexed earlier Toeplitz calculus or an indirectly encompassing theorem remains possible; an absence of search results is not a uniqueness proof. The explicitly known basis is treated only as prior input, not as the new contribution.

## Mathematical value — PASS
For the natural class of horocycle-dependent observables on a noncompact discrete upper-half-plane analogue, the result solves both the forward concentration-spectrum problem and the inverse problem of recovering symbols from horocycle-**labelled** spectral values. It identifies a precise sharp stability constant, a global extremizing symbol, a complete operator algebra, and the blow-up of inversion cost at the Bergman-weight boundary. The labelled-data qualification is essential: unordered spectra alone are insufficient. This is a natural operator-theoretic invariant of the geometry, not an arbitrary parameter substitution.

## Sources and limitations
[1] F. De Mari, M. Monti, E. Rizzo, *Horocyclic harmonic Bergman spaces on homogeneous trees*, arXiv:2309.15047v1 (2023-09-26), Sections 3–5 and Theorem 14. https://arxiv.org/pdf/2309.15047

[2] A. Ottazzi, F. Santagati, *Harmonic Bergman spaces on locally finite trees*, arXiv:2505.03479v1 (2025-05-06), Introduction and Section 3. https://arxiv.org/pdf/2505.03479

Limits: homogeneous trees; combinatorial rather than forward harmonicity; \(\alpha>1\); bounded level-dependent symbols; labelled inversion only; independent audit and historical exhaustive priority check outstanding.

Self-review: passed. Independent audit: not yet performed.
